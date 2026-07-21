---
title: "[Solution] pip Install From URL Failed -- Fix Direct URL Install"
description: "Fix pip install from URL failed errors when installing a package directly from a URL fails. Check URL validity and package format."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `pip install https://example.com/package.whl` failed because the URL is invalid or the file is not a valid package.

## Common Causes

- The URL points to a non-package file
- The URL requires authentication
- The file at the URL is corrupted
- The URL uses HTTP instead of HTTPS

## How to Fix

### 1. Verify the URL

```bash
curl -I https://example.com/package.whl
```

### 2. Download First

```bash
wget https://example.com/package.whl
pip install ./package.whl
```

### 3. Use GitHub Releases

```bash
pip install https://github.com/user/repo/releases/download/v1.0/package.whl
```

### 4. Add Authentication

```bash
pip install https://token@private-repo.example.com/package.whl
```

## Examples

```bash
$ pip install https://example.com/package.whl
ERROR: HTTP error 404: Not Found

$ curl -I https://example.com/package.whl
HTTP/1.1 200 OK
Content-Type: application/zip
```
