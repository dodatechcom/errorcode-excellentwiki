---
title: "[Solution] Conda Not On PATH -- Fix PATH Missing Conda"
description: "Fix conda not on PATH errors when the conda executable is not in the system PATH. Add conda to PATH permanently."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means the shell cannot find `conda` because its installation directory is not in PATH.

## Common Causes

- PATH was not updated after installation
- `.bashrc` does not include the conda PATH
- Using a custom installation directory
- Shell profile was overwritten

## How to Fix

### 1. Add Miniconda to PATH

```bash
echo 'export PATH="$HOME/miniconda3/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### 2. Run conda init

```bash
~/miniconda3/bin/conda init bash
source ~/.bashrc
```

### 3. Use Full Path

```bash
~/miniconda3/bin/conda activate myenv
```

### 4. Create a Symlink

```bash
sudo ln -s ~/miniconda3/bin/conda /usr/local/bin/conda
```

## Examples

```bash
$ conda --version
bash: conda: command not found

$ echo 'export PATH="$HOME/miniconda3/bin:$PATH"' >> ~/.bashrc
$ source ~/.bashrc
$ conda --version
conda 24.1.0
```
