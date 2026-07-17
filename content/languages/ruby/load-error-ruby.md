---
title: "[Solution] Ruby LoadError — Cannot Load Such File Fix"
description: "Fix Ruby LoadError: cannot load such file. Learn how to resolve file loading issues with require, load_path, and gem dependencies."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# LoadError — Cannot Load Such File

A `LoadError` is raised when Ruby can't find or load a file that you're trying to require.

## Description

Ruby uses `require` and `load` to include external files. `LoadError` occurs when the file doesn't exist, isn't in the load path, or has dependencies that can't be resolved.

Common causes:

- **File doesn't exist** — typo in filename or wrong path
- **Missing from load path** — file directory not in `$LOAD_PATH`
- **Gem not installed** — required gem isn't available
- **Circular dependency** — files requiring each other

## Common Causes

```ruby
# Cause 1: File doesn't exist
require "nonexistent_file"  # LoadError: cannot load such file -- nonexistent_file

# Cause 2: Wrong path
require "lib/my_helper"  # LoadError (if not in load path)

# Cause 3: Missing gem
require "nonexistent_gem"  # LoadError: cannot load such file -- nonexistent_gem

# Cause 4: Circular dependency
# file_a.rb requires file_b.rb, file_b.rb requires file_a.rb
```

## How to Fix

### Fix 1: Check file existence

```ruby
# Wrong
require "my_file"  # LoadError

# Correct
if File.exist?("my_file.rb")
  require "my_file"
end
```

### Fix 2: Add directory to load path

```ruby
# Wrong
require "lib/helper"  # LoadError

# Correct
$LOAD_PATH.unshift File.join(__dir__, "lib")
require "helper"
```

### Fix 3: Use relative paths

```ruby
# Wrong
require "config/database"  # LoadError

# Correct
require_relative "config/database"
```

### Fix 4: Install missing gems

```ruby
# Wrong
require "nokogiri"  # LoadError (if not installed)

# Correct
# Run: gem install nokogiri
require "nokogiri"
```

## Examples

```ruby
# Example 1: Conditional require
begin
  require "optional_feature"
rescue LoadError
  puts "Optional feature not available"
end

# Example 2: Dynamic require
files = Dir["lib/**/*.rb"]
files.each { |f| require f }
```

## Related Errors

- [SyntaxError]({{< relref "/languages/ruby/syntax-error-ruby" >}}) — unexpected token in code
- [NameError]({{< relref "/languages/ruby/name-error" >}}) — undefined variable or constant
- [IOError]({{< relref "/languages/ruby/io-error" >}}) — input/output operation failed
