---
title: "[Solution] Java cannot find symbol: method — Fix Missing Method Error"
description: "Fix Java compiler error 'cannot find symbol: method X' by checking method name, imports, API version, and method signatures. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 404
---

# Java Compiler Error: cannot find symbol: method

This compile-time error occurs when the compiler cannot find a method with the given name and parameter list on the target type. The method either doesn't exist, has a different name, requires different parameter types, or isn't accessible.

## Error Message

```
error: cannot find symbol
  symbol:   method toUpperCase()
  location: variable str of type String
        str.toUpperCase()
            ^
```

Other variants:

```
error: cannot find symbol
  symbol:   method sortBy(Comparator)
  location: class java.util.List
error: cannot find symbol
  symbol:   method getData()
  location: class com.example.MyClass
```

## Common Causes

### Cause 1: Typo in Method Name

A simple misspelling is one of the most common causes.

```java
String name = "hello";
name.toUpperCasee(); // ERROR: cannot find symbol: method toUpperCasee()
```

### Cause 2: Wrong Parameter Types

The method exists but with different parameter types.

```java
List<String> list = List.of("a", "b", "c");
list.get("0"); // ERROR: cannot find symbol: method get(String)
// List.get() requires int, not String
```

### Cause 3: Missing Import

The method is on a type that isn't imported.

```java
// Missing: import java.util.stream.Collectors;
String result = list.stream()
    .collect(Collectors.joining(", ")); // ERROR: cannot find symbol: Collectors
```

### Cause 4: Wrong API Version

Using a method that doesn't exist in the current Java version.

```java
// strip() was added in Java 11
String s = "  hello  ";
s.strip(); // ERROR if compiling with Java 8
```

### Cause 5: Method on Wrong Type

Calling an instance method that belongs to a different type.

```java
Integer num = 42;
num.parseDouble("3.14"); // ERROR: parseDouble is on Double, not Integer
```

### Cause 6: Private Method Called from Outside

```java
class Secret {
    private void internalMethod() { }
}

public void test() {
    Secret s = new Secret();
    s.internalMethod(); // ERROR: cannot find symbol
}
```

## Solutions

### Fix 1: Correct the Method Name

```java
String name = "hello";
name.toUpperCase(); // OK
```

### Fix 2: Use the Correct Parameter Types

```java
List<String> list = List.of("a", "b", "c");
list.get(0); // OK — int index
```

### Fix 3: Add the Missing Import

```java
import java.util.stream.Collectors;

String result = list.stream()
    .collect(Collectors.joining(", ")); // OK
```

### Fix 4: Check the Java Version

Use a compatible method for your target Java version.

```java
// For Java 8 compatibility:
String s = "  hello  ";
s.trim(); // Available since Java 1.0

// Or upgrade to Java 11+ and use:
s.strip(); // Added in Java 11
```

### Fix 5: Call the Method on the Correct Type

```java
Double.parseDouble("3.14"); // Static method on Double class
```

### Fix 6: Make the Method Accessible

```java
class Secret {
    public void internalMethod() { } // Changed from private to public
}
```

## Prevention Checklist

- Use your IDE's auto-complete to avoid typos and discover available methods
- Verify the method signature matches your argument types
- Check which Java version your project targets (`sourceCompatibility` in Gradle or `maven.compiler.source` in Maven)
- Ensure all required classes are imported — use IDE import shortcuts (`Ctrl+Shift+O` in IntelliJ, `Ctrl+Shift+I` in Eclipse)
- Read the Javadoc for the class you're using to find the correct method
- Check access modifiers — the method must be `public` or accessible in the same package

## Related Errors

- [non-static method cannot be referenced from a static context (non-static-method)](/languages/java/non-static-method)
- [incompatible types (incompatible-types)](/languages/java/incompatible-types)
- [invalid method reference (invalid-method-reference)](/languages/java/invalid-method-reference)
- [X is abstract; cannot be instantiated (abstract-method)](/languages/java/abstract-method)
