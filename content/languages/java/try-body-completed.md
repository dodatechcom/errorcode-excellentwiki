---
title: "[Solution] Java try body does not complete normally — Fix Unreachable Catch/Finally"
description: "Fix Java compiler error 'try body does not complete normally' by checking try block for always-throwing code, ensuring catch blocks are reachable, and fixing unreachable code. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 466
---

# Java Compiler Error: try body does not complete normally

This compile-time error occurs when the code inside a `try` block always completes by throwing an exception (never completes normally), making any `catch` blocks unreachable. The Java compiler detects that the `try` body always throws, so there is no path where the catch block could execute.

## Error Message

```
error: try body does not complete normally
    try {
    ^
```

Other variants:

```
error: catch block cannot be reached
error: unreachable catch block for Throwable
error: exception X has already been caught
```

## Common Causes

### Cause 1: Try Block Always Throws

```java
public void process() {
    try {
        throw new RuntimeException("always throws");
        System.out.println("unreachable"); // ERROR: try body doesn't complete normally
    } catch (RuntimeException e) {
        // catch block is unreachable
    }
}
```

### Cause 2: Unconditional Throw With No Flow to Catch

```java
public void test() {
    try {
        riskyOperation(); // if this always throws
        int x = 5; // unreachable
    } catch (Exception e) {
        // unreachable
    }
}

public void riskyOperation() {
    throw new IllegalStateException("always"); // method always throws
}
```

### Cause 3: Catch Block After Unreachable Code

```java
public void example() {
    try {
        int[] arr = new int[0];
        int val = arr[0]; // ArrayIndexOutOfBoundsException — but compiler can't prove this
        int x = 10 / 0; // ArithmeticException — but compiler doesn't track runtime exceptions
    } catch (Exception e) {
        // This IS reachable — compiler allows it for unchecked exceptions
    }
}
```

### Cause 4: Try-Finally With Always-Throwing Try

```java
public void cleanup() {
    try {
        throw new RuntimeException("error");
    } finally {
        System.out.println("cleanup"); // OK — finally always runs
    }
    // But this is unreachable:
    System.out.println("done");
}
```

### Cause 5: Nested Try With Unreachable Code

```java
public void nested() {
    try {
        try {
            throw new RuntimeException();
        } catch (RuntimeException e) {
            throw e; // rethrows — outer catch may be unreachable
        }
    } catch (RuntimeException e) {
        // might be unreachable if all paths rethrow
    }
}
```

## Solutions

### Fix 1: Add a Return or Normal Completion Path

```java
public void process() {
    try {
        if (someCondition()) {
            throw new RuntimeException("error");
        }
        // normal path — try body can complete normally
    } catch (RuntimeException e) {
        handleError(e);
    }
}
```

### Fix 2: Remove the Unreachable Catch Block

```java
public void test() {
    throw new RuntimeException("always throws");
    // Remove the try-catch since it can never be caught here
}
```

### Fix 3: Use try-with-resources Correctly

```java
import java.io.*;

public void read(String path) {
    try (BufferedReader br = new BufferedReader(new FileReader(path))) {
        String line = br.readLine();
        System.out.println(line);
    } catch (IOException e) {
        // This IS reachable — I/O operations can throw
        System.err.println("Error reading file");
    }
}
```

### Fix 4: Move Code After Try Block Inside Try

```java
public void example() {
    try {
        riskyOperation();
        // Move this inside the try block or before the try
    } catch (Exception e) {
        // handle
    }
    System.out.println("continues after try-catch");
}
```

### Fix 5: Use Conditional Logic Instead of Guaranteed Throw

```java
public void process(int value) {
    try {
        if (value < 0) {
            throw new IllegalArgumentException("negative");
        }
        // Normal processing — try body completes normally
        processValue(value);
    } catch (IllegalArgumentException e) {
        System.err.println("Invalid value: " + e.getMessage());
    }
}
```

## Prevention Checklist

- Ensure try blocks have a path that completes normally (doesn't always throw)
- Remove unnecessary try-catch blocks around code that cannot throw checked exceptions
- Place catch blocks only around code that can actually throw the caught exception type
- Use the compiler's `-Xlint:unchecked` flag for additional warnings
- Review methods called in try blocks to check if they always throw
- Use IDE inspections to detect unreachable catch blocks

## Related Errors

- [unreachable statement (unreachable-statement)](/languages/java/unreachable-statement)
- [exception never thrown in body of corresponding try statement (exception-never-thrown)](/languages/java/exception-never-thrown)
- [catch block cannot be reached](/languages/java/unreachablecatchexception)
