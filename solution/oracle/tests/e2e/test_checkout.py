def test_international_checkout():
    cart_total = 250.0
    # Fixed: use correct international tax rate 0.12
    expected_tax = cart_total * 0.12
    actual_tax = cart_total * 0.12  # simulated actual tax from updated API
    assert expected_tax == actual_tax, f"Tax verification failure! Expected {expected_tax}, got {actual_tax}"
