---
title: "[Solution] Netlify Split Test Configuration Error — How to Fix"
description: "Fix Netlify split test configuration errors. Resolve A/B test setup failures, traffic distribution issues, and variant problems."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
comments: true
---

A Netlify split test configuration error occurs when your A/B test or split test cannot be created, started, or is not distributing traffic correctly across your variants.

## What This Error Means

Netlify Split Testing allows you to run A/B tests by splitting traffic between different deploy previews or branches. When the test configuration is invalid, traffic may not be distributed, the test may not start, or all users may see only one variant.

## Why It Happens

- The test has fewer than two variants configured
- The branches or deploy previews referenced no longer exist
- Traffic weight distribution does not add up to 100%
- The test URL pattern is invalid or too broad
- The test was paused or expired
- Deploy previews were deleted but the test still references them
- The test is trying to split traffic on a page that returns non-HTML content
- The Netlify CLI or API is used incorrectly to manage the test

## Common Error Messages

- `Invalid split test configuration` — Test settings are invalid
- `Variants not found` — Referenced branches or deploys do not exist
- `Traffic distribution error` — Weights do not sum to 100%
- `Split test could not be created` — Missing required fields

## How to Fix It

### Verify Test Configuration

```bash
# Check split test status via Netlify API
curl -X GET "https://api.netlify.com/api/v1/sites/SITE_ID/split_tests" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" | jq '.[] | {id, name, active, branches}'

# Check specific test details
curl -X GET "https://api.netlify.com/api/v1/sites/SITE_ID/split_tests/TEST_ID" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Set Up Split Tests Correctly

```toml
# netlify.toml — configure split test context
[build]
  command = "npm run build"

# Split tests work best with branch-based deploys
# In Netlify Dashboard:
# 1. Go to Split Testing
# 2. Click "New Split Test"
# 3. Select the page path to test
# 4. Add variants from existing branches or deploys
```

### Fix Traffic Distribution

```bash
# Traffic weights must sum to 100%
# Example for 3 variants:
# Control: 34%
# Variant A: 33%
# Variant B: 33%

# Via API
curl -X POST "https://api.netlify.com/api/v1/sites/SITE_ID/split_tests" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
    "name": "Homepage Test",
    "path": "/",
    "variants": [
      {"branch": "main", "weight": 50},
      {"branch": "feature-new-hero", "weight": 50}
    ]
  }'
```

### Ensure Variant Branches Exist

```bash
# Check that branches exist
git branch -a | grep feature-new-hero

# If the branch was deleted, recreate it from the deploy
git checkout -b feature-new-hero origin/main

# Or use an existing deploy preview
# In Netlify Dashboard: Deploys > Find the deploy > Copy deploy ID
```

### Test with Cookies

```javascript
// Force a specific variant for testing
// Netlify sets a cookie: nf_split=<variant-id>

// To preview a specific variant in development
document.cookie = 'nf_split=variant-a-id; path=/';

// Or use URL parameter (for development only)
const params = new URLSearchParams(window.location.search);
if (params.has('variant')) {
  document.cookie = `nf_split=${params.get('variant')}; path=/`;
}
```

### End a Split Test

```bash
# End a split test via API
curl -X PATCH "https://api.netlify.com/api/v1/sites/SITE_ID/split_tests/TEST_ID" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{"active": false}'

# Or end via Netlify Dashboard:
# Split Testing > Click on test > End Test
# Select the winning variant to promote to production
```

### Verify Split Test Assignment

```javascript
// Check which variant a user is seeing
const nfSplit = document.cookie
  .split('; ')
  .find(row => row.startsWith('nf_split='));

if (nfSplit) {
  const variantId = nfSplit.split('=')[1];
  console.log('User assigned to variant:', variantId);
} else {
  console.log('No variant assigned (control group)');
}
```

### Track Split Test Results

```javascript
// Track conversion events for each variant
function trackConversion(event, variant) {
  // Send to your analytics tool
  gtag('event', event, {
    event_category: 'split_test',
    event_label: variant,
  });
}

// On the conversion page
const params = new URLSearchParams(window.location.search);
const variant = document.cookie
  .split('; ')
  .find(row => row.startsWith('nf_split='))
  ?.split('=')[1] || 'control';

trackConversion('signup', variant);
```

## Common Scenarios

- **Variant branch deleted:** A split test references `feature-redesign` but that branch was merged and deleted. The variant shows as "not found" in the dashboard.
- **Traffic 0/100:** Both variants have 0% weight assigned, causing Netlify to show only one variant 100% of the time.
- **Wrong path pattern:** The test is configured for `/blog/*` but the page you want to test is at `/` (the root path, not under `/blog/`).

## Prevent It

1. Never delete variant branches while a split test is active — merge but keep the branch until the test concludes
2. Verify traffic weights sum to exactly 100% before starting the test
3. Use the Netlify Dashboard preview feature to verify each variant renders correctly before distributing traffic

## Related Pages

- [Netlify Deploy Error]({{< relref "/tools/netlify/netlify-deploy-error" >}}) — Deployment failed
- [Netlify Redirect Error]({{< relref "/tools/netlify/netlify-redirect-error" >}}) — Redirect misconfiguration
