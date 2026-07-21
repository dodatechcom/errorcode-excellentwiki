---
title: "[Solution] Poetry Export No Requirements -- Fix Empty Export Output"
description: "Fix Poetry export produces no requirements when exporting to requirements.txt. Check pyproject.toml dependencies and lock file state."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `poetry export` produced an empty requirements.txt file. No packages were exported despite having dependencies defined.

## Common Causes

- `poetry.lock` is missing or empty
- All dependencies are in optional groups not included by default
- The --without flag excluded all packages
- The `pyproject.toml` has no dependencies defined

## How to Fix

### 1. Include All Groups

```bash
poetry export -f requirements.txt --with dev,test,all
```

### 2. Check What Would Be Exported

```bash
poetry show
```

### 3. Generate Lock File First

```bash
poetry lock
poetry export -f requirements.txt -o requirements.txt
```

### 4. Include Dev Dependencies

```bash
poetry export -f requirements.txt --with dev
```

## Examples

```bash
$ poetry export -f requirements.txt -o requirements.txt
$ cat requirements.txt
# (empty)

$ poetry show
# (empty -- lock file is missing)

$ poetry lock && poetry export -f requirements.txt -o requirements.txt
$ cat requirements.txt
requests==2.31.0
flask==3.0.0
```
