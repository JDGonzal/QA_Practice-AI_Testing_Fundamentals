import os
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from transformers import (
    DistilBertTokenizer,
    DistilBertForSequenceClassification,
    Trainer,
    TrainingArguments,
    DataCollatorWithPadding,
)
from datasets import Dataset

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
    features = f"Features: Sepal length {example['SepalLengthCm']} cm, Sepal width {example['SepalWidthCm']} cm, "\
        f"Petal length of {example['PetalLengthCm']} cm, Petal width of {example['PetalWidthCm']} cm."
    return {"text": features}


dataset = dataset.map(convert_to_text)

# Step 4: Map the 'Species' column to numerical lables for classification
label_mapping = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}

# Ensure 'Species' is correctly mapped
dataset = dataset.map(lambda x: {"label": label_mapping[x["Species"]]})

# Step 5: Tokenize the dataset
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)


def tokenize_data(example):
    return tokenizer(example["text"], truncation=True, padding="max_length", max_length=128)


tokenized_dataset = dataset.map(tokenize_data, batched=True)

# Step 6: k-Fold Cross-Validation
kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
df = pd.DataFrame(tokenized_dataset)

results = []
model_checkpoint = "distilbert-base-uncased"

for fold, (train_idx, val_idx) in enumerate(kf.split(df, df["label"])):
    print(f"\n--- Fold {fold+1} ---")

    # Step 7: Create result directories
    fold_result_dir = f"{current_path}results_fold{fold+1}"
    os.makedirs(fold_result_dir, exist_ok=True)

    # Step 8: Create result training and validation sets
    train_data = df.iloc[train_idx]
    eval_data = df.iloc[val_idx]
    train_dataset = Dataset.from_pandas(train_data)
    eval_dataset = Dataset.from_pandas(eval_data)

    # Step 9: Load a pre-trained DistriBERT model
    model = DistilBertForSequenceClassification.from_pretrained(
        model_checkpoint, num_labels=3)

    # Step 10: Define training arguments with increased epochs and logging
    training_arg = TrainingArguments(
        output_dir=fold_result_dir,
        eval_strategy="epoch",  # Performs evaluation at the end of each epoch
        save_strategy="epoch",  # Save checkpoints at the end at each poch
        learning_rate=5e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        num_train_epochs=3,  # Increased epochs for better training
        weight_decay=0.01,
        logging_dir=f"{current_path}logs_fold_{fold+1}",
        logging_steps=10,
        save_total_limit=2,  # Keep only the last 2 checkpoints
        load_best_model_at_end=True,  # Load the best model at the end of training
    )

    # Step 11: Inicialize Trainer
    trainer = Trainer(
        model=model,
        args=training_arg,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        data_collator=data_collator,
    )

    # Step 12: Train the model and save the results
    trainer.train()
    trainer.save_model(fold_result_dir)
    print("Training completed. Best model saved at:", training_arg.output_dir)

    # Step 13: Update checkpoint for next fold
    # Use the best model of current fold as starting point for the next
    model_checkpoint = fold_result_dir

    # Step 14: Evaluate the model
    eval_results = trainer.evaluate()
    results.append(eval_results)

    print(f"Results for fold {fold+1}: {eval_results}")

# Step 15: Calculate average metrics across all folds
average_results = {key: sum(r[key]for r in results)/len(results)
                   for key in results[0]}
print("\n--- Average Results Across all Folds ---")

for key, value in average_results.items():
    print(f"{key}: {value:.4f}")

# Final Output
print("\nTraining and evaluation completed. Models and checkpoints are saved in respective fold directories.")
