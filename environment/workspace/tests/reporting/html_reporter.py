def generate_report(passed_count, total_count):
    # Broken: direct division without safety checks leads to ZeroDivisionError
    pass_rate = (passed_count / total_count) * 100
    return f"Pass rate: {pass_rate}%"
