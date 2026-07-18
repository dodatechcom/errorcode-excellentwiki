---
title: "[Solution] Julia ReadOnlyMemoryError — Cannot Modify Read-Only Data"
description: "Fix Julia ReadOnlyMemoryError when modifying immutable or mapped memory. Learn about array immutability, memory mapping, and data copying."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `ReadOnlyMemoryError` is thrown when you try to modify data that is stored in read-only memory. This commonly occurs with memory-mapped files, string literals, or immutable arrays that cannot be changed after creation.

## Why It Happens

The most common cause is modifying a memory-mapped file. When you use `mmap` to map a file into memory, the mapped region may be read-only. Attempting to write to it throws this error.

Another frequent cause is trying to modify a string literal or a SubArray that shares memory with an immutable parent. In Julia, strings are immutable, and attempting to modify them directly fails.

Shared array memory that was created with read-only permissions also causes this error. If an array was created from a read-only buffer (like from a shared memory segment or a file mapping), writing to it is not allowed.

Immutable data structures like tuples and named tuples cannot be modified after creation. Attempting to assign to a field of an immutable type produces this error.

Finally, `Vector{UInt8}` created from a string literal may share memory with the string, which is immutable. Modifying the vector fails because the underlying memory is read-only.

## How to Fix It

### Copy data before modifying

```julia
# Wrong — modifying memory-mapped read-only data
data = mmap("file.bin")
data[1] = 0x00  # ReadOnlyMemoryError

# Correct — copy first
data = copy(mmap("file.bin"))
data[1] = 0x00
```

### Use Array instead of SubArray for modifications

```julia
# Wrong — SubArray shares memory with parent
str = "hello"
vec = view(str, 1:3)
vec[1] = 'H'  # ReadOnlyMemoryError

# Correct — create independent array
vec = collect(str[1:3])
vec[1] = 'H'
```

### Use mutable containers instead of immutable ones

```julia
# Wrong — tuples are immutable
t = (1, 2, 3)
t[1] = 10  # Error

# Correct — use a mutable container
v = [1, 2, 3]
v[1] = 10
```

### Use string interpolation for string modifications

```julia
str = "hello"
new_str = "H" * str[2:end]  # Create new string
```

### Use Array constructor for independent copies

```julia
original = [1, 2, 3]
copy_arr = Array(original)  # Independent copy
copy_arr[1] = 10  # Works
```

## Common Mistakes

- Assuming memory-mapped files are writable without checking the mode
- Modifying views into immutable strings
- Not understanding that tuples and named tuples are immutable
- Sharing array memory between processes without considering write permissions
- Using `view` when you need an independent copy

## Related Pages

- [Julia SystemError](/languages/julia/julia-system-error/)
- [Julia BoundsError](/languages/julia/julia-boundserror/)
- [Julia ErrorException](/languages/julia/julia-error-exception/)
