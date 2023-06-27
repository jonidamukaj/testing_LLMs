import openai
import json

# Load your API key from a secure location
openai.api_key = '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'

# Prompt templates
prompt_templates = [
    "Please describe briefly the following scientific author and consider the following information: Name: {name}\n, {publications}\n publications since {since_year}\n,  {journal_articles}\n journal articles,{proceedings_papers}\n proceedings papers.",
    "Please describe briefly with a few words the: \n\nName: Name: {name}\n, {publications}\n publications since {since_year}\n,  {journal_articles}\n journal articles,{proceedings_papers}\n proceedings papers.",
]

def generate_prompt(data, template):
    # Construct the prompt using the template and user data
    prompt = template.format(**data)

    # Generate text using ChatGPT API
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=00,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract the generated text from the API response
    generated_text = response.choices[0].text.strip()

    # Print the generated text
    print(generated_text)


def main():
    # Load data from JSON file
    with open('data.json', 'r') as file:
        user_data_list = json.load(file)

    prompt_idx = 0  # Index to iterate over prompt templates

    for user_data in user_data_list:
        # Get the prompt template based on the index
        prompt_template = prompt_templates[prompt_idx % len(prompt_templates)]

        for template in prompt_templates:
            # Generate prompt based on user data and template
            generate_prompt(user_data, template)

        # Ask if the user wants to continue or exit
        choice = input("Do you want to continue (Y/N)? ")
        if choice.lower() != 'y':
            break

        prompt_idx += 1


if __name__ == '__main__':
    main()
