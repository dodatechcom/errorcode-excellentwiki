---
title: "[Solution] Ruby LoadError: cannot load such file — Load Path Fix"
description: "Fix Ruby LoadError: cannot load such file by understanding $LOAD_PATH, require vs require_relative, and gem resolution."
languages: ["ruby"]
severities: ["error"]
error_types: ["load"]
weight: 75
---

# LoadError: cannot load such file — Load Path Fix

A `LoadError: cannot load such file` occurs when Ruby cannot find the specified file in any directory on the `$LOAD_PATH`.

## Description

Ruby searches for files in directories listed in `$LOAD_PATH`. When you `require 'foo'`, Ruby looks for `foo.rb` or `foo.so`/`foo.dll` in each directory. If not found, `LoadError` is raised.

Common scenarios:

- **Gem not installed** — the gem providing the file isn't available.
- **File not in load path** — directory isn't in `$LOAD_PATH`.
- **Wrong require name** — using `require 'foo/bar'` instead of `require 'foo'`.
- **Bundler not activated** — running script outside of `bundle exec`.

## Common Causes

```ruby
# Cause 1: Gem not installed
require 'redis'  # LoadError: cannot load such file -- redis

# Cause 2: File not in load path
require 'custom_lib/my_file'  # LoadError if not in $LOAD_PATH

# Cause 3: Running outside Bundler context
# In Gemfile, but running: ruby script.rb
require 'activerecord'  # LoadError

# Cause 4: Wrong file extension or name
require 'my_helper'  # LoadError if file is my_helper.rb but named my_helper.txt
```

## Solutions

### Fix 1: Check and modify $LOAD_PATH

```ruby
# See current load path
puts $LOAD_PATH

# Add a directory
$LOAD_PATH.unshift('/path/to/my/lib')

# Check if a specific path is included
puts $LOAD_PATH.include?('/path/to/my/lib')
```

### Fix 2: Use Bundler correctly

```bash
# Install gems from Gemfile
bundle install

# Run script with Bundler
bundle exec ruby script.rb

# Or in Rails
bundle exec rails console
```

### Fix 3: Use require_relative for project files

```ruby
# Wrong — requires the file to be in $LOAD_PATH
require 'services/user_service'

# Correct — relative to the current file's directory
require_relative 'services/user_service'
```

### Fix 4: Use Gemfile for gem dependencies

```ruby
# Gemfile
source 'https://rubygems.org'

gem 'nokogiri'
gem 'redis', '~> 5.0'
gem 'pg'
```

## Related Errors

- [LoadError](load-error) — general load error.
- [NameError](name-error) — undefined constant after failed require.
- [Gem::LoadError](load-error) — specific to gem version conflicts.
