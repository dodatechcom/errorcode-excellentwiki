---
title: "[Solution] Heroku Pipeline Error - Fix Pipeline Promotion Failed"
description: "Fix Heroku pipeline promotion failures when deploying between stages. Resolve config, addon, and review app promotion issues."
tools: ["heroku"]
error-types: ["pipeline-error"]
severities: ["error"]
weight: 5
---

This error means a Heroku pipeline promotion from one stage to another failed. The target app could not receive the configuration, addons, or slug from the source app.

## What This Error Means

When you promote an app in a pipeline and it fails, you see:

```
Promotion failed: app config does not match
# or
Error: Cannot promote to app with different addon plan
# or
Pipeline promotion error: target app build failed
```

Pipeline promotions move code and configuration from staging to production. Failures indicate mismatches between pipeline stages.

## Why It Happens

- The target app has different addon plans than the source
- Environment variables are missing in the target app
- The target app has a different buildpack configuration
- The target app is in maintenance mode
- The slug on the source app is not compiled yet
- The target app has incompatible config vars

## How to Fix It

### Check pipeline status

```bash
heroku pipelines:info my-pipeline -a my-app
```

Verify all apps in the pipeline are properly configured.

### Promote with specific config vars

```bash
heroku pipelines:promote -a staging-app --to production
```

Ensure staging and production have matching addon plans.

### Sync config vars between apps

```bash
heroku config -a staging-app --json > config.json
heroku config:set $(cat config.json | jq -r 'to_entries | map("\(.key)=\(.value)") | .[]') -a production
```

### Verify addon compatibility

```bash
heroku addons -a staging-app
heroku addons -a production
```

Both apps need the same addon types (even if different plans).

### Check promotion order

```bash
heroku pipelines:promote -r staging -a my-pipeline
```

Promote from the correct stage (review -> staging -> production).

### Use CI for automated promotions

```yaml
# .circleci/config.yml
- run:
    name: Promote to production
    command: heroku pipelines:promote -a staging-app
```

### Handle build failures in promotion

```bash
heroku builds -a production
heroku builds:info <build-id> -a production
```

Check if the target app's build failed during promotion.

### Review app configuration

```bash
heroku review-apps -a my-pipeline
```

Ensure review apps have correct configuration before promoting to staging.

## Common Mistakes

- Not keeping addon plans consistent across pipeline stages
- Promoting before the staging app has a compiled slug
- Missing environment variables that exist in staging but not production
- Not testing the staging app before promoting to production
- Forgetting that promotion copies the slug, not the git history

## Related Pages

- [Heroku Deploy Error]({{< relref "/tools/heroku/heroku-deploy-error" >}}) -- deployment issues
- [Heroku Config Error]({{< relref "/tools/heroku/heroku-config-error" >}}) -- configuration problems
- [Heroku Review App Error]({{< relref "/tools/heroku/heroku-review-app-error" >}}) -- review app issues
