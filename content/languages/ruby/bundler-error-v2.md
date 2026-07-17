---
title: "[Solution] Bundler::GemNotFound Error Fix"
description: "Fix Bundler gem not found errors when required gems are missing."
languages: ["ruby"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["bundler", "gem", "Gemfile", "missing", "ruby"]
weight: 5
---

# Bundler::GemNotFound Error Fix

A Bundler gem not found error occurs when a gem required by the Gemfile is not installed.

## What This Error Means

Bundler manages gem dependencies. `GemNotFound` fires when a gem listed in `Gemfile.lock` isn't installed in the current gem environment.

## Common Causes

- `bundle install` not run after Gemfile change
- Wrong Ruby version or gemset
- Gem was removed from system
- Bundler version mismatch
- Platform-specific gem missing

## How to Fix

### 1. Run bundle install

```bash
# CORRECT: Install missing gems
bundle install
```

### 2. Check Bundler version

```bash
# CORRECT: Use correct Bundler version
bundle --version
# If Gemfile.lock specifies a version, install it
gem install bundler -v "$(grep BUNDLED_WITH Gemfile.lock | awk '{print $2}')"
```

### 3. Clear and reinstall

```bash
# CORRECT: Fresh install
rm -rf vendor/bundle
bundle install --jobs 4 --retry 3
```

### 4. Check Ruby version

```bash
# CORRECT: Use correct Ruby version
ruby --version
# If using rbenv/rvm, switch to correct version
rbenv install 3.2.2
rbenv local 3.2.2
bundle install
```

### 5. Handle platform-specific gems

```bash
# CORRECT: Add platform if needed
bundle lock --add-platform x86_64-linux
bundle install
```

## Related Errors

- [Bundler Error]({{< relref "/languages/ruby/bundler-error" >}}) — general Bundler errors
- [Load Error]({{< relref "/languages/ruby/load-error" >}}) — missing files
- [Gem Install Error]({{< relref "/languages/ruby/gem-install-error" >}}) — gem installation
