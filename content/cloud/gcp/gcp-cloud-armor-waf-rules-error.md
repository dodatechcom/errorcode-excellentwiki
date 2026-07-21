---
title: "[Solution] GCP Cloud Armor WAF Rules Error"
description: "Fix Cloud Armor WAF rules errors. Resolve WAF rule configuration, pre-configured rules, and custom rule issues in Google Cloud Armor."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Armor WAF Rules Error

The Cloud Armor WAF Rules error occurs when WAF rules are misconfigured, causing either false positives or insufficient protection.

## Common Causes

- Pre-configured rules (SQL injection, XSS) are not enabled
- Custom rule expressions have syntax errors
- Rules conflict with each other due to priority ordering
- OWASP ModSecurity Core Rule Set thresholds are too low
- Rule actions do not match expected behavior

## How to Fix

### 1. List WAF rules
```bash
gcloud compute security-policies rules list POLICY_NAME \
  --format="table(priority,expression,action,description)"
```

### 2. Enable SQL injection protection
```bash
gcloud compute security-policies rules update 2147483642 \
  --security-policy=POLICY_NAME \
  --expression="evaluatePreconfiguredExpr('sqli-stable')" \
  --action=deny-403
```

### 3. Enable XSS protection
```bash
gcloud compute security-policies rules update 2147483641 \
  --security-policy=POLICY_NAME \
  --expression="evaluatePreconfiguredExpr('xss-stable')" \
  --action=deny-403
```

### 4. Add custom WAF rule
```bash
gcloud compute security-policies rules create 500 \
  --security-policy=POLICY_NAME \
  --expression="evaluatePreconfiguredExpr('lfi-stable')" \
  --action=deny-403
```

## Examples

### Check WAF rule matches
```bash
gcloud logging read "resource.type=http_load_balancer \
  AND jsonPayload.enforcedSecurityPolicy.outcome=deny" \
  --limit=50
```

### Create rate-based rule
```bash
gcloud compute security-policies rules create 1000 \
  --security-policy=POLICY_NAME \
  --expression="true" \
  --action=throttle \
  --rate-limit-threshold-count=100 \
  --rate-limit-threshold-interval-sec=60
```

## Related Errors

- [GCP Cloud Armor Error]({{< relref "/cloud/gcp/gcp-cloud-armor-error" >}})
- [GCP Security Rules]({{< relref "/cloud/gcp/gcp-security-rules" >}})
