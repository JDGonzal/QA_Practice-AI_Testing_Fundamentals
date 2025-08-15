import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import math

# Load the pre-trained model and tokenizer

model_name = "gpt2"  # You can change to "gpt2-medium", "gpt2-large", etc.
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Set the pad_token to the eos_token to handle padding correctly
tokenizer.pad_token = tokenizer.eos_token
model.eval()  # Set the model to evaluation mode


def calculate_perplexity(text):
    # Strip whitespace and validate that text is not emptu
    text = text.strip()
    if not text:
        print("Error: input text is empty. Please provide valid text.")
        return None

    # Toeknize and prepare the input with padding for batch compability
    encodings = tokenizer(text, return_tensors="pt",
                          padding=True, truncation=True)

    # Ensure input tensor dimensions are  expected
    input_ids = encodings["input_ids"]
    attention_mask = encodings["attention_mask"] if "attention_mask" in encodings else None

    # Check if the input tensor has valid content
    if input_ids.size(1) == 0:
        print("Error: Tokenization result in an empty input. Please check your text")
        return None

    # Calculate the loss (negaitve log likelihood)
    with torch.no_grad():
        outputs = model(input_ids=input_ids,
                        attention_mask=attention_mask, labels=input_ids)
        loss = outputs.loss.item()

    # Calculate perplexity
    perplexity = math.exp(loss)
    return perplexity


# Text to calculate perplexity on
text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Donec ullamcorper libero ut interdum posuere. "
        "Quisque et tincidunt ipsum, in cursus sem. "
        "Proin turpis turpis, tempus id lectus a, mollis ultricies leo. "
        "Integer mollis dolor fringilla, aliquam diam vitae, cursus enim.")

# Debugging: Print the input to verify it is not-empy after stripping
print(f"Debug: Received input - `{text}`")


perplexity =calculate_perplexity(text)

if perplexity is not None:
  print(f"Perplexity: {perplexity}")
