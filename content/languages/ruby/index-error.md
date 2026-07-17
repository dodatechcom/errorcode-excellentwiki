---
title: "[Solution] Ruby IndexError — Index Out of Range Fix"
description: "Fix Ruby IndexError: index X out of range. Check array/string bounds, use safe access methods, and validate indices."
languages: ["ruby"]
severities: ["error"]
error_types: ["index"]
weight: 90
---

# IndexError — Index Out of Range Fix

An `IndexError` is raised when you try to access an array or string at an index that doesn't exist.

## Description

Ruby arrays and strings are zero-indexed. Accessing an index beyond the length or below zero raises `IndexError`. Negative indices count from the end (-1 is the last element).

Common scenarios:

- **Index too large** — accessing index >= length.
- **Negative index too far** — accessing index < -length.
- **Empty collection** — accessing any index on an empty array/string.
- **Off-by-one errors** — using `<=` instead of `<` in loops.

## Common Causes

```ruby
# Cause 1: Index beyond array length
arr = [1, 2, 3]
arr[10]  # IndexError: index 10 out of array

# Cause 2: Negative index too far
arr = [1, 2, 3]
arr[-10]  # IndexError: index -10 out of array

# Cause 3: Empty array
arr = []
arr[0]  # nil (actually returns nil, not IndexError)

# Cause 4: Off-by-one in loop
arr = [1, 2, 3]
(0..arr.length).each do |i|
  puts arr[i]  # IndexError on last iteration
end
```

## Solutions

### Fix 1: Check bounds before accessing

```ruby
# Wrong
value = arr[index]

# Correct
if index >= 0 && index < arr.length
  value = arr[index]
else
  puts "Index out of bounds"
end
```

### Fix 2: Use safe access methods

```ruby
arr = [1, 2, 3]

# Wrong — raises IndexError
arr[10]  # IndexError

# Correct — returns nil for out of bounds
arr.at(10)  # nil
arr.dig(10)  # nil (also works for nested access)

# Use fetch with a default
arr.fetch(10, "default")  # "default"
```

### Fix 3: Fix loop boundaries

```ruby
arr = [1, 2, 3]

# Wrong — off by one
(0..arr.length).each { |i| puts arr[i] }

# Correct — use ... for exclusive range
(0...arr.length).each { |i| puts arr[i] }

# Or use each_with_index
arr.each_with_index { |val, i| puts "#{i}: #{val}" }
```

### Fix 4: Handle negative indices safely

```ruby
arr = [1, 2, 3]

# Check if negative index is valid
index = -5
if index.abs <= arr.length
  puts arr[index]
else
  puts "Index out of bounds"
end
```

## Related Errors

- [RangeError](range-error) — number too large for range.
- [TypeError](type-error) — wrong type used as index.
- [NoMethodError](no-method-error) — calling method on nil from failed access.
