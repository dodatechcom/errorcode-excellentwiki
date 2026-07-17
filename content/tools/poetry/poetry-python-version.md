---
title: "[Solution] Poetry Python Version Error — Fix Incompatible Python Versions"
description: "Fix Poetry Python version errors when no installed Python version satisfies the project constraint. Install and configure the correct Python interpreter."
tools: ["poetry"]
error-types: ["version-error"]
severities: ["error"]
weight: 5
---

This error means Poetry cannot find an installed Python version that satisfies the version constraint defined in `pyproject.toml`. The resolver refuses to create a virtual environment or install packages.

## What This Error Means

Poetry checks every Python interpreter on your system against the `python` constraint in `pyproject.toml`. When none match, you see:

```
PythonVersionError

Poetry requires Python [constraint], but the running Python is [installed-version]
```

Or:

```
SolverProblemError

No python version found that satisfies the constraint python = "^3.11"
```

## Why It Happens

- The project requires Python 3.10+ but only Python 3.8 is installed
- You upgraded `pyproject.toml` to require a newer Python but did not install it
- The system Python version does not match the one Poetry locates via `pyenv` or `asdf`
- On macOS, the Xcode Command Line Tools ship an older Python that Poetry picks up first

## How to Fix It

### Check Your Current Python Versions

```bash
python3 --version
pyenv versions
```

### Install the Required Python Version

```bash
pyenv install 3.11.4
pyenv local 3.11.4
```

Or with `asdf`:

```bash
asdf install python 3.11.4
asdf local python 3.11.4
```

### Tell Poetry to Use a Specific Python

```bash
poetry env use /path/to/python3.11
```

Or by version number:

```bash
poetry env use python3.11
```

### Relax the Python Constraint

Edit `pyproject.toml`:

```
[tool.poetry.dependencies]
python = "^3.8"
```

Widening from `^3.11` to `^3.8` allows Poetry to use older Pythons if that is acceptable for your project.

### Verify Poetry Sees the Correct Interpreter

```bash
poetry env info
```

This shows the Python version Poetry plans to use, the venv path, and the platform.

### On macOS: Avoid the System Python

```bash
# Check which Python Poetry resolves to
which poetry
poetry env info --full-path

# If it points to /usr/bin/python3, override it
poetry env use $(brew --prefix)/bin/python3.11
```

## Common Mistakes

- Editing `pyproject.toml` to require a Python version without installing it
- Running `poetry env use` with a version not installed by `pyenv` or `asdf`
- Not checking `poetry env info` after changing the Python constraint
- Assuming `python3` in the shell is the same Python Poetry uses

## Related Pages

- [Poetry Venv Error]({{< relref "/tools/poetry/poetry-venv-error" >}}) -- virtual environment creation failed
- [Poetry Install Error]({{< relref "/tools/poetry/poetry-install-error" >}}) -- install failures
- [Poetry Dependency Conflict]({{< relref "/tools/poetry/poetry-dependency-conflict" >}}) -- resolver conflicts
