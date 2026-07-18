---
title: "[Solution] Poetry Script Not Found in Poetry Run Error — How to Fix"
description: "Fix Poetry run script not found errors. Resolve missing script entries, entry point issues, and command execution failures in Poetry projects."
tools: ["poetry"]
error-types: ["run-error"]
severities: ["error"]
weight: 5
comments: true
---

This error means `poetry run` could not find the script or command you specified. The script is not defined in your project's entry points, is not installed in the virtual environment, or the package providing it is not installed.

## Why It Happens

- The script is not defined in `[tool.poetry.scripts]` in `pyproject.toml`
- The package that provides the script is not installed or not listed as a dependency
- You are running a script before `poetry install` has been executed
- The script name is misspelled or uses a different name than expected
- The virtual environment does not contain the script's package
- The script is defined in a dependency's `pyproject.toml` but that dependency is not installed

## Common Error Messages

```
Exception in thread Thread-1:
FileNotFoundError: [Errno 2] No such file or directory: 'package-name'
```

```
RuntimeError

Package "package-name" is not installed.
```

```
CommandNotFound

Command 'my-script' not found in the virtual environment.
```

```
poetry run: command not found: my-script
```

## How to Fix It

### 1. Check if Scripts Are Defined

```bash
grep -A 20 "\[tool.poetry.scripts\]" pyproject.toml
```

Ensure your script is listed:

```toml
[tool.poetry.scripts]
my-script = "package.module:main"
```

### 2. Install the Package in Development Mode

```bash
poetry install
```

This installs your project's package and registers its scripts.

### 3. Check Available Scripts

```bash
poetry run which my-script
poetry run pip show package-name
```

### 4. Run the Script Directly via Python

```bash
poetry run python -m package.module
```

Or:

```bash
poetry run python -c "from package.module import main; main()"
```

### 5. Reinstall After Changing Scripts

```bash
poetry install
poetry run my-script
```

If you modified `pyproject.toml` after the initial install, re-run `poetry install`.

### 6. Check the Virtual Environment

```bash
poetry env info
ls $(poetry env info -p)/bin/ | grep my-script
```

If the script is not in the venv's `bin/` directory, the package providing it is not installed.

### 7. Run Without `poetry run`

```bash
# Find the script directly
poetry run which python
poetry run python -m package.module
```

## Common Scenarios

**New project script not found.** Run `poetry install` after defining scripts in `pyproject.toml` to register them:

```bash
poetry install
poetry run my-script
```

**Third-party script not found.** The package providing the script may not be a direct dependency. Add it:

```bash
poetry add package-name
poetry run package-name  # should now work
```

**Script works locally but not in CI.** Ensure `poetry install` runs before attempting to use scripts:

```yaml
# GitHub Actions example
- run: |
    poetry install
    poetry run my-script
```

## Prevent It

1. Always run `poetry install` after modifying `[tool.poetry.scripts]` in `pyproject.toml`
2. Use `poetry run python -m package.module` as a fallback when script names are uncertain
3. Define all script entry points explicitly in `pyproject.toml` rather than relying on implicit discovery
