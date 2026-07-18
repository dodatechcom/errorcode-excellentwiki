---
title: "[Solution] Heroku Maintenance Mode - Fix App in Maintenance Mode"
description: "Fix Heroku apps stuck in maintenance mode. Enable, disable, and troubleshoot maintenance mode for planned downtime and deployments."
tools: ["heroku"]
error-types: ["maintenance-mode"]
severities: ["warning"]
weight: 5
---

This error means your Heroku app is in maintenance mode and returning 503 errors to all visitors. This is intentional during planned maintenance but problematic if left enabled.

## What This Error Means

When maintenance mode is enabled, all requests receive a generic maintenance page:

```
HTTP 503 Service Unavailable
```

Heroku serves a static maintenance page while the app is in this state. No application code runs while maintenance mode is active.

## Why It Happens

- You enabled maintenance mode for a planned migration and forgot to disable it
- A deployment script enabled maintenance mode but did not complete the process
- A collaborator enabled maintenance mode without notifying the team
- The app was in maintenance mode when the last deployment occurred
- A build failure left the app in maintenance mode

## How to Fix It

### Check maintenance mode status

```bash
heroku maintenance -a my-app
```

This shows whether maintenance mode is currently on or off.

### Disable maintenance mode

```bash
heroku maintenance:off -a my-app
```

### Enable maintenance mode for planned work

```bash
heroku maintenance:on -a my-app
```

### Use a custom maintenance page

```bash
heroku maintenance:on -m "Upgrading database. Back in 10 minutes." -a my-app
```

### Check if the app is responding

```bash
curl -I https://my-app.herokuapp.com
```

A 503 response confirms maintenance mode is active.

### Verify the last deployment

```bash
heroku builds -a my-app
```

Check if a deployment occurred while maintenance mode was on.

### Automate maintenance mode in deployment

```bash
#!/bin/bash
heroku maintenance:on -a my-app
heroku run python manage.py migrate -a my-app
heroku maintenance:off -a my-app
```

### Use config vars to show maintenance pages

```bash
heroku config:set MAINTENANCE_MODE=true -a my-app
```

Implement custom maintenance page logic in your application.

## Common Mistakes

- Forgetting to disable maintenance mode after completing maintenance
- Enabling maintenance mode without notifying users first
- Not testing the custom maintenance page before enabling maintenance mode
- Leaving maintenance mode on for extended periods
- Not checking maintenance mode status after a failed deployment

## Related Pages

- [Heroku Deploy Error]({{< relref "/tools/heroku/heroku-deploy-error" >}}) -- deployment issues
- [Heroku Config Error]({{< relref "/tools/heroku/heroku-config-error" >}}) -- configuration problems
- [Heroku Dyno Error]({{< relref "/tools/heroku/heroku-dyno-error" >}}) -- dyno issues
