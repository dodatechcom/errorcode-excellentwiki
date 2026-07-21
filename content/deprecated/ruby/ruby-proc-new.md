---
title: "[Solution] Deprecated Function Migration: Proc.new to lambda or -> syntax"
description: "Migrate from deprecated Proc.new to lambda or stabby lambda syntax in Ruby."
deprecated_function: "Proc.new { |x| x * 2 }"
replacement_function: "lambda { |x| x * 2 } or ->(x) { x * 2 }"
languages: ["ruby"]
deprecated_since: "Ruby 1.9+"
---

# [Solution] Deprecated Function Migration: Proc.new to lambda or -> syntax

The `Proc.new { |x| x * 2 }` has been deprecated in favor of `lambda { |x| x * 2 } or ->(x) { x * 2 }`.

## Migration Guide

Proc.new creates a Proc that does not check argument count. Lambda enforces argument count.

## Before (Deprecated)

```ruby
square = Proc.new { |x| x * x }
square.call()  # no error
square.call(1, 2, 3)  # no error
```

## After (Modern)

```ruby
square = ->(x) { x * x }
greet = ->(name) { "Hello, #{name}" }

# Argument checking
square.call()  # ArgumentError
square.call(1)  # works
```

## Key Differences

- -> is the most concise syntax
- lambda checks argument count
- Proc.new does not check arguments
- Use lambda for most functional patterns
