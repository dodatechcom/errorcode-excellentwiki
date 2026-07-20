---
title: "[Solution] Apache SSLCACertificatePath Invalid"
description: "The directory specified for CA certificates does not exist or has incorrect format."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The directory specified for CA certificates does not exist or has incorrect format.

## Common Causes

- Directory does not exist
- CA certificate files are not in hashed format
- File permissions prevent Apache from reading

## How to Fix

- Create the directory and run: c_rehash /path/to/ca/
- Use SSLCACertificateFile for a single bundle instead
- Verify with: ls -la /path/to/ca/

## Examples

```
['mkdir -p /etc/ssl/cacerts\nc_rehash /etc/ssl/cacerts\nSSLCACertificatePath /etc/ssl/cacerts']
```
