def generate_report(passed_count, total_count):
    # Guard against division by zero.
    if total_count == 0:
        pass_rate = 0.0
    else:
        pass_rate = (passed_count / total_count) * 100
    return f"Pass rate: {pass_rate}%"
