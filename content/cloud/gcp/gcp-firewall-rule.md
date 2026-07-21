---
title: "[Solution] GCP Firewall Rule Error"
description: "INVALID when firewall rule operations fail."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Firewall Rule Error` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Rule name is incorrect
- Priority conflicts
- Source/destination range invalid
- Network does not exist

## How to Fix

### List firewall rules

```bash
gcloud compute firewall-rules list
```
### Check rule

```bash
gcloud compute firewall-rules describe my-rule
```
### Create rule

```bash
gcloud compute firewall-rules create my-rule --network my-vpc --allow=tcp:80,tcp:443 --source-ranges=0.0.0.0/0
```

## Examples

- Firewall rule priority conflicts with existing rule
- Source range 10.0.0 is not valid CIDR

## Related Errors

- [GCP VPC Error]({{< relref "/cloud/gcp/gcp-vpc-error" >}}) -- General VPC errors
- [Allow Rule]({{< relref "/cloud/gcp/gcp-vpc-allow-rule" >}}) -- Allow rules
