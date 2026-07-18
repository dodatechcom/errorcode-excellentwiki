---
title: "[Solution] Heroku Deploy Rejected - Fix Push Rejected Deploy Protection"
description: "Fix Heroku push rejected errors when deploy protection blocks deployment. Resolve review apps, pipeline rules, and git push issues."
tools: ["heroku"]
error-types: ["deploy-rejected"]
severities: ["error"]
weight: 5
---

This error means Heroku rejected your git push because deploy protection rules are active. The push was blocked by pipeline review requirements or deployment gates.

## What This Error Means

When deploy protection blocks a push, you see:

```
remote: !   Push rejected, deploy protection rule failed
# or
remote: !   Not authorized to deploy to production
# or
remote: !   Review app required before production deployment
```

Heroku pipelines can enforce deployment rules that require review, approval, or specific conditions before code reaches production.

## Why It Happens

- The pipeline has a review app requirement for production
- Deploy protection rules require manual approval
- The branch being pushed is not allowed for deployment
- CI/CD checks have not passed before the push
- The user pushing does not have deploy permissions
- The pipeline requires a specific merge process

## How to Fix It

### Check pipeline deploy rules

```bash
heroku pipelines:info my-pipeline -a my-app
```

Review the pipeline configuration for protection rules.

### Review deploy protection settings

```bash
heroku pipelines:diff -a my-app
```

Check what changes would be deployed and any blocking rules.

### Disable review requirement temporarily

```bash
heroku pipelines:update -a my-pipeline --review=false
```

### Add the user as a collaborator

```bash
heroku access:add user@example.com -a my-app --privilege deploy
```

Ensure the deploying user has deploy permissions.

### Deploy via the Heroku dashboard

```bash
# Or use Heroku API
curl -X POST https://api.heroku.com/apps/my-app/builds \
  -H "Authorization: Bearer $HEROKU_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"source":{"url":"https://github.com/user/repo/tarball/main"}}'
```

### Use Heroku CI instead of git push

```yaml
# Heroku CI config in app.json
{
  "scripts": {
    "test": "python manage.py test"
  }
}
```

### Check CI pipeline status

```bash
heroku CI -a my-app
```

Ensure CI tests pass before deployment.

### Merge to the correct branch

```bash
git checkout main
git merge feature-branch
git push heroku main
```

Deploy from the branch that pipeline rules allow.

## Common Mistakes

- Not understanding pipeline deploy rules before setting them up
- Pushing to the wrong branch that pipeline rules block
- Forgetting that Heroku requires explicit deploy permissions for team members
- Not running tests locally before pushing to a protected branch
- Assuming git push bypasses pipeline review requirements

## Related Pages

- [Heroku Deploy Error]({{< relref "/tools/heroku/heroku-deploy-error" >}}) -- deployment issues
- [Heroku Pipeline Error]({{< relref "/tools/heroku/heroku-pipeline-error" >}}) -- pipeline configuration
- [Heroku Review App Error]({{< relref "/tools/heroku/heroku-review-app-error" >}}) -- review app issues
