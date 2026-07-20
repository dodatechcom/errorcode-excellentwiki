---
title: "[Solution] Java the import X conflicts with a type defined in another import — Fix Import Conflict"
description: "Fix Java compiler error 'the import X conflicts with a type defined in another import' by removing duplicate imports, using fully qualified names, or using static imports. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 454
---

# Java Compiler Error: the import X conflicts with a type defined in another import

This compile-time error occurs when two imports define the same simple name, creating an ambiguity the compiler cannot resolve. This can happen when importing a class whose name matches another import, or when a wildcard import conflicts with a specific import.

## Error Message

```
error: the import java.util.List conflicts with a type defined in another import
import java.util.List;
       ^
```

Other variants:

```
error: the import com.example.List conflicts with a type defined in another import
error: type List is already defined
error: name clash: List and List conflict
```

## Common Causes

### Cause 1: Duplicate Specific Imports

```java
import java.util.List;
import java.util.List; // ERROR: duplicate import
```

### Cause 2: Same Name From Different Packages

```java
import java.util.List;
import com.myapp.List; // ERROR: the import com.myapp.List conflicts with java.util.List
```

### Cause 3: Wildcard Import Clashes With Specific Import

```java
import java.util.*; // imports java.util.List
import java.util.List; // OK — specific import overrides wildcard
// But: import java.awt.List; would conflict with java.util.List from wildcard
```

### Cause 4: Static Import Clashes With Class Import

```java
import static java.lang.Math.PI;
import static java.util.concurrent.TimeUnit.SECONDS;

// No conflict here — but this would conflict:
import static java.lang.Math.abs;
import com.example.Math; // ERROR: conflicts with static import of java.lang.Math.abs
```

### Cause 5: Class Name Matches Existing Import

```java
import java.util.List;

public class List { // ERROR: type List is already defined from java.util.List
    // ...
}
```

## Solutions

### Fix 1: Remove the Duplicate Import

```java
import java.util.List; // keep only one import
// removed: import java.util.List; // duplicate
```

### Fix 2: Use Fully Qualified Name

```java
import java.util.List;
import com.myapp.List as MyAppList; // Java doesn't support import aliasing

// Instead, use fully qualified name:
java.util.List<String> javaList = new java.util.ArrayList<>();
com.myapp.List myList = new com.myapp.List();
```

### Fix 3: Use Static Import for Disambiguation

```java
import static java.lang.Math.PI;
import static java.lang.Math.abs;

// Use fully qualified name for conflicting class
java.util.List<String> items = new java.util.ArrayList<>();
```

### Fix 4: Rename Your Class to Avoid Conflict

```java
import java.util.List;

public class MyCustomList { // renamed from List to avoid conflict
    // ...
}
```

### Fix 5: Organize Imports

```java
// Let IDE organize imports — remove wildcards and resolve conflicts
// IntelliJ: Ctrl+Alt+O
// Eclipse: Ctrl+Shift+O
// VS Code: Shift+Alt+O
```

## Prevention Checklist

- Avoid wildcard imports (`import java.util.*`) — use specific imports instead
- Check for naming conflicts before importing classes with common names (List, Map, Set)
- Use fully qualified names when two classes have the same simple name
- Organize imports regularly using IDE tools
- Avoid naming your classes the same as common JDK or library classes
- Use packages with distinctive names to reduce naming collisions

## Related Errors

- [cannot find symbol (cannot-find-symbol)](/languages/java/cannot-find-symbol)
- [method is already defined in class (method-overload)](/languages/java/method-overload)
- [type X is already defined in this scope](/languages/java/already-defined)
