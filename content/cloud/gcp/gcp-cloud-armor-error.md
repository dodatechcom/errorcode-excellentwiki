---
title: "[Solution] GCP Cloud Armor Error"
description: "Fix GCP Cloud Armor errors. Resolve Cloud Armor security policy issues."
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

A GCP Cloud Armor error occurs when Cloud Armor blocks legitimate traffic or cannot process security rules.

## Common Causes

- Security policy blocking valid requests
- IP allowlist/denylist misconfigured
- Rate limiting rules too aggressive
- Adaptive protection false positives
- Backend service not associated with policy

## How to Fix

### Check Security Policy

```bash
gcloud compute security-policies list
gcloud compute security-policies describe my-policy
```

### Test Rule Evaluation

```bash
gcloud compute security-policies rules test 1000 \
  --expression="origin.ipgeo.country == 'US'" \
  --preview
```

### Add Rule

```bash
gcloud compute security-policies rules create 1000 \
  --security-policy my-policy \
  --expression="origin.ipgeo.country == 'US'" \
  --action=allow
```

### Associate with Backend

```bash
gcloud compute backend-services update my-backend \
  --security-policy my-policy --global
```

### Check Logs

```bash
gcloud logging read "resource.type=http_load_balancer AND jsonPayload.enforcedSecurityPolicy.outcome=DENY" --limit 50
```

## Examples

```bash
# Example 1: Traffic blocked
# 403 Forbidden from Cloud Armor
# Fix: check security policy rules

# Example 2: Rate limit hit
# 429 Too Many Requests
# Fix: adjust rate limiting rules
```

## Related Errors

- [GCP Cloud CDN Error]({{< relref "/cloud/gcp/gcp-cloud-cdn-error" >}}) — Cloud CDN error
- [GCP Cloud VPN Error]({{< relref "/cloud/gcp/gcp-cloud-vpn-error" >}}) — Cloud VPN error
