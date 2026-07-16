---
title: "GCP Network Error: The Network Has Been Lost"
description: "Network error: The network has been lost — Fix Google Cloud network connectivity errors."
cloud: ["gcp"]
error-types: ["api-error"]
severities: ["error"]
tags: ["gcp", "network", "vpc", "connectivity", "firewall", "cloud-run", "gke"]
weight: 5
---

The `Network error: The network has been lost` error occurs when a Google Cloud service loses network connectivity. This can affect Cloud Run, GKE, Compute Engine, and other services that depend on VPC networking.

## Common Causes

- VPC firewall rules blocking required ports
- Cloud NAT not configured for private instances to reach the internet
- DNS resolution failure for private DNS zones
- Network peering configuration is missing or broken
- The instance's network interface is misconfigured

## How to Fix

Check firewall rules:

```bash
gcloud compute firewall-rules list --format="table(name, direction, sourceRanges, allowed)" \
  --filter="network:default"
```

Create a firewall rule to allow required traffic:

```bash
gcloud compute firewall-rules create allow-internal \
  --network=default \
  --action=ALLOW \
  --direction=INGRESS \
  --source-ranges=10.128.0.0/9 \
  --rules=tcp:80,tcp:443,tcp:8080
```

Check Cloud NAT configuration:

```bash
gcloud compute routers get-nat-mapping-info default-router \
  --region=us-central1
```

Verify DNS resolution:

```bash
# From a VM
nslookup my-service.internal

# Check private DNS zone
gcloud dns managed-zones list --format="table(name, dnsName)"
```

## Examples

- Cloud Run service cannot reach a Cloud SQL instance in a private VPC without Cloud NAT
- GKE pods cannot resolve internal service names because DNS peering is not configured
- Firewall rule allows ingress on port 80 but not port 8080 where the application listens

## Related Errors

- [GCP Compute Error]({{< relref "/cloud/gcp/compute-error" >}}) — zone resource exhaustion.
- [GCP GKE Error]({{< relref "/cloud/gcp/gke-error" >}}) — GKE cluster issues.
- [Azure NSG Error]({{< relref "/cloud/azure/nsg-error" >}}) — Azure equivalent.
