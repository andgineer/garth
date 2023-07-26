import re

CAMEL_TO_SNAKE = re.compile(r"((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))")


def camel_to_snake(camel_str: str) -> str:
    snake_str = CAMEL_TO_SNAKE.sub(r"_\1", camel_str)
    return snake_str.lower()


def camel_to_snake_dict(camel_dict: dict) -> dict:
    return {camel_to_snake(k): v for k, v in camel_dict.items()}