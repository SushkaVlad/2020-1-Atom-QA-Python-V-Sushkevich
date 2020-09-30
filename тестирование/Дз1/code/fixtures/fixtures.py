import pytest
import random


@pytest.fixture(scope="function")
def random_key():
    return random.randint(4, 150)


@pytest.fixture(scope="session")
def string_to_reverse():
    return 'Hello world!'
