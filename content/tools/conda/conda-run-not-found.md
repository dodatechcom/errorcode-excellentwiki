---
title: "[Solution] Conda Run Not Found -- Fix conda run Command Issues"
description: "Fix conda run not found errors when conda run cannot find the specified command or package in the target environment."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `conda run -n envname command` failed because the command does not exist in the target environment.

## Common Causes

- The command is not installed in the target environment
- The command name is misspelled
- The environment does not have the required packages
- The command requires activation that conda run does not provide

## How to Fix

### 1. Check Installed Packages

```bash
conda run -n myenv conda list | grep command
```

### 2. Install the Command

```bash
conda install -n myenv package-name
```

### 3. Use the Full Path

```bash
conda run -n myenv $(conda info --base)/envs/myenv/bin/command
```

### 4. Activate Instead

```bash
source $(conda info --base)/etc/profile.d/conda.sh
conda activate myenv
command
```

## Examples

```bash
$ conda run -n myenv jupyter notebook
CommandNotFoundError: 'jupyter' not found in environment 'myenv'

$ conda install -n myenv jupyter
$ conda run -n myenv jupyter notebook
```
