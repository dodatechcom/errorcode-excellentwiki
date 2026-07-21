---
title: "[Solution] Grafana Dashboard SAML Error"
description: "How to fix Grafana SAML errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- SAML metadata XML invalid
- Certificate not matching IdP
- ACS URL incorrect

## How to Fix

```ini
[auth.saml]
enabled = true
certificate_path = /etc/grafana/saml/cert.pem
private_key_path = /etc/grafana/saml/key.pem
metadata_path = /etc/grafana/saml/metadata.xml
```

## Examples

```bash
xmllint --noout /etc/grafana/saml/metadata.xml
```
