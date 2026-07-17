---
title: "[Solution] GCP Cloud DNS Error"
description: "Fix GCP Cloud DNS errors. Resolve DNS zone and record issues."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
tags: ["gcp", "cloud-dns", "dns", "zone", "record"]
weight: 5
---

A GCP Cloud DNS error occurs when DNS queries fail or DNS records cannot be managed. This affects domain resolution and traffic routing.

## Common Causes

- DNS zone does not exist
- Nameservers not updated at domain registrar
- Record type or name is incorrect
- TTL too low causing stale cache
- DNSSEC configuration issues

## How to Fix

### List Managed Zones

```bash
gcloud dns managed-zones list
```

### Check DNS Records

```bash
gcloud dns record-sets list --zone=my-zone
```

### Create Record

```bash
gcloud dns record-sets create api.example.com. \
  --zone=my-zone --type=A --ttl=300 --rrdatas="1.2.3.4"
```

### Get Nameservers

```bash
gcloud dns managed-zones describe my-zone --format="value(nameServers)"
```

### Export Zone

```bash
gcloud dns record-sets export zone-file.txt --zone=my-zone --output-file=zone.txt
```

### Test DNS

```bash
dig example.com
dig api.example.com
```

## Examples

```bash
# Example 1: Zone not found
# Managed zone 'my-zone' not found
# Fix: create the DNS zone

# Example 2: Nameservers not updated
# DNS resolution fails at registrar
# Fix: update nameservers at domain registrar
```

## Related Errors

- [GCP Cloud CDN Error]({{< relref "/cloud/gcp/gcp-cloud-cdn-error" >}}) — Cloud CDN error
- [Azure DNS Error]({{< relref "/cloud/azure/azure-dns-error" >}}) — Azure DNS error
