---
title: "[Solution] Conda Batch Mode Error -- Fix Non-Interactive Conda Commands"
description: "Fix conda batch mode error when running conda in scripts or CI. Handle prompts and confirmations in non-interactive sessions."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means conda is trying to show an interactive prompt in a non-interactive session (like a script or CI pipeline).

## Common Causes

- conda asks for confirmation but no TTY is available
- A solver prompt requires user input
- `conda update` asks about changing default packages
- `conda clean` asks for confirmation

## How to Fix

### 1. Use -y Flag

```bash
conda install -y package
conda clean -y --all
```

### 2. Set Always-Yes

```bash
conda config --set always_yes true
```

### 3. Use --force

```bash
conda update --force conda
```

### 4. Pipe Yes to Conda

```bash
yes | conda update conda
```

## Examples

```bash
$ conda update conda
Proceed ([y]/n)?
# (hangs in CI)

$ conda config --set always_yes true
$ conda update conda
Collecting package metadata: done
```
