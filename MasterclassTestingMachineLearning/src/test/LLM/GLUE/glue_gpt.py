import os
from dotenv import load_dotenv  # Load environment variables
from openai import OpenAI
import numpy as np
from datasets import load_dataset
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

print("1. Initialize OpenAI client")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    load_dotenv()  # Carga las variables de entorno del archivo .env
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# print("OpenAI API Key:", OPENAI_API_KEY)

# Instantiate OpenAI client
openai_client = OpenAI(api_key=OPENAI_API_KEY)


def get_openai_response(prompt):
    """
    Sends a prompt to OpenAi's API using the updateaded OPENAI client retrieves the response
    """
    try:
        completion = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        chat_reponse = completion.choices[0].message.content.strip()
        return chat_reponse
    except Exception as e:
        print(f"An error ccurred: {e}")
        return None


def evaluate_ssts_first_50():
    """
    Evaluate the SST-2 taks using the OpenAI API and computes metrics for the first 50 validations examples.
    """
    print("Load the SST-2 dataset")
    dataset = load_dataset("glue", "sst2")
    validation_set = dataset["validation"]

    print("Ensure we are iterating over dicctionaries (convert to a list fo dictionaries)")
    validation_examples = list(validation_set)

    print("Store predictions and labels")
    predictions = []
    labels = []

    print("Evaluate only the first 50 examples")
    for idx, example in enumerate(validation_examples[:50]):
        print("Ensure 'sentence' is accessed correctly")
        prompt = f"Classify the sentiment of the following sendentece as poistive or negative: \"{example['sentence']}\""

        print("Get the model's prediction using OpenAI API")
        response = get_openai_response(prompt=prompt)

        # Show sprompt and response
        print(f"Prompt ({idx+1}): {prompt}")
        print(f"Response: {response}")

        if response is not None:
            print("Convert the response to a label (e.g., 0 or 1)")
            if "positive" in response.lower():
                predictions.append(1)
            elif "negative" in response.lower():
                predictions.append(0)
            else:
                print(f"Unexpected response: {response}")
        else:
            predictions.append(-1)  # HAndle API failures
        print("Store the true label")
        labels.append(example["label"])

    print("Filter out invalid predictions")
    valid_indices = [i for i, pred in enumerate(predictions) if pred != -1]
    valid_predictions = [predictions[i] for i in valid_indices]
    valid_labels = [labels[i] for i in valid_indices]

    print("Compute evaluation metrics")
    accuracy = accuracy_score(valid_labels, valid_predictions)
    precision = precision_score(
        valid_labels, valid_predictions, average="binary")
    recall = recall_score(valid_labels, valid_predictions, average="binary")
    f1 = f1_score(valid_labels, valid_predictions, average="binary")

    print("Display results")
    results = {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1-Score": f1,
    }
    for metric, value in results.items():
        print(f"{metric}: {value:.4f}")

print("run the evaluation for the first 50 SST-2 examples")
if __name__ == "__main__":
    evaluate_ssts_first_50()
