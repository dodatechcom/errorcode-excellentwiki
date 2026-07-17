---
title: "[Solution] Ruby FrozenError: Can't Modify Frozen String Fix"
description: "Fix Ruby FrozenError: can't modify frozen String. Learn why string literals are frozen and how to work with immutable strings."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A `FrozenError` when modifying a frozen String occurs when the `# frozen_string_literal: true` magic comment is active. All string literals in the file become frozen and cannot be modified in place.

## Common Causes

- `# frozen_string_literal: true` directive in file
- Explicitly freezing a string with `.freeze`
- Receiving a frozen string from an API or library
- String in a frozen hash or array

## How to Fix

```ruby
# WRONG: Modifying frozen string with << (shovel operator)
# frozen_string_literal: true
greeting = "hello"
greeting << " world"  # FrozenError: can't modify frozen String: "hello"

# CORRECT: Use concatenation instead
greeting = "hello" + " world"  # "hello world"
```

```ruby
# WRONG: Modifying string in place
# frozen_string_literal: true
str = "hello"
str.replace("world")  # FrozenError

# CORRECT: Create new string
str = "hello"
str = "world"  # Reassign (creates new string)
```

```ruby
# WRONG: Mutating frozen string from hash
# frozen_string_literal: true
data = { name: "hello" }.freeze
data[:name] << " world"  # FrozenError

# CORRECT: Use merge to create new hash
data = { name: "hello" }.freeze
data = data.merge(name: "hello world")
```

```ruby
# WRONG: Using gsub! on frozen string
# frozen_string_literal: true
str = "hello"
str.gsub!("h", "H")  # FrozenError

# CORRECT: Use gsub (non-mutating)
str = "hello"
str = str.gsub("h", "H")  # "Hello"
```

## Examples

```ruby
# Example 1: Check if string is frozen
"hello".frozen?       # true (with frozen_string_literal)
+"hello".frozen?      # false (unfroze with unary +)

# Example 2: Unfreeze a string
str = "hello".freeze
str = str.dup  # Creates unfrozen copy
str << " world"  # OK

# Example 3: String interpolation creates new string
# frozen_string_literal: true
name = "Alice"
greeting = "Hello, #{name}!"  # New string (not frozen)
greeting << " How are you?"   # OK
```

## Related Errors

- [FrozenError](frozenerror-ruby) — general frozen object error
- [TypeError](typeerror-ruby) — wrong type for operation
- [NoMethodError](nomethoderror-ruby) — method not available
