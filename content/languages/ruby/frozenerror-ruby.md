---
title: "[Solution] Ruby FrozenError — Can't Modify Frozen Object Fix"
description: "Fix Ruby FrozenError: can't modify frozen object. Learn why frozen objects can't be mutated and how to use dup or clone."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["frozenerror", "frozen", "immutable", "ruby"]
weight: 5
---

## What This Error Means

A `FrozenError` (formerly `RuntimeError`) is raised when you try to modify a frozen object. Freezing an object makes it immutable — any attempt to change its state raises an error. String literals are frozen by default with `# frozen_string_literal: true`.

## Common Causes

- Modifying a frozen string literal
- Trying to mutate a frozen array or hash
- Calling `<<` or `concat` on a frozen string
- Modifying a constant's value

## How to Fix

```ruby
# WRONG: Modifying frozen string literal
# frozen_string_literal: true
str = "hello"
str << " world"  # FrozenError: can't modify frozen String: "hello"

# CORRECT: Create a new string
str = "hello" + " world"  # "hello world"
str = +"hello"  # unfreezes the string
str << " world"  # OK
```

```ruby
# WRONG: Modifying frozen array
arr = [1, 2, 3].freeze
arr << 4  # FrozenError: can't modify frozen Array

# CORRECT: Duplicate before modifying
arr = [1, 2, 3].freeze
arr = arr.dup
arr << 4  # [1, 2, 3, 4]
```

```ruby
# WRONG: Modifying frozen hash
hash = { a: 1 }.freeze
hash[:b] = 2  # FrozenError

# CORRECT: Merge instead of mutating
hash = { a: 1 }.freeze
hash = hash.merge(b: 2)  # {:a=>1, :b=>2}
```

```ruby
# WRONG: Trying to unfreeze with dup on immutable
123.dup  # TypeError: can't dup Integer

# CORRECT: Use freeze/unfreeze pattern carefully
str = "hello".freeze
new_str = str.dup  # "hello" (unfrozen copy)
new_str << " world"
```

## Examples

```ruby
# Example 1: String literal freezing
# frozen_string_literal: true
s1 = "hello"
s2 = "hello"
s1.object_id == s2.object_id  # true (same object)
s1 << " world"  # FrozenError

# Example 2: Freeze check
"hello".frozen?  # true (with frozen_string_literal)
+"hello".frozen?  # false

# Example 3: Recursive freeze
data = { names: ["Alice"] }.freeze
data[:names] << "Bob"  # FrozenError (inner array also frozen)
```

## Related Errors

- [RuntimeError](runtimeerror-ruby) — general runtime error
- [TypeError](typeerror-ruby) — wrong type for operation
- [NoMethodError](nomethoderror-ruby) — calling method on frozen object
