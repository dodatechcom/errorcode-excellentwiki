---
title: "[Solution] Java unreachable statement — Remove Dead Code or Fix Control Flow"
description: "Fix Java compiler error 'unreachable statement' by removing code after return/break/continue/throw or fixing infinite loops. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 400
---

# Java Compiler Error: unreachable statement

This compile-time error occurs when the compiler detects code that can never be executed. The Java Language Specification requires a compile-time check for statement reachability, and `javac` will refuse to compile code it determines is unreachable.

## Error Message

```
error: unreachable statement
        System.out.println("This never executes");
        ^
```

Other variants:

```
error: unreachable statement
        int x = 5;
        ^
```

## Common Causes

### Cause 1: Code After return Statement

Placing executable statements after a `return` makes them unreachable.

```java
public int getValue() {
    return 42;
    System.out.println("Done"); // ERROR: unreachable statement
}
```

### Cause 2: Code After break/continue/throw

Statements following `break`, `continue`, or `throw` in the same block are unreachable.

```java
public void process() {
    for (int i = 0; i < 10; i++) {
        break;
        System.out.println(i); // ERROR: unreachable statement
    }
}
```

### Cause 3: Code After Always-Throwing Statement

```java
public void configure() {
    throw new RuntimeException("fatal");
    int config = loadConfig(); // ERROR: unreachable statement
}
```

### Cause 4: Code in Always-True or Always-False Branches

```java
public void check() {
    if (true) {
        return;
    }
    System.out.println("unreachable"); // ERROR: unreachable statement
}
```

### Cause 5: Code After Infinite Loop

```java
public void run() {
    while (true) {
        // infinite loop
    }
    System.out.println("never reached"); // ERROR: unreachable statement
}
```

### Cause 6: Fall-through with Unreachable Case

```java
public void handle(String input) {
    switch (input) {
        case "A":
            return;
        case "B":
            System.out.println("B"); // reachable
            break;
        default:
            System.out.println("default");
            break;
    }
    // unreachable after certain paths
}
```

## Solutions

### Fix 1: Remove Unreachable Code

Delete the dead code entirely.

```java
public int getValue() {
    return 42;
    // Removed unreachable println
}
```

### Fix 2: Reorder Statements

Move the unreachable code before the terminating statement.

```java
public void process() {
    System.out.println("This executes first");
    for (int i = 0; i < 10; i++) {
        System.out.println(i);
        break;
    }
}
```

### Fix 3: Place Code in Conditional Blocks

Wrap dead code in a reachable conditional.

```java
public int getValue() {
    if (debug) {
        System.out.println("Debug info");
    }
    return 42;
}
```

### Fix 4: Fix the Infinite Loop

Ensure the loop has a proper exit condition.

```java
public void run() {
    int count = 0;
    while (count < 10) {
        System.out.println(count);
        count++;
    }
    System.out.println("Loop finished");
}
```

### Fix 5: Restructure Control Flow

Use proper branching so all paths are reachable.

```java
public void check(int value) {
    if (value > 0) {
        System.out.println("positive");
    } else {
        System.out.println("non-positive");
    }
}
```

## Prevention Checklist

- Remove dead code promptly — don't leave commented-out logic in live blocks
- Use an IDE's "dead code" inspection to catch unreachable code early
- When refactoring, verify that control flow terminators (`return`, `throw`, `break`) don't accidentally trap subsequent logic
- Avoid `if (true)` / `if (false)` constants; use named boolean flags instead
- After converting a loop to infinite, move any post-loop code into the loop or before it
- Review switch statements for missing `break` and unreachable fall-through paths

## Related Errors

- [cannot find symbol: method X (method-not-found)](/languages/java/method-not-found)
- [non-static method cannot be referenced from a static context (non-static-method)](/languages/java/non-static-method)
- [constant expression required (constant-expression-required)](/languages/java/constant-expression-required)
