---
title: "[Solution] Heroku App Not Found or No Access — How to Fix"
description: "Fix Heroku app not found errors by verifying app name, checking account access, confirming team membership, using correct git remote, and configuring multi-account authentication."
tools: ["heroku"]
error-types: ["app-not-found"]
severities: ["error"]
weight: 5
comments: true
---

A Heroku app not found error occurs when a CLI command or API request references an application that does not exist or the requesting user does not have access to it. This is one of the most common Heroku CLI errors.

## What This Error Means

When you run a Heroku CLI command with `--app my-app` or `-a my-app`, Heroku's API looks up the application by name. The API response depends on the app's existence and the user's permissions:

- If the app does not exist at all, you get a "not found" error
- If the app exists but your account does not have access, you also get a "not found" error (Heroku does not reveal app existence to unauthorized users)
- If the app is in a team/enterprise account and you are not a member, you cannot see it

This error can also occur with git remotes if the remote is misconfigured or points to a non-existent app.

## Why It Happens

- The app name is misspelled or incorrect in the CLI command
- The app exists but you are logged into the wrong Heroku account
- The app is in a Heroku Team or Enterprise account that you do not belong to
- The app was deleted by another team member
- The git remote `heroku` points to a different or deleted app
- The app is in a different region and the CLI is configured for the wrong region
- The API token does not have permission to access the app
- The app uses spaces or special characters in its name

## Common Error Messages

```
 ▸    Couldn't find that app.
# or
 ▸    !    `my-app` is not a valid Heroku app name
# or
 ▸    You do not have access to the app my-app
# or
 ▸    Git remote heroku points to a different app (old-app vs my-app)
```

## How to Fix It

### 1. Verify the App Exists

```bash
# List all apps you have access to
heroku apps

# Search for a specific app
heroku apps --all | grep my-app

# Check the app's region and owner
heroku apps:info my-app
```

### 2. Check Which Account You Are Logged Into

```bash
# Check current authentication
heroku auth:whoami
heroku auth:token

# If you are logged into the wrong account:
heroku logout
heroku login

# Or use the -i flag for non-interactive login
heroku login -i
```

### 3. Check Team and Organization Access

```bash
# List your teams
heroku teams

# List apps in a specific team
heroku apps --team my-team

# Check if you are a member of the correct team
heroku members -t my-team
```

### 4. Fix Git Remote Configuration

```bash
# View current git remotes
git remote -v

# The heroku remote should point to:
# https://git.heroku.com/my-app.git
# or
# git@heroku.com:my-app.git

# Fix a wrong remote
git remote remove heroku
heroku git:remote -a my-app

# Add a remote for a team app
heroku git:remote -a my-app -r staging
```

### 5. Check with Pipeline and Review Apps

```bash
# If the app is part of a pipeline
heroku pipelines:list
heroku pipelines:info my-pipeline

# Review apps are temporary and may have been deleted
# Recreate if needed
heroku review-app:create my-pr-42
```

### 6. Use API Token for Scripts

```bash
# Get a fresh API token
heroku auth:token

# Use the token in scripts
curl -H "Authorization: Bearer $(heroku auth:token)" \
    -H "Accept: application/vnd.heroku+json; version=3" \
    https://api.heroku.com/apps/my-app
```

### 7. Check for Deleted Apps

```bash
# Apps deleted within the last 30 days can be recovered
heroku apps:list --include-deleted

# To recover a deleted app (contact Heroku support)
# Or redeploy from your git repository
git push heroku main
```

### 8. Use the Correct Region

```bash
# Check which region your app is in
heroku regions

# Access a US-based app even if you are in Europe
heroku apps:info my-app --region us

# Set the default region
heroku config:set HEROKU_REGION=eu -a my-app
```

## Common Scenarios

### Multiple Heroku Accounts

A developer has both personal and work Heroku accounts. They are logged into their personal account but trying to access a work app. The app does not appear in `heroku apps`. Switch accounts with `heroku login` using the work credentials.

### App Deleted by Team Member

A team member accidentally deletes a production app. Other team members see "app not found" when running CLI commands. Recover the app within 30 days by contacting Heroku support, or redeploy from the latest git commit.

### Stale Git Remote After App Recreation

A team deletes and recreates a Heroku app with the same name. The local git remote still contains the old app's ID, causing `heroku run` and other commands to fail. Run `heroku git:remote -a my-app` to update the remote.

## Prevent It

- Use Heroku Pipelines with consistent naming conventions for apps
- Maintain team membership documentation and regularly audit access
- Use separate git remotes for staging and production (e.g., `git remote add staging ...`)
- Set `HEROKU_APP` environment variable in CI/CD to avoid app name mismatches
- Use Heroku Platform API with app IDs (UUIDs) instead of names in automation
- Implement app naming conventions (e.g., `project-environment-count`)
- Audit Heroku teams quarterly and remove inactive members
- Use Heroku's `app.json` manifest for review app standardization

## Related Pages

- [Heroku Config Error](/tools/heroku/heroku-config-error)
- [Heroku Rate Limit Error](/tools/heroku/heroku-rate-limit-error)
- [Heroku CLI Configuration Error](/tools/heroku/heroku-rc-error)
