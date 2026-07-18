---
title: "[Solution] Groovy MetaClass Method Not Found Error"
description: "Fix Groovy MetaClass method not found error. Configure metaclass extensions and method resolution properly."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The MetaClass method not found error occurs when Groovy's meta-object protocol cannot locate a method through the metaclass hierarchy. This affects both static and dynamic method resolution.

## Why It Happens

- Metaclass method added to wrong class: The method was added to a different class than expected.
- Method defined on metaClass but not invoked correctly: The invocation syntax does not match the definition.
- Per-instance metaclass conflicts with class metaclass: Instance-level metaclass may shadow class-level methods.
- Runtime metaclass changes not propagated: Changes to metaclass are not thread-safe by default.
- MethodMissing not implemented for dynamic dispatch: The fallback for missing methods is not defined.

## How to Fix It

Add methods to metaclass properly:

```groovy
String.metaClass.shout = { ->
    delegate.toUpperCase() + "!"
}

println "hello".shout()  // HELLO!
```

Implement methodMissing for dynamic dispatch:

```groovy
class DynamicClass {
    def methodMissing(String name, args) {
        println "Called: $name with $args"
        "dynamic result"
    }
}

def obj = new DynamicClass()
println obj.anyMethod("test")
```

Check metaclass before invoking:

```groovy
def metaClass = myObject.metaClass
if (metaClass.respondsTo(myObject, "targetMethod", String)) {
    myObject.targetMethod("value")
} else {
    println "Method not available on metaclass"
}
```

Use per-instance metaclass carefully:

```groovy
def obj1 = new MyClass()
def obj2 = new MyClass()

obj1.metaClass.customMethod = { "custom" }
// Only obj1 has customMethod, obj2 does not
```

Use @Category for type-safe metaclass extensions:

```groovy
@Category(String)
class StringEnhancements {
    String shout() {
        this.toUpperCase() + "!"
    }
}

use(StringEnhancements) {
    println "hello".shout()
}
```

Use ExpandoMetaClass for dynamic classes:

```groovy
String.metaClass {
    shout = { -> delegate.toUpperCase() + "!" }
    whisper = { -> delegate.toLowerCase() + "..." }
}

println "HELLO".shout()  // HELLO!
println "HELLO".whisper()  // hello...
```

Handle method resolution order:

```groovy
class Animal { String speak() { "..." } }
class Dog extends Animal { String speak() { "Woof!" } }

Dog.metaClass.speak = { -> "Bark!" }
def dog = new Dog()
println dog.speak()  // Bark!
```

Use category classes for type-safe extensions:

```groovy
@Category(String)
class StringExtensions {
    String shout() {
        this.toUpperCase() + "!"
    }
    String repeat(int times) {
        this * times
    }
}

use(StringExtensions) {
    println "hello".shout()
    println "ha".repeat(3)
}
```

## Common Mistakes

- Adding method to wrong class metaclass. Verify the target class before adding methods.
- Not using delegate in metaclass closures. The delegate refers to the object the method is called on.
- Assuming metaclass changes are thread-safe. Use synchronization for concurrent access.
- Forgetting that metaclass changes affect all instances of the class.
- Not using @CompileStatic compatible approaches when static compilation is required.
- Not cleaning up metaclass changes in tests. Use MetaClassCleanup or resetMetaClass.

## Related Pages

- [groovy-missing-method-v2]({{< relref "/languages/groovy/groovy-missingmethod-v2" >}}) - missing method
- [groovy-missing-property-v2]({{< relref "/languages/groovy/groovy-missingproperty-v2" >}}) - missing property
- [groovy-ast-error]({{< relref "/languages/groovy/groovy-asterror-v2" >}}) - AST transformation error
- [groovy-gstring-error]({{< relref "/languages/groovy/groovy-gstring-error" >}}) - GString interpolation
