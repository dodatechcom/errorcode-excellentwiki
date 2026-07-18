---
title: "[Solution] Rails Bundle Error — How to Fix"
description: "Fix Rails Bundler errors. Resolve dependency conflicts, gem installation failures, and lockfile issues."
frameworks: ["rails"]
error-types: ["dependency-error"]
severities: ["error"]
weight: 5
comments: true
---

A Rails Bundler error occurs when Bundler cannot resolve, install, or load gem dependencies.

## Why It Happens

Bundler errors stem from version conflicts, missing gems, lockfile mismatches, or network issues during installation.

## Common Error Messages

```
Bundler::GemNotFound: Could not find rake in locally installed gems
```

```
Bundler::VersionConflict: conflicting dependencies
```

```
Could not find gem 'pg' with any of the gem sources
```

```
Bundler::InstallError: some gems could not be installed
```

## How to Fix It

### 1. Clean Install Gems

Remove and reinstall gems.

```bash
gem install bundler
bundle install --clean
```

### 2. Resolve Version Conflicts

Update the Gemfile.

```ruby
gem 'rails', '~> 7.0'
bundle update
```

### 3. Fix Platform-Specific Gems

Handle different platform builds.

```ruby
platforms :ruby do
  gem 'nokogiri'
end
```

### 4. Debug Gem Loading

Identify loading failures.

```bash
gem list | grep puma
grep puma Gemfile.lock
gem which puma
```

## Common Scenarios

**Scenario 1: Bundle install fails with conflict.**
Run `bundle update` or adjust constraints.

**Scenario 2: Gem not found after deployment.**
Ensure `bundle install` runs during deploy.

**Scenario 3: Native extension fails.**
Install system dependencies.

## Prevent It

1. **Commit Gemfile.lock.**
Always commit the lock file.

2. **Use `bundle exec`.**
Run `bundle exec rails server`.

3. **Update gems regularly.**
Run `bundle update` periodically.

