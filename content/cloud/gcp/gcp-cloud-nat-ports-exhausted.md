---
title: "[Solution] GCP Cloud NAT Ports Exhausted"
description: "Fix Cloud NAT port exhaustion errors. Resolve Cloud NAT port allocation, VM limits, and network address translation issues in GCP."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud NAT Ports Exhausted

The Cloud NAT Ports Exhausted error occurs when a Cloud NAT gateway runs out of available ports for NAT translations, causing outbound connection failures.

## Common Causes

- Too many concurrent outbound connections from VMs
- NAT gateway min_ports_per_vm is set too low
- VM count exceeds NAT gateway capacity
- Long-lived connections hold ports unnecessarily
- Ephemeral port range is insufficient

## How to Fix

### 1. Check NAT gateway status
```bash
gcloud compute routers describe ROUTER_NAME \
  --region=REGION \
  --format="yaml(nat)"
```

### 2. Increase min_ports_per_vm
```bash
gcloud compute routers update-nat NAT_NAME \
  --router=ROUTER_NAME \
  --region=REGION \
  --min-ports-per-vm=4096
```

### 3. Enable dynamic port allocation
```bash
gcloud compute routers update-nat NAT_NAME \
  --router=ROUTER_NAME \
  --region=REGION \
  --enable-dynamic-port-allocation
```

### 4. Create separate NAT per workload
```bash
gcloud compute routers nats create WORKLOAD_NAT \
  --router=ROUTER_NAME \
  --region=REGION \
  --nat-all-subnet-ip-ranges \
  --auto-allocate-nat-external-ips
```

## Examples

### Monitor NAT port usage
```bash
gcloud monitoring time-series list \
  --filter='metric.type="network.googleapis.com/nat/nat_ports"' \
  --interval-start-time=$(date -u -d "1 hour ago" +%Y-%m-%dT%H:%M:%SZ)
```

### Check NAT allocation logs
```bash
gcloud logging read "resource.type=nat_gateway \
  AND jsonPayload.event_subtype=~\"allocations\"" \
  --limit=20
```

## Related Errors

- [GCP Cloud NAT Error]({{< relref "/cloud/gcp/gcp-nat-gateway-(cloud-nat)" >}})
- [GCP VPC Error]({{< relref "/cloud/gcp/gcp-vpc-error" >}})
