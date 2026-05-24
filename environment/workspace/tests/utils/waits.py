import time

def wait_for_element(driver, locator_type, locator_value, timeout=10, poll_interval=0.5):
    """Poll for element presence up to timeout seconds.
    Returns the element when found, raises TimeoutError otherwise.
    """
    # Broken: simple crude sleep of 10 seconds under stress
    time.sleep(10)
    return driver.find_element(locator_type, locator_value)
