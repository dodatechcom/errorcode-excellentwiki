---
title: "[Solution] Ruby IndexError — Index Out of Range Fix"
description: "Fix Ruby IndexError: index out of range. Learn how to safely access array elements with bounds checking."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["indexerror", "index-out-of-range", "array", "ruby"]
weight: 5
---

# IndexError — Index Out of Range

An `IndexError` is raised when you try to access an array element at an index that doesn't exist.

## Description

Ruby arrays have fixed indices from `0` to `length - 1` (and negative indices from `-1` to `-length`). Accessing an index outside these bounds raises `IndexError`.

Common causes:

- **Off-by-one error** — accessing index equal to array length
- **Negative index out of range** — accessing beyond `-array.length`
- **Empty array access** — trying to access elements in an empty array
- **Dynamic index miscalculation** — computed index exceeds bounds

## Common Causes

```ruby
# Cause 1: Off-by-one error
arr = [1, 2, 3]
arr[3]  # IndexError: index 3 outside of array bounds: -3...3

# Cause 2: Negative index out of range
arr = [1, 2, 3]
arr[-4]  # IndexError: index -4 outside of array bounds: -3...3

# Cause 3: Empty array access
arr = []
arr[0]  # IndexError: index 0 outside of array bounds: 0...0

# Cause 4: Dynamic index exceeds bounds
arr = [10, 20, 30]
index = arr.length
arr[index]  # IndexError: index 3 outside of array bounds: -3...3
```

## How to Fix

### Fix 1: Check array length before access

```ruby
# Wrong
arr = [1, 2, 3]
arr[5]  # IndexError

# Correct
if index < arr.length
  arr[index]
else
  nil
end
```

### Fix 2: Use dig for nested arrays

```ruby
# Wrong
matrix = [[1, 2], [3, 4]]
matrix[5][0]  # IndexError

# Correct
matrix.dig(1, 0)  # 3
matrix.dig(5, 0)  # nil (no error)
```

### Fix 3: Use safe access pattern

```ruby
# Wrong
value = arr[index]  # IndexError

# Correct
value = arr[index] if index.between?(0, arr.length - 1)
```

### Fix 4: Use slice for range access

```ruby
# Wrong
arr = [1, 2, 3]
arr[0..5]  # [1, 2, 3] (no error, but unexpected)

# Correct
arr.slice(0, [5, arr.length].min)  # [1, 2, 3]
```

## Examples

```ruby
# Example 1: Safe array access
arr = [10, 20, 30]
safe_access = proc { |a, i| i.between?(0, a.length - 1) ? a[i] : nil }
safe_access.call(arr, 1)  # 20
safe_access.call(arr, 10)  # nil

# Example 2: Negative indices
arr = [1, 2, 3]
arr[-1]  # 3 (last element)
arr[-3]  # 1 (first element)
arr[-4]  # IndexError
```

## Related Errors

- [NoMethodError]({{< relref "/languages/ruby/no-method-error" >}}) — undefined method for object
- [KeyError]({{< relref "/languages/ruby/keyerror-ruby" >}}) — key not found in hash
- [RangeError]({{ < relref "/languages/ruby/range-error" >}}) — number too large or too small
