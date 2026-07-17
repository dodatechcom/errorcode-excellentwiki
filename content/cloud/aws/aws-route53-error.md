---
title: "[Solution] AWS Route53 DNS Error"
description: "Fix AWS Route53 DNS errors. Resolve DNS resolution and routing issues."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

A Route53 DNS error occurs when DNS queries fail or return incorrect results. This can affect domain resolution and traffic routing.

## Common Causes

- Hosted zone does not exist for the domain
- NS records not pointing to Route53 name servers
- Record type or name is incorrect
- TTL too low causing stale cache
- Domain registration expired

## How to Fix

### List Hosted Zones

```bash
aws route53 list-hosted-zones
```

### Check DNS Records

```bash
aws route53 list-resource-record-sets \
  --hosted-zone-id Z1234567890
```

### Test DNS Resolution

```bash
dig example.com
dig example.com @ns-1.awsdns-01.com
```

### Create Record

```bash
aws route53 change-resource-record-sets \
  --hosted-zone-id Z1234567890 \
  --change-batch '{
    "Changes": [{
      "Action": "CREATE",
      "ResourceRecordSet": {
        "Name": "api.example.com",
        "Type": "A",
        "TTL": 300,
        "ResourceRecords": [{"Value": "1.2.3.4"}]
      }
    }]
  }'
```

### Check Domain Registration

```bash
aws route53 domains get-domain-detail --domain-name example.com
```

## Examples

```bash
# Example 1: DNS resolution fails
dig example.com
;; connection timed out
# Fix: verify NS records match Route53 name servers

# Example 2: Wrong record type
# Expected A record, got CNAME
# Fix: update record type in Route53
```

## Related Errors

- [AWS CloudFront Error]({{< relref "/cloud/aws/aws-cloudfront-error" >}}) — CloudFront error
- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) — S3 access denied
