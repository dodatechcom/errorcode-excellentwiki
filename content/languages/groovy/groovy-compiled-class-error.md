---
title: "[Solution] Groovy Cannot Cast Class to Interface Error"
description: "Fix Groovy ClassCastException when casting compiled class to interface. Resolve type compatibility issues."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The compiled class casting error occurs when Groovy tries to cast an object to an interface it does not implement. This often appears with statically compiled code or Java interop where duck typing is not available.

## Why It Happens

- Class does not implement target interface: The object's class does not have the interface in its hierarchy.
- Dynamic proxy generation failed: Groovy cannot create a proxy for the target interface.
- Static compilation prevents duck typing: @CompileStatic requires explicit type relationships.
- Java class loaded by different classloader: Classloader isolation prevents type recognition.
- Mixin or delegation does not create real interface: Groovy mixins do not create actual type relationships.

## How to Fix It

Verify interface implementation:

```groovy
interface Greeter {
    String greet(String name)
}

class HelloGreeter implements Greeter {
    String greet(String name) {
        "Hello, $name"
    }
}

def greeter = new HelloGreeter() as Greeter
println greeter.greet("Alice")
```

Use duck typing with @CompileStatic alternatives:

```groovy
// WRONG: Cannot cast if not implementing interface
def process(Greeter g) { g.greet("World") }
process(myObject)  // ClassCastException if myObject doesn't implement Greeter

// CORRECT: Check interface first
if (myObject instanceof Greeter) {
    process(myObject as Greeter)
} else {
    println "Object does not implement Greeter"
}
```

Create dynamic proxy for duck typing:

```groovy
def proxy = Proxy.newProxyInstance(
    Greeter.getClassLoader(),
    [Greeter] as Class[],
    { proxy, method, args -> myObject.invokeMethod(method.name, args) }
) as Greeter
```

Use @Mixin for interface composition:

```groovy
@groovy.transform.Mixin(HelloGreeter)
class FlexibleClass { }
```

Use @CompileStaticCompatible approaches:

```groovy
// Instead of duck typing, use explicit interfaces
@CompileStatic
class MyService {
    void process(Greeter g) {
        g.greet("World")
    }
}
```

## Common Mistakes

- Assuming Groovy duck typing works with @CompileStatic. Static compilation requires explicit types.
- Not considering classloader differences in plugin systems. Classes from different classloaders are not compatible.
- Forgetting that mixins do not create real type relationships. They only add methods.
- Using `as` keyword without verifying interface availability at runtime.
- Not testing with both dynamic and static compilation modes.

## Related Pages

- [groovy-classcast-error-v2]({{< relref "/languages/groovy/groovy-casterror-v2" >}}) - class cast error
- [groovy-missing-method-v2]({{< relref "/languages/groovy/groovy-missingmethod-v2" >}}) - missing method
- [groovy-ast-error]({{< relref "/languages/groovy/groovy-asterror-v2" >}}) - AST transformation error
- [groovy-deprecated-api]({{< relref "/languages/groovy/groovy-deprecated-api" >}}) - deprecated API
