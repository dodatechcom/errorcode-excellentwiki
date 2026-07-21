---
title: "[Solution] Poetry Script Exit Code -- Fix Non-Zero Exit from poetry run"
description: "Fix poetry run exit code errors when a command run via poetry run returns a non-zero exit status. Debug the underlying command."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means the command executed by `poetry run` exited with a non-zero status code. Poetry propagates the exit code to the calling shell.

## Common Causes

- The script encountered a runtime error
- A test suite failed
- The application requires environment variables not set
- The script depends on resources not available

## How to Fix

### 1. Check the Exit Code

```bash
poetry run <command>
echo $?
```

### 2. Run with Verbose Output

```bash
poetry run -vvv <command>
```

### 3. Check Environment Variables

```bash
poetry run env | grep -i myapp
```

### 4. Run the Script Directly in the Venv

```bash
$(poetry env info --path)/bin/<command>
```

## Examples

```bash
$ poetry run python app.py
Exit code: 1

# Add debug output:
$ poetry run python -c "import myapp; print(myapp.__version__)"
ModuleNotFoundError: No module named 'myapp'

$ poetry install
$ poetry run python app.py
Server started on port 8000
```
