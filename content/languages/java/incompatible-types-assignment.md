---
title: "[Solution] Java incompatible types: possible lossy conversion — Fix Narrowing Conversion"
description: "Fix Java compiler error 'incompatible types: possible lossy conversion from X to Y' by adding an explicit cast or using a wider type. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 402
---

# Java Compiler Error: incompatible types: possible lossy conversion

This compile-time error occurs when Java detects a narrowing primitive conversion that would lose information. Unlike widening conversions (e.g., `int` to `long`), narrowing conversions (e.g., `long` to `int`, `double` to `int`) can lose precision or magnitude, so Java requires an explicit cast.

## Error Message

```
error: incompatible types: possible lossy conversion from long to int
        int x = longValue;
              ^
```

Other variants:

```
error: incompatible types: possible lossy conversion from double to int
error: incompatible types: possible lossy conversion from float to long
error: incompatible types: possible lossy conversion from double to float
```

## Common Causes

### Cause 1: Assigning long to int

The `long` type is 64-bit; `int` is only 32-bit.

```java
public void example() {
    long big = 1_000_000L;
    int small = big; // ERROR: possible lossy conversion from long to int
}
```

### Cause 2: Assigning double to int or float

Floating-point types cannot be implicitly converted to integer types.

```java
public void example() {
    double pi = 3.14159;
    int whole = pi; // ERROR: possible lossy conversion from double to int

    double big = 1.79E308;
    float small = big; // ERROR: possible lossy conversion from double to float
}
```

### Cause 3: Assigning long to short or byte

Even smaller integer types require explicit casts.

```java
public void example() {
    long value = 100L;
    short s = value; // ERROR: possible lossy conversion
    byte b = value;  // ERROR: possible lossy conversion
}
```

### Cause 4: Assigning float to int

Floating-point to integer conversion loses fractional part.

```java
public void example() {
    float f = 3.99f;
    int i = f; // ERROR: possible lossy conversion
}
```

### Cause 5: Method Return Value Narrowing

Returning a wider type from a narrower return type.

```java
public int getCount() {
    long big = 42L;
    return big; // ERROR: possible lossy conversion from long to int
}
```

## Solutions

### Fix 1: Add an Explicit Cast

Casting tells the compiler you accept the potential loss.

```java
long big = 1_000_000L;
int small = (int) big; // OK — truncates if value exceeds int range

double pi = 3.14159;
int whole = (int) pi; // OK — truncates to 3
```

### Fix 2: Use the Wider Type

Change the variable or parameter type to match.

```java
long big = 1_000_000L;
long result = big; // OK — both long

double pi = 3.14159;
double result = pi; // OK — both double
```

### Fix 3: Use Math Methods for Safe Conversion

```java
long big = 1_000_000L;
int safeInt = Math.toIntExact(big); // Throws ArithmeticException if overflow

double pi = 3.14159;
int rounded = (int) Math.round(pi); // Rounds to 3
```

### Fix 4: Use Appropriate Wrapping Methods

```java
double pi = 3.14159;
int whole = Double.valueOf(pi).intValue(); // Explicit conversion
```

### Fix 5: Change Method Signature

Update the return type to match what you're returning.

```java
public long getCount() {
    long big = 42L;
    return big; // OK
}
```

## Prevention Checklist

- Be aware of type sizes: `byte(8) < short(16) < int(32) < long(64)` and `float(32) < double(64)`
- Use `Math.toIntExact()` when converting `long` to `int` to detect overflow at runtime
- Use `Math.round()` or `Math.floor()` / `Math.ceil()` before casting floating-point to integer
- Prefer `BigDecimal` over `double` for financial/precision-sensitive calculations
- Use your IDE's inspections to flag potential narrowing conversions

## Related Errors

- [incompatible types (incompatible-types)](/languages/java/incompatible-types)
- [loss of precision warning in multi-catch](/languages/java/multicatch)
- [unchecked cast warning (unchecked-cast)](/languages/java/unchecked-cast)
