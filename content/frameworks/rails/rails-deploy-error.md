---
title: "[Solution] Rails Deploy Error — How to Fix"
description: "Fix Rails deployment errors. Resolve Capistrano, Docker, and production server configuration issues."
frameworks: ["rails"]
error-types: ["deployment-error"]
severities: ["error"]
weight: 5
comments: true
---

A Rails deployment error occurs when the application fails to deploy due to server configuration, asset compilation, or environment issues.

## Why It Happens

Deployment errors stem from missing environment variables, incorrect server configuration, asset precompilation failures, or database migration issues.

## Common Error Messages

```
PG::ConnectionBad: FATAL: password authentication failed
```

```
Sprockets::FileNotFound: couldn't find file 'application.js'
```

```
Unmet dependency: puma ~> 5.0
```

```
ActionView::MissingTemplate: Missing template layouts/application
```

## How to Fix It

### 1. Configure Production Environment

Set up all required environment variables.

```ruby
config.cache_classes = true
eager_load = true
config.consider_all_requests_local = false
config.action_controller.perform_caching = true
config.public_file_server.enabled = ENV['RAILS_SERVE_STATIC_FILES'].present?
```

### 2. Set Up Database in Production

Configure and migrate the database.

```bash
export DATABASE_URL='postgresql://user:pass@host/dbname'
RAILS_ENV=production rails db:migrate
RAILS_ENV=production rails db:seed
```

### 3. Precompile Assets

Compile before deploying.

```bash
RAILS_ENV=production rails assets:precompile
```

### 4. Configure Puma for Production

Set up the web server.

```ruby
max_threads_count = ENV.fetch('RAILS_MAX_THREADS') { 5 }
min_threads_count = ENV.fetch('RAILS_MIN_THREADS') { max_threads_count }
threads min_threads_count, max_threads_count
port ENV.fetch('PORT') { 3000 }
environment ENV.fetch('RAILS_ENV') { 'development' }
workers ENV.fetch('WEB_CONCURRENCY') { 2 }
preload_app!
```

## Common Scenarios

**Scenario 1: Deployment fails with DB connection error.**
Verify DATABASE_URL is correct.

**Scenario 2: Assets return 404 in production.**
Run precompile and enable static files.

**Scenario 3: Application crashes on startup.**
Check `tail -f log/production.log`.

## Prevent It

1. **Deploy with Capistrano or Docker.**
Use automated deployment tools.

2. **Set up staging environment.**
Deploy to staging first.

3. **Monitor deployment health.**
Set up uptime monitoring.

