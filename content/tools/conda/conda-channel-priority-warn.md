---
title: "[Solution] Conda Channel Priority Warning -- Fix Channel Mixing Warning"
description: "Fix conda channel priority warning when mixing channels without strict priority. Set channel priority to strict mode."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means conda is warning about packages being pulled from different channels without strict priority ordering. This can cause inconsistent installs.

## Common Causes

- Using both defaults and conda-forge channels
- Channel priority is set to flexible (default)
- Packages exist on multiple channels with different versions

## How to Fix

### 1. Set Strict Channel Priority

```bash
conda config --set channel_priority strict
```

### 2. Use Only One Channel

```bash
conda config --remove channels defaults
conda config --add channels conda-forge
```

### 3. Pin Channel per Package

```bash
conda install -c conda-forge numpy
conda install -c defaults scipy
```

### 4. Verify Channel Order

```bash
conda config --show channels
conda config --show channel_priority
```

## Examples

```bash
$ conda install numpy
Warning: numpy pulled from conda-forge, not defaults

$ conda config --set channel_priority strict
$ conda install numpy
Solving environment: done
```
