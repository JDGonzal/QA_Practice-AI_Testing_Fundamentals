import os
from openai import OpenAI
from dotenv import load_dotenv  # Load environment variables
from deepeval.benchmarks import TruthfulQA
from deepeval.benchmarks.tasks import TruthfulQATask
from deepeval.benchmarks.modes import TruthfulQAMode


# 1. Initialize OpenAI client
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    load_dotenv()  # Load environment variables from .env file
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Instantiate OpenAI client
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# 2. Define a model class that will be passed to the benchmark


class GPT35Model:
    def __init__(self, model_name="gpt-3.5-turbo"):
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
    
# Initialize your GPT-3.5 model
gpt35_model = GPT35Model()

# Define the benchmark with specific tasks and modes
benchmark = TruthfulQA(
    tasks=[TruthfulQATask.ADVERTISING, TruthfulQATask.FICTION],  # Use the TruthfulQATask enums
    mode=TruthfulQAMode.MC2
)

# Evaluate the GPT-3.5 model
try:
    # Pass the model instance directly if the benchmark is designed to handle such objects
    results = benchmark.evaluate(gpt35_model)
    print("Evaluation completed successfully!")
    print(f"Results: {results}")
except Exception as e:
    print(f"An error occurred: {e}")
