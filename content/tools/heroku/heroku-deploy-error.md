---
title: "[Solution] Heroku Push Rejected Error — Fix Deployment Rejections"
description: "Fix Heroku push rejected errors. Resolve git push failures, buildpack issues, and deployment rejection problems."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
---

A Heroku push rejected error occurs when your git push to Heroku is rejected. This can happen due to build failures, invalid code, or configuration issues that prevent the deployment from proceeding.

## What This Error Means

When Heroku rejects your push, it returns an error like:

```
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://git.heroku.com/my-app.git'
```

Or the push succeeds but the build fails:

```
remote: -----> Building...
remote: !     Push rejected, failed to compile Node.js app.
```

## Why It Happens

- The build fails during compilation
- Missing package.json or requirements.txt
- The buildpack cannot detect your language
- The app has errors that prevent startup
- The Procfile is misconfigured
- Dependencies are not in the correct file
- The push was to the wrong remote

## How to Fix It

### Check Heroku Remote

```bash
# Verify Heroku remote is set
git remote -v

# Add remote if missing
heroku git:remote -a my-app
```

### Check Build Logs

```bash
# View recent build logs
heroku logs --tail

# View specific build output
heroku logs --source app
```

### Fix Buildpack Detection

```bash
# Manually set buildpack
heroku buildpacks:set heroku/nodejs

# Add multiple buildpacks
heroku buildpacks:add heroku/nodejs
heroku buildpacks:add heroku/python
```

### Ensure Required Files Exist

```bash
# For Node.js
ls package.json package-lock.json

# For Python
ls requirements.txt Procfile

# For Ruby
ls Gemfile
```

### Fix Procfile

```yaml
# Procfile (no extension)
web: node server.js
worker: python worker.py
```

### Force Push (Use Carefully)

```bash
# If you need to force push to Heroku
git push heroku main --force
```

### Check App Status

```bash
# Check if app exists
heroku apps:info

# Check build status
heroku ps
```

### Redeploy

```bash
# Make a small change and redeploy
echo "" >> README.md
git add README.md
git commit -m "Trigger redeploy"
git push heroku main
```

## Common Mistakes

- Not committing package-lock.json or yarn.lock
- Using npm scripts that only work locally
- Missing Procfile for non-Node.js apps
- Not specifying the correct buildpack
- Pushing to the wrong Heroku remote

## Related Pages

- [Heroku Build Error]({{< relref "/tools/heroku/heroku-build-error" >}}) — Build failed / compilation error
- [Heroku Runtimes Error]({{< relref "/tools/heroku/heroku-runtimes-error" >}}) — No such app
