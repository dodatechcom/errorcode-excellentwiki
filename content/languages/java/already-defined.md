---
title: "[Solution] Java variable is already defined in method — Fix Duplicate Local Variable"
description: "Fix Java compiler error 'variable X is already defined in method' by renaming duplicate variables or restructuring scope. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 409
---

# Java Compiler Error: variable is already defined in method

This compile-time error occurs when you declare a local variable with the same name as another local variable in the same scope. Java does not allow two local variables with the same name in the same method scope.

## Error Message

```
error: variable x is already defined in method compute()
        int x = 20;
          ^
```

Other variants:

```
error: variable count is already defined in method process()
error: variable result is already defined in scope
```

## Common Causes

### Cause 1: Duplicate Variable in Same Scope

```java
public void compute() {
    int x = 10;
    int x = 20; // ERROR: variable x is already defined in method compute()
}
```

### Cause 2: Variable Shadowing in Same Scope

```java
public void process() {
    String name = "Alice";
    String name = "Bob"; // ERROR: variable name is already defined
}
```

### Cause 3: Loop Variable Reuse

```java
public void iterate() {
    for (int i = 0; i < 10; i++) {
        System.out.println(i);
    }
    for (int i = 0; i < 5; i++) { // OK — i is in a new scope
        System.out.println(i);
    }
    System.out.println(i); // ERROR: i is out of scope
}
```

### Cause 4: Lambda Parameter Conflict

```java
public void example() {
    int x = 10;
    list.forEach(x -> System.out.println(x)); // ERROR: variable x is already defined
}
```

### Cause 5: Catch Parameter Conflict

```java
public void handleException() {
    String error = "none";
    try {
        riskyOperation();
    } catch (Exception error) { // ERROR: variable error is already defined
        System.out.println(error);
    }
}
```

### Cause 6: Method Parameter Same as Local

```java
public void add(int x) {
    int x = x + 1; // ERROR: variable x is already defined
}
```

## Solutions

### Fix 1: Rename the Duplicate Variable

```java
public void compute() {
    int x = 10;
    int y = 20; // renamed from x
    System.out.println(x + y);
}
```

### Fix 2: Use Different Variable Names

```java
public void process() {
    String firstName = "Alice";
    String secondName = "Bob"; // different name
}
```

### Fix 3: Use Block Scope

```java
public void compute() {
    int x = 10;
    {
        int x2 = 20; // different name in inner scope
        System.out.println(x + x2);
    }
}
```

### Fix 4: Rename Lambda Parameters

```java
public void example() {
    int x = 10;
    list.forEach(item -> System.out.println(x + item)); // renamed parameter
}
```

### Fix 5: Rename Catch Parameter

```java
public void handleException() {
    String error = "none";
    try {
        riskyOperation();
    } catch (Exception ex) { // renamed from error to ex
        error = ex.getMessage();
    }
    System.out.println(error);
}
```

### Fix 6: Rename Method Parameter or Local

```java
public void add(int value) {
    int result = value + 1; // renamed local
    System.out.println(result);
}
```

## Prevention Checklist

- Use descriptive, unique variable names to avoid accidental duplication
- Keep variable scopes as small as possible — declare variables close to first use
- Use IDE refactoring tools to rename variables safely
- Avoid reusing variable names across different blocks in the same method
- Use lambda parameter names that don't conflict with surrounding variables
- Consider using `final` variables for values that shouldn't change

## Related Errors

- [variable X might not have been initialized (variable-not-init)](/languages/java/variable-not-init)
- [unreachable statement (unreachable-statement)](/languages/java/unreachable-statement)
- [non-static method cannot be referenced from a static context (non-static-method)](/languages/java/non-static-method)
