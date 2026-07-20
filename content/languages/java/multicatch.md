---
title: "[Solution] Java cannot convert thrown type to multi-catch parameter — Fix Multi-Catch Exception"
description: "Fix Java compiler error 'cannot convert thrown type to multi-catch parameter' by removing redundant catch types or checking exception hierarchy. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 418
---

# Java Compiler Error: cannot convert thrown type to multi-catch parameter

This compile-time error occurs when multi-catch exception types have a subtype relationship — one exception type is a subclass of another. Java's multi-catch syntax (Java 7+) requires that the caught exception types be unrelated in the class hierarchy, since the compiler generates a synthetic method that handles each type independently.

## Error Message

```
error: Alternatives in a multi-catch statement cannot be related by subclassing
        catch (IOException | FileNotFoundException e)
                 ^
```

Other variants:

```
error: the exception FileNotFoundException is a subclass of the exception IOException
error: cannot convert thrown type FileNotFoundException to multi-catch parameter IOException
```

## Common Causes

### Cause 1: Subclass Listed After Superclass

```java
try {
    readFile();
} catch (IOException | FileNotFoundException e) { // ERROR: FileNotFoundException extends IOException
    // ...
}
```

### Cause 2: Exception Hierarchy Overlap

```java
try {
    riskyOperation();
} catch (RuntimeException | IllegalArgumentException e) { // ERROR: IAE extends RuntimeException
    // ...
}

// Also:
try {
    dbOperation();
} catch (SQLException | BatchUpdateException e) { // ERROR: BatchUpdateException extends SQLException
    // ...
}
```

### Cause 3: Custom Exception Hierarchy

```java
class BaseException extends Exception { }
class SpecificException extends BaseException { }

try {
    customOperation();
} catch (BaseException | SpecificException e) { // ERROR: SpecificException extends BaseException
    // ...
}
```

### Cause 4: AutoCloseable Exception Hierarchy

```java
try (var resource = getResource()) {
    resource.use();
} catch (Exception | IOException e) { // ERROR: IOException extends Exception
    // ...
}
```

### Cause 5: Multiple Checked Exceptions with Inheritance

```java
class ParserException extends Exception { }
class JsonParserException extends ParserException { }

try {
    parse();
} catch (ParserException | JsonParserException e) { // ERROR
    // ...
}
```

## Solutions

### Fix 1: Remove the Subclass from Multi-Catch

Keep only the superclass — it already covers the subclass.

```java
try {
    readFile();
} catch (IOException e) { // IOException already covers FileNotFoundException
    // ...
}
```

### Fix 2: Use Only the Most Specific Type

If you want to handle the specific exception differently, catch it separately.

```java
try {
    readFile();
} catch (FileNotFoundException e) {
    System.out.println("File not found");
} catch (IOException e) {
    System.out.println("IO error");
}
```

### Fix 3: Keep Only Unrelated Exception Types

```java
try {
    riskyOperation();
} catch (IOException | ParseException e) { // OK — unrelated types
    // ...
}
```

### Fix 4: Use Separate Catch Blocks

When you need different handling for each exception type.

```java
try {
    riskyOperation();
} catch (FileNotFoundException e) {
    handleNotFound();
} catch (IOException e) {
    handleIOError();
}
```

### Fix 5: Keep Only the Base Type in Multi-Catch

```java
try {
    customOperation();
} catch (BaseException e) { // covers SpecificException too
    // ...
}
```

## Prevention Checklist

- Review the exception class hierarchy before using multi-catch
- Use only unrelated exception types in a single catch clause
- Keep only the superclass if you want to handle all exceptions the same way
- Use separate catch blocks when you need different handling per exception type
- Check the Java API documentation for exception inheritance relationships
- Be aware that `Exception` covers all checked exceptions — don't combine it with specific subtypes

## Related Errors

- [X is abstract; cannot be instantiated (abstract-method)](/languages/java/abstract-method)
- [variable X might not have been initialized (variable-not-init)](/languages/java/variable-not-init)
- [try-with-resources is not applicable to variable type (try-with-resources)](/languages/java/try-with-resources)
