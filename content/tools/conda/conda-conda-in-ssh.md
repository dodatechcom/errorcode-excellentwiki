---
title: "[Solution] Conda In SSH -- Fix Conda in SSH Sessions"
description: "Fix conda in SSH errors when conda commands fail in SSH sessions due to missing shell initialization. Initialize conda for non-interactive shells."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means conda is not available or does not work correctly in SSH sessions because shell initialization is missing.

## Common Causes

- `.bashrc` has an interactive check that skips conda init
- SSH session does not source the conda profile
- The shell is non-interactive and conda init block is guarded

## How to Fix

### 1. Check .bashrc for Guard

Look for lines like `[ -z "$PS1" ] && return` that skip conda initialization in non-interactive shells.

### 2. Move Conda Init Above the Guard

Move the conda initialization block to the top of `.bashrc`.

### 3. Source Conda Manually

```bash
source ~/miniconda3/etc/profile.d/conda.sh
conda activate myenv
```

### 4. Use SSH with Login Shell

```bash
ssh -t user@host "bash -l -c 'conda activate myenv && command'"
```

## Examples

```bash
$ ssh user@server
$ conda activate myenv
CommandNotFoundError: 'conda' does not exist

# Fix: Move conda init block to the top of .bashrc
```
