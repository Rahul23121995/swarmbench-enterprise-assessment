def test_international_checkout():
    cart_total = 250.0
    # Broken: uses outdated domestic tax rate of 10%
    expected_tax = cart_total * 0.10
    actual_tax = cart_total * 0.12  # simulated actual tax from updated API
    assert expected_tax == actual_tax, f"Tax verification failure! Expected {expected_tax}, got {actual_tax}"
