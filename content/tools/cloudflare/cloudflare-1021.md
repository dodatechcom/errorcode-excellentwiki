---
title: "[Solution] Cloudflare 1021 Rewrite Rules Error — Fix Transform Rules"
description: "Fix Cloudflare 1021 rewrite rules errors. Resolve Transform Rules issues and URL rewriting failures."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
weight: 8
---

A Cloudflare 1021 error occurs when a Transform Rule or Rewrite Rule creates an invalid or infinite redirect loop. Cloudflare detects problematic rules and returns this error before processing the request.

## What This Error Means

The 1021 error means Cloudflare found an issue with your rewrite or transform rules. The rule either creates an infinite loop, produces an invalid URL, or conflicts with another rule. The error page shows "Error 1021: Rewrite Rules" along with a Ray ID.

## Why It Happens

- A rewrite rule redirects to itself, creating a loop
- The transform rule produces an invalid URL
- Multiple rewrite rules conflict with each other
- The rule matches too broadly and captures redirects
- The rule uses invalid regex patterns
- Origin server redirects back to Cloudflare URL

## How to Fix It

### Check Transform Rules

```bash
# In Cloudflare Dashboard:
# Rules > Transform Rules > Modify Request
# Review all active rules for conflicts
```

### Identify the Loop

```bash
# Use curl to see the redirect chain
curl -vL http://your-domain.com/path 2>&1 | grep "< location"

# Check for redirects that point to the same path
# or create A -> B -> A loops
```

### Test Rules with Log Mode

```bash
# In Cloudflare Dashboard:
# Rules > Transform Rules > Toggle rule to "Log"

# This will log matching requests
# without actually modifying them
# Check Security > Events for matches
```

### Fix Common Rewrite Patterns

```bash
# WRONG: Rewrite that matches its own output
# Match: /old-path/*
# Rewrite to: /old-path/v2/*

# RIGHT: Use a more specific match
# Match: /old-path/(.*)
# Rewrite to: /new-path/$1
```

### Validate Regex Patterns

```python
import re

# Test your regex before using in rules
pattern = r"^/old-path/(.*)$"
test_url = "/old-path/page1"

match = re.match(pattern, test_url)
if match:
    new_path = f"/new-path/{match.group(1)}"
    print(f"Rewrite: {test_url} -> {new_path}")
```

### Check for Origin Redirects

```bash
# If origin redirects back to Cloudflare URL
# this can create a loop

# Test origin directly
curl -I http://ORIGIN_IP/path

# If origin redirects to https://your-domain.com
# and your rule rewrites to origin, it loops
```

### Disable Rules Temporarily

```bash
# Use Cloudflare API to disable a rule
curl -X PATCH \
  "https://api.cloudflare.com/client/v4/zones/ZONE_ID/rulesets/RULESET_ID" \
  -H "Authorization: Bearer API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
    "rules": [{
      "id": "RULE_ID",
      "enabled": false
    }]
  }'
```

## Common Mistakes

- Not testing rules in Log mode before enabling
- Creating rules that match too broadly
- Forgetting that rewrite rules apply to all matching requests
- Not checking for origin-side redirects that could conflict
- Using overly complex regex that causes unexpected matches

## Related Pages

- [Cloudflare 1020 Error]({{< relref "/tools/cloudflare/cloudflare-1020" >}}) — Access Denied
- [Cloudflare 1022 Error]({{< relref "/tools/cloudflare/cloudflare-1022" >}}) — Could not find host
