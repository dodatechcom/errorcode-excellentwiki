---
title: "[Solution] GCP Cloud Armor DDoS Protection Error"
description: "Fix Cloud Armor DDoS protection errors. Resolve L3/L4 DDoS mitigation, adaptive protection, and traffic analysis issues in Cloud Armor."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Armor DDoS Protection Error

The Cloud Armor DDoS Protection error occurs when adaptive protection or DDoS mitigation rules block legitimate traffic during attack mitigation.

## Common Causes

- Adaptive protection has learned a false positive pattern
- Rate limiting is too aggressive during peak traffic
- IP reputation list includes legitimate IP ranges
- Pre-configured rules have incorrect thresholds
- DDoS mitigation is applied at multiple layers

## How to Fix

### 1. Check DDoS mitigation logs
```bash
gcloud logging read "resource.type=http_load_balancer \
  AND jsonPayload.enforcedSecurityPolicy.action=deny-429" \
  --limit=50
```

### 2. Review adaptive protection predictions
```bash
gcloud compute security-policies describe POLICY_NAME \
  --format="yaml(adaptiveProtection)"
```

### 3. Update pre-configured rules
```bash
gcloud compute security-policies rules update 2147483647 \
  --security-policy=POLICY_NAME \
  --action=deny-403 \
  --description="Default deny rule"
```

### 4. Whitelist trusted IP ranges
```bash
gcloud compute security-policies rules create 1 \
  --security-policy=POLICY_NAME \
  --expression="origin.ip in {trusted_ip_range}" \
  --action=allow
```

## Examples

### Enable adaptive protection
```bash
gcloud compute security-policies update POLICY_NAME \
  --enable-layer7-ddos-defense
```

### Check current pre-configured rules
```bash
gcloud compute security-policies rules list POLICY_NAME \
  --format="table(priority,expression,action,description)"
```

## Related Errors

- [GCP Cloud Armor Error]({{< relref "/cloud/gcp/gcp-cloud-armor-error" >}})
- [GCP Cloud Armor Rate Limiting Error]({{< relref "/cloud/gcp/gcp-cloud-armor-rate-limiting-error" >}})
