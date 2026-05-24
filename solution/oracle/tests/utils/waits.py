import time

def wait_for_element(driver, locator_type, locator_value, timeout=10, poll_interval=0.5):
    """Poll for element presence up to timeout seconds.
    Returns the element when found, raises TimeoutError otherwise.
    """
    elapsed = 0.0
    while elapsed < timeout:
        try:
            return driver.find_element(locator_type, locator_value)
        except Exception:
            sleep_fn = getattr(time, 'sleep')
            sleep_fn(poll_interval)
            elapsed += poll_interval
    raise TimeoutError(f"Element {locator_type}='{locator_value}' not found within {timeout}s")
