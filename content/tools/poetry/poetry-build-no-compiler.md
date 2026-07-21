---
title: "[Solution] Poetry Build No Compiler -- Fix Missing C Compiler"
description: "Fix Poetry build no compiler errors when building packages that require C compilation. Install GCC or the platform compiler."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry tried to build a package with C extensions but could not find a C compiler. The build fails immediately.

## Common Causes

- `gcc` or `cc` is not installed
- Xcode Command Line Tools are not installed on macOS
- The compiler is not in PATH
- Build essentials package is missing

## How to Fix

### 1. Install GCC on Linux

```bash
sudo apt install build-essential
```

### 2. Install Xcode Tools on macOS

```bash
xcode-select --install
```

### 3. Install Specific Compiler

```bash
# Debian/Ubuntu
sudo apt install gcc g++

# CentOS/RHEL
sudo yum groupinstall "Development Tools"
```

### 4. Use Only Binary Wheels

```bash
pip install --only-binary=:all: <package>
```

## Examples

```bash
$ poetry install
error: command 'gcc' failed: No such file or directory

$ sudo apt install build-essential
$ poetry install
Installing dependencies from lock file (use --sync to update)...
```
