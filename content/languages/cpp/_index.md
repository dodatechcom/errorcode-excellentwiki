---
title: "[Solution] C++ Errors — Compiler, Runtime & Exception Fixes"
description: "Find solutions for C++ errors including std::bad_alloc and std::out_of_range. Code examples with explanations."
languages: ["cpp"]
---

C++ errors range from cryptic template instantiations to hard-to-debug memory corruption. This section covers the most common runtime exceptions with minimal reproducible code examples and concrete fixes.

## Error Codes

| Error | Description | Fix |
|-------|-------------|-----|
| [std::bad_alloc](/languages/cpp/std-bad-alloc/) | Memory allocation failed — `new` cannot allocate requested memory | Handle the exception with try/catch, reduce allocation size, and check for memory leaks |
| [std::out_of_range](/languages/cpp/std-out-of-range/) | Vector or string index out of bounds — accessing beyond the container size | Use `.at()` for bounds-checked access, validate index with `.size()`, and use iterators |

## Quick Debug

```bash
# Compile with warnings and sanitizer
g++ -Wall -Wextra -fsanitize=address,undefined -g -o myapp main.cpp
./myapp
```
