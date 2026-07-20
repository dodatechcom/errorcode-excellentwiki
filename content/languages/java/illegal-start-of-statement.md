---
title: "[Solution] Java illegal start of statement — Fix Invalid Statement Placement"
description: "Fix Java compiler error illegal start of statement by checking placement, verifying syntax, and moving statements to the correct location. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 127
---

# Java Compiler Error: illegal start of statement

This compile-time error occurs when a statement appears in the wrong location or uses invalid syntax. Unlike `illegal start of expression`, this error typically means a complete statement is placed where the language grammar does not allow it.

## Error Message

```
error: illegal start of statement
```

## Common Causes

### Cause 1: Semicolon After If Condition

```java
public class Example {
    public static void main(String[] args) {
        if (true); {  // Semicolon terminates the if
            System.out.println("This always runs");
        }
    }
}
```

### Cause 2: Statement Before Package Declaration

```java
import java.util.List; // Must come after package
package com.example; // Package must be first

public class Example { }
```

### Cause 3: Code Outside Method or Class

```java
public class Example {
    System.out.println("Hello"); // Statement directly in class body
    public static void main(String[] args) { }
}
```

### Cause 4: Invalid Use of break/continue

```java
public class Example {
    public static void main(String[] args) {
        break; // break outside of loop or switch
    }
}
```

### Cause 5: Statement After Return

```java
public class Example {
    public static void main(String[] args) {
        return;
        System.out.println("Dead code"); // Unreachable statement
    }
}
```

## Solutions

### Fix 1: Remove the Erroneous Semicolon

```java
public class Example {
    public static void main(String[] args) {
        if (true) { // No semicolon after condition
            System.out.println("Conditional block");
        }
    }
}
```

### Fix 2: Move Package to First Line

```java
package com.example;

import java.util.List;

public class Example { }
```

### Fix 3: Place Statements Inside Methods

```java
public class Example {
    public static void main(String[] args) {
        System.out.println("Hello"); // Statement inside method
    }
}
```

### Fix 4: Use break Inside Loop or Switch

```java
public class Example {
    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) {
            if (i == 5) {
                break; // Valid: break inside loop
            }
            System.out.println(i);
        }
    }
}
```

### Fix 5: Remove Unreachable Code

```java
public class Example {
    public static void main(String[] args) {
        return; // Return here
        // Removed unreachable code
    }
}
```

## Prevention Checklist

- Never place a semicolon directly after `if`, `for`, `while`, or `switch` conditions
- Package declaration must be the first non-comment line in the file
- All executable statements must be inside methods or blocks
- `break` and `continue` can only appear inside loops or switch statements
- Remove code after unconditional `return`, `throw`, or `break`
- Use IDE code analysis to catch misplaced statements

## Related Errors

- [illegal-start-of-expression](/languages/java/illegal-start-of-expression/)
- [unreachable-statement](/languages/java/unreachable-statement/)
- [reached-eof-while-parsing](/languages/java/reached-eof-while-parsing/)
