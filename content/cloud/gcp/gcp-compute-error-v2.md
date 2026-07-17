---
title: "[Solution] GCP Compute Engine — quota exceeded"
description: "Fix GCP Compute Engine quota exceeded. Resolve instance and resource quota limits."
cloud: ["gcp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["gcp", "compute", "engine", "quota", "exceeded", "limit", "resources"]
weight: 5
---

A Compute Engine quota exceeded error means you have reached the resource limit for the requested resource type in the project or region. The request is rejected until quota is released or increased.

## What This Error Means

GCP imposes default quotas on all Compute Engine resources — CPUs, persistent disks, IP addresses, GPU accelerators, and more. These quotas are per-project and per-region. When you attempt to create a resource that would push your usage over the quota limit, Compute Engine returns a `QUOTA_EXCEEDED` error with the specific quota name, current usage, and requested amount. Quotas are not instance limits — they apply across all resources of that type in the region.

## Common Causes

- Too many VMs or CPUs already allocated in the region
- Static IP addresses allocated but not in use
- Persistent disks consuming SSD/HDD quota
- GPU quota exhausted in the region
- Preemptible/Spot VM quota reached
- Network endpoint group quota exceeded

## How to Fix

### Check Current Quotas

```bash
gcloud compute project-info describe \
  --project my-project \
  --format="flatten(quotas)"
```

### List Quotas by Region

```bash
gcloud compute project-info describe \
  --format="table(quotas.limit, quotas.metric, quotas.usage)" \
  --filter="quotas.metric:CPUS"
```

### Request Quota Increase

```bash
gcloud compute project-info add-quotas \
  --region us-central1 \
  --quotas name=CPUS,limit=64
```

### Check Resource Usage

```bash
# List all instances
gcloud compute instances list --format="table(name,zone,status,machineType.basename())"

# List all disks
gcloud compute disks list --format="table(name,sizeGb,type.basename())"
```

### Release Unused Resources

```bash
# Delete unused instances
gcloud compute instances delete old-instance --zone us-central1-a

# Release static IPs
gcloud compute addresses delete unused-ip --region us-central1
```

### Use Resource Estimator

```bash
# Estimate before requesting increase
gcloud compute regions describe us-central1 \
  --format="table(quotas.limit,quotas.metric)" \
  --filter="quotas.metric:IN_USE_ADDRESSES"
```

### Try Different Region

```bash
gcloud compute regions list \
  --format="table(name,status)" \
  --filter="status=UP"
```

## Related Errors

- [GCP Compute Error]({{< relref "/cloud/gcp/gcp-compute-error" >}}) — original compute error
- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error-v2" >}}) — instance limit exceeded
- [Azure VM Error]({{< relref "/cloud/azure/azure-vm-error-v2" >}}) — allocation failed
