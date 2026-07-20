---
title: "[Solution] AWS Direct Connect Error — physical/VLAN/BGP failures"
description: "Fix AWS Direct Connect errors. Resolve Direct Connect physical, VLAN, and BGP peering issues."
error-types: ["api-error"]
severities: ["error"]
weight: 111
---

An AWS Direct Connect error occurs when physical connections fail, VLAN configurations mismatch, or BGP peering sessions go down. Direct Connect provides dedicated network access to AWS but requires precise configuration at each layer.

## Common Causes

- Physical port status is down or not provisioned
- VLAN ID does not match between AWS and customer router
- BGP session is not establishing (ASN mismatch)
- LOA-CFA document not approved
- Redundant connection not configured

## How to Fix

### Check Connection Status

```bash
aws directconnect describe-connections \
  --connection-id dxcon-xxx
```

### Verify Virtual Interface

```bash
aws directconnect describe-virtual-interfaces \
  --connection-id dxcon-xxx
```

### Check BGP Status

```bash
aws directconnect describe-virtual-interface \
  --virtual-interface-id dxvif-xxx \
  --query 'VirtualInterface.BgpPeers[*].{ASN:asn,BGPStatus:bgpStatus,State:state}'
```

### Create Virtual Interface

```bash
aws directconnect create-virtual-interface \
  --connection-id dxcon-xxx \
  --virtual-interface-name my-vif \
  --vlan 100 \
  --asn 65000 \
  --amazonAddress 192.168.1.1/30 \
  --customerAddress 192.168.1.2/30
```

### Confirm Connection

```bash
aws directconnect confirm-connection \
  --connection-id dxcon-xxx
```

## Examples

```bash
# Example 1: BGP not established
# BgpPeerState: down, State: available
# Fix: verify ASN and IP addresses match on both sides

# Example 2: VLAN mismatch
# VirtualInterfaceState: down
# Fix: ensure VLAN ID matches between AWS and customer equipment
```

## Related Errors

- [AWS Transit Gateway Error]({{< relref "/cloud/aws/aws-transit-gateway-error" >}}) — Transit Gateway errors
- [AWS VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) — VPC connectivity errors
- [AWS Route53 Error]({{< relref "/cloud/aws/aws-route53-error" >}}) — Route53 DNS errors
