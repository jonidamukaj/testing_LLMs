import csv

data = [
    {
        "name": "Ben Shneiderman",
        "existing_text": "Ben Shneiderman is an active and longtime research contributor with more than 400 publications  since 1972. Shneiderman's published work includes 208 journal articles  and 197 proceedings papers ",
        "generated_text1": "Ben Shneiderman is an American computer scientist and professor of Computer Science at the University of Maryland. He has published over 400 scientific articles since 1972, including 208 journal articles and 197 proceedings papers. He is a pioneer in the field of human-computer interaction and is best known for his development of the \"direct manipulation\" user interface style, which is now widely used in many modern computer operating systems. He is also an active advocate for the ethical use of technology, and has written several books",
        "generated_text2": "Ben Shneiderman: Prolific Author (400 publications, 208 journal articles, 197 proceedings papers since 1972)."
    },
    {
        "name": "Fabian Beck",
        "existing_text": "Fabian Beck is an active researcher since 2008 and has published 61 research papers , including 17 journal articles  and 44 proceedings papers . Out of the total 61 publications, the author published 26 articles as first author . The author received a PhD degree from University of Trier, Germany with the dissertation published in 2013 and titled \u201cUnderstanding Multi-Dimensional Code Couplings\u201d.",
        "generated_text1": "Fabian Beck is a prolific scientist with 61 publications since 2008, including 17 journal articles and 44 proceedings papers. He has made significant contributions to the scientific field and has been widely published in various journals and proceedings.",
        "generated_text2": "Fabian Beck is a prolific author, with 61 publications since 2008, including 17 journal articles and 44 proceedings papers."
    },
    {
        "name": "Mary Jean Harrold",
        "existing_text": "Mary Jean Harrold is an active and longtime research contributor with more than 100 publications  since 1989. Harrold's published work includes 41 journal articles  and 105 proceedings papers",
        "generated_text1": "Mary Jean Harrold is a prolific scientific author with over 100 publications, including 41 journal articles and 105 proceedings papers since 1989. Her research spans a variety of topics and she is widely regarded as a leading expert in her field.",
        "generated_text2": "Mary Jean Harrold is an experienced scientist, having published over 100 works since 1989, including 41 journal articles and 105 proceedings papers."
    },
    {
        "name": "Stephan Diehl",
        "existing_text": "Stephan Diehl is an active and longtime research contributor with more than 100 publications  since 1994. Diehl's published work includes 38 journal articles  and 89 proceedings papers . The author received a PhD degree from Saarland University, Saarbr\u00fccken, Germany with the dissertation published in 1996 and titled \u201cSemantics-directed generation of compilers and abstract machines\u201d.",
        "generated_text1": "Stephan Diehl is a prolific scientist and author with over 100 publications since 1994. He has authored 38 journal articles and 89 proceedings papers. His research focuses on a wide range of topics, including computer science, artificial intelligence, and machine learning. He is highly regarded in his field and his work has been widely cited by other authors.",
        "generated_text2": "Stephan Diehl is a prolific researcher with over 100 publications since 1994, including 38 journal articles and 89 proceedings papers."
    },
    {
        "name": "Daniel Weiskopf",
        "existing_text": "Daniel Weiskopf is an active researcher with more than 250 publications  since 1999. Weiskopf's published work includes 122 journal articles  and 147 proceedings papers",
        "generated_text1": "Daniel Weiskopf is a highly prolific scientist with an impressive 250 publications since 1999. He has written 122 journal articles and 147 proceedings papers, demonstrating his expertise in the field.",
        "generated_text2": "Daniel Weiskopf: Prolific researcher (250 publications, 122 journal articles since 1999, 147 proceedings papers)."
    },
    {
        "name": "Michael Burch",
        "existing_text": "Michael Burch is an active researcher with more than 100 publications  since 2004, where most contributions appeared since 2013 (71 publications). Burch's published work includes 23 journal articles  and 89 proceedings papers",
        "generated_text1": "Michael Burch is a prolific scientific author with over 100 publications since 2004. He has written 23 journal articles and 89 proceedings papers. He is an expert in his field and his research has been widely cited and recognized.",
        "generated_text2": "Michael Burch: prolific scholar (100 publications, 23 journal articles, 89 proceedings papers since 2004)."
    }
]

# Specify the CSV file path
csv_file = "resultsinCSV.csv"

# Write the data to the CSV file
with open(csv_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "existing_text", "generated_text1", "generated_text2"])
    writer.writeheader()
    writer.writerows(data)

print("Data has been written to the CSV file:", csv_file)