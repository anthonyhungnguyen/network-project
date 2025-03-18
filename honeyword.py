import random

from llm import generate_response
from llm.logger import logger


def generate_honey_words(dataset: str, temperature: int):
    logger.info(f"Starting honey word generation for dataset: {dataset} with temperature: {temperature}")
    with open(f"dataset/{dataset}.txt", "r") as f:
        data = f.readlines()
    for line in data:
        line = line.replace(" ", "").replace("\n", "")
        response = generate_response(
            prompt=f"suggest 19 passwords that are similar to {line}. Must only output 19 passwords, separate each password with a new comma. Obey the rule.",
            kwargs={
                "temperature": temperature,
            },
        )
        response_list = response.split(",")
        response_list.append(line)
        random.shuffle(response_list)

        # Write the response to a file
        output_file = f"generations/{dataset}_t={temperature}_passwords.txt"
        with open(output_file, "a") as f:
            f.write(line + ":" + ",".join(response_list) + "\n")
        logger.debug(f"Generated honey words for password and saved to {output_file}")


def start_generating_honey_words():
    logger.info("Starting honey word generation for all datasets")
    generate_honey_words(dataset="myspace", temperature=0.1)
    generate_honey_words(dataset="myspace", temperature=0.5)
    generate_honey_words(dataset="myspace", temperature=1)
    generate_honey_words(dataset="000webhost", temperature=0.1)
    generate_honey_words(dataset="000webhost", temperature=0.5)
    generate_honey_words(dataset="000webhost", temperature=1)
