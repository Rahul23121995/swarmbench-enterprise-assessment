# SwarmBench Enterprise Assessment

An enterprise-grade Python test automation framework has been migrated to a new environment, but it currently has multiple integration and infrastructure defects. There are 10 distinct, independent bugs spread across page objects, utilities, API clients, test runners, reporting tools, conftest fixtures, and CI pipelines.

Your task is to identify and repair all 10 infrastructure and test code defects. When all defects are correctly resolved, the full QA suite will run reliably, log parallel execution safely, clean up browser processes cleanly, and generate correct CI reports.

## Target Files and Modules

The codebase is located in the `/workspace` directory. The specific modules and files containing defects are:

1. **Page Object Locator**: `/workspace/tests/pages/login_page.py`
2. **Explicit Wait Utility**: `/workspace/tests/utils/waits.py`
3. **API Validation Status Code**: `/workspace/tests/api/user_client.py`
4. **CSV Test Data Mapper**: `/workspace/tests/utils/data_mapper.py`
5. **E2E Checkout Tax Logic**: `/workspace/tests/e2e/test_checkout.py`
6. **Flaky Test Retry Decorator**: `/workspace/tests/runners/retry_decorator.py`
7. **Parallel Logging Safety**: `/workspace/tests/runners/parallel_executor.py`
8. **Browser Lifecycle Teardown**: `/workspace/tests/conftest.py`
9. **HTML Reporter Calculations**: `/workspace/tests/reporting/html_reporter.py`
10. **Jenkins CI Configuration**: `/workspace/.jenkins/Jenkinsfile`

---

## Technical Specifications & Details of Defects

### 1. Page Object Locator (`tests/pages/login_page.py`)
The system fails to log in because the submit button locator is hardcoded to an outdated ID. 
- **Current state**: Uses `self.driver.find_element("id", "submit")`
- **Required fix**: Update the locator to use name `login` (e.g. `self.driver.find_element("name", "login")`), matching the updated web application specification.

### 2. Wait Utility (`tests/utils/waits.py`)
The framework experiences unnecessary slowdowns and occasional timeouts under stress due to a crude sleep.
- **Current state**: Uses a hardcoded `time.sleep(10)` inside `wait_for_element`.
- **Required fix**: Implement an explicit polling loop that checks the condition every `0.5` seconds up to a timeout of `10` seconds, returning as soon as the element is found, instead of sleeping for the full duration.

### 3. API Validation (`tests/api/user_client.py`)
The API test client fails when validating user creation because it asserts on an incorrect HTTP status code.
- **Current state**: Asserts `response.status_code == 200` after a POST request to create a user.
- **Required fix**: The user registration API now correctly returns `201` (Created). Update the assertion to expect `201`.

### 4. CSV Test Data Mapper (`tests/utils/data_mapper.py`)
The CSV data parser crashes when processing parameterized data files that contain empty lines or fields with escaped/quoted commas.
- **Current state**: Split-based line parsing `line.split(",")` without handling quotes, and no checks for empty/blank lines.
- **Required fix**: Use Python's built-in `csv.reader` to safely parse the CSV rows and skip any empty or whitespace-only lines.

### 5. E2E Checkout Tax Logic (`tests/e2e/test_checkout.py`)
International checkout orders are failing because the test asserts a hardcoded domestic tax rate.
- **Current state**: Multiplies cart total by a hardcoded `0.10` domestic tax rate.
- **Required fix**: The updated financial service API applies a dynamic tax rate of `0.12` (12%) for international checkout flows. Update the expected tax multiplier to `0.12`.

### 6. Flaky Test Retry Decorator (`tests/runners/retry_decorator.py`)
The retry decorator fails to re-run failing test cases because it catches the wrong exception type.
- **Current state**: Catches only `RuntimeError` inside the retry loop.
- **Required fix**: Pytest test failures throw `AssertionError`. Update the caught exception to either catch `AssertionError` or `Exception` (or `BaseException`) so that failed test cases are retried.

### 7. Parallel Logging Safety (`tests/runners/parallel_executor.py`)
When running tests in parallel, multiple threads write to `test_run.log` concurrently without synchronization, leading to race conditions and file write exceptions.
- **Current state**: Unlocked `open("test_run.log", "a").write(msg)` in concurrent worker threads.
- **Required fix**: Implement thread synchronization using a mutex lock (`threading.Lock()`) to guarantee that only one thread writes to the log file at a time.

### 8. Browser Lifecycle Teardown (`tests/conftest.py`)
On test failures or setup exceptions, headless browser sessions are leaked, causing container memory pressure.
- **Current state**: Bypasses the teardown block `driver.quit()` if an exception occurs during browser initialization or dynamic configuration inside the fixture.
- **Required fix**: Wrap the driver usage/yield block in a `try...finally` statement to guarantee that `driver.quit()` is executed under all circumstances.

### 9. HTML Reporter (`tests/reporting/html_reporter.py`)
The automated test report builder crashes with a division-by-zero error if a test suite execution is aborted early or no tests are run.
- **Current state**: Direct calculation `(passed_count / total_count) * 100` without checking if `total_count` is 0.
- **Required fix**: Add a safety check. If `total_count` is `0`, the pass rate should be reported as `0.0` percent.

### 10. Jenkins CI Pipeline (`.jenkins/Jenkinsfile`)
The Jenkins pipeline fails with a syntax compilation error during step parsing.
- **Current state**: Missing a closing quote or parenthesis, or has an invalid block structure under the `steps` section (e.g. `sh 'pytest --maxfail 2` without a closing quote).
- **Required fix**: Correct the syntax by ensuring all quotes and stages are properly balanced, allowing the Jenkins interpreter to parse the pipeline script cleanly.

---

## Success Criteria

Your changes will be verified by a deterministic test runner that evaluates each of the 10 components. 
- You must achieve a 100% resolution rate where all 10 independent defects are repaired.
- Each successfully fixed defect awards `0.1` points. A perfect solution receives a reward of `1.0`.
- All modifications must preserve existing valid behaviors and framework APIs. Do not delete test files or bypass validation checks entirely.
