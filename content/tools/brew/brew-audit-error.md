---
title: "[Solution] Brew Audit Error -- Fix Formula Audit Failure"
description: "Fix brew audit errors when Homebrew audits find issues in a formula. Fix the identified problems."
tools: ["brew"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `brew audit <formula>` found errors or warnings that need to be fixed.

## Common Causes

- Deprecated API usage
- Missing license declaration
- Incorrect checksum
- Version scheme issues

## How to Fix

### 1. Run Audit

```bash
brew audit <formula>
```

### 2. Fix Specific Issues

```bash
# Add missing license
head -5 <formula>.rb
# Should include: license "MIT"
```

### 3. Checksum Update

```bash
brew fetch --build-from-source <formula>
# Compare new checksum with formula
```

### 4. Allow Specific Warnings

```bash
brew audit --except=strict <formula>
```

## Examples

```bash
$ brew audit wget
Error: Missing license in wget.rb

# Add to formula:
license "GPL-3.0-or-later"
```
