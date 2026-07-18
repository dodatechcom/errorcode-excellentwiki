---
title: "[Solution] C pkg-config Error — How to Fix"
description: "Fix pkg-config errors including missing .pc files and wrong paths."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C pkg-config Error — How to Fix

pkg-config provides compiler flags. Errors include .pc not found and wrong version requirements.

## Common Error Messages

- `Package libfoo was not found`
- `requires newer version`
- `PKG_CONFIG_PATH not set`
- `No package found`

## How to Fix It

### Set PKG_CONFIG_PATH

```bash
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:$PKG_CONFIG_PATH
pkg-config --cflags --libs libfoo
```

### Makefile usage

```makefile
CC=gcc
CFLAGS=$(shell pkg-config --cflags libfoo)
LDFLAGS=$(shell pkg-config --libs libfoo)

prog: main.o
	$(CC) -o prog main.o $(LDFLAGS)
```

### Check version

```bash
pkg-config --modversion libfoo
```

### Debug

```bash
pkg-config --list-all | grep foo
```

## Common Scenarios

### Scenario 1: .pc file not in standard path

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 2: Version requirement too high

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 3: Not using pkg-config output

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

## Prevent It

- **Tip 1:** Set PKG_CONFIG_PATH for custom locations
- **Tip 2:** Use pkg-config --cflags and --libs
- **Tip 3:** Check with pkg-config --list-all
