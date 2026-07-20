---
title: "[Solution] Java cannot reference X before supertype constructor has been called — Fix Constructor Order"
description: "Fix Java compiler error 'cannot reference X before supertype constructor has been called' by avoiding subclass field usage in super constructors, or moving initialization to instance blocks. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 453
---

# Java Compiler Error: cannot reference X before supertype constructor has been called

This compile-time error occurs when you try to use a subclass field or method in a `this()` or `super()` constructor call, before the superclass constructor has completed. In Java, the superclass constructor must execute before the subclass can access `this` — the object is not fully initialized until all constructors in the chain have finished.

## Error Message

```
error: cannot reference this.name before supertype constructor has been called
        super(this.name);
            ^
```

Other variants:

```
error: cannot reference fieldName before supertype constructor has been called
error: cannot reference this before supertype constructor has been called
```

## Common Causes

### Cause 1: Passing Subclass Field to Super Constructor

```java
public class Animal {
    private String type;

    public Animal(String type) {
        this.type = type;
    }
}

public class Dog extends Animal {
    private String breed;

    public Dog(String breed) {
        super(this.breed); // ERROR: cannot reference this.breed before super()
        this.breed = breed;
    }
}
```

### Cause 2: Calling Subclass Method in Super Call

```java
public class Base {
    private int value;

    public Base(int value) {
        this.value = value;
    }
}

public class Child extends Base {
    public Child() {
        super(computeValue()); // ERROR: cannot reference computeValue() before super()
    }

    public static int computeValue() { return 42; }
}
```

### Cause 3: Using Subclass Field in this() Constructor Chain

```java
public class Parent {
    public Parent(String s) { }
}

public class Child extends Parent {
    private String name;

    public Child() {
        this(name); // ERROR: cannot reference name before super() is called
    }

    public Child(String name) {
        super(name);
        this.name = name;
    }
}
```

### Cause 4: Passing Subclass Field Through this() to super()

```java
public class Base {
    public Base(int x) { }
}

public class Derived extends Base {
    private int config;

    public Derived(int config) {
        this(config, 0); // OK — chaining to another constructor
    }

    public Derived(int config, int extra) {
        super(config + this.config); // ERROR: cannot reference this.config before super()
    }
}
```

## Solutions

### Fix 1: Compute Value Without Subclass Fields

```java
public class Dog extends Animal {
    private String breed;

    public Dog(String breed) {
        super(dogType(breed)); // compute without referencing this
        this.breed = breed;
    }

    private static String dogType(String breed) {
        return "dog:" + breed;
    }
}
```

### Fix 2: Move Subclass Initialization to Instance Block

```java
public class Base {
    private int x;

    public Base(int x) {
        this.x = x;
    }
}

public class Child extends Base {
    private int derived;

    {
        derived = computeDerived(); // initialized after super() completes
    }

    public Child() {
        super(10); // super() must be first statement
    }

    private int computeDerived() { return 42; }
}
```

### Fix 3: Use Static Method That Doesn't Need Instance State

```java
public class Base {
    public Base(int value) { }
}

public class Child extends Base {
    private String name;

    public Child(String name) {
        super(resolveValue(name)); // static method — no instance access
        this.name = name;
    }

    private static int resolveValue(String name) {
        return name != null ? name.length() : 0;
    }
}
```

### Fix 4: Pass Raw Values Only

```java
public class Animal {
    private final String type;

    public Animal(String type) {
        this.type = type;
    }
}

public class Dog extends Animal {
    private final String breed;

    public Dog(String breed) {
        super("dog"); // pass literal, not subclass field
        this.breed = breed;
    }
}
```

### Fix 5: Use Factory Method Instead

```java
public class Animal {
    protected String type;

    protected Animal() {}

    public static Animal create(String breed) {
        Animal a = new Dog();
        a.type = "dog:" + breed; // assign after construction
        return a;
    }
}
```

## Prevention Checklist

- Never pass subclass fields or methods to `super()` or `this()` constructor calls
- Use static methods or raw values when computing arguments for super constructor calls
- Defer subclass initialization to instance initializer blocks when it depends on the object being constructed
- Avoid `this()` constructor chains that reference uninitialized fields
- Use factory methods when constructor logic is complex
- Keep super constructor arguments simple and independent of subclass state

## Related Errors

- [non-static method cannot be referenced from a static context (non-static-method)](/languages/java/non-static-method)
- [variable X might not have been initialized (variable-not-init)](/languages/java/variable-not-init)
- [exception in initializer error (exceptionininitializererror)](/languages/java/exceptionininitializererror)
