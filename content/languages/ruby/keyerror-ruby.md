---
title: "[Solution] Ruby KeyError — Key Not Found Fix"
description: "Fix Ruby KeyError: key not found. Learn how to safely access hash keys with fetch, dig, and default values."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["keyerror", "hash", "key-not-found", "ruby"]
weight: 5
---

# KeyError — Key Not Found

A `KeyError` is raised when you try to access a hash key that doesn't exist using `fetch` or `Hash#key?`.

## Description

Ruby hashes raise `KeyError` when you use `fetch` to access a non-existent key. Unlike bracket notation (`[]`), `fetch` doesn't return `nil` by default — it raises an error.

Common causes:

- **Using fetch without default** — accessing a key that doesn't exist
- **Assuming key exists** — not checking if a key is present before access
- **Typo in key name** — misspelling a key
- **Missing nested key** — accessing a deeply nested key that's absent

## Common Causes

```ruby
# Cause 1: fetch without default value
config = { "host" => "localhost" }
config.fetch("port")  # KeyError: key not found: "port"

# Cause 2: Typo in key name
user = { "name" => "Alice", "email" => "alice@example.com" }
user.fetch("ename")  # KeyError: key not found: "ename"

# Cause 3: Missing nested key
data = { "user" => { "name" => "Alice" } }
data.fetch("user").fetch("address")  # KeyError: key not found: "address"

# Cause 4: Integer vs String key confusion
hash = { 1 => "one", 2 => "two" }
hash.fetch("1")  # KeyError: key not found: "1"
```

## How to Fix

### Fix 1: Use fetch with default value

```ruby
# Wrong
config.fetch("port")  # KeyError

# Correct
config.fetch("port", 8080)  # 8080
```

### Fix 2: Use bracket notation with default

```ruby
# Wrong
config.fetch("port")  # KeyError

# Correct
config["port"] || 8080  # 8080
```

### Fix 3: Use dig for nested access

```ruby
# Wrong
data.fetch("user").fetch("address")  # KeyError

# Correct
data.dig("user", "address")  # nil (no error)
data.dig("user", "address") || "No address"
```

### Fix 4: Check key existence first

```ruby
# Wrong
value = hash.fetch("key")  # KeyError

# Correct
if hash.key?("key")
  value = hash["key"]
end
```

## Examples

```ruby
# Example 1: Safe hash access
config = { "database" => { "host" => "localhost", "port" => 5432 } }
host = config.dig("database", "host")  # "localhost"
timeout = config.dig("database", "timeout")  # nil
timeout ||= 30  # 30

# Example 2: Building with defaults
settings = {}
defaults = { "theme" => "dark", "lang" => "en" }
result = defaults.merge(settings)
result.fetch("theme")  # "dark"
```

## Related Errors

- [NoMethodError]({{< relref "/languages/ruby/no-method-error" >}}) — undefined method for object
- [TypeError]({{< relref "/languages/ruby/typeerror-ruby" >}}) — wrong object type for an operation
- [IndexError]({{< relref "/languages/ruby/index-error" >}}) — index out of range in array
