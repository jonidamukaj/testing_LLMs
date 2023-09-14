import json

# Load data from the first JSON file
with open("testing/paragraph3/curie_Results.json", 'r') as file1:
    data1 = json.load(file1)

# Load data from the second JSON file
with open("testing/paragraph3/curie2_Results.json", 'r') as file2:
    data2 = json.load(file2)

# Create a list to store the combined data
combined_data = []

# Check if both files have the same number of records
if len(data1) == len(data2):
    for i in range(len(data1)):
        # Combine the generated texts from both files
        combined_entry = {
            "name": data1[i]["name"],
            "existing_text": data1[i]["existing_text"],
            "generated_text1": data1[i]["generated_text1"] + data2[i]["generated_text1"],
            "generated_text2": data1[i]["generated_text2"] + data2[i]["generated_text2"],
            "generated_text3": data1[i]["generated_text3"] + data2[i]["generated_text3"]
        }
        combined_data.append(combined_entry)
else:
    print("The number of records in the two files does not match.")

# Save the combined data to a new JSON file
with open('combined_data.json', 'w') as combined_file:
    json.dump(combined_data, combined_file, indent=4)

print("Data combined and saved to combined_data.json")


prompt_template1 = "Please describe briefly the following scientific author and consider the following information:Name: Anna Smith, \nAnother co-author: {another_co_author}\n Year of collaboration with another co-author:  {another_co_author_year}\n Number of publications with another co-author: {another_co_author_publications}\n First Collaboration: {first_collaboration}\nFirst Collaboration Field: {first_collaboration_field}\n Number of papers in the first collaboration: {first_collaboration_papers}\n Second Collaboration: {second_collaboration}\n Number of papers in the second collaboration: {second_collaboration_papers}"
prompt_template2 = "Please describe briefly with a few words the following scientific author and consider the following information: Name: Ben Adams, \nAnother co-author: {another_co_author}\n Year of collaboration with another co-author:  {another_co_author_year}\n Number of publications with another co-author: {another_co_author_publications}\n First Collaboration: {first_collaboration}\nFirst Collaboration Field: {first_collaboration_field}\n Number of papers in the first collaboration: {first_collaboration_papers}\n Second Collaboration: {second_collaboration}\n Number of papers in the second collaboration: {second_collaboration_papers}"
prompt_template3 ="Generate a concise description of the given scientific author based on the following details:Name: Marie Mueller, \nAnother co-author: {another_co_author}\n Year of collaboration with another co-author:  {another_co_author_year}\n Number of publications with another co-author: {another_co_author_publications}\n First Collaboration: {first_collaboration}\nFirst Collaboration Field: {first_collaboration_field}\n Number of papers in the first collaboration: {first_collaboration_papers}\n Second Collaboration: {second_collaboration}\n Number of papers in the second collaboration: {second_collaboration_papers}"

