from datasets import Dataset
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, Trainer
import pandas as pd
import os

# Step 1: Load the evaluation dataset
current_path = "./src/test/LLM/Data_Spliting/"
# eval_file = current_path+"iris_eval.csv"
eval_file = current_path+"iris_train.csv"
eval_data = pd.read_csv(eval_file)

# Step 1: Validate the existence of the evaluation file
if not os.path.exists(eval_file):
    raise FileNotFoundError(f"Evaluation file not found: {eval_file}")

# Step 1.1: Validate the columns in the dataset
required_columns = ['SepalLengthCm',
                    'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
if not all(col in eval_data.columns for col in required_columns):
    raise ValueError(
        f"The dataset must contain the following columns: {required_columns}")

# Step 2: Convert the dataset to Hugging face Dataset
eval_dataset = Dataset.from_pandas(eval_data)

# Step 3: Preprocess the dataset: convert features into textual descriptions


def convert_to_text(example):
    features = f"Sepal length: {example['SepalLengthCm']}, Sepal width: {example['SepalWidthCm']}, "\
        f"Petal length: {example['PetalLengthCm']}, Petal width: {example['PetalWidthCm']}."
    return {"text": features}


eval_dataset = eval_dataset.map(convert_to_text)

# Step 4: Tokenize the dataset
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")


def tokenizer_data(example):
    return tokenizer(example["text"], truncation=True, padding="max_length", max_length=128)


tokenized_eval_dataset = eval_dataset.map(tokenizer_data, batched=True)

# Step 5: Load the trained model
# model_path = current_path + "results/checkpoint-60" # Usado en el subtítulo 45
model_path = current_path + "results_fold5/checkpoint-18" # Cambiado en el subtítulo 48
model = DistilBertForSequenceClassification.from_pretrained(
    model_path, local_files_only=True)  # Path to the saved model
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Trained model not found: {model_path}")

# Step 6: Initialize Trainer
trainer = Trainer(
    model=model,
    tokenizer=tokenizer,
)

# Step 7: Make predictions
predictions = trainer.predict(tokenized_eval_dataset)

# Step 8: Evaluate predictions and save results
predicted_labels = predictions.predictions.argmax(axis=1)  # Get the predicted class
actual_labels = eval_dataset["Species"]  # Original labels

# Step 9: Map label indices back to species names
label_mapping = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}
reverse_label_mapping = {v: k for k,
                         v in label_mapping.items()}  # Reverse mapping

# Step 10: Calculate accuracy
predicted_labels = predictions.predictions.argmax(
    axis=1)  # Fix access to predictions
actual_labels = eval_data["Species"]  # Use eval_data for actual labels

if len(predicted_labels) != len(actual_labels):
    raise ValueError(
        "Mismatch between number of predictions and actual labels.")

correct_predictions = sum(
    reverse_label_mapping[predicted_labels[i]] == actual_labels[i]
    for i in range(len(actual_labels))
)
accuracy = correct_predictions / len(actual_labels)

# Print and save results
print(f"Accuracy: {accuracy:.2f}")

# Save evaluation results to a CSV file
output_file = current_path + "evaluation_results.csv"
eval_data["PredictedLabel"] = [reverse_label_mapping[label]
                               for label in predicted_labels]
eval_data.to_csv(output_file, index=False)
print(f"Evaluation results saved to {output_file}")
