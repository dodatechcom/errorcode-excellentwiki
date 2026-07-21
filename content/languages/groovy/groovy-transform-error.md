---
title: "[Solution] Groovy AST Transform"
description: "AST transformation errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy AST Transform

AST transformation errors.

### Common Causes
Wrong annotation; missing @Retention

### How to Fix
```groovy
@Immutable
class Person {
    String name
    int age
}
```

### Examples
```groovy
@Sortable
class Employee implements Comparable<Employee> {
    String name
    int salary
}
```
