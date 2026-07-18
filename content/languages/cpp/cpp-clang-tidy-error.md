---
title: "[Solution] C++ clang-tidy Error — How to Fix"
description: "Fix C++ clang-tidy errors including false positive warnings, incorrect check configurations, and compilation database issues in static analysis."
languages: ["cpp"]
severities: ["error"]
error_types: ["compile-time"]
weight: 5
comments: true
---

# [Solution] C++ clang-tidy Error — How to Fix

clang-tidy static analysis errors include false positive warnings from incomplete type information, failed checks due to missing compilation databases, and configuration issues when checks conflict or depend on unavailable clang modules.

## Why It Happens

clang-tidy errors occur when `.clang-tidy` configuration is malformed, when `compile_commands.json` is missing or incomplete, when checks depend on headers not found in include paths, when modernize checks conflict with existing code style, or when third-party library headers trigger false positives.

## Common Error Messages

1. `error: unable to find compilation database for file`
2. `warning: use of uninitialized variable — false positive`
3. `error: clang-tidy check 'modernize-use-auto' failed`
4. `warning: header not found — include path missing`

## How to Fix It

### Fix 1: Generate Compilation Database

```bash
# For CMake projects
cmake -B build -DCMAKE_EXPORT_COMPILE_COMMANDS=ON

# For non-CMake projects, create compile_commands.json manually or use bear
bear -- cmake --build build

# Run clang-tidy with compilation database
clang-tidy src/*.cpp -p build/
```

### Fix 2: Configure .clang-tidy Properly

```yaml
# .clang-tidy
Checks: >
  -*,
  modernize-*,
  bugprone-*,
  performance-*,
  -modernize-use-trailing-return-type,
  -bugprone-easily-swappable-parameters

CheckOptions:
  - key: modernize-use-nullptr.NullMacros
    value: 'NULL'
```

### Fix 3: Fix Include Path Issues

```bash
# CORRECT — pass extra compiler flags for include paths
clang-tidy src/main.cpp -p build/ -- -I/usr/include/custom -std=c++17

# Or add to .clang-tidy via ExtraArgs
```

```yaml
# .clang-tidy with extra args
ExtraArgs:
  - '-std=c++17'
  - '-I/path/to/extra/includes'
```

### Fix 4: Suppress False Positives Selectively

```cpp
#include <iostream>
#include <vector>

// CORRECT — suppress specific warning for this line
// NOLINTNEXTLINE(performance-unnecessary-copy-initialization)
void process(const std::vector<int>& data) {
    // This copy is intentional for modification
    // NOLINTBEGIN(performance-unnecessary-copy-initialization)
    auto copy = data;
    copy.push_back(42);
    // NOLINTEND(performance-unnecessary-copy-initialization)

    std::cout << "Size: " << copy.size() << "\n";
}

int main() {
    process({1, 2, 3});
    return 0;
}
```

## Common Scenarios

- **Missing compile_commands.json**: Without it, clang-tidy can't determine compiler flags.
- **False positives**: Checks like `bugprone-narrowing-conversions` fire on intentional narrowing.
- **Check conflicts**: Some checks produce contradictory suggestions.

## Prevent It

1. Generate `compile_commands.json` as part of your CMake configuration.
2. Start with a minimal set of checks and add more as code quality improves.
3. Use `NOLINT` comments sparingly — prefer fixing the underlying issue.

## Related Errors

- [clang-format error]({{< relref "/languages/cpp/cpp-clang-format-error.md" >}}) — formatting issues.
- [cppcheck error]({{< relref "/languages/cpp/cpp-cppcheck-error.md" >}}) — static analysis issues.
- [Compiler warnings]({{< relref "/languages/cpp/cpp-sanitizer-error.md" >}}) — build warnings.
