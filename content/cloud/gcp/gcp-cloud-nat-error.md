---
title: "[Solution] GCP Cloud NAT Error"
description: "Fix GCP Cloud NAT errors. Resolve Cloud NAT connectivity issues."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
tags: ["gcp", "cloud-nat", "nat", "networking", "egress"]
weight: 5
---

A GCP Cloud NAT error occurs when VMs cannot access the internet through Cloud NAT. This affects outbound connectivity for private instances.

## Common Causes

- Cloud NAT gateway not configured
- Router not associated with the VPC
- VM does not have a route to the NAT gateway
- NAT IP addresses exhausted
- Cloud NAT logs not showing traffic

## How to Fix

### Check Router

```bash
gcloud compute routers describe my-router --region=us-central1
```

### Create NAT Gateway

```bash
gcloud compute routers nats create my-nat \
  --router=my-router --region=us-central1 \
  --nat-all-subnet-ip-ranges --auto-allocate-nat-external-ips
```

### Check NAT Status

```bash
gcloud compute routers nats list --router=my-router --region=us-central1
```

### Check Routes

```bash
gcloud compute routes list --filter="name=default-route"
```

### Verify External IP

```bash
gcloud compute addresses list --filter="name=nat-manual"
```

## Examples

```bash
# Example 1: VM cannot reach internet
# Connection timed out from private VM
# Fix: create Cloud NAT gateway

# Example 2: NAT IP exhausted
# All NAT IPs are in use
# Fix: add more NAT IP addresses
```

## Related Errors

- [GCP Cloud VPN Error]({{< relref "/cloud/gcp/gcp-cloud-vpn-error" >}}) — Cloud VPN error
- [GCP Cloud DNS Error]({{< relref "/cloud/gcp/gcp-cloud-dns-error" >}}) — Cloud DNS error
