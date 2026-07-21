---
title: "[Solution] Deprecated Function Migration: Struct.new with assign to keyword_init"
description: "Migrate from deprecated Struct assignment to keyword_init."
deprecated_function: "MyStruct.new('a', 'b')"
replacement_function: "MyStruct.new(field1: 'a', field2: 'b')"
languages: ["ruby"]
deprecated_since: "Ruby 2.5+"
---

# [Solution] Deprecated Function Migration: Struct.new with assign to keyword_init

The `MyStruct.new('a', 'b')` has been deprecated in favor of `MyStruct.new(field1: 'a', field2: 'b')`.

## Migration Guide

keyword_init is more readable.

## Before (Deprecated)

```ruby
Point = Struct.new(:x, :y)
p = Point.new(1, 2)
```

## After (Modern)

```ruby
Point = Struct.new(:x, :y, keyword_init: true)
p = Point.new(x: 1, y: 2)
```

## Key Differences

- keyword_init is more readable
