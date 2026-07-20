---
title: "[Solution] GCP Cloud Interconnect Error — Interconnect VLAN virtual-circuit BGP errors"
description: "Fix GCP Cloud Interconnect errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 103
---

Cloud Interconnect errors occur when there are issues with dedicated or partner interconnect connections, VLAN attachments, or BGP peering.

## Common Causes
- VLAN attachment not in ACTIVE state
- BGP session not established or flapping
- Interconnect circuit not provisioned
- MTU mismatch between on-premises and GCP
- Partner interconnect provider issues

## How to Fix

### 1. Check interconnect status
```bash
gcloud compute interconnects list
gcloud compute interconnects describe INTERCONNECT_NAME --region=REGION
```

### 2. Verify VLAN attachments
```bash
gcloud compute interconnects attachments list --region=REGION
gcloud compute interconnects attachments describe ATTACHMENT_NAME --region=REGION
```

### 3. Check BGP sessions
```bash
gcloud compute routers get-status ROUTER_NAME --region=REGION
```

### 4. Create VLAN attachment
```bash
gcloud compute interconnects attachments dedicated create ATTACHMENT_NAME \
  --interconnect=INTERCONNECT_NAME \
  --vlan=100 \
  --region=REGION \
  --router=ROUTER_NAME \
  --router-region=REGION
```

### 5. Update router interface
```bash
gcloud compute routers update-router ROUTER_NAME \
  --region=REGION \
  --update-interface=name=INTERFACE_NAME,ip-range=169.254.0.1/30,interconnect-attachment=ATTACHMENT_NAME
```

## Examples

### Verify BGP peering
```bash
gcloud compute routers get-status my-router \
  --region=us-central1 \
  --format="value(bgpPeers[].name, bgpPeers[].state)"
```

### Create router for interconnect
```bash
gcloud compute routers create my-router \
  --network=my-vpc \
  --region=us-central1 \
  --asn=64512
```

## Related Errors
- [GCP Cloud VPN Error](/cloud/gcp/gcp-cloud-vpn-error/)
- [GCP VPC Network Error](/cloud/gcp/gcp-vpc-error/)
- [GCP Cloud NAT Error](/cloud/gcp/gcp-cloud-nat-error/)