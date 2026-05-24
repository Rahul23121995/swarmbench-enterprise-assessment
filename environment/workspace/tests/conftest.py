import pytest

@pytest.fixture(scope="function")
def driver():
    # Mock driver creation
    driver = object()
    # Broken: no try...finally layout to guarantee driver cleanup on failures
    yield driver
    driver.quit()
