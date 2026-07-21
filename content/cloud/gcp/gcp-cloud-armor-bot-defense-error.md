---
title: "[Solution] GCP Cloud Armor Bot Defense Error"
description: "Fix Cloud Armor bot defense errors. Resolve WAF bot detection, CAPTCHA, and reCAPTCHA Enterprise issues in Google Cloud Armor."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Armor Bot Defense Error

The Cloud Armor Bot Defense error occurs when legitimate traffic is mistakenly blocked by bot detection rules or CAPTCHA challenges fail.

## Common Causes

- Preconfigured WAF rules trigger false positive bot detection
- CAPTCHA challenge is not properly implemented on the client
- reCAPTCHA Enterprise site key is incorrect
- Bot detection threshold blocks legitimate automated traffic
- User-agent string matches known bot patterns

## How to Fix

### 1. Check blocked requests
```bash
gcloud logging read "resource.type=http_load_balancer \
  AND jsonPayload.enforcedSecurityPolicy.action=deny-403" \
  --limit=20
```

### 2. Create exception for known good bots
```bash
gcloud compute security-policies rules create 500 \
  --security-policy=POLICY_NAME \
  --expression="userAgent() matches 'Googlebot'" \
  --action=allow
```

### 3. Enable reCAPTCHA
```bash
gcloud compute security-policies rules update 1000 \
  --security-policy=POLICY_NAME \
  --recaptcha-token-config=site-key=SITE_KEY,actions=login,signup
```

### 4. Add bot exception
```bash
gcloud compute security-policies rules update 200 \
  --security-policy=POLICY_NAME \
  --expression="origin.ip in {trusted_ip_range}" \
  --action=allow
```

## Examples

### List bot detection rules
```bash
gcloud compute security-policies rules list POLICY_NAME \
  --format="table(priority,expression,action)"
```

### Check reCAPTCHA score
```bash
curl -X POST "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments" \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -d '{"event":{"token":"TOKEN","siteKey":"KEY","userAgent":"Mozilla/5.0"}}'
```

## Related Errors

- [GCP Cloud Armor Error]({{< relref "/cloud/gcp/gcp-cloud-armor-error" >}})
- [GCP Security Rules]({{< relref "/cloud/gcp/gcp-security-rules" >}})
