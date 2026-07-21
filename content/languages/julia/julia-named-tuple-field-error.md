---
title: "Julia Named Tuple Field Access Error"
description: "Fix Julia named tuple errors when accessing fields that do not exist or using incorrect field names."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Named tuple field access errors occur when you try to access a field by name that does not exist, or when the field name does not match exactly (including case sensitivity).

## Common Causes

- Typo in field name
- Field name has different case than expected
- Accessing named tuple that was created with different keys
- Using dot notation on a regular tuple
- Field name is a reserved word used as key

## How to Fix

```julia
# WRONG: Field name typo
nt = (name="Alice", age=30)
nt.nme  # Error: type NamedTuple has no field nme

# CORRECT: Use exact field name
nt.name  # "Alice"
```

```julia
# WRONG: Wrong field name from function return
function get_info()
    return (name="Bob", city="NYC")
end
info = get_info()
info.address  # Error: no field 'address'

# CORRECT: Check available fields
info = get_info()
fieldnames(typeof(info))  # (:name, :city)
```

## Examples

```julia
# Example 1: Create and access named tuples
point = (x=1.0, y=2.0, z=3.0)
println(point.x)  # 1.0
println(point[:y])  # 2.0 (alternative syntax)

# Example 2: Merge named tuples
a = (x=1, y=2)
b = (z=3, w=4)
c = merge(a, b)
println(c)  # (x=1, y=2, z=3, w=4)

# Example 3: Named tuple from Dict
d = Dict(:name => "Alice", :age => 30)
nt = NamedTuple(d)
println(nt.name)  # "Alice"
```

## Related Errors

- [Key error](julia-key-error) -- dictionary key issues
- [UndefVarError](undefined-sym) -- undefined variable
