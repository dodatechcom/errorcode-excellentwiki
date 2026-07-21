---
title: "[Solution] GCP Serial Console"
description: "SerialConsoleError for serial access."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Serial Console` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Serial logging not enabled
- Interactive mode requires user
- OS login blocking serial

## How to Fix

### Enable serial

```bash
gcloud compute instances add-metadata myVM --metadata serial-port-enable=1
```

## Examples

- Example scenario: serial logging not enabled
- Example scenario: interactive mode requires user
- Example scenario: os login blocking serial

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
