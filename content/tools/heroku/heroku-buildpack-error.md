---
title: "[Solution] Heroku Buildpack Compilation Failed — How to Fix"
description: "Fix Heroku buildpack compilation failures by checking language runtime versions, resolving dependency conflicts, reviewing build logs, and managing multiple buildpacks correctly."
tools: ["heroku"]
error-types: ["buildpack-error"]
severities: ["error"]
weight: 5
comments: true
---

A Heroku buildpack compilation error occurs when your application fails to build during deployment. The buildpack detects your application's language and framework, installs dependencies, and compiles assets. Build failures prevent the deployment from completing.

## What This Error Means

Buildpacks are scripts that compile your application into a deployable slug. Heroku detects the buildpack based on your application's files (e.g., `Gemfile` for Ruby, `requirements.txt` for Python, `package.json` for Node.js). The build process includes installing dependencies, running build scripts, and compiling assets. If any step fails, the build fails and the deployment is rejected.

Unlike runtime errors that happen after deployment, build errors prevent deployment entirely. The previous version of your application continues running.

## Why It Happens

- The required language runtime version is not available or is deprecated
- A dependency version is incompatible with the runtime or other dependencies
- The buildpack is outdated or incompatible with your application
- Multiple buildpacks conflict with each other
- A build step (e.g., asset compilation, database migration) exceeds the 15-minute build timeout
- The application is too large for the slug size limit (500MB compressed)
- A native extension fails to compile due to missing system libraries
- The `Procfile` or `app.json` has incorrect syntax

## Common Error Messages

```
 ▸    No matching version found for ruby-3.0.0
# or
 !     Error: Unable to find a compatible version of Node.js
# or
 ▸    Could not find python version 3.12.0
# or
 ▸    Slug size too large (exceeds 500 MB limit)
```

## How to Fix It

### 1. View Build Logs

```bash
# View the last build log
heroku builds:output -a my-app --tail

# List recent builds
heroku builds -a my-app -n 5

# View a specific build
heroku builds:output <build-id> -a my-app
```

The build log contains the exact error message. Scroll to the end to find the failure reason.

### 2. Update Runtime Version

```bash
# Check what versions are available (Ruby example)
heroku stack:versions -a my-app

# Specify a supported Ruby version in Gemfile
# ruby '3.2.2'

# Specify Node.js version in package.json
# "engines": { "node": "20.x" }

# Specify Python version in runtime.txt
# python-3.11.6
```

### 3. Resolve Dependency Conflicts

```bash
# For Ruby/Bundler — update Gemfile.lock
bundle update

# For Node.js — clear cache and reinstall
rm -rf node_modules package-lock.json
npm install

# For Python — use pinned versions
pip freeze > requirements.txt
# or use pipenv
pipenv lock
```

### 4. Configure Multiple Buildpacks

```bash
# List current buildpacks
heroku buildpacks -a my-app

# Add buildpacks in order
heroku buildpacks:clear -a my-app
heroku buildpacks:set heroku/nodejs -a my-app
heroku buildpacks:add heroku/ruby -a my-app

# Node.js buildpack must come before Ruby if you need Node for asset compilation
```

### 5. Fix Slug Size Issues

```bash
# Check current slug size
heroku apps:info -a my-app | grep "Slug Size"

# Reduce slug size:
# - Remove development dependencies
# - Use .slugignore file
echo "*.psd
*.pdf
test/
spec/
docs/
node_modules/*.map" > .slugignore

# - Clean caches in build scripts
# For Node.js: npm prune --production
# For Python: pip install --no-cache-dir
```

### 6. Handle Native Extension Compilation

```bash
# Native extensions require system libraries (e.g., libpq-dev, libxml2)
# Some buildpacks include these, others require adding Aptfile

# Create an Aptfile for system packages
echo "libpq-dev
libxml2-dev
libxslt1-dev" > Aptfile

# Or use the heroku-buildpack-apt
heroku buildpacks:add --index 1 heroku-community/apt -a my-app
```

### 7. Clear Build Cache

```bash
# Force a clean build by clearing the cache
heroku builds:cache:purge -a my-app

# Or set an environment variable to change cache keys
heroku config:set BUILD_CACHE_VERSION=2 -a my-app

# Deploy again
git commit --allow-empty -m "Clear build cache"
git push heroku main
```

### 8. Handle Asset Compilation Failures

```bash
# For Rails apps, precompile assets locally or use:
heroku config:set RAILS_SERVE_STATIC_FILES=true -a my-app

# For Node.js, set NODE_ENV during build
heroku config:set NODE_ENV=production -a my-app

# Skip asset compilation in favor of CI pipeline
heroku config:set ASSET_HOST=https://cdn.example.com -a my-app
```

## Common Scenarios

### Ruby Version Deprecated by Heroku

The application specifies `ruby 2.7.0` in its Gemfile. Heroku no longer supports Ruby 2.7 and the build fails with "No matching version found." Update the Ruby version to 3.2.2 or later, update the Gemfile.lock, and redeploy.

### Node.js Native Module Fails to Compile

A Node.js application depends on `node-sass`, which requires native compilation. The build fails because the prebuilt binary is not available for Heroku's stack. Replace `node-sass` with `sass` (Dart Sass), which is pure JavaScript and does not require native compilation.

### Monorepo Structure Not Recognized

A monorepo contains both a Node.js frontend and a Python backend. Heroku cannot detect which buildpack to use. Set explicit buildpacks in order: `heroku/nodejs` then `heroku/python`, and configure the `Procfile` to start the correct service.

## Prevent It

- Pin runtime versions to versions explicitly supported by Heroku
- Test builds locally with `heroku buildpacks:detect` before pushing
- Use a staging pipeline to test build changes before production
- Keep buildpacks updated with `heroku buildpacks:upgrade`
- Maintain a `.slugignore` file to exclude unnecessary files
- Run `bundle audit` or `npm audit` before deployment
- Set up CI to run `heroku builds:create` for build validation
- Monitor slug size and set alerts when approaching the 500MB limit

## Related Pages

- [Heroku Release Error](/tools/heroku/heroku-release-error)
- [Heroku Config Error](/tools/heroku/heroku-config-error)
- [Heroku App Not Found](/tools/heroku/heroku-app-not-found)
