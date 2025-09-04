import os
import torch
from datasets import load_dataset, Dataset
from transformers import AutoTokenizer, AutoModelForMultipleChoice
from torch.utils.data import DataLoader
import json

# Set the number of samples to use (modify this as need)
NUM_SAMPLES = 100  # Adjust the number of samples to test on


# Get th full path of files
def get_full_path(file_name):
    CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
    # print("Current Path:", CURRENT_PATH)
    current_working_directory = os.getcwd().replace("\\", "/")
    # print(f"Current Working Directory: {current_working_directory}")
    CURRENT_PATH = CURRENT_PATH.replace(current_working_directory, ".")
    DATASET_PATH = os.path.join(
        CURRENT_PATH, file_name).replace("\\", "/")
    return DATASET_PATH


# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained('roberta-base')
model = AutoModelForMultipleChoice.from_pretrained("roberta-base")


# Load datasets
def load_custom_dataset(file_path, num_samples=None):
    with open(file_path, "r") as f:
        dataset = Dataset.from_list([json.loads(line) for line in f])
        if num_samples:
            # Limit to the spefied number of samples
            dataset = dataset.select(range(num_samples))
        return dataset


val_data = load_custom_dataset(
    get_full_path("hellaswag_val.jsonl"), NUM_SAMPLES)
test_data = load_custom_dataset(
    get_full_path("hellaswag_test.jsonl"), NUM_SAMPLES)


# Preprocess the data
def preprocess_function(examples):
    first_sentences = [[context]*4 for context in examples["ctx"]]
    answer_choices = examples["endings"]

    first_sentences = sum(first_sentences, [])
    answer_choices = sum(answer_choices, [])

    tokenize_examples = tokenizer(
        first_sentences, answer_choices, truncation=True, padding="max_length", max_length=128)

    return {k: [tokenize_examples[k][i:i+4] for i in range(0, len(tokenize_examples[k]), 4)]for k in tokenize_examples}


# Preprocess datasets
encoded_val = val_data.map(preprocess_function, batched=True)
encoded_test = test_data.map(preprocess_function, batched=True)


# Prepare the DataLoader
def collate_fn(batch):
    input_ids = torch.tensor([item["input_ids"] for item in batch])
    attention_mask = torch.tensor([item["attention_mask"]for item in batch])
    labels = torch.tensor([int(item["label"])
                          for item in batch]) if 'label' in batch[0] else None
    return {"input_ids": input_ids, "attention_mask": attention_mask, "labels": labels}


# DataLoader
val_dataloader = DataLoader(encoded_val, batch_size=8, collate_fn=collate_fn)
test_dataloader = DataLoader(encoded_test, batch_size=8, collate_fn=lambda x: collate_fn(
    [{k: v for k, v in item.items() if k != 'label'} for item in x]))

# Run the model and compute accuracy on validation set
device = torch.device("cpu")
model.to(device)


# Verication of data model
def evaluate_model(dataloader, compute_accuracy=True):
    model.eval()
    num_correct = 0
    num_total = 0
    predictions = []

    with torch.no_grad():
        for batch in dataloader:
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)

            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            logits = outputs.logits
            pred = torch.argmax(logits, dim=1).tolist()
            predictions.extend(pred)

            if compute_accuracy and 'labels' in batch:
                labels = batch["labels"].to(device)
                num_correct += (torch.tensor(pred) == labels).sum().item()
                num_total += labels.size(0)
    if compute_accuracy:
        accuracy = num_correct/num_total
        print(f"Validation Accuracy: {accuracy:.4f}")
    return predictions


# Evaluate on valiation set
print(f"Evaluate on validation set (first {NUM_SAMPLES} samples)...")
evaluate_model(val_dataloader)

# Make predictions on test set
print(f"Making predictions on test set (first {NUM_SAMPLES} samples)...")
test_predictions = evaluate_model(test_dataloader, compute_accuracy=False)

# Save test predictions
with open(get_full_path("test_predictions.jsonl"), "w")as f:
    for pred in test_predictions:
        f.write(json.dumps({"prediction": pred})+"\n")
print("Test predictions saved to 'test_predictions.jsonl'")
