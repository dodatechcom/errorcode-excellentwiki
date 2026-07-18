---
title: "[Solution] Groovy Missing Method Signature Error"
description: "Fix Groovy MissingMethodException when no method signature matches. Resolve method dispatch and argument issues."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `MissingMethodException` with "No signature of method matches" occurs when Groovy cannot find any method on an object that accepts the given argument types. The dynamic dispatch system fails to coerce arguments to match available method signatures.

## Why It Happens

- Method exists but argument types cannot be coerced: Groovy cannot convert the provided types to match the method signature.
- Calling Java method with Groovy-specific types: GString, ranges, and closures do not always map to Java types.
- GString passed where String is expected: Java methods expect `java.lang.String`, not `groovy.lang.GString`.
- Closure passed to method expecting specific functional interface: The closure must be explicitly converted.
- Spread operator results in wrong argument count: The `*.` operator may produce unexpected results.

## How to Fix It

Convert GString to String before passing to Java methods:

```groovy
def name = "Alice"
// WRONG: Passing GString to Java method
def file = new File("/home/${name}/data.txt")

// CORRECT: Explicit String conversion
def file = new File("/home/${name.toString()}/data.txt")
def file2 = new File("/home/${name as String}/data.txt")
```

Use explicit type casting for ambiguous arguments:

```groovy
def list = [1, 2, 3]
// WRONG: MissingMethodException
list.add(0, "new")

// CORRECT: Cast to proper type
((List) list).add(0, "new")
list.add(0, "new" as Object)
```

Check method signature with reflection:

```groovy
def methods = myObject.getClass().methods.collect { 
    "${it.name}(${it.parameterTypes.collect { it.simpleName }.join(', ')})" 
}
println methods
```

Handle Closure type mismatches with explicit conversion:

```groovy
// WRONG: Closure does not match SAM interface
def runner = { println "hello" }
exec(runner)

// CORRECT: Use explicit conversion
exec(runner as Runnable)

// Or use SAM type
Runnable runnable = { println "hello" }
exec(runnable)
```

Use the spread operator carefully:

```groovy
def lists = [[1, 2], [3, 4, 5]]
// WRONG: Different closure arity
lists.collect { it.collect { a, b -> a + b } }

// CORRECT: Variable arguments
lists.collect { it.collect { args -> args.sum() } }
```

## Common Mistakes

- Passing GString interpolation to Java library methods without conversion.
- Forgetting that Groovy auto-boxes primitives differently than Java.
- Not converting list types for Java generic expectations.
- Using spread operator on null collections without safe navigation.
- Assuming Groovy will automatically find the closest matching method signature.

## Related Pages

- [groovy-missingproperty-v2]({{< relref "/languages/groovy/groovy-missingproperty-v2" >}}) - missing property
- [groovy-classcast-error-v2]({{< relref "/languages/groovy/groovy-casterror-v2" >}}) - class cast error
- [groovy-closure-error]({{< relref "/languages/groovy/groovy-closureerror-v2" >}}) - closure call error
- [groovy-null-pointer-v2]({{< relref "/languages/groovy/groovy-nullpointererror-v2" >}}) - null pointer error
