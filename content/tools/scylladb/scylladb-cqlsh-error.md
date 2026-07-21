---
title: "[Solution] ScyllaDB cqlsh Error"
description: "How to fix ScyllaDB cqlsh client errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- cqlsh version mismatch with server
- Connection refused
- Python dependencies missing
- Wrong credentials

## How to Fix

Test connection:

```bash
cqlsh localhost 9042
```

Install correct version:

```bash
pip install cqlsh==6.2.0
```

## Examples

```bash
cqlsh --version
cqlsh -u admin -p secret localhost 9042
```
