---
title: "[Solution] Ruby Bundler::GemNotFound Fix"
description: "Fix Bundler::GemNotFound in Ruby. Learn why gems can't be found and how to resolve bundler dependency issues."
languages: ["ruby"]
severities: ["error"]
error-types: ["dependency-error"]
tags: ["bundler", "gem-not-found", "dependencies", "ruby"]
weight: 5
---

## What This Error Means

A `Bundler::GemNotFound` is raised when Bundler cannot find a gem specified in the `Gemfile`. This typically means the gem isn't installed or the `Gemfile.lock` is out of sync with the `Gemfile`.

## Common Causes

- Gem not installed (`bundle install` not run)
- Gem removed from Gemfile but still in lock file
- Wrong Ruby version for the gem
- Platform-specific gem not available

## How to Fix

```ruby
# WRONG: Running app without installing gems
# Bundler::GemNotFound: Could not find nokogiri

# CORRECT: Run bundle install
# $ bundle install
```

```ruby
# WRONG: Gemfile and lock file mismatch
# Gemfile has gem 'rails', '~> 7.0'
# Gemfile.lock has rails 6.1.0

# CORRECT: Update bundle
# $ bundle update
# Or remove lock and reinstall
# $ rm Gemfile.lock
# $ bundle install
```

```ruby
# WRONG: Wrong Ruby version
# Gemfile: ruby '3.0.0'
# System: ruby 2.7.0

# CORRECT: Use correct Ruby version
# $ rbenv install 3.0.0
# $ rbenv local 3.0.0
# $ bundle install
```

## Examples

```ruby
# Example 1: Check installed gems
# $ bundle list

# Example 2: Check gem paths
# $ bundle info rails

# Example 3: Force reinstall
# $ bundle install --force
```

## Related Errors

- [Gem::InstallError](gem-install-error) — gem installation failed
- [Native extension error](native-extension-error) — native extension build failed
- [LoadError](loaderror-ruby) — cannot load such file
