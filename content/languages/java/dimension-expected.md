---
title: "[Solution] Java dimension expected — Fix Missing Array Dimension"
description: "Fix Java compiler error dimension expected by adding array size or [], checking syntax, and verifying array creation. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 133
---

# Java Compiler Error: dimension expected

This compile-time error occurs when the compiler expects an array dimension (size or brackets) but finds something else instead. It typically appears when declaring or creating arrays with incorrect syntax.

## Error Message

```
error: dimension expected
```

## Common Causes

### Cause 1: Missing Brackets in Declaration

```java
public class Example {
    public static void main(String[] args) {
        int arr; // Should be int[] arr;
        arr = new int[5];
    }
}
```

### Cause 2: Missing Size in Array Creation

```java
public class Example {
    public static void main(String[] args) {
        int[] arr = new int(); // Should be new int[5] or new int[]
    }
}
```

### Cause 3: Wrong Syntax for Multidimensional Array

```java
public class Example {
    public static void main(String[] args) {
        int[][] arr = new int[3,4]; // Java uses [3][4] not [3,4]
    }
}
```

### Cause 4: Missing Dimension After Type in Method Parameter

```java
public class Example {
    public static void process(int arr) { // Should be int[] arr
        System.out.println(arr.length);
    }
}
```

### Cause 5: Empty Brackets in New Expression

```java
public class Example {
    public static void main(String[] args) {
        int[] arr = new int[]; // Missing size or initializer
    }
}
```

## Solutions

### Fix 1: Add Array Brackets to Declaration

```java
public class Example {
    public static void main(String[] args) {
        int[] arr; // Added brackets
        arr = new int[5];
        System.out.println(arr.length);
    }
}
```

### Fix 2: Provide Array Size

```java
public class Example {
    public static void main(String[] args) {
        int[] arr = new int[5]; // Provided size
        System.out.println(arr.length);
    }
}
```

### Fix 3: Use Correct Multidimensional Syntax

```java
public class Example {
    public static void main(String[] args) {
        int[][] arr = new int[3][4]; // Correct: separate brackets
        System.out.println(arr.length);    // 3
        System.out.println(arr[0].length); // 4
    }
}
```

### Fix 4: Add Array Brackets to Parameter

```java
public class Example {
    public static void process(int[] arr) { // Added brackets
        System.out.println(arr.length);
    }

    public static void main(String[] args) {
        process(new int[]{1, 2, 3});
    }
}
```

### Fix 5: Use Initializer Instead of Empty new

```java
public class Example {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3}; // Array initializer
        // Or:
        int[] arr2 = new int[]{1, 2, 3};
    }
}
```

## Prevention Checklist

- Always include `[]` after the type when declaring arrays
- Provide either a size `[n]` or an initializer `{...}` when creating arrays
- Use separate brackets for each dimension: `[3][4]` not `[3,4]`
- Method parameters need `[]` to indicate array type
- Use IDE auto-complete for array declarations
- Verify array syntax before compiling

## Related Errors

- [illegal-array-creation](/languages/java/illegal-array-creation/)
- [negativearraysizeexception](/languages/java/negativearraysizeexception/)
- [arrayindexoutofboundsexception](/languages/java/arrayindexoutofboundsexception/)
