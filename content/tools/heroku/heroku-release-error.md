---
title: "[Solution] Heroku Release Failed or Rolled Back — How to Fix"
description: "Fix Heroku release phase failures by checking release commands, build manifest issues, database migration errors, and reviewing release output logs for troubleshooting."
tools: ["heroku"]
error-types: ["release-error"]
severities: ["error"]
weight: 5
comments: true
---

A Heroku release phase error occurs when the release command defined in your `Procfile` or `app.json` fails. This prevents the new version of your application from being deployed, and the previous release remains active.

## What This Error Means

The release phase in Heroku runs a command defined in your `Procfile` (e.g., `release: rake db:migrate`) after a successful build but before your application starts. If this command exits with a non-zero code, the release is marked as failed and the deployment is rolled back automatically.

Unlike a build error (which happens during slug compilation), a release error happens at runtime during the release process. The app continues running the previous release until the issue is fixed.

## Why It Happens

- Database migration commands fail due to schema conflicts or connection issues
- The release command references environment variables that are not set
- A third-party service required during release is unavailable
- The release process exceeds the 60-minute timeout
- The `Procfile` has incorrect syntax for the release command
- Multiple releases are queued and concurrent migrations conflict
- The app is in maintenance mode, preventing release execution
- Insufficient memory or dyno resources for the release process

## Common Error Messages

```
 ▸    Error: release command failed with exit code 1
# or
 ▸    Could not find database config for environment 'production'
# or
 ▸    !   Release command returned a non-zero exit code
# or
 ▸    Timeout exceeded while running release command
```

## How to Fix It

### 1. View Release Output and Logs

```bash
# Check release history
heroku releases -a my-app

# View specific release output
heroku releases:output v42 -a my-app

# Stream release logs
heroku logs --tail -a my-app
```

The release output shows the exact error message from the release command. This is the most important diagnostic step.

### 2. Run the Release Command Manually

```bash
# Run a one-off dyno to test the release command
heroku run "rake db:migrate" -a my-app

# If it fails, you get immediate feedback
# Fix the issue, commit, and redeploy
```

Running the command in a one-off dyno mimics the release environment and helps identify missing config vars, connection issues, or migration errors.

### 3. Check Config Vars

```bash
# List all config vars
heroku config -a my-app

# Check for missing required vars
heroku config:get DATABASE_URL -a my-app
heroku config:get RAILS_MASTER_KEY -a my-app
```

Release commands often depend on config vars. Missing or incorrect values cause failures.

### 4. Fix the Procfile Release Command

```bash
# Check current Procfile
cat Procfile

# A valid release command:
release: rake db:migrate

# For Rails apps with encrypted credentials:
release: RAILS_MASTER_KEY=$RAILS_MASTER_KEY rake db:migrate

# For npm-based apps:
release: npm run migrate
```

### 5. Handle Concurrent Release Conflicts

```bash
# Check if there are pending releases
heroku releases -a my-app | head -10

# Cancel a stuck release
heroku releases:cancel -a my-app

# Enable maintenance mode before running migrations manually
heroku maintenance:on -a my-app
heroku run "rake db:migrate" -a my-app
heroku maintenance:off -a my-app
```

### 6. Increase Release Timeout for Long Migrations

```bash
# The default timeout is 60 minutes
# For large databases, optimize migrations to run faster:
# - Batch large data migrations
# - Use background jobs for long-running tasks
# - Split into multiple smaller releases

# Example: Use `find_each` in Rails migrations
# User.find_each(batch_size: 500) do |user|
#   user.update_attribute(:new_column, compute_value(user))
# end
```

### 7. Debug with a Simple Release Command

```bash
# Temporarily replace the release command with a simple echo
echo "release: echo 'Release phase running'" > Procfile

# Deploy to test the pipeline
git commit -am "test: simple release command"
git push heroku main

# Once confirmed, restore the real release command
```

## Common Scenarios

### Rails Database Migration Failure on Production

A Rails application adds a new column with a default value to a large table. The migration runs `ALTER TABLE` which locks the table and times out. The release phase fails and Heroku rolls back. The fix is to add the column with a nullable value first, then backfill the data, then add the default constraint.

### Missing Environment Variable for Release

A Node.js app uses `process.env.DATABASE_URL` in the release command, but the config var is named `DB_URL` in Heroku. The release fails with `undefined` connection string. Rename the config var or update the code to use `DB_URL`.

### Conflicting Migrations from Multiple Deploys

Two developers push to the same Heroku app within seconds. Both deployments trigger release commands that run `rake db:migrate`. The second migration fails because the first already applied a migration. Heroku serializes release commands, so this is rare. Use `disable_ddl_transaction` for risky migrations.

## Prevent It

- Always test release commands locally with production-like config
- Use `heroku run` to test release commands before deploying
- Make database migrations reversible and failure-resistant
- Add null checks and fallbacks in release scripts
- Monitor release phase execution time and optimize slow operations
- Use a staging pipeline to test releases before production
- Set up notifications for release failures using Heroku webhooks
- Keep release commands idempotent (safe to run multiple times)

## Related Pages

- [Heroku Dyno Error](/tools/heroku/heroku-dyno-error)
- [Heroku Config Error](/tools/heroku/heroku-config-error)
- [Heroku Buildpack Error](/tools/heroku/heroku-buildpack-error)
