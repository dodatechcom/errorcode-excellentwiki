---
title: "[Solution] GCP Instance Template"
description: "InstanceTemplateError for templates."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Instance Template` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Template name taken
- Source instance not found
- Deprecated properties used

## How to Fix

### List templates

```bash
gcloud compute instance-templates list
```

## Examples

- Example scenario: template name taken
- Example scenario: source instance not found
- Example scenario: deprecated properties used

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
