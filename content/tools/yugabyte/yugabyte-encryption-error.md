---
title: "YugabyteDB Encryption Error"
description: "Encryption at rest or in transit error"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Encryption configuration is failing.

## Common Causes
- Encryption key not found
- TLS certificate expired
- Key rotation failed

## How to Fix
```bash
# Check encryption status
yb-admin list_universe_config

# Rotate encryption key
yb-admin rotate_encryption_key
```

## Examples
```bash
# Check TLS certificate
openssl x509 -in /path/to/cert.pem -text -noout
# Verify encryption
curl http://localhost:9000/conf | grep encryption
```

