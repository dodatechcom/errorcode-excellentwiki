---
title: "[Solution] Ruby SyntaxError — Syntax Error Fix"
description: "Fix Ruby SyntaxError: syntax error. Learn why Ruby can't parse your code and how to fix common syntax mistakes."
languages: ["ruby"]
severities: ["error"]
error-types: ["syntax-error"]
weight: 5
---

## What This Error Means

A `SyntaxError` is raised when Ruby cannot parse your code due to invalid syntax. This is a compile-time error that occurs before the code runs, typically during file loading or parsing.

## Common Causes

- Missing `end` keyword for blocks, classes, or methods
- Unclosed parentheses or brackets
- Invalid character or symbol usage
- Wrong indentation (not a syntax error but can indicate issues)

## How to Fix

```ruby
# WRONG: Missing end
class User
  def name
    "Alice"
  # Missing 'end' for class

# CORRECT: Match all open keywords with end
class User
  def name
    "Alice"
  end
end
```

```ruby
# WRONG: Unclosed parentheses
result = (1 + 2 * 3  # SyntaxError

# CORRECT: Close all parentheses
result = (1 + 2 * 3)
```

```ruby
# WRONG: Invalid symbol
:name:  # SyntaxError: syntax error, unexpected ':'

# CORRECT: Proper symbol syntax
:name  # OK
{ name: "Alice" }  # OK
```

```ruby
# WRONG: Wrong string interpolation
puts "Hello #{name"  # SyntaxError

# CORRECT: Close interpolation
puts "Hello #{name}"
```

## Examples

```ruby
# Example 1: Missing end for if
if true
  puts "hello"
# SyntaxError: unexpected end-of-input

# Example 2: Wrong operator
x = 1 ++ 2  # SyntaxError

# Example 3: Invalid character
puts "Hello™"  # OK (UTF-8 is fine)
puts "Hello\xFF"  # OK
```

## Related Errors

- [LoadError](loaderror-ruby) — cannot load such file
- [NameError](nameerror-ruby) — uninitialized constant
- [NoMethodError](nomethoderror-ruby) — undefined method
