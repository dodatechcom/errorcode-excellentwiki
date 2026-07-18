---
title: "Solved Python Coverage Error — How to Fix"
date: 2026-03-15T11:30:20+00:00
description: "Learn how to resolve Python coverage.py measurement errors, configuration issues, and reporting failures."
categories: ["python"]
keywords: ["python coverage", "coverage.py error", "code coverage", "coverage configuration", "coverage reporting"]
error-types: ["runtime-error"]
severities: ["error"]
languages: ["python"]
weight: 5
comments: true
---

## Why It Happens

Coverage.py errors arise from incorrect configuration, file path mismatches, or incompatibilities with specific code patterns. The tool may fail to measure coverage accurately or report misleading results.

Common causes include:
- Source paths not correctly specified in configuration
- C extensions or compiled code cannot be traced
- Coverage data from different runs not properly combined
- Subprocess or multiprocessing code not being measured
- Branch coverage conflicting with line coverage settings

## Common Error Messages

```bash
$ coverage run -m pytest
No data was collected
```

```bash
# Coverage configuration error
$ coverage report
Cannot use --omit with --include
```

```bash
# Branch coverage issues
$ coverage run --branch -m pytest
Coverage.py warning: Couldn't parse source file
```

## How to Fix It

### 1. Configure Coverage Correctly

Use `pyproject.toml` or `.coveragerc` for proper configuration.

```toml
# pyproject.toml
[tool.coverage.run]
source = ["src/mypackage"]
branch = true
parallel = true
omit = [
    "*/tests/*",
    "*/migrations/*",
    "*/__pycache__/*",
    "setup.py",
    "conftest.py"
]

[tool.coverage.report]
precision = 2
show_missing = true
skip_covered = true
fail_under = 80
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if self.debug:",
    "raise NotImplementedError",
    "pass",
    "except ImportError:"
]

[tool.coverage.html]
directory = "htmlcov"

[tool.coverage.xml]
output = "coverage.xml"
```

```python
# Alternative: .coveragerc file
# [run]
# source = src/mypackage
# branch = true
# omit = */tests/*
#
# [report]
# show_missing = true
# fail_under = 80
```

### 2. Handle Subprocess Coverage

Measure coverage across multiple processes.

```python
# conftest.py
import coverage
import os

def pytest_configure(config):
    os.environ["COVERAGE_PROCESS_START"] = "pyproject.toml"

# In your subprocess code
import coverage
coverage.process_startup()
```

```toml
# pyproject.toml additions for subprocess
[tool.coverage.run]
source = ["src"]
concurrency = ["thread", "greenlet", "gevent"]

[tool.coverage.paths]
source = [
    "src/mypackage",
    "*/site-packages/mypackage"
]
```

```bash
# Combine coverage from parallel runs
coverage combine
coverage report
coverage html
```

### 3. Use Coverage API for Programmatic Control

Access coverage data directly in code.

```python
import coverage
import json

def measure_coverage(target_func, *args, **kwargs):
    cov = coverage.Coverage(branch=True)
    cov.start()
    
    result = target_func(*args, **kwargs)
    
    cov.stop()
    cov.save()
    
    # Get coverage data
    data = cov.get_data()
    file_coverage = {}
    
    for filename in data.measured_files():
        if "mypackage" in filename:
            lines = data.lines(filename)
            file_coverage[filename] = {
                "executed_lines": sorted(lines),
                "total_statements": len(lines)
            }
    
    # Generate report
    from coverage import SummaryReporter
    import io
    
    buffer = io.StringIO()
    reporter = SummaryReporter(cov, fileobj=buffer)
    reporter.report([cov])
    
    return {
        "result": result,
        "coverage_summary": buffer.getvalue(),
        "file_details": file_coverage
    }

# Usage
result = measure_coverage(my_function, arg1, arg2)
print(result["coverage_summary"])
```

## Common Scenarios

### Scenario 1: Measuring Test Coverage with Unittest

```python
import coverage
import unittest
import sys

def run_with_coverage():
    cov = coverage.Coverage(
        source=["src/mypackage"],
        branch=True,
        omit=["*/tests/*"]
    )
    cov.start()
    
    loader = unittest.TestLoader()
    suite = loader.discover("tests", pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    cov.stop()
    cov.save()
    
    print("\nCoverage Report:")
    cov.report(show_missing=True)
    
    cov.html_report(directory="htmlcov")
    cov.xml_report(outfile="coverage.xml")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_with_coverage()
    sys.exit(0 if success else 1)
```

### Scenario 2: CI Coverage with Threshold Enforcement

```python
# check_coverage.py
import coverage
import sys
import json

def check_coverage_threshold(threshold=80):
    cov = coverage.Coverage()
    cov.load()
    
    report = cov.report()
    
    if report < threshold:
        print(f"Coverage {report:.1f}% is below threshold {threshold}%")
        
        # Generate detailed report
        missing = {}
        data = cov.get_data()
        for filename in data.measured_files():
            analysis = cov._analyze(filename)
            if analysis and analysis.missing:
                missing[filename] = analysis.missing
        
        print("\nFiles with missing coverage:")
        for f, lines in missing.items():
            print(f"  {f}: lines {lines}")
        
        return False
    
    print(f"Coverage {report:.1f}% meets threshold {threshold}%")
    return True

if __name__ == "__main__":
    success = check_coverage_threshold(80)
    sys.exit(0 if success else 1)
```

## Prevent It

- Always use `branch = true` for more accurate coverage measurement
- Set `fail_under` threshold to enforce minimum coverage in CI
- Use `coverage combine` when measuring across multiple test runs
- Exclude generated code, migrations, and test utilities from coverage
- Run `coverage html` to visually inspect uncovered code paths