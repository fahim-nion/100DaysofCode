import pytest



@pytest.fixture(scope = "function")
def preSetupWork():
    print("I set up browser instance!")