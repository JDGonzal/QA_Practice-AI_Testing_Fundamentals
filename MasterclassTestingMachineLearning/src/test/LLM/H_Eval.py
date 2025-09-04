from openai import OpenAI
import os
from deepeval.benchmarks import HumanEval
from typing import Tuple
from dotenv import load_dotenv  # Load environment variables

# Optionally, set the API key here if it's not set as an environment variable
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    load_dotenv()  # Load environment variables from .env file
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found in environment variables.")

# Instantiate the client with the API key
openai_client = OpenAI(api_key=OPENAI_API_KEY)


# Define a model class that will be passed to the benchmark
class GPT35Model:
    def __init__(self, model_name="gpt-4o"):
        self.model_name = model_name

    # This method must return a single string as an answer
    def generate(self, prompt):
        completion = openai_client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        # Correctly access the message content
        if completion.choices and completion.choices[0].message:
            return completion.choices[0].message.content.strip()
        return "No response generated."

    # Method to generate multiple samples
    def generate_samples(self, task=None, k=1, **kwargs):
        # Handling the prompt whether passed directly or within the task dictionary
        prompt = kwargs.get('prompt', task.get('prompt') if isinstance(
            task, dict) and 'prompt' in task else task)
        samples = []
        for _ in range(k):
            samples.append(self.generate(prompt))
        return samples


# Initialize your GPT-3.5 model
gpt35_model = GPT35Model()

# Define the benchmark with specific tasks and modes
benchmark = HumanEval(n=10)

# Evaluate the GPT-3.5 model
try:
    # Pass the model instance directly if the benchmark is designed to handle such objects
    results = benchmark.evaluate(gpt35_model, k=5)
    if isinstance(results, float):
        print(f"Overall TruthfulQA Accuracy: {results}")
    else:
        print(f"Overall Score: {results.overall_score}")
except Exception as e:
    print(f"An error occurred during evaluation: {e}")
