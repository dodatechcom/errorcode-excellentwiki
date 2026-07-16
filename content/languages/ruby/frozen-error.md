---
title: "[Solution] Ruby FrozenError — Can't Modify Frozen String Fix"
description: "Fix Ruby FrozenError: can't modify frozen String. Learn how to handle immutable objects and create mutable copies."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["frozenerror", "frozen", "immutable", "string", "ruby"]
weight: 5
---

# FrozenError — Can't Modify Frozen String

A `FrozenError` is raised when you try to modify a frozen (immutable) object.

## Description

Ruby allows you to freeze objects to make them immutable. Attempting to modify a frozen object raises `FrozenError`. Strings are frozen automatically with `#freeze` or when using string literals in frozen string literals mode.

Common causes:

- **Modifying frozen string** — using `<<` or `concat` on a frozen string
- **String literal freezing** — `# frozen_string_literal: true` pragma
- **Modifying frozen hash keys** — mutating keys in a frozen hash
- **Modifying frozen array elements** — trying to change frozen array contents

## Common Causes

```ruby
# Cause 1: Direct modification of frozen string
str = "hello".freeze
str << "world"  # FrozenError: can't modify frozen String: "hello"

# Cause 2: Frozen string literals pragma
# frozen_string_literal: true
str = "hello"
str << "world"  # FrozenError

# Cause 3: Modifying frozen hash
hash = { a: 1, b: 2 }.freeze
hash[:c] = 3  # FrozenError: can't modify frozen Hash

# Cause 4: Modifying frozen array
arr = [1, 2, 3].freeze
arr << 4  # FrozenError: can't modify frozen Array
```

## How to Fix

### Fix 1: Create mutable copy

```ruby
# Wrong
str = "hello".freeze
str << "world"  # FrozenError

# Correct
str = +"hello"  # Creates mutable copy
str << "world"  # "helloworld"
```

### Fix 2: Use string concatenation

```ruby
# Wrong
str = "hello".freeze
str << "world"  # FrozenError

# Correct
str = "hello" + "world"  # Creates new string
```

### Fix 3: Use replace method

```ruby
# Wrong
str = "hello".freeze
str.replace("world")  # FrozenError

# Correct
str = str.dup
str.replace("world")  # "world"
```

### Fix 4: Use gsub for modifications

```ruby
# Wrong
str = "Hello World".freeze
str.downcase!  # FrozenError

# Correct
str = "Hello World".freeze
str.downcase  # "hello world" (returns new string)
```

## Examples

```ruby
# Example 1: Safe string operations
frozen_str = "hello".freeze
new_str = frozen_str + " world"  # Creates new string
# frozen_str is still "hello"

# Example 2: Hash operations
frozen_hash = { a: 1 }.freeze
new_hash = frozen_hash.merge(b: 2)  # Creates new hash
# frozen_hash is still { a: 1 }
```

## Related Errors

- [TypeError]({{< relref "/languages/ruby/typeerror-ruby" >}}) — wrong object type for an operation
- [NoMethodError]({{< relref "/languages/ruby/no-method-error" >}}) — undefined method for object
- [ArgumentError]({{< relref "/languages/ruby/argumenterror-ruby" >}}) — wrong number of arguments
