---
title: "[Solution] Heroku Review App Error - Fix Review App Creation Failed"
description: "Fix Heroku review app creation failures. Resolve pipeline, config, and database issues preventing review app deployment."
tools: ["heroku"]
error-types: ["review-app-error"]
severities: ["error"]
weight: 5
---

This error means a Heroku review app could not be created from a pull request. The pipeline configuration, database, or build process failed during review app setup.

## What This Error Means

When a review app fails to create, you see:

```
Review app creation failed: unable to provision database
# or
Error: build failed for review app
# or
Review app config is invalid
```

Review apps are temporary Heroku apps created from pull requests. They require a valid pipeline configuration and can fail at multiple stages.

## Why It Happens

- The `app.json` file is missing or has invalid configuration
- The database addon cannot be provisioned for the review app
- The buildpack is not specified and auto-detection fails
- The review app environment variables are not defined
- The pipeline does not have review apps enabled
- The addon plan used in `app.json` is not available
- The repository is not connected to the pipeline

## How to Fix It

### Verify app.json configuration

```json
{
  "name": "my-app",
  "scripts": {
    "postdeploy": "python manage.py migrate"
  },
  "env": {
    "SECRET_KEY": {
      "description": "Secret key",
      "generator": "secret"
    }
  },
  "addons": [
    "heroku-postgresql:essential-0"
  ],
  "buildpacks": [
    { "url": "heroku/python" }
  ]
}
```

### Enable review apps on the pipeline

```bash
heroku review-apps:enable -a my-pipeline
```

### Check database addon availability

```json
"addons": [
  {
    "plan": "heroku-postgresql:essential-0"
  }
]
```

Ensure the database plan exists and is available.

### Test the build locally

```bash
heroku local -f app.json
```

Validate that the build process works before pushing.

### Check review app logs

```bash
heroku logs --tail -a my-pr-review-app
```

Review build and startup logs for errors.

### Set required environment variables

```bash
heroku review-apps:configure -a my-pipeline
```

Configure environment variables that review apps need.

### Verify the repository is connected

```bash
heroku pipelines:info my-pipeline
```

Ensure the pipeline is connected to the correct repository.

### Fix postdeploy scripts

If `postdeploy` scripts fail, review the app will not start. Check for migration errors or missing dependencies.

## Common Mistakes

- Not including an `app.json` in the repository root
- Using addon plans that require manual approval
- Not testing `app.json` locally before pushing
- Forgetting that review apps need database access
- Not setting up environment variable generators for secrets

## Related Pages

- [Heroku Pipeline Error]({{< relref "/tools/heroku/heroku-pipeline-error" >}}) -- pipeline issues
- [Heroku Build Error]({{< relref "/tools/heroku/heroku-build-error" >}}) -- build failures
- [Heroku Config Error]({{< relref "/tools/heroku/heroku-config-error" >}}) -- configuration problems
