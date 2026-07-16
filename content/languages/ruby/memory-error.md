---
title: "[Solution] Ruby NoMemoryError — Out of Memory Fix"
description: "Fix Ruby NoMemoryError. Handle memory exhaustion in Ruby programs and optimize memory usage."
languages: ["ruby"]
severities: ["error"]
error_types: ["memory"]
tags: ["no_memory_error", "memory", "oom", "out_of_memory", "gc"]
weight: 330
---

# NoMemoryError — Out of Memory Fix

A `NoMemoryError` is raised when Ruby cannot allocate memory for an object. This is rare in normal Ruby code but can occur with very large data structures.

## Description

`NoMemoryError` means the Ruby interpreter has run out of memory. This is uncommon in typical Ruby programs but can happen when processing very large files, creating massive arrays, or with memory leaks.

Common scenarios:

- **Huge array allocation** — `Array.new(10**10)`.
- **Reading very large files** — loading entire multi-GB file into memory.
- **Memory leaks** — objects not being garbage collected.
- **C extension memory issues** — native code allocating too much memory.

## Common Causes

```ruby
# Cause 1: Huge array allocation
arr = Array.new(10**10)  # NoMemoryError

# Cause 2: Reading very large file into memory
data = File.read("huge_file.bin")  # NoMemoryError if file is huge

# Cause 3: String concatenation in loop
str = ""
1_000_000.times { str << "a" * 1000 }  # May cause NoMemoryError

# Cause 4: Creating many objects rapidly
arr = []
loop { arr << Object.new }  # NoMemoryError eventually
```

## Solutions

### Fix 1: Process data in chunks

```ruby
# Wrong
data = File.read("huge_file.bin")

# Correct — read in chunks
File.open("huge_file.bin", "rb") do |file|
  while chunk = file.read(8192)
    process(chunk)
  end
end
```

### Fix 2: Use streaming for large data

```ruby
# Wrong
lines = File.readlines("huge_file.csv")

# Correct — iterate line by line
File.foreach("huge_file.csv") do |line|
  process(line)
end
```

### Fix 3: Monitor memory usage

```ruby
# Check current memory usage
puts `ps -o rss= -p #{Process.pid}`.to_i / 1024  # MB

# Force garbage collection
GC.start

# Enable immediate sweep for better memory management
GC.compact if GC.respond_to?(:compact)
```

### Fix 4: Use lazy enumerators

```ruby
# Wrong — creates entire array in memory
(1..Float::INFINITY).select { |n| n.prime? }.first(100)

# Correct — lazy evaluation
(1..Float::INFINITY).lazy.select { |n| n.prime? }.first(100)
```

## Related Errors

- [SystemStackError](stack-level-too-deep) — stack overflow from recursion.
- [ScriptError](script-error) — error in script execution.
- [SignalException](signal-exception) — signal-based exceptions.
