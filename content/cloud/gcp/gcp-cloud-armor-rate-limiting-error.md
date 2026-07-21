---
title: "[Solution] GCP Cloud Armor Rate Limiting Error"
description: "Fix Cloud Armor rate limiting errors. Resolve WAF rate limiting, DDoS protection, and request throttling issues in Google Cloud Armor."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Armor Rate Limiting Error

The Cloud Armor Rate Limiting error occurs when legitimate traffic is blocked or throttled by Cloud Armor security policies due to aggressive rate limiting rules.

## Common Causes

- Rate limit threshold is set too low for expected traffic
- Throttle action blocks all requests from an IP range
- Pre-configured WAF rules trigger false positives
- Client IP changes frequently due to proxy or VPN
- Rate limiting is applied at multiple policy levels

## How to Fix

### 1. Check security policies
```bash
gcloud compute security-policies list --format="table(name,description)"
```

### 2. Update rate limit rule
```bash
gcloud compute security-policies rules update 1000 \
  --security-policy=SECURITY_POLICY \
  --expression="true" \
  --action=throttle \
  --rate-limit-threshold-count=1000 \
  --rate-limit-threshold-interval-sec=60 \
  --conform-action=allow \
  --exceed-action=deny-429
```

### 3. Check Cloud Armor logs
```bash
gcloud logging read "resource.type=http_load_balancer \
  AND jsonPayload.enforcedSecurityPolicy.action=throttle" \
  --limit=20
```

### 4. Add exception for trusted IPs
```bash
gcloud compute security-policies rules create 999 \
  --security-policy=SECURITY_POLICY \
  --expression="origin.ip in {trusted_ip_range}" \
  --action=allow
```

## Examples

### Create rate limiting policy
```bash
gcloud compute security-policies create RATE_LIMIT_POLICY \
  --description="Rate limit policy"

gcloud compute security-policies rules create 1000 \
  --security-policy=RATE_LIMIT_POLICY \
  --expression="true" \
  --action=throttle \
  --rate-limit-threshold-count=500 \
  --rate-limit-threshold-interval-sec=60 \
  --conform-action=allow \
  --exceed-action=deny-429
```

### Check blocked requests
```bash
gcloud logging read "resource.type=http_load_balancer \
  AND jsonPayload.enforcedSecurityPolicy.outcome=deny" \
  --limit=50
```

## Related Errors

- [GCP Cloud Armor Error]({{< relref "/cloud/gcp/gcp-cloud-armor-error" >}})
- [GCP Security Rules]({{< relref "/cloud/gcp/gcp-security-rules" >}})
