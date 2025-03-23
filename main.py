from honeyword import start_generating_honey_words
from llm.logger import logger
from predictor import predict_password


def main():
    logger.info("Starting password generation and prediction pipeline")
    # start_generating_honey_words()
    generation_file = "generations/myspace_t=0.1_passwords.txt"
    logger.info(f"Running prediction on {generation_file}")
    success, total, no_pred = predict_password(generation_file, 0.1, 3)
    logger.info("Pipeline (1) complete")
    success, total, no_pred = predict_password(generation_file, 0.1, 5)
    logger.info("Pipeline (2) complete")
    success, total, no_pred = predict_password(generation_file, 0.1, 10)
    logger.info("Pipeline (3) complete")


if __name__ == "__main__":
    main()
