---
title: "[Solution] Ruby NoMethodError: Did You Mean? — Method Suggestion Fix"
description: "Fix Ruby NoMethodError with DidYouMean suggestions. Learn how Ruby suggests similar methods and how to use or customize the feature."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

When a `NoMethodError` is raised, Ruby's `did_you_mean` gem (included by default since Ruby 2.6) suggests similar method names based on string similarity. This helps identify typos in method calls.

## Common Causes

- Typo in method name (e.g., `lnegth` instead of `length`)
- Similar but wrong method name (e.g., `map` vs `select`)
- Method exists in a different module not included
- CamelCase vs snake_case confusion

## How to Fix

```ruby
# WRONG: Typo in method name
"hello".lnegth  # NoMethodError: undefined method 'lnegth' for "hello":String
#                # Did you mean?  length

# CORRECT: Use suggested method
"hello".length  # 5
```

```ruby
# WRONG: Wrong method name
[1, 2, 3].select  # NoMethodError (needs block)
# Did you mean?  filter

# CORRECT: Use correct method with block
[1, 2, 3].select { |n| n > 1 }  # [2, 3]
```

```ruby
# WRONG: Missing module
class User
  include Comparable  # Forgot to include
end
User.new <=> other  # NoMethodError: undefined method '<=>'

# CORRECT: Include required module
class User
  include Comparable
  def <=>(other)
    name <=> other.name
  end
end
```

```ruby
# WRONG: Private method
class Service
  private
  def authenticate; end
end
Service.new.authenticate  # NoMethodError: private method 'authenticate'

# CORRECT: Make method public or use send
class Service
  def authenticate; end
end
```

## Examples

```ruby
# Example 1: Common typos
"hello".upercase  # Did you mean?  uppercase
[1,2,3].appned(4)  # Did you mean?  append

# Example 2: Custom DidYouMean behavior
DidYouMean::SpellChecker.new(dictionary: ["foo", "bar", "baz"])
  .correct("fooo")  # ["foo"]

# Example 3: Disable suggestions
$VERBOSE = nil  # Hides warnings but not DidYouMean
```

## Related Errors

- [NoMethodError](nomethoderror-ruby) — undefined method (without suggestions)
- [NameError](nameerror-ruby) — uninitialized constant
- [TypeError](typeerror-ruby) — wrong type for operation
