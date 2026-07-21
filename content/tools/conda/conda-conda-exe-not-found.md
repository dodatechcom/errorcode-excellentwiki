---
title: "[Solution] Conda Exe Not Found -- Fix Conda Executable Missing"
description: "Fix conda exe not found errors when the conda executable cannot be located. Check installation and PATH configuration."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means the system cannot find the `conda` executable. The shell cannot locate conda to run any commands.

## Common Causes

- Conda was not installed properly
- The installation directory is not in PATH
- A recent shell update removed conda from PATH
- The conda binary was deleted or moved

## How to Fix

### 1. Find Conda Installation

```bash
find / -name "conda" -type f 2>/dev/null
```

### 2. Add Conda to PATH

```bash
export PATH="$HOME/miniconda3/bin:$PATH"
```

### 3. Source Conda Init

```bash
source ~/miniconda3/etc/profile.d/conda.sh
```

### 4. Reinstall Miniconda

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

## Examples

```bash
$ conda --version
bash: conda: command not found

$ export PATH="$HOME/miniconda3/bin:$PATH"
$ conda --version
conda 24.1.0
```
