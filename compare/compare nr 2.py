import csv
import nltk
from nltk.tokenize import word_tokenize
from difflib import SequenceMatcher
from language_tool_python import LanguageTool

# Function to count the number of words in a given text
def count_words(text):
    tokens = word_tokenize(text)
    return len(tokens)

# Function to find similar phrases using SequenceMatcher ratio
def find_similar_phrases(text1, text2):
    return SequenceMatcher(None, text1, text2).ratio()

# Function to check grammar issues using LanguageTool
def check_grammar(text):
    tool = LanguageTool('en-US')  # Adjust the language as per your requirement
    errors = tool.check(text)
    return len(errors)

# Column names
column1_name = 'Column1'
column2_name = 'Column2'
result_columns = ['Number of Words', 'Similar Phrases', 'Grammar Issues']

# Create a sample input data
input_data = [
    {column1_name: 'Sample text 1', column2_name: 'Sample text 2'},
    {column1_name: 'Another text', column2_name: 'Some other text'}
]

# Create the output data
output_data = []

# Process each input row
for row in input_data:
    # Get the values from the respective columns
    text1 = row[column1_name]
    text2 = row[column2_name]
    
    # Count the number of words
    word_count = count_words(text1)
    
    # Find similar phrases
    similar_phrases = find_similar_phrases(text1, text2)
    
    # Check grammar issues
    grammar_issues = check_grammar(text1)
    
    # Create the output row
    output_row = {
        column1_name: text1,
        column2_name: text2,
        'Number of Words': word_count,
        'Similar Phrases': similar_phrases,
        'Grammar Issues': grammar_issues
    }
    
    # Add the output row to the output data
    output_data.append(output_row)

# CSV file path
output_file = 'output.csv'

# Open the output CSV file
with open(output_file, 'w', newline='') as output_csv:
    # Create a CSV writer object
    writer = csv.DictWriter(output_csv, fieldnames=[column1_name, column2_name] + result_columns)
    
    # Write the header row in the output CSV file
    writer.writeheader()
    
    # Write the output data to the CSV file
    writer.writerows(output_data)

print('Output CSV file created successfully.')
