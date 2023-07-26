import openai
import json

# Load your OpenAI API key
openai.api_key = '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'

# Function to generate text using GPT-3.5
def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,  # Adjust the desired length of the generated text
        n=1,
        stop=None,
        temperature=0.7  # Adjust the temperature for more or less randomness
    )
    return response.choices[0].text.strip()

# Read data from JSON file
def read_data_from_json(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data

# Main function
def generate_text_from_json(json_file_path):
    data = read_data_from_json(json_file_path)
    prompt = data.get("prompt", "")
    generated_text = generate_text(prompt)
    print("Generated Text:")
    print(generated_text)

# Usage example
generate_text_from_json("data.json")
