---
title: "[Solution] GCP SSH Connection Error"
description: "SSHConnectionError for SSH access."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `SSH Connection Error` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Firewall rule blocking (22)
- SSH key not set
- OS Login disabled

## How to Fix

### Add SSH key

```bash
gcloud compute ssh myVM --zone=us-central1-a
```

## Examples

- Example scenario: firewall rule blocking (22)
- Example scenario: ssh key not set
- Example scenario: os login disabled

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
