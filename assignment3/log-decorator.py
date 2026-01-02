# Task 1 writing and Testing a Decorator

import logging 
from functools import wraps

# one time setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        #log pieces
        positional_parameters = list(args) if args else "none"
        keyword_parameters = dict(kwargs) if kwargs else "none"

        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {positional_parameters}")
        logger.log(logging.INFO, f"keyword parameters: {keyword_parameters}")

        result = func(*args, **kwargs)

        logger.log(logging.INFO, f"return: {result}")
        logger.log(logging.INFO, "-------")

        return result
    return wrapper

@logger_decorator
def hello_world():
    print("Hello World!!")

@logger_decorator
def retirn_true(*args):
    return True

@logger_decorator
def return_decorator(**kwargs):
    return logger_decorator

if __name__== "__main__":
    hello_world()
    retirn_true(1, 2, 3, "abc")
    return_decorator(name="Tatiana", city="Los Gatos")

    print("Done. Check decorator.log")

