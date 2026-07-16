---
title: "[Solution] Ruby LoadError — Cannot Load Such File Fix"
description: "Fix Ruby LoadError: cannot load such file. Check file paths, require statements, and $LOAD_PATH configuration."
languages: ["ruby"]
severities: ["error"]
error_types: ["load"]
tags: ["loaderror", "require", "load", "path"]
weight: 70
---

# LoadError — Cannot Load Such File Fix

A `LoadError` is raised when Ruby cannot find or load a file specified with `require`, `load`, or `require_relative`.

## Description

`LoadError` means Ruby tried to load a file but couldn't find it. This covers missing files, incorrect paths, missing gems, and load path issues.

Common scenarios:

- **File doesn't exist** — typo in filename or wrong directory.
- **Missing gem** — gem not installed.
- **Incorrect path** — relative or absolute path is wrong.
- **Load path not configured** — directory not in `$LOAD_PATH`.

## Common Causes

```ruby
# Cause 1: File doesn't exist
require 'my_helper'  # LoadError: cannot load such file -- my_helper

# Cause 2: Gem not installed
require 'nokogiri'  # LoadError: cannot load such file -- nokogiri

# Cause 3: Wrong relative path
require './utils/helper'  # LoadError if path is incorrect

# Cause 4: File exists but can't be loaded (syntax error in the file)
require 'broken_file'  # LoadError if the file has syntax errors
```

## Solutions

### Fix 1: Verify the file exists

```bash
# Check if the file exists
ls -la lib/my_helper.rb

# Check the current directory
pwd
```

### Fix 2: Install missing gems

```bash
# Install the gem
gem install nokogiri

# Or use Bundler
bundle install
```

### Fix 3: Use require_relative for local files

```ruby
# Wrong — depends on current directory
require 'lib/my_helper'

# Correct — relative to the current file
require_relative 'lib/my_helper'
```

### Fix 4: Add directories to $LOAD_PATH

```ruby
# Add a directory to the load path
$LOAD_PATH.unshift('/path/to/my/lib')

# Or use -I flag when running Ruby
# ruby -I/path/to/my/lib script.rb
```

## Related Errors

- [LoadError: cannot load such file](load-path) — detailed load path troubleshooting.
- [NameError](name-error) — undefined constant after failed require.
- [SyntaxError](syntax-error) — syntax error in loaded file.
