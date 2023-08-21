import openai
import json
import csv
import os
import time

# Load your API key from a secure location
openai.api_key = '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'

# Prompt templates
prompt_template1 = "Please describe briefly the following scientific author and consider the following information:Name: Anna Smith, \nMost frequent co-author and past supervisee: {first_co_author}\nCollaboration since: {first_co_author_year}\nNumber of publication with the most frequent co-author:{first_co_author_publications}\nSecond most frequent co-author: {second_co_author}\nCollaboration since: {second_co_author_year}\nNumber of publication with Second most frequent co-author:{second_co_author_publications}"

file_path = os.path.abspath("testing/data_authors.json")
output_file = os.path.abspath("testing/paragraph3/curie2_Results.json")


def save_to_json(data):
    results = []
    if os.path.exists(output_file):
        with open(output_file, 'r') as json_file:
            results = json.load(json_file)

    result = {
        'name': data['name'],
        'existing_text2': data['existing_text3'],
        'generated_text1': data['generated_text1'],
    }

    results.append(result)

    with open(output_file, 'w') as json_file:
        json.dump(results, json_file, indent=4)


def generate_prompt(data):
    # Construct the first prompt using the template and user data
    prompt1 = prompt_template1.format(**data)

    # Generate text using ChatGPT API for the first prompt
    response1 = openai.Completion.create(
        engine='text-ada-001',
        prompt=prompt1,
        temperature=1,
        max_tokens=600,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the generated text from the API response
    generated_text1 = response1.choices[0].text.strip()

   
    # Update the data dictionary with generated texts
    data['generated_text1'] = generated_text1
   
    # Save the data to a JSON file
    save_to_json(data)

   

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
       #if user_data['name'] == "Carla E. Brodley":
            # Generate prompts based on the specified author data
           # generate_prompt(user_data)
            #break  # Exit the loop after processing the specified author

        # Ask if the user wants to continue or exit
        #choice = input("Do you want to continue (Y/N)? ")
        #if choice.lower() != 'y':
        #    break


if __name__ == '__main__':
    main()
