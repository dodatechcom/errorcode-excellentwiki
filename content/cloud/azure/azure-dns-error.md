---
title: "[Solution] Azure DNS Error"
description: "Fix Azure DNS errors. Resolve DNS zone and record issues."
cloud: ["azure"]
error-types: ["api-error"]
severities: ["error"]
tags: ["azure", "dns", "zone", "record", "domain"]
weight: 5
---

An Azure DNS error occurs when DNS resolution fails or DNS records cannot be managed. This can affect domain resolution and traffic routing.

## Common Causes

- DNS zone does not exist in Azure
- Nameservers not updated at domain registrar
- Record type or name is incorrect
- TTL too low causing stale cache
- Record set conflict with existing records

## How to Fix

### List DNS Zones

```bash
az network dns zone list --resource-group myRG
```

### Check DNS Records

```bash
az network dns record-set list --zone-name example.com --resource-group myRG
```

### Create Record

```bash
az network dns record-set a add-record --zone-name example.com --resource-group myRG \
  --record-set-name api --ipv4-address 1.2.3.4
```

### Get Nameservers

```bash
az network dns zone show --name example.com --resource-group myRG \
  --query 'nameServers'
```

### Test DNS Resolution

```bash
dig example.com
dig api.example.com
```

## Examples

```bash
# Example 1: Zone not found
# Resource group 'myRG' does not contain zone 'example.com'
# Fix: create the DNS zone first

# Example 2: Nameservers not updated
# DNS resolution fails
# Fix: update nameservers at domain registrar
```

## Related Errors

- [Azure CDN Error]({{< relref "/cloud/azure/azure-cdn-error" >}}) — CDN error
- [AWS Route53 Error]({{< relref "/cloud/aws/aws-route53-error" >}}) — Route53 DNS error
