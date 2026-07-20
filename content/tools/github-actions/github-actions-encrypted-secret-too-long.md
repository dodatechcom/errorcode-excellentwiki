---
title: "[Solution] GitHub Actions Encrypted Secret Too Long"
description: "Fix GitHub Actions encrypted secret value too long errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Encrypted secret too long errors occur when a secret value exceeds the size limit:

```
Error: Secret value exceeds maximum length of 48KB
```

## Common Causes

- Secret contains a large certificate or key.
- Secret value includes excessive whitespace or newlines.

## How to Fix

**Split large secrets:**

```yaml
steps:
  - name: Setup certs
    run: |
      echo "${{ secrets.CERT_PART1 }}" > cert1.pem
      echo "${{ secrets.CERT_PART2 }}" > cert2.pem
      cat cert1.pem cert2.pem > cert.pem
```

## Examples

```yaml
env:
  CERT_B64: ${{ secrets.CERT_BASE64 }}
steps:
  - run: echo "$CERT_B64" | base64 -d > cert.pem
```
