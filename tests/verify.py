import pathlib
import re
import sys

# Paths inside the container or host
container_workspace = pathlib.Path('/workspace')
if container_workspace.is_dir() and (container_workspace / 'tests').is_dir():
    WORKSPACE = container_workspace
else:
    WORKSPACE = pathlib.Path(__file__).parents[1] / 'environment' / 'workspace'
LOG_DIR = pathlib.Path('/logs/verifier')
LOG_DIR.mkdir(parents=True, exist_ok=True)

score = 0.0
checks = []

def add_check(name, passed, weight):
    global score
    checks.append((name, passed, weight))
    if passed:
        score += weight

# 1. Login locator fix
login_path = WORKSPACE / 'tests' / 'pages' / 'login_page.py'
if login_path.is_file():
    content = login_path.read_text()
    passed = bool(re.search(r'find_element\(\s*"name"\s*,\s*"login"\s*\)', content))
    add_check('login_locator_fixed', passed, 0.1)
else:
    add_check('login_locator_fixed', False, 0.1)

# 2. Wait utility fix
waits_path = WORKSPACE / 'tests' / 'utils' / 'waits.py'
if waits_path.is_file():
    content = waits_path.read_text()
    passed = ('while' in content) and ('time.sleep' not in content)
    add_check('waits_fixed', passed, 0.1)
else:
    add_check('waits_fixed', False, 0.1)

# 3. API validation fix
api_path = WORKSPACE / 'tests' / 'api' / 'user_client.py'
if api_path.is_file():
    content = api_path.read_text()
    passed = bool(re.search(r'assert\s+response\.status_code\s*==\s*201', content))
    add_check('api_status_fixed', passed, 0.1)
else:
    add_check('api_status_fixed', False, 0.1)

# 4. CSV parser fix
csv_path = WORKSPACE / 'tests' / 'utils' / 'data_mapper.py'
if csv_path.is_file():
    content = csv_path.read_text()
    passed = 'import csv' in content and 'csv.reader' in content
    add_check('csv_parser_fixed', passed, 0.1)
else:
    add_check('csv_parser_fixed', False, 0.1)

# 5. Checkout tax fix
checkout_path = WORKSPACE / 'tests' / 'e2e' / 'test_checkout.py'
if checkout_path.is_file():
    content = checkout_path.read_text()
    passed = 'expected_tax = cart_total * 0.12' in content
    add_check('checkout_tax_fixed', passed, 0.1)
else:
    add_check('checkout_tax_fixed', False, 0.1)

# 6. Retry decorator fix
retry_path = WORKSPACE / 'tests' / 'runners' / 'retry_decorator.py'
if retry_path.is_file():
    content = retry_path.read_text()
    passed = 'except Exception' in content or 'except AssertionError' in content
    add_check('retry_decorator_fixed', passed, 0.1)
else:
    add_check('retry_decorator_fixed', False, 0.1)

# 7. Parallel logging fix
parallel_path = WORKSPACE / 'tests' / 'runners' / 'parallel_executor.py'
if parallel_path.is_file():
    content = parallel_path.read_text()
    passed = 'log_lock = threading.Lock' in content and 'with log_lock' in content
    add_check('parallel_logging_fixed', passed, 0.1)
else:
    add_check('parallel_logging_fixed', False, 0.1)

# 8. Conftest teardown fix
conftest_path = WORKSPACE / 'tests' / 'conftest.py'
if conftest_path.is_file():
    content = conftest_path.read_text()
    passed = 'try:' in content and 'finally:' in content and 'driver.quit' in content
    add_check('conftest_fixed', passed, 0.1)
else:
    add_check('conftest_fixed', False, 0.1)

# 9. HTML reporter fix
report_path = WORKSPACE / 'tests' / 'reporting' / 'html_reporter.py'
if report_path.is_file():
    content = report_path.read_text()
    passed = 'if total_count == 0' in content
    add_check('html_reporter_fixed', passed, 0.1)
else:
    add_check('html_reporter_fixed', False, 0.1)

# 10. Jenkinsfile syntax fix
jenkins_path = WORKSPACE / '.jenkins' / 'Jenkinsfile'
if jenkins_path.is_file():
    content = jenkins_path.read_text()
    # Look for matching quotes in sh step
    passed = bool(re.search(r"sh\s+['\"]pytest\s+--maxfail\s+2['\"]", content))
    add_check('jenkinsfile_fixed', passed, 0.1)
else:
    add_check('jenkinsfile_fixed', False, 0.1)

# Write results
reward_path = LOG_DIR / 'reward.txt'
reward_path.write_text(str(round(score, 4)))

# Print detailed output for debugging
for name, passed, weight in checks:
    print(f"{name}: {'PASS' if passed else 'FAIL'} (weight {weight})")
print(f"TOTAL SCORE: {score}")

# Exit with non-zero if any check failed (optional)
if round(score, 4) < 1.0:
    sys.exit(1)
else:
    sys.exit(0)
