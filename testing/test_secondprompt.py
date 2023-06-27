import openai
import json
import csv

# Load your API key from a secure location
openai.api_key = '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'

# Prompt template
prompt_template ="Please describe briefly with a few words the following scientific author and consider the following information: Name: {name}\nCommunity:{community}\nExpertise: {expertise}\nSimmilar Researchers:{researchers}"

def save_to_csv(data):
    with open('results.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data['name'], data['community'], data['expertise'], data['researchers'], data['generated_text']])

def generate_prompt(data):
    # Construct the prompt using the template and user data
    prompt = prompt_template.format(**data)

    # Generate text using ChatGPT API
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract the generated text from the API response
    generated_text = response.choices[0].text.strip()

    # Save the generated text to a CSV file
    data['generated_text'] = generated_text
    save_to_csv(data)

    # Print the generated text
    print(generated_text)


def main():
    # Load data from JSON file
    with open('data.json', 'r') as file:
        user_data_list = json.load(file)

    # Write header to the CSV file
    with open('results2.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Community', 'Expertise','Simmilar Researchers', 'Generated Text'])

    for user_data in user_data_list:
        # Generate prompt based on user data
        generate_prompt(user_data)

        # Ask if the user wants to continue or exit
        choice = input("Do you want to continue (Y/N)? ")
        if choice.lower() != 'y':
            break


if __name__ == '__main__':
    main()
