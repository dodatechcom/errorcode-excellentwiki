---
title: "[Solution] Java fall through from previous case — Fix Switch Fall-Through Warning"
description: "Fix Java compiler warning 'fall through from previous case' by adding break/return, using arrow syntax (Java 14+), or documenting intentional fall-through. Copy-paste solutions."
languages: ["java"]
severities: ["warning"]
error_types: ["compile"]
weight: 462
---

# Java Compiler Warning: fall through from previous case

This compile-time warning occurs when a `case` block in a `switch` statement executes and falls through to the next case without a `break`, `return`, or `throw`. While intentional fall-through is sometimes useful, it is often a bug where the developer forgot to add a break statement.

## Error Message

```
warning: fall through from previous case
        case "admin":
            ^
```

Other variants:

```
warning: fall through from previous case
warning: possible fall-through from previous case
```

## Common Causes

### Cause 1: Missing break Statement

```java
public void process(String role) {
    switch (role) {
        case "admin":
            grantFullAccess(); // falls through to "user" case
        case "user":
            grantLimitedAccess(); // runs for both admin AND user
            break;
    }
}
```

### Cause 2: Missing break in Multiple Cases

```java
public int getDays(String month) {
    switch (month) {
        case "January":
        case "March":
        case "May":
        case "July":
        case "August":
        case "October":
        case "December":
            return 31; // falls through all cases — OK if intentional
        case "April":
        case "June":
        case "September":
        case "November":
            return 30;
        case "February":
            return 28;
    }
    return 0;
}
```

### Cause 3: Switch Expression With Missing Yield

```java
public String describe(int code) {
    return switch (code) {
        case 1 -> "one";
        case 2 -> "two";
        case 3: // old syntax mixed with new
            yield "three";
        case 4: // falls through from 3 if break missing
            yield "four";
    };
}
```

### Cause 4: Accidental Fall-Through With Logic

```java
public void handle(int status) {
    switch (status) {
        case 200:
            System.out.println("OK");
            // forgot break — falls through to 201
        case 201:
            System.out.println("Created");
            break;
        case 404:
            System.out.println("Not Found");
            break;
    }
}
```

## Solutions

### Fix 1: Add break Statements

```java
public void process(String role) {
    switch (role) {
        case "admin":
            grantFullAccess();
            break; // added
        case "user":
            grantLimitedAccess();
            break;
    }
}
```

### Fix 2: Use Arrow Syntax (Java 14+)

```java
public void process(String role) {
    switch (role) {
        case "admin" -> grantFullAccess();  // no fall-through with arrow syntax
        case "user" -> grantLimitedAccess();
    }
}
```

### Fix 3: Document Intentional Fall-Through

```java
public int getDays(String month) {
    switch (month) {
        case "January":
        case "March":
        case "May":
        case "July":
        case "August":
        case "October":
        case "December":
            // $FALL-THROUGH$ intentional — all these months have 31 days
            return 31;
        // ...
    }
    return 0;
}
```

### Fix 4: Use switch Expression (Java 14+)

```java
public String describe(int code) {
    return switch (code) {
        case 1 -> "one";
        case 2 -> "two";
        case 3 -> "three";
        case 4 -> "four";
        default -> "unknown";
    };
}
```

### Fix 5: Add @SuppressWarnings for Intentional Fall-Through

```java
@SuppressWarnings("fallthrough")
public void process(int code) {
    switch (code) {
        case 1:
            System.out.println("one");
            // intentional fall-through
        case 2:
            System.out.println("one or two");
            break;
    }
}
```

## Prevention Checklist

- Always add `break` or `return` at the end of each case block (unless fall-through is intentional)
- Use arrow syntax (`case X ->`) in Java 14+ to prevent fall-through entirely
- Use `// $FALL-THROUGH$` comment convention to document intentional fall-through
- Enable `-Xlint:fallthrough` compiler flag to catch accidental fall-through
- Consider using switch expressions (Java 14+) for cleaner, safer switch logic
- Test switch statements with multiple cases to verify correct behavior

## Related Errors

- [constant expression required (constant-expression-required)](/languages/java/constant-expression-required)
- [case expressions must be constant expressions (string-switch-constant)](/languages/java/string-switch-constant)
- [unreachable statement (unreachable-statement)](/languages/java/unreachable-statement)
