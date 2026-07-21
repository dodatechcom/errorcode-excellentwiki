---
title: "[Solution] Groovy Power Assert"
description: "Power assertion errors in testing."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Power Assert

Power assertion errors in testing.

### Common Causes
Wrong assert syntax; missing message

### How to Fix
```groovy
assert 1 + 1 == 2
```

### Examples
```groovy
assert list.size() == 3 : "Expected 3 items"
```
