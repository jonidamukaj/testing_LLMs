import csv
import difflib
from language_tool_python import LanguageTool

def compare_text_files(file1_path, file2_path, output_file_path):
    # Read the contents of both files
    with open(file1_path, 'r') as file1:
        text1 = file1.read()
    with open(file2_path, 'r') as file2:
        text2 = file2.read()

    # Calculate the number of words in each text file
    num_words1 = len(text1.split())
    num_words2 = len(text2.split())

    # Find similar phrases using difflib
    sequence_matcher = difflib.SequenceMatcher(None, text1, text2)
    matches = sequence_matcher.get_matching_blocks()
    similar_phrases = [text1[match.a:match.a + match.size] for match in matches if match.size > 0]

    # Grammar checking
    tool = LanguageTool('en-US')  # Specify English language
    grammar_issues1 = tool.check(text1)
    grammar_issues2 = tool.check(text2)

    # Write results to a CSV file
    with open(output_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Requirement", "File 1", "File 2", "Grammar issues"])
        writer.writerow(["Number of words", num_words1, num_words2, ""])
        writer.writerow([])
        writer.writerow(["Similar phrases"])
        writer.writerow([])

        # Write similar phrases in a single column
        for phrase in similar_phrases:
            writer.writerow(["", "", phrase, ""])

        writer.writerow([])
        writer.writerow(["", "", "", ""])  # Empty row for formatting
        writer.writerow(["", "", "", "Grammar issues"])

        # Write grammar issues for file 1
        for issue in grammar_issues1:
            writer.writerow(["", "", "", f"{issue} (File 1)"])

        writer.writerow([])  # Empty row for formatting

        # Write grammar issues for file 2
        for issue in grammar_issues2:
            writer.writerow(["", "", "", f"{issue} (File 2)"])

# Provide the paths to the text files and the output CSV file
file1_path = 'text_file1.txt'
file2_path = 'text_file2.txt'
output_file_path = 'comparison_results.csv'

# Call the function to compare the text files and write results to CSV
compare_text_files(file1_path, file2_path, output_file_path)
