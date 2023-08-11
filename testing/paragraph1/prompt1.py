import openai
import json
import csv
import os
import random
import time


# Load your API key from a secure location
openai.api_key = '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'

#name_list = ['Anna Smith', 'Ben Smith', 'Will Smith', 'Mary Adams']
#selected_name = random.choice(name_list)


# Prompt templates
prompt_template1 = "Please describe briefly the following research contributor and consider the following information:\n\nName: Anna Smith\nPublications: {publications}\nJournal Articles: {journal_articles}\nsince year:{since_year}\nProceedings Papers: {proceedings_papers}\n\n"
prompt_template2 = "Please describe briefly with a few words the following research contributor and consider the following information:\n\nName: Ben Smith\nPublications: {publications}\nJournal Articles: {journal_articles}\nsince year:{since_year}\nProceedings Papers: {proceedings_papers}\n\n"
prompt_template3 = "Generate a concise description of the given research contributor based on the following details:\n\nName: Mary Adams\nPublications: {publications}\nJournal Articles: {journal_articles}\nsince year:{since_year}\nProceedings Papers: {proceedings_papers}\n\n"
#prompt_template4 = "Compose a short description of the given scientific author based on the subsequent particulars:\n\nName: Will Smith\nPublications: {publications}\nJournal Articles: {journal_articles}\nsince year:{since_year}\nProceedings Papers: {proceedings_papers}\n\n"


file_path = os.path.abspath("testing/paragraph1/data_authors.json")
output_file = os.path.abspath("testing/paragraph1/CurieNEW.json")


def save_to_json(data):
    results = []
    if os.path.exists(output_file):
        with open(output_file, 'r') as json_file:
            results = json.load(json_file)

    result = {
        'name': data['name'],
        'existing_text': data['existing_text'],
        'generated_text1': data['generated_text1'],
        'generated_text2': data['generated_text2'],
        'generated_text3': data['generated_text3']
        #'generated_text4': data['generated_text4']
    }

    results.append(result)

    with open(output_file, 'w') as json_file:
        json.dump(results, json_file, indent=4)


def generate_prompt(data):
    # Construct the first prompt using the template and user data
    prompt1 = prompt_template1.format(**data)

    # Generate text using ChatGPT API for the first prompt
    response1 = openai.Completion.create(
        engine='text-curie-001',
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
        engine='text-curie-001',
        prompt=prompt2,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract the generated text from the second API response
    generated_text2 = response2.choices[0].text.strip()

    # Construct the third prompt using the template and predefined data
    prompt3 = prompt_template3.format(**data)

    # Generate text using ChatGPT API for the third prompt
    response3 = openai.Completion.create(
        engine='text-curie-001',
        prompt=prompt3,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract the generated text from the third API response
    generated_text3 = response3.choices[0].text.strip()



    # Update the data dictionary with generated texts
    data['generated_text1'] = generated_text1
    data['generated_text2'] = generated_text2
    data['generated_text3'] = generated_text3
    #data['generated_text4'] = generated_text4

    # Save the data to a JSON file
    save_to_json(data)

    # Print the generated texts
    #print("Generated Text 1:", generated_text1)
    #print("Generated Text 2:", generated_text2)
    #print("Generated Text 3:", generated_text3)
    #print("Generated Text 4:", generated_text4)


def main():
    # Load data from JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        user_data_list = json.load(file)

    for user_data in user_data_list:
        # Generate prompts based on user data
        generate_prompt(user_data)

        # Delay for 1 minute before processing the next author
        time.sleep(60)  # Sleep for 60 seconds (1 minute)    

    # Find the data for the author with name "Fabian Beck"
    #for user_data in user_data_list:
        #if user_data['name'] == "Stephan Diehl":
            # Generate prompts based on the specified author data
            #generate_prompt(user_data)
            #break  # Exit the loop after processing the specified author

        # Ask if the user wants to continue or exit
        #choice = input("Do you want to continue (Y/N)? ")
        #if choice.lower() != 'y':
        #    break


if __name__ == '__main__':
    main()


