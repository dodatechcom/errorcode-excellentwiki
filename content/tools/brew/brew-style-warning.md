---
title: "[Solution] Brew Style Warning -- Fix Formula Style Issues"
description: "Fix brew style warnings when Homebrew detects style violations in a formula. Fix the Ruby code style."
tools: ["brew"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `brew style <formula>` found style violations in the formula's Ruby code.

## Common Causes

- Inefficient Ruby patterns
- Deprecated Homebrew methods
- Missing comments or documentation
- Formatting issues

## How to Fix

### 1. Auto-fix Style

```bash
brew style --fix <formula>
```

### 2. Review Warnings

```bash
brew style <formula> 2>&1
```

### 3. Follow Homebrew Style Guide

Read https://docs.brew.sh/Formula-Cookbook#style

### 4. Run RuboCop

```bash
rubocop --only FormulaAudit <formula>.rb
```

## Examples

```bash
$ brew style wget
wget.rb:15:3: W: Use `std_configure_args` instead of manual args

# Fix:
def install
  system "./configure", *std_configure_args
end
```
