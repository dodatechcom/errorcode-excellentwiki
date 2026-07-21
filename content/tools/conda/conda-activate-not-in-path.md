---
title: "[Solution] Conda Activate Not In PATH -- Fix PATH Configuration"
description: "Fix conda activate not in PATH errors when the environment bin directory is not prepended to PATH. Fix shell initialization."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means the activated conda environment's bin directory was not added to your PATH. Commands from the environment are not accessible.

## Common Causes

- Shell hooks are not initialized
- `.bashrc` conda block was removed or corrupted
- Running in a non-interactive shell
- PATH was modified after conda activation

## How to Fix

### 1. Reinitialize Conda

```bash
conda init bash
source ~/.bashrc
```

### 2. Manually Add to PATH

```bash
export PATH="$(conda info --base)/envs/myenv/bin:$PATH"
```

### 3. Use conda run Instead

```bash
conda run -n myenv python script.py
```

### 4. Check Current PATH

```bash
echo $PATH
```

## Examples

```bash
$ conda activate myenv
$ which python
/usr/bin/python  # Wrong -- should be in conda env

$ conda init bash && source ~/.bashrc
$ conda activate myenv
$ which python
/home/user/miniconda3/envs/myenv/bin/python
```
