---
title: "[Solution] Deprecated Function Migration: when-then compact syntax to multi-line case"
description: "Migrate from compact when-then to modern multi-line case/when in Ruby."
deprecated_function: "when x then y"
replacement_function: "when x then y (modern syntax)"
languages: ["ruby"]
deprecated_since: "Ruby 1.9+"
---

# [Solution] Deprecated Function Migration: when-then compact syntax to multi-line case

The `when x then y` has been deprecated in favor of `when x then y (modern syntax)`.

## Migration Guide

Both syntaxes work. Multi-line is more readable for complex cases.

## Before (Deprecated)

```ruby
case input
when Integer then "number"
when String then "string"
when Array then "array"
end
```

## After (Modern)

```ruby
case input
when Integer
    "number"
when String
    "string"
when Array
    "array"
when -> (x) { x.is_a?(Hash) && x[:type] == "special" }
    "special hash"
else
    "unknown"
end
```

## Key Differences

- Both when-then and multi-line are valid
- Multi-line is more readable for complex cases
- Use -> for pattern matching with lambdas
