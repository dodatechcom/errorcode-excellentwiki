---
title: "[Solution] Ruby LoadError — Cannot Load Such File Fix"
description: "Fix Ruby LoadError: cannot load such file. Learn why require/load fails and how to fix load paths and file references."
languages: ["ruby"]
severities: ["error"]
error-types: ["load-error"]
weight: 5
---

## What This Error Means

A `LoadError` is raised when Ruby cannot find or load a file. This happens with `require`, `load`, `require_relative`, and `autoload` when the specified file doesn't exist or isn't accessible.

## Common Causes

- File doesn't exist at the specified path
- Missing `require` statement
- File not in Ruby's load path (`$LOAD_PATH`)
- Wrong file extension (`.rb` vs `.so`)

## How to Fix

```ruby
# WRONG: File not in load path
require 'my_helper'  # LoadError: cannot load such file -- my_helper

# CORRECT: Add directory to load path
$LOAD_PATH.unshift(File.join(__dir__, 'lib'))
require 'my_helper'

# Or use require_relative
require_relative 'lib/my_helper'
```

```ruby
# WRONG: Typo in filename
require 'user_controller'  # File is actually user_controllers.rb

# CORRECT: Verify filename
Dir.glob('**/*controller*')  # Find the correct file
require 'user_controllers'
```

```ruby
# WRONG: Missing .rb extension with load
load 'config'  # May fail depending on Ruby version

# CORRECT: Include extension
load 'config.rb'
```

```ruby
# WRONG: Circular dependency
# a.rb: require 'b'
# b.rb: require 'a'

# CORRECT: Use require_relative or restructure
# a.rb: require_relative 'b'
# b.rb: # Don't require 'a' back
```

## Examples

```ruby
# Example 1: Missing gem
require 'nokogiri'  # LoadError if gem not installed
# Fix: gem install nokogiri

# Example 2: Wrong path
require './helpers'  # LoadError if helpers.rb not in current dir
# Fix: require_relative 'helpers'

# Example 3: Load path issue
puts $LOAD_PATH  # Check where Ruby looks for files
```

## Related Errors

- [NameError](nameerror-ruby) — uninitialized constant (missing require)
- [SyntaxError](syntaxerror-ruby) — syntax error in loaded file
- [LoadError](loaderror-ruby) — file not found
