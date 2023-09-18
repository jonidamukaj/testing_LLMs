import json
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load pre-trained T5 model and tokenizer
model_name = "t5-large"
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

# Load data from JSON file
with open("data_authors.json", "r", encoding="utf-8") as json_file:
    contributors_data = json.load(json_file)


# Choose a prompt template (template1, template2, or template3)
prompt_template1 = "Please describe briefly the following research contributor and consider the following information:\n\nName: {name}\nPublications: {publications}\nJournal Articles: {journal_articles}\nsince year:{since_year}\nProceedings Papers: {proceedings_papers}\n\n"
prompt_template2 = "Please describe briefly with a few words the following research contributor and consider the following information:\n\nName: {name}\nPublications: {publications}\nJournal Articles: {journal_articles}\nsince year:{since_year}\nProceedings Papers: {proceedings_papers}\n\n"
prompt_template3 = "Generate a concise description of the given research contributor based on the following details:\n\nName: {name}\nPublications: {publications}\nJournal Articles: {journal_articles}\nsince year:{since_year}\nProceedings Papers: {proceedings_papers}\n\n"

prompt_template = prompt_template1
# Choose a prompt template (template1, template2, or template3)
# List to store results
results = []

# Generate descriptions for each contributor
for contributor in contributors_data:
    prompt = prompt_template.format(
        name=contributor["name"],
        publications=contributor["publications"],
        journal_articles=contributor["journal_articles"],
        since_year=contributor["since_year"],
        proceedings_papers=contributor["proceedings_papers"]
    )

    # Tokenize the input
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Generate text using the model
    output = model.generate(input_ids, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2, top_k=50, top_p=0.95)

    # Decode the generated output
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    # Store the results
    result = {
        "name": contributor["name"],
        "existing_text": contributor["existing_text"],
        "generated_text": generated_text
    }
    results.append(result)

# Save results to a JSON file
output_file = "generated_large.json"
with open(output_file, "w") as json_output:
    json.dump(results, json_output, indent=4)

print("Results saved to", output_file)
