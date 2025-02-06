import logging

def log_msg(filename):
    logging.basicConfig(filename=filename, filemode='w', format='%(name)s - %(levelname)s - %(message)s')

    logging.warning("This is warning")
    logging.error("This is error")
    logging.info("This is info")
    logging.debug("This is debug")

if __name__ == "__main__":
    log_msg("logs.log")