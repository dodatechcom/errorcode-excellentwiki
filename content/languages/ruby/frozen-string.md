---
title: "[Solution] Ruby RuntimeError: can't modify frozen String Fix"
description: "Fix Ruby RuntimeError: can't modify frozen String. Handle frozen string literals and mutable string operations."
languages: ["ruby"]
severities: ["error"]
error_types: ["frozen"]
weight: 300
---

# RuntimeError: can't modify frozen String Fix

A `RuntimeError: can't modify frozen String` is raised when you try to modify a string that has been frozen. This is common in Ruby 3.0+ with frozen string literal comments.

## Description

Ruby strings can be frozen to make them immutable. In Ruby 3.0+, the `# frozen_string_literal: true` comment freezes all string literals in a file. Modifying these strings raises an error.

Common scenarios:

- **frozen_string_literal: true** — all string literals in the file are frozen.
- **Explicit .freeze** — string explicitly frozen with `.freeze`.
- **Method return values** — some methods return frozen strings.
- **Hash keys** — hash keys are often frozen.

## Common Causes

```ruby
# Cause 1: frozen_string_literal: true comment
# frozen_string_literal: true
str = "hello"
str << " world"  # RuntimeError: can't modify frozen String

# Cause 2: Explicit .freeze
str = "hello".freeze
str << " world"  # RuntimeError: can't modify frozen String

# Cause 3: Hash keys are frozen in some contexts
hash = { "key" => "value" }
hash.each_key do |key|
  key << "_modified"  # RuntimeError: can't modify frozen String
end

# Cause 4: String from external source
str = some_method_returning_frozen_string
str << " more"  # RuntimeError
```

## Solutions

### Fix 1: Use + to create new strings

```ruby
# frozen_string_literal: true
str = "hello"
new_str = str + " world"  # Creates a new unfrozen string
```

### Fix 2: Use String.new for mutable strings

```ruby
# frozen_string_literal: true
str = String.new("hello")
str << " world"  # Works
```

### Fix 3: Use gsub/sub without bang methods

```ruby
# frozen_string_literal: true
str = "hello world"
new_str = str.gsub("world", "Ruby")  # Returns new string
```

### Fix 4: Use dup to unfreeze

```ruby
# frozen_string_literal: true
str = "hello".freeze
mutable_str = str.dup
mutable_str << " world"  # Works
```

## Related Errors

- [FrozenError](frozen-error) — can't modify frozen object (general).
- [TypeError](type-error) — wrong type for operation.
- [NoMethodError](no-method-error) — undefined method on frozen object.
