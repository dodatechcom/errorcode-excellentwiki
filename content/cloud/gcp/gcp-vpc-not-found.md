---
title: "[Solution] GCP VPC Not Found"
description: "NOT_FOUND when the specified VPC network does not exist."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `VPC Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- VPC name is incorrect
- VPC was deleted
- VPC in different project
- VPC is auto-created and not manually managed

## How to Fix

### List VPCs

```bash
gcloud compute networks list
```
### Check VPC

```bash
gcloud compute networks describe my-vpc
```
### Create VPC

```bash
gcloud compute networks create my-vpc --subnet-mode=custom
```

## Examples

- VPC my-vpc not found in project
- VPC was deleted but subnets still reference it

## Related Errors

- [GCP VPC Error]({{< relref "/cloud/gcp/gcp-vpc-error" >}}) -- General VPC errors
- [Subnets Exhausted]({{< relref "/cloud/gcp/gcp-vpc-subnets-exhausted" >}}) -- Subnets
