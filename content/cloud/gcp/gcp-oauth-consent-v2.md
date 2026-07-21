---
title: "[Solution] GCP OAuth Consent"
description: "OAuthConsentError for OAuth."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `OAuth Consent` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Consent screen not published
- Scopes not authorized
- Domain verification pending

## How to Fix

### Configure consent

```bash
gcloud alpha identity-platform oauth-clients list
```

## Examples

- Example scenario: consent screen not published
- Example scenario: scopes not authorized
- Example scenario: domain verification pending

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
