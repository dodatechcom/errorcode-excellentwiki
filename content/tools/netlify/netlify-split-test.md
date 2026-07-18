---
title: "[Solution] Netlify Split Test Error — Fix Branch-Based Split Test Configuration"
description: "Fix Netlify split test errors when branch-based A/B testing configuration fails. Resolve branch settings, traffic distribution, and activation issues."
tools: ["netlify"]
error-types: ["split-test-error"]
severities: ["warning"]
weight: 5
---

A Netlify split test error occurs when branch-based split testing is not configured correctly. Visitors may not be assigned to the correct branch or the test may not activate.

## What This Error Means

Netlify split tests route a percentage of traffic to different branches. When configuration is wrong:

```
Error: Split test "test-name" has no branches configured
```

## Why It Happens

- No branches are configured for the split test
- The branch names in the split test do not match the actual Git branches
- The traffic distribution percentages do not add up to 100
- The split test is active but the branches have no deploys
- The netlify.toml or dashboard configuration has conflicting settings
- The site is not connected to a Git repository
- The required branches have not been deployed yet

## How to Fix It

### Configure Split Tests via Netlify Dashboard

Go to Site > Split Testing > Add a Test and configure branches and traffic percentages.

### Use netlify.toml for Split Test Configuration

```toml
[split_test]
  enabled = true

[[split_test.branches]]
  branch = "main"
  percentage = 50

[[split_test.branches]]
  branch = "experimental"
  percentage = 50
```

### Deploy All Branches First

```bash
git checkout main && git push
git checkout experimental && git push
# Each branch must have a successful deploy
```

### Verify Branch Deploy Status

```bash
netlify deploy --branch main --prod
netlify deploy --branch experimental
```

### Check Branch Names Match Exactly

Branch names in split test configuration must match Git branch names exactly.

### Reset Split Test

Disable and re-enable the split test from the dashboard.

### Check Total Percentage

Ensure branch percentages add up to exactly 100.

## Common Mistakes

- Creating split tests without deploying the branches first
- Using branch names that do not match the actual Git branches
- Setting percentages that do not sum to 100
- Enabling split tests for production without testing on a preview
- Forgetting that split tests work on production deploys only

## Related Pages

- [Netlify Deploy Error]({{< relref "/tools/netlify/netlify-deploy-error" >}}) -- Deploy failures
- [Netlify Domain Error]({{< relref "/tools/netlify/netlify-domain-error" >}}) -- Domain configuration
- [Netlify Build Error]({{< relref "/tools/netlify/netlify-build-error" >}}) -- Build failures
