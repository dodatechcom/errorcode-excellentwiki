---
title: "[Solution] Netlify Deploy Preview Error — Fix Preview Not Generating"
description: "Fix Netlify deploy preview errors when pull request preview deployments fail to generate. Resolve branch settings, build configuration, and notification issues."
tools: ["netlify"]
error-types: ["deploy-error"]
severities: ["error"]
weight: 5
---

A Netlify deploy preview error occurs when a preview deployment for a pull request is not created. The preview URL is not generated or the build fails specifically for previews.

## What This Error Means

Netlify creates preview deployments for pull requests. When they fail:

```
Error: Deploy Preview for PR #123 failed to build
Build failed: Error during build
```

Or:

```
Error: Deploy Preview is not available
No preview URL was generated
```

## Why It Happens

- The build fails specifically for the PR branch but succeeds on main
- The deploy preview feature is not enabled for the branch
- The repository does not have the Netlify webhook configured
- The PR is from a fork without repository access
- The build environment detects an incorrect context (production instead of deploy-preview)
- The `netlify.toml` preview-specific configuration has errors
- The branch name does not match the deploy preview branch settings

## How to Fix It

### Check Deploy Preview Settings

Netlify Dashboard > Site > Deploys > Deploy Settings > Deploy Previews.

### Enable Deploy Previews for Branches

```toml
[build]
  publish = "dist"

[context.deploy-preview]
  command = "npm run build:preview"
```

### Add Context-Specific Configuration

```toml
[context.production]
  command = "npm run build"

[context.deploy-preview]
  command = "npm run build:preview"
  publish = "dist-preview"

[context.branch-deploy]
  command = "npm run build:branch"
```

### Check Branch Naming

```toml
[build]
  # Only generate previews for branches starting with "feature/"
  ignore = "git diff --quiet HEAD^ HEAD . && [[ $BRANCH != feature/* ]]"
```

### Re-trigger Deploy Preview

Close and re-open the pull request to trigger a new deploy preview.

### Check Fork PR Configuration

For PRs from forks, enable "Deploy Previews for Pull Requests from Forks" in settings.

### Verify Webhook

Check GitHub > Repository > Settings > Webhooks for the Netlify webhook.

## Common Mistakes

- Not creating a deploy-preview context in netlify.toml when preview builds have different requirements
- Not enabling deploy previews for branches in the dashboard settings
- Assuming deploy previews work the same as production builds
- Forgetting to check the deploy log for preview-specific errors

## Related Pages

- [Netlify Deploy Error]({{< relref "/tools/netlify/netlify-deploy-error" >}}) -- Deploy failures
- [Netlify Build Error]({{< relref "/tools/netlify/netlify-build-error" >}}) -- Build failures
- [Netlify Plugin Error]({{< relref "/tools/netlify/netlify-plugin-error" >}}) -- Plugin issues
