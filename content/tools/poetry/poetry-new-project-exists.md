---
title: "[Solution] Poetry New Project Exists -- Fix Directory Already Created"
description: "Fix poetry new project exists error when the target directory already exists. Use --name or create in a different location."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `poetry new <project-name>` was run but a directory with that name already exists. Poetry refuses to overwrite existing content.

## Common Causes

- The project was already created previously
- A directory with the same name exists for another purpose
- A failed previous attempt left a partial directory

## How to Fix

### 1. Remove the Existing Directory

```bash
rm -rf existing-project
poetry new existing-project
```

### 2. Use a Different Name

```bash
poetry new my-new-project
```

### 3. Create in a Subdirectory

```bash
poetry new projects/my-new-project
```

### 4. Initialize in Existing Directory

```bash
cd existing-directory
poetry init
```

## Examples

```bash
$ poetry new myproject
A "myproject" directory already exists.

$ rm -rf myproject
$ poetry new myproject
Created package myproject in myproject
```
