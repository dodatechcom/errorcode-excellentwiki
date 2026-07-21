---
title: "[Solution] Objective-C Category Conflict"
description: "Category method conflicts with existing methods."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Category Conflict

Category method conflicts with existing methods.

### Common Causes
Overriding existing methods; no warning

### How to Fix
```objc
// Avoid overriding existing methods
// Use unique prefix
df_void MyCategory_doSomething(id self, SEL _cmd) {
    // implementation
}
```

### Examples
```objc
// Use method swizzling to extend existing methods
// Or use a subclass instead of category
```
