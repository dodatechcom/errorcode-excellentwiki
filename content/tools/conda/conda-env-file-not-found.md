---
title: "[Solution] Conda Env File Not Found -- Fix Missing environment.yml"
description: "Fix conda env file not found errors when conda cannot locate environment.yml. Specify the correct file path."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `conda env create -f environment.yml` was run but the file does not exist at the specified path.

## Common Causes

- The file was deleted or never created
- You are in the wrong directory
- The filename is different (e.g., `env.yml`)
- The file extension is wrong

## How to Fix

### 1. Check File Exists

```bash
ls -la environment.yml
```

### 2. Export Current Environment

```bash
conda env export > environment.yml
```

### 3. Specify the Correct Path

```bash
conda env create -f /path/to/environment.yml
```

### 4. Use a Different Filename

```bash
conda env create -f env.yml
```

## Examples

```bash
$ conda env create -f environment.yml
FileNotFoundError: environment.yml not found

$ ls *.yml
env.yml

$ conda env create -f env.yml
Collecting package metadata: done
Solving environment: done
```
