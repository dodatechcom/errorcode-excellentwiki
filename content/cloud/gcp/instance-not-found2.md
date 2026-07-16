---
title: "GCP Instance Not Found: Instance 'X' Was Not Found"
description: "Instance 'X' was not found — Fix Google Cloud Compute Engine instance lookup errors."
cloud: ["gcp"]
error-types: ["api-error"]
severities: ["error"]
tags: ["gcp", "compute", "instance", "not-found", "gce", "vm"]
weight: 5
---

The `Instance 'X' was not found` error occurs when a Google Cloud API call references a Compute Engine instance that does not exist in the project or zone. The instance may have been deleted, the name may be incorrect, or the zone may be wrong.

## Common Causes

- The instance was deleted or never created
- Wrong zone specified in the command
- Typo in the instance name
- The instance is in a different project than the one currently active

## How to Fix

Check the current project and zone:

```bash
gcloud config get-value project
gcloud config get-value compute/zone
```

List instances in the current project:

```bash
gcloud compute instances list \
  --format="table(name, zone, status, networkInterfaces[0].networkIP)"
```

Search across all zones:

```bash
gcloud compute instances list --zones="us-central1-*" \
  --filter="name:my-vm"
```

Recreate the instance if needed:

```bash
gcloud compute instances create my-vm \
  --zone=us-central1-a \
  --machine-type=e2-medium \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud
```

## Examples

- Terraform tries to SSH into an instance that was destroyed by a previous `terraform destroy`
- Script uses `us-central1-b` but the instance is in `us-central1-a`
- Deployed to the wrong project — `gcloud config set project my-staging-project` was set

## Related Errors

- [GCP Network Error]({{< relref "/cloud/gcp/network-error" >}}) — network connectivity issues.
- [GCP Compute Error]({{< relref "/cloud/gcp/compute-error" >}}) — zone resource exhaustion.
- [Azure VM Not Found]({{< relref "/cloud/azure/vm-not-found" >}}) — Azure equivalent.
