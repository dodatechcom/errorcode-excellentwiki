---
title: "Julia Dict Key Type Conversion Error"
description: "Fix Julia Dict key type errors when using mixed key types or converting between key types incorrectly."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Dict key type errors occur when you try to access a dictionary with a key of the wrong type, or when the dictionary's key type does not allow the type you are trying to use.

## Common Causes

- Dictionary has concrete key type but lookup uses different type
- Using Symbol key when String key exists (or vice versa)
- Integer key when Float64 key was stored
- Implicit key type conversion not supported
- Mixed key types in same dictionary

## How to Fix

```julia
# WRONG: Wrong key type
d = Dict("a" => 1, "b" => 2)
d[:a]  # KeyError: :a not found (Symbol vs String)

# CORRECT: Use matching key type
d["a"]  # 1
```

```julia
# WRONG: Type mismatch in Dict
d = Dict{Int, String}()
d["1"] = "one"  # Error: String not convertible to Int

# CORRECT: Use correct type
d[1] = "one"  # works
# or use AbstractDict with Any key
d = Dict{Any, String}()
d["1"] = "one"
d[1] = "one"
```

## Examples

```julia
# Example 1: Typed Dict
d = Dict{Symbol, Int}(:x => 1, :y => 2, :z => 3)
println(d[:x])  # 1

# Example 2: Convert keys
str_dict = Dict("a" => 1, "b" => 2)
sym_dict = Dict(Symbol(k) => v for (k, v) in str_dict)
println(sym_dict)  # Dict(:a=>1, :b=>2)

# Example 3: Mixed keys with Any type
mixed = Dict{Any, Any}("name" => "Alice", :age => 30, 1 => "first")
println(mixed)
```

## Related Errors

- [Key error](julia-key-error) -- key not found
- [TypeError](julia-type-error) -- type mismatch
