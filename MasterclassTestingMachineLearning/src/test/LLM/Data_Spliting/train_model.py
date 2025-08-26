from datasets import Dataset
from transformers import (
    DistilBertTokenizer,
    DistilBertForSequenceClassification,
    Trainer,
    TrainingArguments,
)
import pandas as pd
import os

# Step 1: Load your dataset from a CSV file
current_path = "./src/test/LLM/Data_Spliting/"
train_file = current_path + "iris_train.csv"
data = pd.read_csv(train_file)

# Step 1.1: Validate the existence of the training file
if not os.path.exists(train_file):
    raise FileNotFoundError(f"Training file not found: {train_file}")

# Step 1.2: Validate the columns in the dataset
required_columns = ['SepalLengthCm', 'SepalWidthCm',
                    'PetalLengthCm', 'PetalWidthCm', 'Species']
if not all(col in data.columns for col in required_columns):
    raise ValueError(
        f"The dataset must contain the following columns: {required_columns}")

# Step 2: Convert the dataset to Hugging Face Dataset
dataset = Dataset.from_pandas(data)

# Step 3: Preprocess the datase: Convert all feature column into a single textual description


def convert_to_text(example):
    features = f"This flower has a sepal length of {example['SepalLengthCm']} cm, a sepal width of {example['SepalWidthCm']} cm, "\
        f"a petal length of {example['PetalLengthCm']} cm, and a petal width of {example['PetalWidthCm']} cm."
    return {"text": features}


dataset = dataset.map(convert_to_text)

# Step 4: Map the 'Species' column to numerical lables for classification
label_mapping = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}

# Ensure 'Species' is correctly mapped
dataset = dataset.map(lambda x: {"label": label_mapping[x["Species"]]})

# Drop unnecessary columns
dataset = dataset.remove_columns(
    {"Id", "SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"})

# Step 5: Tokenize the dataset
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")


def tokenize_data(example):
    return tokenizer(example["text"], truncation=True, padding="max_length", max_length=128)


tokenized_dataset = dataset.map(tokenize_data, batched=True)

# Step 6: Split the dataset into training and evaluation sets
train_test_split = tokenized_dataset.train_test_split(test_size=0.2, seed=42)
train_dataset = train_test_split["train"]
eval_dataset = train_test_split["test"]

# Step 7: Load a pre-trained DistriBERT model
model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased", num_labels=3)

# Step 8: Define training arguments with increased epochs and logging
training_arg = TrainingArguments(
    output_dir=current_path + "results",
    eval_strategy="epoch",  # Performs evaluation at the end of each epoch
    save_strategy="epoch",  # Save checkpoints at the end at each poch
    learning_rate=5e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=10,  # Increased epochs for better training
    weight_decay=0.01,
    logging_dir=current_path + "logs",
    logging_steps=10,
    save_total_limit=2,
    load_best_model_at_end=True,  # Load the best model at the end of training
)

# Step 9: Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_arg,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
)

# Step 10: Train the model and save the results
trainer.train()
print("Training completed. Best model saved at:", training_arg.output_dir)
