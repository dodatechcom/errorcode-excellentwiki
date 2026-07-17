---
title: "[Solution] Heroku No Such App Error — Fix App Not Found"
description: "Fix Heroku no such app errors. Resolve app lookup failures, naming issues, and account access problems."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
weight: 3
---

A Heroku no such app error occurs when the Heroku CLI or API cannot find the specified application. This can be due to a wrong app name, account mismatch, or the app being deleted.

## What This Error Means

```
 !    No such app: my-app
```

Heroku cannot locate an application with the given name in your account or team.

## Why It Happens

- The app name is misspelled
- The app belongs to a different account or team
- The app was deleted
- You are not logged into the correct Heroku account
- The Heroku remote URL is wrong
- The app was renamed

## How to Fix It

### Check App Name

```bash
# List your apps
heroku apps

# Check which app the current directory is linked to
heroku apps:info

# Get detailed app information
heroku apps:info --app my-app
```

### Rename an App

```bash
# If the app was renamed, update the reference
heroku apps:rename new-name --app old-name

# Or transfer to a new name
git remote set-url heroku https://git.heroku.com/new-name.git
```

### Verify Login

```bash
# Check current user
heroku auth:whoami

# Login if needed
heroku login
```

### Check Team Access

```bash
# List team apps
heroku apps --team=your-team

# Transfer ownership if needed
heroku apps:transfer new-owner@email.com -a my-app
```

### Fix Git Remote

```bash
# Check remotes
git remote -v

# If wrong, update the remote
git remote set-url heroku https://git.heroku.com/my-app.git

# Or use Heroku CLI
heroku git:remote -a my-app
```

### Find App by URL

```bash
# If you know the app URL
heroku apps:info --app https://my-app.herokuapp.com

# Or from the dashboard
# https://dashboard.heroku.com/apps/my-app
```

### Check for Deleted Apps

```bash
# Recently deleted apps can be restored
heroku apps --all --json | jq '.[].name'

# Restore if needed (within deletion window)
# Contact Heroku support

# Check app status before operations
heroku ps --app my-app
```

### Use Heroku CLI for Discovery

```bash
# Search across all apps you have access to
heroku apps --all

# Filter by team
heroku apps --team=your-team

# Check pipeline membership
heroku pipelines --all
```

## Common Mistakes

- Using the wrong app name after renaming
- Not being logged into the correct Heroku account
- Confusing personal apps with team apps
- Having multiple Heroku accounts configured
- Not updating git remote after app transfer

## Related Pages

- [Heroku Deploy Error]({{< relref "/tools/heroku/heroku-deploy-error" >}}) — Push rejected to Heroku
- [Heroku API Error]({{< relref "/tools/heroku/heroku-api-error" >}}) — Heroku API returned error
