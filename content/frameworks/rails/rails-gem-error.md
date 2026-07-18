---
title: "[Solution] Rails Gem Error — How to Fix"
description: "Fix Rails gem errors. Resolve missing gem issues, version conflicts, and gem loading failures."
frameworks: ["rails"]
error-types: ["dependency-error"]
severities: ["error"]
weight: 5
comments: true
---

A Rails gem error occurs when a required gem cannot be found, loaded, or has conflicting versions.

## Why It Happens

Gem errors happen when gems are missing from the Gemfile, after bundle failures, when versions conflict, or native extensions fail.

## Common Error Messages

```
LoadError: cannot load such file -- devise
```

```
Gem::LoadError: Could not find devise in locally installed gems
```

```
Bundler::GemNotFound: Could not find nokogiri
```

```
Gem::Ext::BuildError: Failed to build gem native extension
```

## How to Fix It

### 1. Install Missing Gems

Run bundle install.

```bash
bundle install
bundle install --without development test
```

### 2. Fix Native Extension Errors

Install system dependencies.

```bash
apt-get install libpq-dev libxml2-dev libxslt-dev
bundle install
```

### 3. Resolve Version Conflicts

Update gems.

```bash
bundle outdated
bundle update devise
```

### 4. Handle Gem Loading Failures

Debug loading issues.

```bash
gem list | grep devise
grep devise Gemfile.lock
gem which devise
```

## Common Scenarios

**Scenario 1: New clone fails with missing gems.**
Run `bundle install` after cloning.

**Scenario 2: Native extension fails.**
Install build tools: `apt install build-essential`.

**Scenario 3: Version conflict after update.**
Run `bundle update` or pin versions.

## Prevent It

1. **Commit Gemfile.lock.**
Always commit the lock file.

2. **Use `bundle exec` for commands.**
Run `bundle exec rails server`.

3. **Document system dependencies.**
Keep README with required packages.

