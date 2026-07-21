---
title: "[Solution] pip Requirements Cycle -- Fix Circular Dependency in Requirements"
description: "Fix pip requirements cycle errors when requirements.txt creates a circular dependency. Identify and break the cycle."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means pip's resolver detected a circular dependency chain in the packages listed in requirements.txt.

## Common Causes

- Package A depends on B which depends on A
- requirements.txt has duplicate entries with different versions
- A local package references itself

## How to Fix

### 1. Show the Dependency Tree

```bash
pip install pipdeptree
pipdeptree --warn fail
```

### 2. Identify the Cycle

```bash
pipdeptree --packages <package>
```

### 3. Remove the Circular Dependency

Edit requirements.txt or the offending package's dependencies.

### 4. Install Packages One at a Time

```bash
while read line; do pip install "$line"; done < requirements.txt
```

## Examples

```bash
$ pip install -r requirements.txt
ERROR: pip's dependency resolver found a circular dependency

$ pip install pipdeptree
$ pipdeptree --warn fail
# Shows the circular chain
```
