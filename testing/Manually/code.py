import csv

# Define the data in the same format as provided
data = [
    ["Paragraph", "Model", "Coherence", "Consistency", "Relevance", "Fluency", "comment"],
    ["Paragraph1", "ada", 1.783333333, 1.383333333, 1.366666667, 3, ""],
    ["Paragraph1", "curie", 2.533333333, 1.783333333, 1.416666667, 3.616666667, ""],
    ["Paragraph1", "davinci", 4.016666667, 3.733333333, 3.9, 4.033333333, ""],
    ["Paragraph1", "turbo", 4.866666667, 4, 4.266666667, 4.916666667, ""],
    ["Paragraph2", "ada", 2.633333333, 2.616666667, 2.7, 2.816666667, "hallucinated text, they instead of he/she"],
    ["Paragraph2", "curie", 3.633333333, 3.6, 3.616666667, 4.133333333, ""],
    ["Paragraph2", "davinci", 4.083333333, 3.783333333, 3.95, 3.533333333, ""],
    ["Paragraph2", "turbo", 4.966666667, 4.416666667, 4.95, 4.9, ""],
    ["Paragraph3", "ada", 0, 0, 0, 0, ""],
    ["Paragraph3", "curie", 2.75, 2.416666667, 2.633333333, 2.716666667, "hallucinated text, biologist, physicist etc"],
    ["Paragraph3", "davinci", 3.25, 3.3, 3.316666667, 3.033333333, ""],
    ["Paragraph3", "turbo", 4.166666667, 3.916666667, 4.383333333, 4.3, ""]
]

# Save the data to a CSV file
with open('manually.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data)

print("Data saved to output.csv")
