---
title: "[Solution] Lua Table Length Undefined Behavior Fix"
description: "Fix Lua table length issues where # operator returns unexpected results. Learn how Lua table length works and alternatives."
languages: ["lua"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

Lua's `#` operator for table length can produce undefined behavior on tables that are not proper sequences. A proper sequence is a table where all integer keys from 1 to N are present with no gaps. When holes exist in the array portion, or when the table contains only non-integer keys, the `#` operator may return an arbitrary value between the highest and lowest boundary of the sequence.

## Why It Happens

- The table has gaps (missing integer keys) in its array portion
- Mixed integer and string keys cause the length operator to be unpredictable
- Using `table.remove` on arbitrary positions creates holes
- The table was built by appending keys non-sequentially
- A nil value was assigned to an integer-indexed field
- The table contains only hash-part keys with no integer sequence

## How to Fix It

### Use explicit counters instead of # for non-sequence tables

```lua
-- WRONG: Using # on table with gaps
local t = { [1] = "a", [3] = "c" }
print(#t)  -- undefined: may be 1 or 3

-- CORRECT: Track count explicitly
local t = {}
local count = 0
t[1] = "a"
count = count + 1
t[3] = "c"
count = count + 1
print(count)  -- 2
```

### Use pairs with a counter for non-sequence tables

```lua
-- WRONG: # gives wrong result for sparse tables
local config = { [1] = "x", [5] = "y", [10] = "z" }
for i = 1, #config do
    print(config[i])  -- misses entries
end

-- CORRECT: Use pairs for sparse tables
for key, value in pairs(config) do
    print(key, value)
end
```

### Maintain array integrity with table.insert

```lua
-- WRONG: Creating gaps by direct assignment
local list = {}
list[1] = "a"
list[2] = "b"
list[5] = "e"  -- gap at 3 and 4
print(#list)  -- undefined behavior

-- CORRECT: Use table.insert for sequential data
local list = {}
table.insert(list, "a")
table.insert(list, "b")
-- table.insert always appends to the end
print(#list)  -- 2, predictable
```

### Filter nil values to compact arrays

```lua
-- WRONG: Nil values create holes
local items = { "a", nil, "c", nil, "e" }
print(#items)  -- undefined: 1 or 5

-- CORRECT: Compact the array
local raw = { "a", nil, "c", nil, "e" }
local items = {}
for _, v in ipairs(raw) do
    items[#items + 1] = v
end
print(#items)  -- 3
```

### Use ipairs for guaranteed sequential iteration

```lua
-- WRONG: pairs order is not guaranteed for arrays
local arr = { "a", "b", "c" }
for k, v in pairs(arr) do
    print(k, v)  -- order not guaranteed
end

-- CORRECT: Use ipairs for ordered sequential iteration
local arr = { "a", "b", "c" }
for k, v in ipairs(arr) do
    print(k, v)  -- guaranteed order: 1, 2, 3
end
```

## Common Mistakes

- Assuming `#t` returns the total number of keys including non-integer keys
- Using `#` in a loop condition for tables that may have nil gaps
- Not understanding that Lua 5.1 and 5.3 may return different values for the same sparse table
- Combining `#` with `ipairs` when the table is not a proper sequence
- Expecting `#` to count hash-part keys or negative integer keys

## Related Pages

- [Lua Nil Index Error](lua-nil-index-error) - indexing nil value
- [Lua Table Index Nil](lua-nil-index-error) - table index is nil
- [Lua Nil Call Error](lua-nil-call-error) - calling nil value
- [Lua Argument Type Error](lua-argument-type-error) - wrong argument type
