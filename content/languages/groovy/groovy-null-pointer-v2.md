---
title: "[Solution] Groovy Cannot Invoke Method on Null Reference"
description: "Fix Groovy NullPointerException when calling methods on null. Use safe navigation and null checks in Groovy."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `NullPointerException` occurs when attempting to invoke a method on a null reference. Groovy provides safe navigation operators but does not prevent null pointer errors by default.

## Why It Happens

- Method called on uninitialized variable: The variable has not been assigned a value.
- Return value from method is null: A method returns null and the result is used without checking.
- Collection element is null: Accessing elements from a collection that contains null values.
- Map lookup returns null and method called on result: Chain of method calls on potentially null values.
- Chained method calls without null checks: Each link in the chain could return null.

## How to Fix It

Use safe navigation operator for nullable chains:

```groovy
// WRONG: NullPointerException if user is null
def email = user.getEmail()

// CORRECT: Safe navigation
def email = user?.getEmail()
def domain = user?.getEmail()?.split("@")?.getAt(1)
```

Use Elvis operator for default values:

```groovy
def name = user?.name ?: "Anonymous"
def count = list?.size() ?: 0
def config = loadConfig() ?: defaultConfig()
```

Add null checks at method entry:

```groovy
def processUser(User user) {
    if (user == null) {
        throw new IllegalArgumentException("User cannot be null")
    }
    // Safe to proceed
    user.name
}
```

Use Groovy truth for conditional execution:

```groovy
// Only execute if all values are non-null
if (user?.email && user?.active) {
    sendEmail(user.email)
}
```

Handle null in collection operations:

```groovy
def items = [1, null, 3, null, 5]
items.findAll { it != null }.each { item ->
    process(item)
}

// Or use Groovy truth
items.findAll().each { process(it) }
```

Use Optional for explicit null handling:

```groovy
Optional.ofNullable(user)
    .map { it.email }
    .ifPresent { sendEmail(it) }
```

## Common Mistakes

- Assuming Groovy automatically handles all null cases. Safe navigation must be explicitly used.
- Not using safe navigation in chained calls. Each link in the chain needs `?.`.
- Ignoring null returns from map operations. `map.get(key)` returns null if key is missing.
- Forgetting that Groovy truth treats empty collections as false, which may cause unexpected behavior.
- Using `?.` excessively when explicit null checks would be clearer.

## Related Pages

- [groovy-missing-property-v2]({{< relref "/languages/groovy/groovy-missingproperty-v2" >}}) - missing property
- [groovy-missing-method-v2]({{< relref "/languages/groovy/groovy-missingmethod-v2" >}}) - missing method
- [groovy-index-out-of-bounds]({{< relref "/languages/groovy/groovy-stringindex-v2" >}}) - index out of bounds
- [groovy-classcast-error-v2]({{< relref "/languages/groovy/groovy-casterror-v2" >}}) - class cast error
