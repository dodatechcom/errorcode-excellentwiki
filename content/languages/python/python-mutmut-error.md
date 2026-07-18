---
title: "Solved Python Mutmut Error — How to Fix"
date: 2026-03-15T11:25:45+00:00
description: "Learn how to resolve Python Mutmut mutation testing errors, configuration issues, and false positives."
categories: ["python"]
keywords: ["python mutmut", "mutmut error", "mutation testing", "mutmut configuration", "mutmut false positive"]
error-types: ["runtime-error"]
severities: ["error"]
languages: ["python"]
weight: 5
comments: true
---

## Why It Happens

Mutmut errors occur during mutation testing when the tool cannot properly generate or apply mutations, or when the test suite fails to catch deliberate bugs. Configuration issues and incompatible code patterns are common culprits.

Common causes include:
- Mutmut configuration pointing to non-existent source directories
- Tests not properly covering edge cases making mutations survive
- Mutations in unreachable code or dead code paths
- Conflicts with decorators or metaclasses during AST mutation
- Large codebases causing excessive mutation count

## Common Error Messages

```bash
# No modules to mutate
$ mutmut
No modules to mutate
```

```bash
# Mutmut configuration error
$ mutmut run
Could not find source path for module: mypackage
```

```bash
# Timeout during mutation testing
$ mutmut run
Killed: process timed out after 60 seconds
```

## How to Fix It

### 1. Configure Mutmut Properly

Create a proper `mutmut.yml` configuration file.

```yaml
# mutmut.yml
paths_to_mutate:
  - src/
backup: false
runner: python -m pytest
tests_dir: tests/
min_similarity_time: 0.0
preload_modules:
  - mypackage
exclude_patterns:
  - "*/tests/*"
  - "*/__pycache__/*"
  - "*/migrations/*"
  - "conftest.py"
use_coverage: true
coverage_source: mypackage
```

```python
# Alternative: setup.cfg configuration
# setup.cfg
[mutmut]
paths_to_mutate = src/
tests_dir = tests/
runner = pytest --tb=short -x
exclude_patterns = */tests/*, */__pycache__/*
```

### 2. Improve Test Coverage to Kill Mutations

Add targeted tests that catch specific mutation types.

```python
# Original source: calculator.py
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

# Weak test - mutation survives
def test_divide():
    assert divide(10, 2) == 5

# Strong test - catches mutations
def test_divide_catches_mutations():
    assert divide(10, 2) == 5
    assert divide(10, 3) == 10 / 3  # Catches operator mutations
    assert divide(-10, 2) == -5     # Catches sign mutations
    assert divide(0, 5) == 0        # Catches boundary mutations
    
    with pytest.raises(ValueError):
        divide(10, 0)  # Catches condition mutations
    
    assert divide(10, 1) == 10     # Catches identity mutations
    assert divide(5, 5) == 1       # Catches comparison mutations
```

### 3. Run Mutmut with Performance Optimization

Use parallel execution and filtering for large codebases.

```bash
# Run with limited scope
mutmut run --paths-to-mute src/module.py

# Run in parallel with coverage
mutmut run --use-coverage --runner "pytest -n auto"

# Check results
mutmut results

# Show surviving mutations
mutmut show surviving

# Apply a surviving mutation for review
mutmut apply 42
```

```python
# Custom runner script for better control
# run_mutmut.py
import subprocess
import sys

def main():
    cmd = [
        "mutmut", "run",
        "--paths-to-mute", "src/",
        "--tests-dir", "tests/",
        "--runner", "python -m pytest tests/ -x -q",
        "--exclude-patterns", "*/tests/*,*/conftest.py",
        "--use-coverage"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    
    # Parse results
    results_cmd = ["mutmut", "results"]
    result = subprocess.run(results_cmd, capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    main()
```

## Common Scenarios

### Scenario 1: CI/CD Integration

Running mutation testing in CI pipelines:

```yaml
# .github/workflows/mutation-testing.yml
name: Mutation Testing
on: [pull_request]

jobs:
  mutmut:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install mutmut pytest pytest-cov
      - run: mutmut run --use-coverage
      - run: |
          SURVIVING=$(mutmut results 2>/dev/null | grep "survived" | wc -l)
          if [ "$SURVIVING" -gt 0 ]; then
            echo "Found $SURVIVING surviving mutations"
            mutmut show surviving
            exit 1
          fi
```

### Scenario 2: Filtering Mutations

Exclude irrelevant mutations to focus on critical code.

```python
# Add mutation markers to source code
def critical_function(data):
    # mutmut: no-cover
    logging.debug(f"Debug: {data}")
    
    result = process(data)  # This will be mutated
    return result

# In mutmut.yml, also exclude:
# exclude_patterns:
#   - "*/utils/*"
#   - "*_compat.py"
```

## Prevent It

- Start mutation testing with small, well-tested modules before expanding
- Use `--paths-to-mute` to focus on critical code paths first
- Add boundary condition tests that catch comparison operator mutations
- Configure `exclude_patterns` to skip migrations, configs, and generated code
- Set up CI checks to prevent surviving mutations from being merged