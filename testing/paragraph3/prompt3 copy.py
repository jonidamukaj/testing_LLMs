import openai
import json
import csv
import os
import time

# Load your API key from a secure location
openai.api_key = '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'

# Prompt templates
prompt_template1 = "Please describe briefly the following scientific author and consider the following information:\nName: Anna Smith\n Most frequent co-author and past supervisee: {first_co_author}\nCollaboration since: {first_co_author_year}\nNumber of publication with the most frequent co-author:{first_co_author_publications}\nSecond most frequent co-author: {second_co_author}\nCollaboration since: {second_co_author_year}\nNumber of publication with Second most frequent co-author:{second_co_author_publications}\Another co-author: {another_co_author}\a Year of collaboration with another co-author:  {another_co_author_year}\a Number of publications with another co-author: {another_co_author_publications}\n First Collaboration: {first_collaboration}\n\nFirst Collaboration Field: {first_collaboration_field}\n Number of papers in the first collaboration: {first_collaboration_papers}\n Second Collaboration: {second_collaboration}\n Number of papers in the second collaboration: {second_collaboration_papers}"
prompt_template2 = "Please describe briefly with a few words the following scientific author and consider the following information:\nName: Ben Adams\n Most frequent co-author and past supervisee: {first_co_author}\nCollaboration since: {first_co_author_year}\nNumber of publication with the most frequent co-author:{first_co_author_publications}\nSecond most frequent co-author: {second_co_author}\nCollaboration since: {second_co_author_year}\nNumber of publication with Second most frequent co-author:{second_co_author_publications}\Another co-author: {another_co_author}\a Year of collaboration with another co-author:  {another_co_author_year}\a Number of publications with another co-author: {another_co_author_publications}\n First Collaboration: {first_collaboration}\n\nFirst Collaboration Field: {first_collaboration_field}\n Number of papers in the first collaboration: {first_collaboration_papers}\n Second Collaboration: {second_collaboration}\n Number of papers in the second collaboration: {second_collaboration_papers}"
prompt_template3 ="Generate a concise description of the given scientific author based on the following details:\nName: Marie Mueller\n Most frequent co-author and past supervisee: {first_co_author}\nCollaboration since: {first_co_author_year}\nNumber of publication with the most frequent co-author:{first_co_author_publications}\nSecond most frequent co-author: {second_co_author}\nCollaboration since: {second_co_author_year}\nNumber of publication with Second most frequent co-author:{second_co_author_publications}\Another co-author: {another_co_author}\a Year of collaboration with another co-author:  {another_co_author_year}\a Number of publications with another co-author: {another_co_author_publications}\n First Collaboration: {first_collaboration}\n\nFirst Collaboration Field: {first_collaboration_field}\n Number of papers in the first collaboration: {first_collaboration_papers}\n Second Collaboration: {second_collaboration}\n Number of papers in the second collaboration: {second_collaboration_papers}"


file_path = os.path.abspath("testing/data_authors.json")
output_file = os.path.abspath("testing/paragraph3/ada_Results.json")


def save_to_json(data):
    results = []
    if os.path.exists(output_file):
        with open(output_file, 'r') as json_file:
            results = json.load(json_file)

    result = {
        'name': data['name'],
        'existing_text': data['existing_text3'],
        'generated_text1': data['generated_text1'],
        'generated_text2': data['generated_text2'],
        'generated_text3': data['generated_text3']
    }

    results.append(result)

    with open(output_file, 'w') as json_file:
        json.dump(results, json_file, indent=4)

def generate_prompt(data):
    # Construct the prompts using the templates and user data
    prompts = [
        prompt_template1.format(**data),
        prompt_template2.format(**data),
        prompt_template3.format(**data)
    ]

    generated_texts = []

    for prompt in prompts:
        # Construct messages for gpt-3.5-turbo-0613
        messages = [
            {"role": "user",
            "content":  prompt
            }
        ]

        # Generate text using ChatGPT API
        response = openai.Completion.create(
            model="text-ada-001",
            messages=messages,
            temperature=1,
            max_tokens=300,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
    
        generated_text = response.choices[0].message['content'].strip()
        generated_texts.append(generated_text)

    # Update the data dictionary with generated texts
    data['generated_text1'] = generated_texts[0]
    data['generated_text2'] = generated_texts[1]
    data['generated_text3'] = generated_texts[2]

    # Save the data to a JSON file
    save_to_json(data)

def main():
    # Load data from JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        user_data_list = json.load(file)

    for user_data in user_data_list:
        # Generate prompts based on user data
        generate_prompt(user_data)
    #for user_data in user_data_list:
        #if user_data['name'] == "Carla E. Brodley":
            # Generate prompts based on the specified author data
            #generate_prompt(user_data)
            #break  # Exit the loop after processing the specified author    

        # Delay for 1 minute before processing the next author
        time.sleep(60)

if __name__ == '__main__':
    main()
