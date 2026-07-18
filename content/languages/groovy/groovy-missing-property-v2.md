---
title: "[Solution] Groovy No Such Property Error"
description: "Fix Groovy MissingPropertyException when accessing undefined properties. Check property names and metaclass configuration."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `MissingPropertyException` occurs when Groovy cannot find a property with the given name on an object. This differs from MissingMethodException and often indicates typos, missing getter methods, or incorrect property access patterns.

## Why It Happens

- Typo in property name: The property name does not match any defined property.
- Property defined in superclass not visible: The property is private or protected in a parent class.
- Missing getter/setter for Java bean property: Groovy relies on getter/setter methods for property access on Java objects.
- Dynamic property access on map-based objects: The map key does not exist.
- Property accessed before object initialization: The object is not fully constructed.

## How to Fix It

Verify property exists before accessing using metaclass inspection:

```groovy
if (myObject.hasProperty("targetProp")) {
    def value = myObject.targetProp
} else {
    println "Property does not exist"
}
```

Use safe navigation for nullable objects:

```groovy
def result = myObject?.targetProp
// Returns null instead of MissingPropertyException
```

Add propertyMissing handler for dynamic properties:

```groovy
class DynamicBean {
    def props = [:]
    
    def propertyMissing(String name) {
        if (props.containsKey(name)) {
            props[name]
        } else {
            throw new MissingPropertyException(name, this.class)
        }
    }
    
    def propertyMissing(String name, value) {
        props[name] = value
    }
}
```

Check getter method existence for Java objects:

```groovy
def methods = myObject.getClass().methods*.name
if (methods.contains("getTargetProp")) {
    def value = myObject.getTargetProp()
} else if (methods.contains("isTargetProp")) {
    def value = myObject.isTargetProp()
}
```

Use Expando for dynamic property sets:

```groovy
def obj = new Expando()
obj.name = "Alice"
obj.age = 30
println obj.name
```

Use GStrings for dynamic property access:

```groovy
def propName = "name"
def value = object."${propName}"
```

Handle property access on maps:

```groovy
def map = [name: "Alice", age: 30]
def name = map.name  // Works
def missing = map.email  // Returns null
```

Use metaclass for property interception:

```groovy
MyClass.metaClass.getProperty = { String name ->
    if (name == "custom") {
        return "intercepted"
    }
    delegate.metaClass.getMetaProperty(name)?.getProperty(delegate)
}
```

## Common Mistakes

- Confusing property access with method calls. Property access uses getters/setters behind the scenes.
- Accessing static properties through instance. Use the class name instead.
- Not initializing object before property access. Ensure constructors complete before use.
- Using wrong capitalization in property names. Groovy properties are case-sensitive.
- Forgetting that Groovy generates getters/setters for properties in @CompileStatic mode differently.
- Not handling null returns from property access on optional properties.

## Related Pages

- [groovy-missing-method-v2]({{< relref "/languages/groovy/groovy-missingmethod-v2" >}}) - missing method
- [groovy-null-pointer-v2]({{< relref "/languages/groovy/groovy-nullpointererror-v2" >}}) - null pointer error
- [groovy-metaclass-error]({{< relref "/languages/groovy/groovy-metaclasserror-v2" >}}) - metaclass error
- [groovy-gstring-error]({{< relref "/languages/groovy/groovy-gstring-error" >}}) - GString interpolation
