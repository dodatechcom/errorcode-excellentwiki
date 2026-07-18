---
title: "[Solution] Heroku Addon Error - Fix Addon Provisioning Failed"
description: "Fix Heroku addon provisioning failures. Resolve addon limits, billing issues, and addon service connection problems."
tools: ["heroku"]
error-types: ["addon-error"]
severities: ["error"]
weight: 5
---

This error means a Heroku addon could not be provisioned or connected. The addon provider may have issues, your account may have limits, or the addon configuration may be incorrect.

## What This Error Means

When addon provisioning fails, you see:

```
Addon provisioning failed: plan limit exceeded
# or
Heroku API error: addon already exists on this app
# or
Error: Unable to add addon: billing issue
```

Addons are third-party services that integrate with your Heroku apps. Provisioning failures block access to databases, caching, monitoring, and other services.

## Why It Happens

- Your account has reached the addon plan limit
- A billing issue prevents new addon creation
- The addon provider's API is temporarily unavailable
- The addon already exists on the app
- The addon plan is no longer available
- The addon requires a specific region or tier

## How to Fix It

### Check account limits

```bash
heroku addons --account my-account
```

Review current addons across all apps to identify limits.

### Resolve billing issues

```bash
heroku billing -a my-app
```

Update payment information if there are outstanding charges.

### Verify addon availability

```bash
heroku addons:create heroku-postgresql:essential-0 -a my-app
```

Check that the addon plan still exists and is available.

### Remove unused addons

```bash
heroku addons:destroy heroku-redis:mini -a my-app
```

Freeing up slots allows new addon creation.

### Check addon status

```bash
heroku addons:info -a my-app
```

Verify the addon is fully provisioned and connected.

### Recreate a failed addon

```bash
heroku addons:destroy heroku-postgresql:essential-0 -a my-app
heroku addons:create heroku-postgresql:essential-0 -a my-app
```

### Attach addon to a different app

```bash
heroku addons:attach heroku-postgresql:momentous-hilum-5642 --app target-app
```

Share addons between apps when needed.

### Check addon provider status

```bash
curl -I https://status.heroku.com
```

Heroku platform issues can affect addon provisioning.

## Common Mistakes

- Not checking addon plan limits before attempting creation
- Assuming addon provisioning is instant when it can take minutes
- Not monitoring addon status after creation
- Forgetting that removing an addon may delete its data
- Not setting up addon backups before destroying addons

## Related Pages

- [Heroku Config Error]({{< relref "/tools/heroku/heroku-config-error" >}}) -- configuration issues
- [Heroku Database Error]({{< relref "/tools/heroku/heroku-database-error" >}}) -- database problems
- [Heroku API Error]({{< relref "/tools/heroku/heroku-api-error" >}}) -- API failures
