---
title: "[Solution] Java anonymous class cannot extend another class — Fix Anonymous Class Limitation"
description: "Fix Java compiler error anonymous class cannot extend another class by using named classes, implementing interfaces only, or using lambdas for functional interfaces. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 136
---

# Java Compiler Error: anonymous class cannot extend another class

This compile-time error occurs when an anonymous class attempts to both extend a class and implement an interface. In Java, an anonymous class can extend one class OR implement one interface, but not both simultaneously.

## Error Message

```
error: class MyInterface is not abstract and does not override abstract method method() in MyClass
error: anonymous class cannot extend another class: MyClass
```

## Common Causes

### Cause 1: Extending Class While Implementing Interface

```java
interface Greeting {
    void greet();
}

class BaseGreeting {
    public void greet() { System.out.println("Hello"); }
}

public class Example {
    public static void main(String[] args) {
        Greeting g = new BaseGreeting() implements Greeting { };
        // Error: cannot extend class and implement interface in anonymous class
    }
}
```

### Cause 2: Extending Class With Interface in New Expression

```java
interface Printable {
    void print();
}

class Document {
    public void print() { System.out.println("Printing"); }
}

public class Example {
    public static void main(String[] args) {
        Printable p = new Document() { } as Printable; // Invalid syntax
    }
}
```

### Cause 3: Trying to Implement Multiple Interfaces

```java
interface A { void methodA(); }
interface B { void methodB(); }

public class Example {
    public static void main(String[] args) {
        A a = new Object() implements A, B { };
        // Error: anonymous class can only implement one interface
    }
}
```

### Cause 4: Anonymous Class With Abstract Class and Interface

```java
interface Serializable2 { }

abstract class AbstractShape { abstract double area(); }

public class Example {
    public static void main(String[] args) {
        Object shape = new AbstractShape() implements Serializable2 { };
        // Error: cannot extend abstract class and implement interface
    }
}
```

## Solutions

### Fix 1: Use a Named Class

```java
interface Greeting {
    void greet();
}

class BaseGreeting {
    public void greet() { System.out.println("Hello"); }
}

class CombinedGreeting extends BaseGreeting implements Greeting {
    // Named class can extend and implement
}

public class Example {
    public static void main(String[] args) {
        Greeting g = new CombinedGreeting();
        g.greet();
    }
}
```

### Fix 2: Implement Only the Interface

```java
interface Greeting {
    void greet();
}

public class Example {
    public static void main(String[] args) {
        Greeting g = new Greeting() {
            @Override
            public void greet() {
                System.out.println("Hello");
            }
        };
        g.greet();
    }
}
```

### Fix 3: Use a Lambda for Functional Interface

```java
@FunctionalInterface
interface Greeting {
    void greet();
}

public class Example {
    public static void main(String[] args) {
        Greeting g = () -> System.out.println("Hello"); // Lambda expression
        g.greet();
    }
}
```

### Fix 4: Use Composition Instead of Inheritance

```java
interface Greeting {
    void greet();
}

class BaseGreeting {
    public void baseGreet() { System.out.println("Hello"); }
}

public class Example {
    public static void main(String[] args) {
        BaseGreeting base = new BaseGreeting();
        Greeting g = base::baseGreet; // Method reference
        g.greet();
    }
}
```

### Fix 5: Create Separate Named Inner Class

```java
interface Greeting {
    void greet();
}

class BaseGreeting {
    public void greet() { System.out.println("Hello from base"); }
}

public class Example {
    class CombinedGreeting extends BaseGreeting implements Greeting { }

    public static void main(String[] args) {
        Example ex = new Example();
        Greeting g = ex.new CombinedGreeting();
        g.greet();
    }
}
```

## Prevention Checklist

- Anonymous classes can only extend one class or implement one interface
- Use named classes when you need both extension and implementation
- Prefer lambdas for functional interfaces (single abstract method)
- Use composition over inheritance when combining behaviors
- Consider creating named inner classes for complex anonymous class needs
- Use method references when bridging between classes and interfaces

## Related Errors

- [interface-expected](/languages/java/interface-expected/)
- [override-methods](/languages/java/override-methods/)
- [abstract-method-in-abstract-class](/languages/java/abstract-method-in-abstract-class/)
