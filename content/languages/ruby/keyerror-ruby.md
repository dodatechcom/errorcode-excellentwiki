---
title: "[Solution] Ruby KeyError — Key Not Found in Hash Fix"
description: "Fix Ruby KeyError: key not found. Learn why hash key lookups fail and how to use default values or fetch with fallbacks."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["keyerror", "hash", "key-not-found", "ruby"]
weight: 5
---

## What This Error Means

A `KeyError` is raised when you access a hash using `fetch` with a key that doesn't exist and no default value is provided. Unlike `[]`, `fetch` raises an error instead of returning `nil`.

## Common Causes

- Using `fetch` without a default for a missing key
- Typo in hash key name
- Accessing nested hash with missing intermediate key
- Data structure changed but code wasn't updated

## How to Fix

```ruby
# WRONG: fetch without default for missing key
config = { "host" => "localhost" }
port = config.fetch("port")  # KeyError: key not found: "port"

# CORRECT: Provide a default value
port = config.fetch("port", 3000)  # 3000
```

```ruby
# WRONG: Missing nested key
user = { name: "Alice", address: { city: "NYC" } }
zip = user.fetch(:address).fetch(:zip)  # KeyError

# CORRECT: Use dig for safe nested access
zip = user.dig(:address, :zip)  # nil
```

```ruby
# WRONG: Typo in key name
settings = { "color" => "blue" }
value = settings.fetch("colour")  # KeyError

# CORRECT: Verify key exists first
value = settings.key?("color") ? settings["color"] : nil
```

## Examples

```ruby
# Example 1: Simple fetch
hash = { a: 1, b: 2 }
hash.fetch(:c)  # KeyError: key not found: :c
hash.fetch(:c, 0)  # 0

# Example 2: Using a block
hash.fetch(:c) { |key| puts "Missing key: #{key}" }

# Example 3: Hash with default
hash = Hash.new(0)
hash[:missing]  # 0 (no error)
```

## Related Errors

- [NoMethodError](nomethoderror-ruby) — calling method on nil from hash
- [TypeError](typeerror-ruby) — wrong type for hash operation
- [IndexError](indexerror-ruby) — index out of range in array
