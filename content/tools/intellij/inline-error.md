---
title: "[Solution] IntelliJ IDEA Inline refactoring failed"
description: "Fix IntelliJ IDEA inline refactoring failures. Resolve inline method, inline variable, and inline constant errors."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "inline", "refactoring", "method-inlining", "constant-inlining"]
severity: "error"
---

# Inline refactoring failed

## Error Message

```
Inline refactoring failed
Cannot inline method: recursive call detected
Inline constant: value used in annotation cannot be inlined
Inline variable: variable has multiple conflicting assignments
Cannot inline: method has overriding implementations
```

## Common Causes

- Method contains recursive calls that prevent safe inlining
- Constant is used in annotations which require compile-time constants
- Variable is modified in multiple branches preventing inlining
- Method has overriding implementations in subclasses
- Inlined code would exceed method length or complexity limits

## Solutions

### Solution 1: Inline Method with Override Handling

When a method has overrides, choose to inline only the current implementation or all occurrences.

```
# Position cursor on method name
# Right-click → Refactor → Inline (Ctrl+Alt+N)

# In the inline dialog:
# Select 'All invocations' or 'Current invocation only'
# ☑ Inline recursively (if applicable)
# Click 'OK' to preview and apply

# For methods with overrides:
# The IDE will warn about override implementations
# Choose to inline into the current class only
# Or refactor the class hierarchy first
```

### Solution 2: Resolve Recursive Inline Issues

Break recursive calls before attempting to inline the method.

```java
// Before (recursive method):
public int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);  // recursive call
}

// Solution 1: Replace recursion with iteration first:
public int factorial(int n) {
    int result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}
// Then inline the iterative version

// Solution 2: Inline only non-recursive parts:
# Select specific lines inside the method
# Extract into a helper, then inline the helper
```

### Solution 3: Inline Constants and Variables

Inline simple constants and variables when they are used in few places.

```java
// Inline Constant:
private static final int MAX_SIZE = 100;
// Usage: if (list.size() > MAX_SIZE) {...}

// After inline:
if (list.size() > 100) {...}
// The constant declaration is removed

// Inline Variable:
String formatted = name.trim().toUpperCase();
System.out.println(formatted);

// After inline:
System.out.println(name.trim().toUpperCase());
// The variable declaration is removed

# In IDE:
# Cursor on constant/variable → Refactor → Inline (Ctrl+Alt+N)
```

### Solution 4: Break Complex Inlining into Steps

For complex inlining operations, perform the refactoring in smaller steps.

```
# Step 1: Simplify the method to be inlined
#   Remove complex branching and loops
#   Extract helper methods for complex logic

# Step 2: Inline simple methods first
#   Right-click → Refactor → Inline

# Step 3: Inline the simplified result
#   This two-step approach reduces error risk

# Alternative: Use manual inlining
# 1. Copy the method body
# 2. Replace each call site with the body
# 3. Adjust parameters and return values
# 4. Delete the original method
# 5. Run 'Code → Optimize Imports' to clean up
```

## Prevention Tips

- Inline small methods that are only called once to reduce indirection
- Use inline refactoring before removing unused methods to ensure no side effects
- Review inlined code carefully for variable name shadowing or scope issues
- Use Inline Constant to eliminate magic numbers and improve code readability

## Related Errors

- [Extract Error]({{< relref "/tools/intellij/extract-error" >}})
- [Refactoring Failed]({{< relref "/tools/intellij/refactoring-error" >}})
- [Move Error]({{< relref "/tools/intellij/move-error" >}})
