import pytest

@pytest.fixture(scope="function")
def driver():
    # Mock driver creation
    driver = object()
    try:
        yield driver
    finally:
        # Ensure cleanup even if setup or test raises an exception
        try:
            driver.quit()
        except Exception:
            pass
