---
title: "[Solution] Poetry Shell No Virtualenv -- Fix poetry shell Missing Venv"
description: "Fix poetry shell no virtualenv errors when there is no virtual environment to activate. Create the venv first with poetry install."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `poetry shell` was run but no virtual environment exists for the current project. Poetry cannot activate a non-existent venv.

## Common Causes

- You never ran `poetry install` for this project
- The virtual environment was deleted
- You are in a different directory than the project root
- `poetry.toml` disables virtualenv creation

## How to Fix

### 1. Create the Virtualenv

```bash
poetry install
```

### 2. Check for Existing Venv

```bash
poetry env info
```

### 3. Manually Activate

```bash
source $(poetry env info --path)/bin/activate
```

### 4. Configure In-Project Venv

```bash
poetry config virtualenvs.in-project true
poetry install
poetry shell
```

## Examples

```bash
$ poetry shell
VirtualenvNotFoundError: No virtualenv found for this project

$ poetry install
Creating virtualenv myproject-py3.11

$ poetry shell
Spawning shell within /home/user/.cache/pypoetry/virtualenvs/myproject-py3.11
```
