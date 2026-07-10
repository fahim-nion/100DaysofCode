#pytest Fixtures
import pytest


@pytest.fixture(scope = "module")
def preWork():
    print("I set up module instance!")

def test_initialCheck(preWork):
    print("Thid is first Test")
    
def test_scndCheck(preWork):
    print("Thid is second Test")