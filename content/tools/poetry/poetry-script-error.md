---
title: "[Solution] Poetry Script Error - Fix Script Not Found or Entry Point Error"
description: "Fix Poetry script not found errors and entry point configuration issues. Resolve missing console scripts and broken poetry run commands."
tools: ["poetry"]
error-types: ["script-error"]
severities: ["error"]
weight: 5
---

This error means Poetry cannot find or execute a script entry point defined in your project. The console script is either not registered, the module path is wrong, or the project is not installed in the current environment.

## What This Error Means

When you run `poetry run <script>` or install a package that defines console_scripts and the entry point is invalid, you see:

```
PoetryException: Failed to run the command: ...
# or
bash: <script>: command not found
# or
ModuleNotFoundError: No module named '<module>'
```

This happens because the entry point module path does not resolve to a callable function, or the package was never installed with its entry points registered.

## Why It Happens

- The `packages` configuration in `pyproject.toml` does not include the module containing the entry point
- The module path in `[tool.poetry.scripts]` is misspelled
- The package was installed via pip instead of `poetry install`
- The virtual environment does not have the package installed
- The entry point function was renamed or moved but the script definition was not updated
- A dependency that provides the script was removed from the lock file

## How to Fix It

### Verify the scripts section

```toml
[tool.poetry.scripts]
my-command = "my_package.cli:main"
```

Ensure the module path `my_package.cli` matches the actual file and `main` is a callable function.

### Reinstall the package

```bash
poetry install
```

This registers all console scripts from `pyproject.toml` in the virtual environment.

### Check if the script is installed

```bash
poetry run which <script-name>
poetry run pip show <package-name>
```

If the script is not found, the package may not be installed correctly.

### Verify the package structure

```toml
[tool.poetry]
packages = [{include = "my_package"}]
```

If your package directory does not match the project name, you must specify `packages` explicitly.

### Test the entry point directly

```bash
poetry run python -c "from my_package.cli import main; main()"
```

If this works but `poetry run my-command` does not, the script registration is broken.

### Use poetry run with the full module path

```bash
poetry run python -m my_package.cli
```

This bypasses the entry point system entirely as a temporary workaround.

## Common Mistakes

- Typo in the module path under `[tool.poetry.scripts]`
- Forgetting that `packages` must include the module that defines the entry point
- Installing with `pip install -e .` instead of `poetry install` which does not register scripts
- Not running `poetry install` after changing script definitions
- Assuming scripts work outside the virtual environment created by Poetry

## Related Pages

- [Poetry Install Error]({{< relref "/tools/poetry/poetry-install-error" >}}) -- installation failures
- [Poetry Build Error]({{< relref "/tools/poetry/poetry-build-error" >}}) -- build failures
- [Poetry Venv Error]({{< relref "/tools/poetry/poetry-venv-error" >}}) -- virtual environment issues
