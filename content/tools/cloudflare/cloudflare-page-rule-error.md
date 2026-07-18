---
title: "[Solution] Cloudflare Page Rule Conflict or Misconfiguration Error — How to Fix"
description: "Fix Cloudflare page rule conflicts or misconfigurations. Resolve overlapping rules, broken URL patterns, and redirect loops."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
comments: true
---

A Cloudflare page rule conflict or misconfiguration error occurs when multiple page rules match the same URL and their settings contradict each other, or when a rule is misconfigured and causes unexpected behavior on your site. Page rules control caching, security, performance, and routing settings for specific URL patterns.

## What This Error Means

Cloudflare processes page rules in order from most specific to least specific. When two rules match the same URL with conflicting settings (e.g., one rule forces HTTPS and another disables it), Cloudflare applies the first matching rule. Misconfiguration can cause redirect loops, cache bypass on content that should be cached, or security settings being disabled when they should be active.

## Why It Happens

- Multiple rules match the same URL pattern with conflicting settings
- Wildcard patterns are too broad and match unintended URLs
- A rule disables security features that another rule requires
- Redirect rules create infinite loops (A redirects to B, B redirects to A)
- Rule priority ordering causes unexpected behavior
- Rules reference URLs that no longer exist after a site redesign
- The page rules limit for your plan has been reached
- Rules use incorrect syntax in the URL pattern field

## Common Error Messages

- `You have exceeded the maximum number of allowed page rules` — Too many rules on your plan
- `Page rule target is invalid` — The URL pattern is malformed
- `Redirect loop detected` — Conflicting redirect rules cause infinite loops
- `Page rule could not be saved` — Validation error in rule settings
- `Rule already exists` — Duplicate rule detected

## How to Fix It

### Audit Existing Rules

```bash
# List all page rules via API
curl -X GET "https://api.cloudflare.com/client/v4/zones/ZONE_ID/pagerules" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" | jq '.result[] | {id, targets, actions, priority}'

# Get detailed info on a specific rule
curl -X GET "https://api.cloudflare.com/client/v4/zones/ZONE_ID/pagerules/RULE_ID" \
  -H "Authorization: Bearer YOUR_API_TOKEN" | jq '.result'
```

### Identify Conflicting Rules

```javascript
// Check for rules that match overlapping patterns
const rules = [
  { pattern: '*.example.com/*', settings: { always_use_https: true } },
  { pattern: '*.example.com/*', settings: { ssl: 'off' } },
];

// Find conflicts by checking for rules that match the same URL
function findConflicts(rules, testUrl) {
  const matching = rules.filter(rule =>
    matchPattern(rule.pattern, testUrl)
  );

  // Check for conflicting settings
  const conflicts = [];
  for (let i = 0; i < matching.length; i++) {
    for (let j = i + 1; j < matching.length; j++) {
      if (hasConflict(matching[i].settings, matching[j].settings)) {
        conflicts.push({ rule1: matching[i], rule2: matching[j] });
      }
    }
  }
  return conflicts;
}
```

### Fix Redirect Loops

```javascript
// WRONG: Creates a loop
// Rule 1: example.com/* → https://example.com/$1
// Rule 2: https://example.com/* → http://example.com/$1

// RIGHT: Use a single rule with proper conditions
// Rule 1: example.com/* → Always Use HTTPS (single rule, no loop)

// In Cloudflare Dashboard:
// SSL/TLS > Edge Certificates > Always Use HTTPS
// This is safer than creating redirect page rules
```

### Optimize Rule Specificity

```bash
# Rules are evaluated most-specific to least-specific
# Place more specific rules first

# Good rule ordering:
# 1. example.com/api/*    → Bypass Cache (most specific)
# 2. example.com/blog/*   → Cache Everything
# 3. *.example.com/*      → Always Use HTTPS (least specific)

# Use the API to set priority
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/ZONE_ID/pagerules/RULE_ID" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{"priority": 1}'
```

### Delete Unused or Redundant Rules

```bash
# Find rules with no matching traffic
curl -X GET "https://api.cloudflare.com/client/v4/zones/ZONE_ID/pagerules?status=active" \
  -H "Authorization: Bearer YOUR_API_TOKEN" | jq '.result[] | {id, targets}'

# Delete a specific rule
curl -X DELETE "https://api.cloudflare.com/client/v4/zones/ZONE_ID/pagerules/RULE_ID" \
  -H "Authorization: Bearer YOUR_API_TOKEN"

# Disable a rule without deleting it (safer)
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/ZONE_ID/pagerules/RULE_ID" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{"status": "disabled"}'
```

### Test Rules Before Activating

```bash
# Use Cloudflare's preview mode to test rules
# In Dashboard: Rules > Page Rules > Create Page Rule
# Toggle "Disabled" to test without affecting traffic

# Or use the API to create a disabled rule
curl -X POST "https://api.cloudflare.com/client/v4/zones/ZONE_ID/pagerules" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
    "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "example.com/api/*"}}],
    "actions": [{"id": "disable_security"}],
    "priority": 1,
    "status": "disabled"
  }'
```

### Use Transform Rules Instead

```bash
# Cloudflare Transform Rules are more powerful than page rules
# and do not count against your page rule limit

# In Dashboard: Rules > Transform Rules
# You can:
# - Rewrite URLs (similar to page rules but more flexible)
# - Modify headers
# - Set dynamic redirects with conditions
# - Use regex patterns for matching
```

## Common Scenarios

- **Redirect loop after migration:** You set up a "Force HTTPS" page rule but your origin server also redirects HTTP to HTTPS, creating a double redirect that some clients interpret as a loop.
- **Cache settings conflict:** One rule says "Cache Everything" for `example.com/*` while another says "Bypass Cache" for `example.com/api/*`. If the patterns overlap incorrectly, API responses may be cached.
- **Security rule override:** A rule disables "Browser Integrity Check" for a path that should be protected, allowing bot traffic through.

## Prevent It

1. Use Cloudflare's `Always Use HTTPS` toggle globally instead of creating individual page rules for HTTPS redirects
2. Limit page rule patterns to the narrowest possible scope and test each rule with `curl` before activating
3. Keep a documented table of all page rules with their patterns, settings, and expected behavior

## Related Pages

- [Cloudflare WAF Blocked]({{< relref "/tools/cloudflare/cloudflare-1020" >}}) — Access denied by WAF
- [Cloudflare Cache Error]({{< relref "/tools/cloudflare/cloudflare-cache-error" >}}) — Cache configuration issues
