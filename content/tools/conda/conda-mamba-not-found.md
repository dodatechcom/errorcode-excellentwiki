---
title: "[Solution] Conda Mamba Not Found -- Fix Missing Mamba Solver"
description: "Fix conda mamba not found errors when mamba is not installed. Install mamba as a faster alternative to the conda solver."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means the `mamba` command is not installed or not in your PATH. Mamba is a faster drop-in replacement for conda.

## Common Causes

- Mamba was never installed
- Mamba is installed in a different environment
- The PATH does not include mamba's location
- Miniforge was not installed

## How to Fix

### 1. Install Mamba

```bash
conda install -n base -c conda-forge mamba
```

### 2. Use conda-libmamba-solver Instead

```bash
conda install -n base -c conda-forge conda-libmamba-solver
conda config --set solver libmamba
```

### 3. Install Miniforge

```bash
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
bash Miniforge3-Linux-x86_64.sh
```

### 4. Verify Installation

```bash
mamba --version
```

## Examples

```bash
$ mamba install numpy
bash: mamba: command not found

$ conda install -n base -c conda-forge mamba
$ mamba --version
mamba 1.5.3
$ mamba install numpy
```
