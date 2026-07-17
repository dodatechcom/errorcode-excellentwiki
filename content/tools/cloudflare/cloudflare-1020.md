---
title: "[Solution] Cloudflare 1020 Access Denied Error — Fix Firewall Rules"
description: "Fix Cloudflare 1020 access denied errors. Resolve IP-based access restrictions and firewall rule conflicts."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
weight: 7
---

A Cloudflare 1020 error means access to your website was denied by a Cloudflare firewall rule or Access policy. This is a client-side error triggered when a visitor's request matches a blocking rule you have configured.

## What This Error Means

The 1020 error page shows "Access denied" and includes a Ray ID for debugging. This means one of your Cloudflare security rules blocked the request. It could be an IP Access rule, a WAF rule, a Rate Limiting rule, or a Cloudflare Access policy.

## Why It Happens

- Your IP is blocked by an IP Access rule
- A Cloudflare Access policy denies the request
- A WAF custom rule matches the request
- Rate Limiting rules are blocking excessive requests
- The Country or ASN is blocked by a rule
- Bot Fight Mode is blocking legitimate traffic

## How to Fix It

### Check Security Events

```bash
# In Cloudflare Dashboard:
# Security > Events
# Look for the Ray ID from the error page
# Find which rule blocked the request
```

### Review Firewall Rules

```bash
# In Cloudflare Dashboard:
# Security > WAF > Custom rules
# Check for overly broad blocking rules

# Common issue: blocking your own IP
# Add your IP to the allowlist
```

### Add IP to Allowlist

```bash
# In Cloudflare Dashboard:
# Security > WAF > Tools > IP Access Rules

# Add rule:
# IP: your.office.ip.address
# Action: Allow
# Notes: "Office IP"
```

### Fix Cloudflare Access Policies

```bash
# In Cloudflare Dashboard:
# Zero Trust > Access > Applications

# Check that your application's policy
# includes the correct identity provider
# and user emails
```

### Use API to Check Rules

```bash
# List firewall rules
curl -X GET "https://api.cloudflare.com/client/v4/zones/ZONE_ID/firewall/rules" \
  -H "Authorization: Bearer API_TOKEN" | jq '.result'

# Disable a specific rule
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/ZONE_ID/firewall/rules/RULE_ID" \
  -H "Authorization: Bearer API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{"paused":true}'
```

### Debug with Ray ID

```bash
# Use the Ray ID from the error page
# to find the exact rule that blocked you

# Check Security > Events for that Ray ID
# The event log shows which rule matched
```

## Common Mistakes

- Accidentally blocking your own IP address
- Using overly broad IP ranges in blocking rules
- Not testing firewall rules in Log Only mode first
- Forgetting that firewall rules apply to the entire zone
- Not regularly reviewing security events for false positives

## Related Pages

- [Cloudflare 1021 Error]({{< relref "/tools/cloudflare/cloudflare-1021" >}}) — Rewrite Rules
- [Cloudflare 1022 Error]({{< relref "/tools/cloudflare/cloudflare-1022" >}}) — Could not find host
