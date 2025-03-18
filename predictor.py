from llm import generate_response
from llm.logger import logger


def predict_password(generation_path: str, temperature: int, bag: int):
    logger.info(
        f"Starting password prediction on {generation_path} with temperature={temperature}, bag={bag}"
    )
    with open(generation_path, "r") as f:
        data = f.readlines()

    no_pred = 0
    success = 0
    total = len(data)

    logger.info(f"Processing {total} passwords for prediction")

    for line in data:
        line = line.replace("\n", "")
        password, *honey_words = line.split(":")
        honey_words = [word for word in honey_words if word != ""]

        response = generate_response(
            prompt=f"suggest {bag} words from the list that seem to be user chosen passwords {','.join(honey_words)}. Must only output {bag} passwords, separate each password with a new comma. Obey the rule.",
            kwargs={
                "temperature": temperature,
            },
        )
        logger.info(f"Predicted: {response} for password: {password}")
        if response == "":
            no_pred += 1
        elif password in response:
            success += 1
    logger.info(
        f"Prediction complete - Success: {success}/{total} ({success / total * 100:.2f}%), No predictions: {no_pred}"
    )
    return success, total, no_pred
