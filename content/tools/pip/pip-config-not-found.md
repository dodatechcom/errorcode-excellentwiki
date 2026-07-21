---
title: "[Solution] pip Config Not Found -- Fix pip Configuration File Missing"
description: "Fix pip config not found errors when pip cannot locate its configuration file. Create or specify the correct config path."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means pip tried to read a configuration file that does not exist at the specified path.

## Common Causes

- The config file was deleted
- PIP_CONFIG_FILE environment variable points to wrong path
- Global pip.conf was removed

## How to Fix

### 1. Check Config Location

```bash
pip config list
pip config debug
```

### 2. Create Default Config

```bash
pip config set global.timeout 60
```

### 3. Set Environment Variable

```bash
export PIP_CONFIG_FILE=/path/to/pip.conf
```

### 4. Reset to Defaults

```bash
pip config unset global.index-url
```

## Examples

```bash
$ pip install requests
ConfigurationError: Config file not found at /etc/pip.conf

$ pip config debug
global.index-url = 'https://pypi.org/simple'

$ pip install requests
Successfully installed requests-2.31.0
```
