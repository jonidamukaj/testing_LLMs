import openai
import json
import csv
import os

# Load your API key from a secure location
openai.api_key = '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'

# Prompt templates
prompt_template1 = "Please describe briefly the following scientific author and consider the following information:\n\nName: {name}\nPublications: {publications}\nJournal Articles: {journal_articles}\nsince year:{since_year}\nProceedings Papers: {proceedings_papers}\n\n"
prompt_template2 = "Please describe briefly with a few words the following scientific author and consider the following information:\n\nName: {name}\nPublications: {publications}\nJournal Articles: {journal_articles}\nsince year:{since_year}\nProceedings Papers: {proceedings_papers}\n\n"
file_path = os.path.abspath("testing/data_authors.json")
output_file = os.path.abspath("testing/results1.json")


def save_to_json(data):
    results = []
    if os.path.exists(output_file):
        with open(output_file, 'r') as json_file:
            results = json.load(json_file)

    result = {
        'name': data['name'],
        'existing_text': data['existing_text'],
        'generated_text1': data['generated_text'],
        'generated_text2': data['generated_text2']
    }

    results.append(result)

    with open(output_file, 'w') as json_file:
        json.dump(results, json_file, indent=4)


def generate_prompt(data):
    # Construct the first prompt using the template and user data
    prompt1 = prompt_template1.format(**data)

    # Generate text using ChatGPT API for the first prompt
    response1 = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt1,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract the generated text from the API response
    generated_text1 = response1.choices[0].text.strip()

    # Construct the second prompt using the template and user data
    prompt2 = prompt_template2.format(**data)

    # Generate text using ChatGPT API for the second prompt
    response2 = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt2,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract the generated text from the second API response
    generated_text2 = response2.choices[0].text.strip()

    # Update the data dictionary with generated texts
    data['generated_text'] = generated_text1
    data['generated_text2'] = generated_text2

    # Save the data to a JSON file
    save_to_json(data)

    # Print the generated texts
    print("Generated Text 1:", generated_text1)
    print("Generated Text 2:", generated_text2)


def main():
    # Load data from JSON file
    with open(file_path, 'r') as file:
        user_data_list = json.load(file)

    for user_data in user_data_list:
        # Generate prompts based on user data
        generate_prompt(user_data)

        # Ask if the user wants to continue or exit
        choice = input("Do you want to continue (Y/N)? ")
        if choice.lower() != 'y':
            break


if __name__ == '__main__':
    main()
