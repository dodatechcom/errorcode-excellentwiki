---
title: "[Solution] Ruby SyntaxError — Unexpected Token Fix"
description: "Fix Ruby SyntaxError: unexpected token. Learn how to identify and correct syntax issues in Ruby code."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# SyntaxError — Unexpected Token

A `SyntaxError` is raised when Ruby encounters code that violates the language's syntax rules.

## Description

Ruby's parser checks code syntax before execution. `SyntaxError` indicates the parser found something it can't understand. These errors are caught at parse time, before any code runs.

Common causes:

- **Missing `end` keyword** — unclosed blocks or methods
- **Unmatched parentheses** — missing closing brackets
- **Invalid character** — unexpected symbols in code
- **String interpolation issues** — malformed `#{}` blocks

## Common Causes

```ruby
# Cause 1: Missing end keyword
def greet(name)
  puts "Hello, #{name}"
# SyntaxError: unexpected end-of-input

# Cause 2: Unmatched parentheses
result = (1 + 2  # SyntaxError: unexpected syntax error

# Cause 3: Invalid character
price = $100  # SyntaxError: unexpected constant

# Cause 4: String interpolation issues
str = "Hello #{name"  # SyntaxError: syntax error
```

## How to Fix

### Fix 1: Add missing end keywords

```ruby
# Wrong
def greet(name)
  puts "Hello, #{name}"

# Correct
def greet(name)
  puts "Hello, #{name}"
end
```

### Fix 2: Match parentheses

```ruby
# Wrong
result = (1 + 2

# Correct
result = (1 + 2)
```

### Fix 3: Fix string interpolation

```ruby
# Wrong
str = "Hello #{name"

# Correct
str = "Hello #{name}"
```

### Fix 4: Use proper variable naming

```ruby
# Wrong
price = $100  # SyntaxError

# Correct
price = 100
```

## Examples

```ruby
# Example 1: Common syntax patterns
if condition
  do_something
else
  do_other
end

# Example 2: Proper block syntax
[1, 2, 3].each { |n| puts n }
[1, 2, 3].each do |n|
  puts n
end
```

## Related Errors

- [LoadError]({{< relref "/languages/ruby/load-error" >}}) — file not found
- [NameError]({{< relref "/languages/ruby/name-error" >}}) — undefined variable or constant
- [NoMethodError]({{< relref "/languages/ruby/no-method-error" >}}) — undefined method for object
