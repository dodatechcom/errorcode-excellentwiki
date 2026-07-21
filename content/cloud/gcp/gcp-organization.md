---
title: "[Solution] GCP Organization"
description: "OrganizationError for org nodes."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Organization` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Organization not found
- User not part of the org
- Org policy restricts operation

## How to Fix

### Get organization

```bash
gcloud organizations list
```

## Examples

- Example scenario: organization not found
- Example scenario: user not part of the org
- Example scenario: org policy restricts operation

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
