---
title: "[Solution] GCP Cloud Interconnect Attachment Error"
description: "Fix Cloud Interconnect attachment errors. Troubleshoot Dedicated/Partner Interconnect VLAN, BGP, and connectivity issues in GCP."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Interconnect Attachment Error

The Cloud Interconnect Attachment error occurs when VLAN attachments fail to establish connectivity between on-premises networks and GCP via Dedicated or Partner Interconnect.

## Common Causes

- VLAN attachment is in a FAILED state
- BGP session is not established
- Interconnect capacity is fully utilized
- Partner Interconnect circuit is down
- MTU mismatch between on-premises and GCP routers

## How to Fix

### 1. Check attachment status
```bash
gcloud compute interconnect attachments describe ATTACHMENT_NAME \
  --region=REGION --format="yaml(state,bgpSession,partnerMetadata)"
```

### 2. Verify BGP session
```bash
gcloud compute routers get-router-interface \
  --router=ROUTER_NAME \
  --region=REGION \
  --interface=INTERFACE_NAME
```

### 3. Check Interconnect status
```bash
gcloud compute interconnects describe INTERCONNECT_NAME \
  --location=LOCATION \
  --format="yaml(operationalStatus,linkType,requestedLinkSpeed)"
```

### 4. Update BGP peering
```bash
gcloud compute routers update-bgp-peer ROUTER_NAME \
  --region=REGION \
  --interface=INTERFACE_NAME \
  --peer-name=PEER_NAME \
  --peer-ip-address=169.254.0.2 \
  --advertised-route-priority=100
```

## Examples

### Create Partner Interconnect attachment
```bash
gcloud compute interconnect attachments create PARTNER_ATTACH \
  --region=us-central1 \
  --type=PARTNER \
  --router=ROUTER_NAME \
  --edge-availability-domain=availability-zone1
```

### List all Interconnects
```bash
gcloud compute interconnects list --format="table(name,location,linkType,operationalStatus)"
```

## Related Errors

- [GCP Cloud Interconnect Error]({{< relref "/cloud/gcp/gcp-cloud-interconnect-error" >}})
- [GCP Dedicated Interconnect]({{< relref "/cloud/gcp/gcp-dedicated-interconnect" >}})
