import os
import json
import requests

import sacrebleu
from dotenv import load_dotenv  # Load environment variables


def get_openai_response(prompt):
    """
    Send a prompt to OpenAI's ChatGPT and retieves the response
    Args:
        prompt (string): User's request to OPENAI o GPT-4
    """
    # 1. Initialize OpenAI client
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        load_dotenv()  # Load environment variables from .env file
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    openai_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    data = {
        "model": "gpt-4",  # Ensure this is the correct model name
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500,  # Adjust as need
        "n": 1,
        "stop": None,
        "temperature": 0.7
    }

    try:
        # Use json=data instead of data=json.dumps(data)
        response = requests.post(openai_url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()

        # For debugging:
        print("Full API Response: ", json.dumps(result, indent=2))

        chat_response = result['choices'][0]['message']['content'].strip()
        return chat_response, result  # Return both the translation and the full response

    except Exception as e:
        print(f"An error occurred: {e}")
    return None, None


def calculate_bleu(reference, candidate):
    """
    Calculates the BLEU score between the reference and candidate translations
    Args:
        reference (_type_): _description_
        candidate (_type_): _description_
    """
    bleu = sacrebleu.corpus_bleu([candidate], [[reference]])
    return bleu.score


def main():
    """
    Main function to execute the workflow
    """

    # Input English sentence
    print("\nThe quick brown fox jumps over the lazy dog.")
    english_sentence = input("Enter the English sentence: ").strip()
    if not english_sentence:
        print("We need an English Sentence. Exiting...")
        return
    # Input benchmark Spanish translation
    print("\nEl rápido zorro marrón salta sobre el perro perezoso.")
    benchmark_traslation = input(
        "Enter the benchhmark Spanish traslation: ").strip()
    if not benchmark_traslation:
        print("We need an Spanish Sentence. Exiting...")
        return
    # Construct the prompt to translate from English to Spanish
    prompt = f"Translate the following sentence from English to Spahish: {english_sentence}"

    print("\nSending prompt to ChatGPT...\n")
    chatgpt_translation, api_response = get_openai_response(prompt=prompt)
    if not chatgpt_translation:
        print("Failed to get a response from chatGPT")
        return

    print("=== Input ad Benchmark ===")
    print(f"English Sentence: {english_sentence} ")
    print(f"Benckmark Spanish Translation: {benchmark_traslation}")
    print("===========================\n")

    print("=== ChatGPT's Translation ===")
    print(chatgpt_translation)
    print("===========================\n")

    # Calculate BLEU score
    bleu_score = calculate_bleu(benchmark_traslation, chatgpt_translation)
    print(f"BLEU Score: {bleu_score}")


print("\nFull API Response for Debugging:")
if __name__ == "__main__":
    main()
