---
title: "[Solution] GCP Cloud DNS Zone Deletion Error"
description: "Fix Cloud DNS zone deletion errors. Resolve DNS zone removal, record cleanup, and zone dependency issues in Google Cloud DNS."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud DNS Zone Deletion Error

The Cloud DNS Zone Deletion error occurs when a DNS zone cannot be deleted because it still contains records or has dependent resources.

## Common Causes

- Zone contains record sets that must be removed first
- Cloud DNS peering zone depends on this zone
- DNSSEC is enabled and must be disabled before deletion
- Domain is registered via Cloud Domains and linked
- Another service (Load Balancer) creates records in this zone

## How to Fix

### 1. List record sets in zone
```bash
gcloud dns record-sets list --zone=ZONE_NAME \
  --format="table(name,type,ttl)"
```

### 2. Delete all record sets
```bash
for record in $(gcloud dns record-sets list --zone=ZONE_NAME --format="value(name,type)"); do
  NAME=$(echo $record | cut -d' ' -f1)
  TYPE=$(echo $record | cut -d' ' -f2)
  gcloud dns record-sets delete $NAME --zone=ZONE_NAME --type=$TYPE
done
```

### 3. Disable DNSSEC
```bash
gcloud dns managed-zones update ZONE_NAME --dnssec-state=off
```

### 4. Delete the zone
```bash
gcloud dns managed-zones delete ZONE_NAME
```

## Examples

### Check zone status
```bash
gcloud dns managed-zones describe ZONE_NAME \
  --format="yaml(name,dnsName,dnssecConfig)"
```

### List peering zones
```bash
gcloud dns peering-zones list --network=VPC_NAME
```

## Related Errors

- [GCP Cloud DNS Error]({{< relref "/cloud/gcp/gcp-cloud-dns-error" >}})
- [GCP DNS GCP]({{< relref "/cloud/gcp/gcp-dns-(gcp)" >}})
