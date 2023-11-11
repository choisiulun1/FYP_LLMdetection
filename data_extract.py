import json


def extract_squad_data(file_path):
    # Load the JSON file
    with open(file_path, "r") as file:
        squad_data = json.load(file)

    # Iterate through the data and yield a data object
    for article in squad_data["data"]:
        title = article["title"]
        for paragraph in article["paragraphs"]:
            context = paragraph["context"]
            for qa in paragraph["qas"]:
                question = qa["question"]
                is_impossible = qa["is_impossible"]
                answers = qa["answers"] if not is_impossible else []

                # Create a data object
                data_object = {
                    "title": title,
                    "context": context,
                    "question": question,
                    "is_impossible": is_impossible,
                    "answers": answers,
                }

                # Yield the data object
                yield data_object


# Example usage
file_path = "./Squad/dev-v2.0.json"

# Process each data object as needed

print(next(extract_squad_data(file_path)))
