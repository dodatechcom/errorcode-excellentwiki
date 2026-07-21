---
title: "[Solution] GCP Cloud DNS Record Set Error"
description: "Fix Cloud DNS record set errors. Resolve DNS zone, record creation, and name resolution issues in Google Cloud DNS."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud DNS Record Set Error

The Cloud DNS Record Set error occurs when DNS records cannot be created, updated, or resolved due to zone configuration or naming issues.

## Common Causes

- DNS zone name does not match the domain
- Record set name is not fully qualified (missing trailing dot)
- SOA and NS records are missing or malformed
- TTL values are too low for propagation
- Private zone is not associated with the correct VPC

## How to Fix

### 1. Check existing record sets
```bash
gcloud dns record-sets list --zone=ZONE_NAME \
  --format="table(name,type,ttl,rrdatas)"
```

### 2. Create an A record
```bash
gcloud dns record-sets create example.com. \
  --zone=ZONE_NAME \
  --type=A \
  --ttl=300 \
  --rrdatas="34.102.136.180"
```

### 3. Update record set
```bash
gcloud dns record-sets transaction start --zone=ZONE_NAME
gcloud dns record-sets transaction update example.com. \
  --zone=ZONE_NAME \
  --type=A \
  --ttl=300 \
  --rrdatas="34.102.136.181"
gcloud dns record-sets transaction execute --zone=ZONE_NAME
```

### 4. Verify DNS resolution
```bash
dig example.com @8.8.8.8
nslookup example.com
```

## Examples

### Create CNAME record
```bash
gcloud dns record-sets create www.example.com. \
  --zone=ZONE_NAME \
  --type=CNAME \
  --ttl=300 \
  --rrdatas="example.com."
```

### Delete a record
```bash
gcloud dns record-sets delete old.example.com. \
  --zone=ZONE_NAME \
  --type=A
```

## Related Errors

- [GCP Cloud DNS Error]({{< relref "/cloud/gcp/gcp-cloud-dns-error" >}})
- [GCP DNS GCP]({{< relref "/cloud/gcp/gcp-dns-(gcp)" >}})
