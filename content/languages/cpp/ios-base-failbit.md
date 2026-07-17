---
title: "[Solution] C++ std::ios_base::failbit - stream failure"
description: "Fix C++ std::ios_base::failbit stream failure. Handle logical I/O stream errors."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["ios-base", "failbit", "stream", "logical-error", "io"]
weight: 5
---

# std::ios_base::failbit - stream failure

`failbit` is set when a logical I/O error occurs, such as reading an integer from a string containing "hello". The stream is still usable after clearing.

## Common Causes

```cpp
// Cause 1: Format mismatch
std::stringstream ss("hello");
int val;
ss >> val; // failbit set

// Cause 2: End of input
std::stringstream ss("1 2");
int a, b;
ss >> a >> b; // b gets failbit if only one number

// Cause 3: File not found
std::ifstream file("missing.txt"); // failbit on open
```

## How to Fix

### Fix 1: Check after read

```cpp
int val;
if (ss >> val) {
    // success
} else {
    std::cerr << "Format error" << std::endl;
    ss.clear();
}
```

### Fix 2: Use peek to check

```cpp
if (ss.peek() != EOF) {
    int val;
    ss >> val;
}
```

### Fix 3: Reset stream state

```cpp
ss.clear(); // clear failbit
ss.str("new data"); // provide new data
```

## Related Errors

- [std::ios_base::badbit]({{< relref "/languages/cpp/ios-base-badbit" >}}) — critical error.
- [std::ios_base::eofbit]({{< relref "/languages/cpp/ios-base-eofbit" >}}) — end of file.
- [std::ios_base::failure]({{< relref "/languages/cpp/ios-base-failure" >}}) — stream exception.
