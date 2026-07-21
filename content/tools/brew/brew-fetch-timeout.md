---
title: "[Solution] Brew Fetch Timeout -- Fix Download Timeout Error"
description: "Fix brew fetch timeout errors when downloading formula bottles or source tarballs takes too long. Configure timeouts and mirrors."
tools: ["brew"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Homebrew timed out while downloading a formula's bottle or source code.

## Common Causes

- Slow network connection
- Homebrew server is under load
- Large formula download takes too long
- Corporate proxy adds latency

## How to Fix

### 1. Retry the Install

```bash
brew install <formula>
```

### 2. Use a Faster Mirror

```bash
export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles
```

### 3. Build from Source

```bash
brew install --build-from-source <formula>
```

### 4. Check Homebrew Servers

```bash
curl -I https://formulae.brew.sh/api/formula/<formula>.json
```

## Examples

```bash
$ brew install wget
Error: Fetching /usr/local/opt/wget failed: timeout

$ export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles
$ brew install wget
```
