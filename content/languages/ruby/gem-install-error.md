---
title: "[Solution] Ruby Gem::InstallError Fix"
description: "Fix Gem::InstallError in Ruby. Learn why gem installation fails and how to resolve common gem installation issues."
languages: ["ruby"]
severities: ["error"]
error-types: ["dependency-error"]
weight: 5
---

## What This Error Means

A `Gem::InstallError` is raised when RubyGems cannot install a gem. This can happen due to network issues, missing dependencies, platform incompatibilities, or native extension build failures.

## Common Causes

- Network connectivity issues
- Missing system dependencies for native extensions
- Platform-specific gem not available
- Insufficient permissions

## How to Fix

```ruby
# WRONG: Installing gem without dependencies
# $ gem install nokogiri  # Fails if libxml2 not installed

# CORRECT: Install system dependencies first
# Ubuntu/Debian:
# $ sudo apt-get install libxml2-dev libxslt1-dev
# Then install gem
# $ gem install nokogiri
```

```ruby
# WRONG: Wrong platform
# $ gem install specific_platform_gem  # Platform mismatch

# CORRECT: Specify platform
# $ gem install nokogiri --platform ruby
```

```ruby
# WRONG: Permission denied
# $ gem install rails  # Permission denied

# CORRECT: Use --user-install or bundler
# $ gem install rails --user-install
# Or use bundle with proper setup
```

## Examples

```ruby
# Example 1: Install with verbose output
# $ gem install rails --verbose

# Example 2: Check gem platform
# $ gem platform

# Example 3: Install from specific source
# $ gem install rails --source https://rubygems.org/
```

## Related Errors

- [Bundler::GemNotFound](bundler-error) — gem not found in bundle
- [Native extension error](native-extension-error) — native extension build failed
- [LoadError](loaderror-ruby) — cannot load such file
