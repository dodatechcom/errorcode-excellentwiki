---
title: "[Solution] Ruby Native Extension Error Fix"
description: "Fix Ruby native extension build errors. Learn why native extensions fail to compile and how to install required build tools."
languages: ["ruby"]
severities: ["error"]
error-types: ["build-error"]
tags: ["native-extension", "compilation", "c-extension", "ruby"]
weight: 5
---

## What This Error Means

A native extension error occurs when a Ruby gem with C extensions fails to compile during installation. This typically happens when required build tools or libraries are missing from the system.

## Common Causes

- Missing C compiler (gcc, clang)
- Missing header files for libraries
- Wrong version of development tools
- Platform-specific compilation issues

## How to Fix

```ruby
# WRONG: Installing gem without build tools
# $ gem install mysql2
# ERROR: Failed to build native extension

# CORRECT: Install build tools first
# Ubuntu/Debian:
# $ sudo apt-get install build-essential libmysqlclient-dev
# $ gem install mysql2
```

```ruby
# WRONG: Missing header files
# $ gem install nokogiri
# ERROR: libxml2 is missing

# CORRECT: Install development libraries
# Ubuntu/Debian:
# $ sudo apt-get install libxml2-dev libxslt1-dev
# $ gem install nokogiri
```

```ruby
# WRONG: Wrong Ruby version for gem
# Ruby 2.7 trying to install gem requiring 3.0+

# CORRECT: Use compatible Ruby version
# $ rbenv install 3.0.0
# $ rbenv local 3.0.0
```

## Examples

```ruby
# Example 1: Check if gem has native extension
# $ gem specification nokogiri | grep extensions

# Example 2: Verbose installation
# $ gem install nokogiri -- --use-system-libraries

# Example 3: Common build dependencies
# Ubuntu: build-essential libssl-dev libreadline-dev zlib1g-dev
# macOS: xcode-select --install
```

## Related Errors

- [Gem::InstallError](gem-install-error) — gem installation failed
- [Bundler::GemNotFound](bundler-error) — gem not found in bundle
- [LoadError](loaderror-ruby) — cannot load such file
