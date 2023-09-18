import os
import json

# Load the JSON data from the file
with open('data_authors.json', 'r', encoding='utf-8') as file:
    author_data = json.load(file)

# Initialize a list to store the results for each author
author_results = []

# Loop through each author's data and create the text
for author in author_data:
    author_name = author['name']
    frequent_co_author = author.get('first_co_author', 'N/A')
    frequent_co_author_collaboration_since = author.get('first_co_author_year', 'N/A')
    frequent_co_author_publications = author.get('first_co_author_publications', 'N/A')
    second_co_author = author.get('second_co_author', 'N/A')
    second_co_author_collaboration_since = author.get('second_co_author_year', 'N/A')
    second_co_author_publications = author.get('second_co_author_publications', 'N/A')
    another_co_author = author.get('another_co_author', 'N/A')
    another_co_author_collaboration_year = author.get('another_co_author_year', 'N/A')
    another_co_author_publications = author.get('another_co_author_publications', 'N/A')
    first_collaboration = author.get('first_collaboration', 'N/A')
    first_collaboration_field = author.get('first_collaboration_field', 'N/A')
    first_collaboration_papers = author.get('first_collaboration_papers', 'N/A')
    second_collaboration = author.get('second_collaboration', 'N/A')
    second_collaboration_papers = author.get('second_co_author_publications', 'N/A')

    # Create a formatted text for the author
    author_text = f"Please describe briefly the following scientific author and consider the following information:\n"
    author_text += f"Name: {author_name}\n"
    author_text += f"Most frequent co-author and past supervisee: {frequent_co_author}\n"
    author_text += f"Collaboration since: {frequent_co_author_collaboration_since}\n"
    author_text += f"The number of publications with the most frequent co-author: {frequent_co_author_publications}\n"
    author_text += f"Second most frequent co-author: {second_co_author}\n"
    author_text += f"Collaboration since: {second_co_author_collaboration_since}\n"
    author_text += f"Number of publications with Second most frequent co-author: {second_co_author_publications}\n"
    author_text += f"Another co-author: {another_co_author}\n"
    author_text += f"Year of collaboration with another co-author: {another_co_author_collaboration_year}\n"
    author_text += f"Number of publications with another co-author: {another_co_author_publications}\n"
    author_text += f"First Collaboration: {first_collaboration}\n"
    author_text += f"First Collaboration Field: {first_collaboration_field}\n"
    author_text += f"Number of papers in the first collaboration: {first_collaboration_papers}\n"
    author_text += f"Second Collaboration: {second_collaboration}\n"
    author_text += f"Number of papers in the second collaboration: {second_collaboration_papers}\n\n"

    # Append the author's text to the results list
    author_results.append(author_text)



# Specify the folder path to save the JSON file
folder_path = "testing/authors_results.json"
os.makedirs(folder_path, exist_ok=True)

# Define the full path for the text file
text_file_path = os.path.join(folder_path, 'authors_results.txt')

# Write the results to the text file in the specified folder
with open(text_file_path, 'w', encoding='utf-8') as text_file:
    text_file.writelines(author_results)

print(f"Author results have been written to '{text_file_path}'")
