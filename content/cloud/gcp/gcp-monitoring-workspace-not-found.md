---
title: "[Solution] GCP Monitoring Workspace Not Found"
description: "NOT_FOUND when the specified monitoring workspace does not exist."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Monitoring Workspace Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Workspace name is incorrect
- Workspace was deleted
- Workspace in different project
- Workspace not accessible to caller

## How to Fix

### List workspaces

```bash
gcloud monitoring workspaces list
```
### Check workspace

```bash
gcloud monitoring workspaces describe my-workspace
```
### Create workspace

```bash
gcloud monitoring workspaces create --project my-project
```

## Examples

- Workspace my-workspace not found
- Workspace deleted but alerts still reference it

## Related Errors

- [GCP Monitoring Error]({{< relref "/cloud/gcp/gcp-cloud-monitoring-error" >}}) -- General Monitoring errors
- [Metric Descriptor]({{< relref "/cloud/gcp/gcp-monitoring-metric-descriptor" >}}) -- Metric descriptors
