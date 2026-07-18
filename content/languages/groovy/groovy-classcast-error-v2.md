---
title: "[Solution] Groovy ClassCast Cannot Cast Object to Class"
description: "Fix Groovy ClassCastException when casting objects. Resolve type coercion and inheritance issues in Groovy code."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `ClassCastException` occurs when Groovy attempts to cast an object to an incompatible type. This happens during explicit casts, method calls expecting specific types, or implicit type coercion in assignments.

## Why It Happens

- Explicit cast to incompatible type: The `as` keyword is used with incompatible types.
- Method expects specific type but receives different one: Java interop requires exact type matches.
- Collection contains mixed types: Lists or maps with heterogeneous elements.
- Proxy or decorator does not implement target interface: Dynamic proxies may not implement the expected interface.
- Closure cast to wrong functional interface type: The closure signature does not match the SAM interface.

## How to Fix It

Use instanceof check before casting to prevent runtime exceptions:

```groovy
def obj = getData()
if (obj instanceof String) {
    def str = (String) obj
    process(str)
} else {
    println "Expected String but got ${obj.getClass().name}"
}
```

Use Groovy safe type coercion:

```groovy
def value = "42"

// WRONG: Direct cast may fail
def num = value as Integer

// CORRECT: Use safe conversion
def num = value.isInteger() ? value as Integer : 0

// Or use try-catch
try {
    def num = value as Integer
} catch (NumberFormatException e) {
    println "Cannot convert to integer"
}
```

Handle collection type issues:

```groovy
def mixedList = [1, "two", 3.0]
mixedList.each { item ->
    if (item instanceof Number) {
        processNumber(item as Number)
    } else if (item instanceof String) {
        processString(item as String)
    }
}
```

Use asType for custom conversions in classes:

```groovy
class Money {
    BigDecimal amount
    String currency
    
    def asType(Class type) {
        if (type == String) {
            return "${currency} ${amount}"
        }
        super.asType(type)
    }
}

def money = new Money(amount: 100, currency: "USD")
def str = money as String  // "USD 100"
```

Use collect for type-safe list transformation:

```groovy
def strings = ["1", "2", "three", "4"]
def numbers = strings.findAll { it.isInteger() }.collect { it as Integer }
```

## Common Mistakes

- Casting collections without verifying element types first.
- Forgetting that Groovy uses duck typing differently than Java.
- Not handling null in cast operations. `null as String` returns null but may cause issues downstream.
- Assuming implicit coercion works for all types. Some conversions require explicit `as` keyword.
- Not considering that @CompileStatic changes type checking behavior.

## Related Pages

- [groovy-missing-method-v2]({{< relref "/languages/groovy/groovy-missingmethod-v2" >}}) - missing method
- [groovy-null-pointer-v2]({{< relref "/languages/groovy/groovy-nullpointererror-v2" >}}) - null pointer
- [groovy-index-out-of-bounds]({{< relref "/languages/groovy/groovy-stringindex-v2" >}}) - index out of bounds
- [groovy-compiled-class-error]({{< relref "/languages/groovy/groovy-compiled-class-error" >}}) - compiled class error
