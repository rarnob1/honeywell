import logging

class logclass:
    @staticmethod
    def log_gen():
        # Set up logging
        logging.basicConfig(
            filename='C:\\Users\\Rafi Ornob\\PycharmProjects\\honeywell\\logs\\swaglabs.log',  # Log file path
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Log message format
            level=logging.INFO  # Log level
        )
        logger = logging.getLogger()
        return logger