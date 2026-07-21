---
title: "[Solution] pip Install Timeout -- Fix Package Download Timeout"
description: "Fix pip install timeout errors when package downloads take too long and the connection times out. Increase timeout and use faster mirrors."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means pip's HTTP request to PyPI timed out before the download completed. The default timeout is 15 seconds.

## Common Causes

- Slow network connection or high latency
- PyPI server is under heavy load
- Large packages take too long to download
- Corporate proxy adds latency

## How to Fix

### 1. Increase Timeout

```bash
pip install --timeout 120 <package>
```

### 2. Use a Faster Mirror

```bash
pip install -i https://mirrors.aliyun.com/pypi/simple/ <package>
```

### 3. Download First, Then Install

```bash
pip download <package> -d ./wheels
pip install --no-index --find-links=./wheels <package>
```

### 4. Retry with Exponential Backoff

```bash
for i in 1 2 3; do
  pip install <package> && break
  sleep $((5 * i))
done
```

## Examples

```bash
$ pip install tensorflow
ReadTimeout: HTTPSConnectionPool(host='files.pythonhosted.org'): Read timed out. (read timeout=15)

$ pip install --timeout 120 tensorflow
Downloading tensorflow-2.15.0-cp311-cp311-manylinux.whl...
```
