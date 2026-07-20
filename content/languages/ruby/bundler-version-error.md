---
title: "[Solution] Ruby Bundler::GemNotFound Fix"
description: "Fix Bundler::GemNotFound: Could not find gem in locally installed gems. Learn why gem version conflicts occur and how to resolve them."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "ruby"
tags: ["bundler, gems, dependencies, version-conflict"]
severity: "error"
---

# Bundler::GemNotFound

## Error Message

```
Bundler::GemNotFound: Could not find gem 'nokogiri' in locally installed gems.
```

## Common Causes

- Gem is not installed — bundle install was not run or failed silently
- Gemfile.lock references a version not available in configured gem sources
- Ruby version changed, causing platform-specific gems to be missing
- Gem source (rubygems.org) is unreachable or configured incorrectly

## Solutions

### Solution 1: Run bundle install to Install Missing Gems

Ensure all gems specified in the Gemfile are installed in the current bundle.

```ruby
# Install all missing gems
$ bundle install

# If specific gem is problematic
$ bundle install --retry 3

# Force reinstall to fix corrupted gems
$ bundle install --force
```

### Solution 2: Update the Gemfile.lock

Remove and regenerate the lock file to resolve version conflicts between the Gemfile and lock file.

```ruby
# WRONG: Gemfile.lock is stale
# Gemfile says: gem 'rails', '~> 7.1'
# Gemfile.lock has: rails (7.0.8)

# CORRECT: Regenerate lock file
$ rm Gemfile.lock
$ bundle install

# Or update specific gem
$ bundle update rails
```

### Solution 3: Check Ruby Version Compatibility

When switching Ruby versions, gems with native extensions need to be recompiled for the new version.

```ruby
# Check current Ruby version
$ ruby --version

# If version changed, reinstall native gems
$ gem install nokogiri
$ bundle install

# Ensure Gemfile specifies Ruby version
# Gemfile
ruby '3.2.2'
```

### Solution 4: Verify Gem Source Configuration

Check that the gem source in the Gemfile is accessible and correct.

```ruby
# Check current sources
$ bundle config list

# See configured gem sources
$ cat Gemfile
source 'https://rubygems.org'

# If behind a proxy or mirror
$ bundle config set --local mirror.https://rubygems.org https://your-mirror.example.com

# Test source connectivity
$ gem sources -l
```

## Prevention Tips

- Always run bundle install after modifying the Gemfile
- Commit Gemfile.lock to version control to ensure consistent installs
- Use rbenv or rvm to manage Ruby versions and avoid gem incompatibilities
- Use bundle exec to run commands within the correct bundle context

## Related Errors

- [Gem::InstallError]({{< relref "/languages/ruby/gem-install-error" >}})
- [LoadError]({{< relref "/languages/ruby/loaderror-ruby" >}})
- [Bundler::GemNotFound v2]({{< relref "/languages/ruby/bundler-error-v2" >}})
