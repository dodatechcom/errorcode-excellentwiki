---
title: "[Solution] C Makefile Error — How to Fix"
description: "Fix Makefile errors including tabs vs spaces, missing deps, and variables."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Makefile Error — How to Fix

Makefile errors include spaces instead of tabs, missing dependencies, and wrong variable expansion.

## Common Error Messages

- `missing separator`
- `recipe commenced before first target`
- `Nothing to be done`
- `implicit rule fails`

## How to Fix It

### Tab indentation

```makefile
CC=gcc
CFLAGS=-Wall -g

prog: main.o utils.o
	$(CC) $(CFLAGS) -o prog main.o utils.o

main.o: main.c utils.h
	$(CC) $(CFLAGS) -c main.c

clean:
	rm -f *.o prog
```

### Auto variables

```makefile
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@
```

### Declare PHONY

```makefile
.PHONY: all clean test
all: prog
clean:
	rm -f *.o prog
```

### Auto deps

```makefile
-include $(wildcard *.d)
%.o: %.c
	$(CC) $(CFLAGS) -MMD -MP -c $< -o $@
```

## Common Scenarios

### Scenario 1: Recipe uses spaces instead of tabs

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 2: Missing header dependency causes stale builds

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 3: Target rebuilt every time due to missing .PHONY

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

## Prevent It

- **Tip 1:** Always use tabs for recipes
- **Tip 2:** Declare phony targets
- **Tip 3:** Use -MMD -MP for auto header deps
