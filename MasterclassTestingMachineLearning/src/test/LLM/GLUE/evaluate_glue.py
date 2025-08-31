import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments, DataCollatorWithPadding
from datasets import load_dataset
import evaluate

current_path = "./src/test/LLM/GLUE/"

print("1. Load the BERT-base model and tokenizer")
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(
    model_name, num_labels=2)

print("2. Load the GLUE dataset (e.g. SST-2 fror sentiment analysis)")
task = "sst2"  # Change this for other GLUE tasks (e.e, 'mrpc', 'qqp')
dataset = load_dataset("glue", task)


print("3. Preprocess the dataset")


def preprocess_function(examples):
    return tokenizer(examples["sentence"], truncation=True, padding="max_length", max_length=128)


encoded_dataset = dataset.map(preprocess_function, batched=True)

print("4. Load evaluation metric using 'evaluate'")
metric = evaluate.load("glue", task)


print("5. Define a function to compute the metrics")


def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = logits.argmax(axis=1)
    return metric.compute(predictions=predictions, references=labels)


print("6. Create a DataCollaator for dynamic padding")
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

print("7. Prepare evaluation aguments")
training_args = TrainingArguments(
    output_dir=current_path+"results",
    per_device_eval_batch_size=64,
    logging_dir=current_path+"logs",
    do_train=False,  # No Trainings
    do_eval=True,  # Only evaluation
)

print("8. Initialize Trainer fro evaluation")
trainer = Trainer(
    model=model,
    args=training_args,
    eval_dataset=encoded_dataset["validation"],
    compute_metrics=compute_metrics,
    data_collator=data_collator,  # Use data collator instead of tokenizer
)

print("9. Evaluate all model on the evaluation set")
results = trainer.evaluate()

# DEBUG: Print all metrics  returned by the evaluation
print("Evaluation results:", results)

print("10. Filter GLUE-specific metrics")
exclude_metrics = ["eval_loss", "eval_runtime", "eval_samples_per_second",
                   "eval_steps_per_second", "eval_model_prepare_time"]
glue_metrics = {k: v for k, v in results.items() if k not in exclude_metrics}

print("Convert GLUE metrics to a DataFrame for visulization")
result_df = pd.DataFrame.from_dict(
    glue_metrics, orient="index", columns=["value"])
result_df.reset_index(inplace=True)
result_df.columns = ["Metric", "Value"]

# DEBUG: Ensure DataFrame is populated correcytly
print("Filtered Results for Graph:", result_df)

print("11. Plot the GLUE metrics")
plt.figure(figsize=(10,6))
sns.barplot(x="Metric", y="Value", data=result_df, palette="viridis")
plt.title(f"GLUE Evaluation Results for Tasks: {task.upper()}", fontsize=16)
plt.xlabel("Metrics", fontsize=14)
plt.ylabel("Values", fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()
plt.show()
