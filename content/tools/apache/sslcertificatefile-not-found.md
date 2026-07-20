---
title: "[Solution] Apache SSLCertificateFile Not Found"
description: "The SSL certificate file specified does not exist or is not readable by Apache."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The SSL certificate file specified does not exist or is not readable by Apache.

## Common Causes

- File path is incorrect or typo
- Certificate file was deleted or not yet generated
- File permissions prevent Apache from reading it
- SELinux context is wrong

## How to Fix

- Verify the file path and existence
- Check permissions: ls -la /path/to/cert.pem
- Regenerate or re-download the certificate
- Fix SELinux: restorecon -Rv /etc/ssl/

## Examples

```
['SSLCertificateFile /etc/ssl/certs/ssl-cert-snakeoil.pem\nSSLCertificateKeyFile /etc/ssl/private/ssl-cert-snakeoil.key']
```
