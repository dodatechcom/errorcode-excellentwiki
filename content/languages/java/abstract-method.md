---
title: "[Solution] Java X is abstract; cannot be instantiated — Fix Abstract Class / Interface"
description: "Fix Java compiler error 'X is abstract; cannot be instantiated' by using concrete implementations, factory methods, or anonymous classes. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 408
---

# Java Compiler Error: X is abstract; cannot be instantiated

This compile-time error occurs when you try to use `new` on an abstract class or interface. Abstract classes and interfaces cannot be instantiated directly — you must create a concrete subclass that implements all abstract methods.

## Error Message

```
error: Shape is abstract; cannot be instantiated
        Shape s = new Shape();
                   ^
```

Other variants:

```
error: Animal is abstract; cannot be instantiated
error: Comparable is abstract; cannot be instantiated
error: List is abstract; cannot be instantiated
```

## Common Causes

### Cause 1: Direct Instantiation of Abstract Class

```java
abstract class Shape {
    abstract double area();
}

public void example() {
    Shape s = new Shape(); // ERROR: Shape is abstract; cannot be instantiated
}
```

### Cause 2: Direct Instantiation of Interface

```java
public void example() {
    Runnable r = new Runnable(); // ERROR: Runnable is abstract; cannot be instantiated
}
```

### Cause 3: Instantiating a Class with Unimplemented Abstract Methods

A class is implicitly abstract if it has any abstract methods.

```java
abstract class Animal {
    abstract void speak();
    abstract void eat();
}

class Dog extends Animal {
    void speak() { System.out.println("Woof"); }
    void eat() { System.out.println("Eating kibble"); }
    // Missing: no abstract methods left — Dog is concrete, OK

class Cat extends Animal {
    void speak() { System.out.println("Meow"); }
    // Missing: eat() is not implemented — Cat is still abstract
}

public void example() {
    Cat c = new Cat(); // ERROR: Cat is abstract; cannot be instantiated
}
```

### Cause 4: Instantiating a Functional Interface Without Lambda

```java
public void example() {
    Comparator<String> comp = new Comparator<>(); // ERROR
}
```

### Cause 5: Abstract Class Used as Type

```java
abstract class Base {
    abstract void execute();
}

// This is fine — polymorphism
Base b = getConcreteImpl(); // OK if getConcreteImpl() returns a concrete subclass

// This is NOT fine
Base b2 = new Base(); // ERROR
```

## Solutions

### Fix 1: Create a Concrete Subclass

```java
abstract class Shape {
    abstract double area();
}

class Circle extends Shape {
    private double radius;

    Circle(double radius) { this.radius = radius; }

    double area() { return Math.PI * radius * radius; }
}

public void example() {
    Shape s = new Circle(5.0); // OK — Circle is concrete
}
```

### Fix 2: Use an Anonymous Class

```java
Runnable r = new Runnable() {
    @Override
    public void run() {
        System.out.println("Running");
    }
}; // OK
```

### Fix 3: Use a Lambda (for Functional Interfaces)

```java
Runnable r = () -> System.out.println("Running"); // OK
Comparator<String> comp = (a, b) -> a.compareTo(b); // OK
```

### Fix 4: Use a Factory Method

```java
abstract class Shape {
    abstract double area();

    public static Shape circle(double radius) {
        return new Circle(radius); // factory method returns concrete type
    }
}

public void example() {
    Shape s = Shape.circle(5.0); // OK
}
```

### Fix 5: Implement All Abstract Methods in Subclass

```java
abstract class Animal {
    abstract void speak();
    abstract void eat();
}

class Cat extends Animal {
    void speak() { System.out.println("Meow"); }
    void eat() { System.out.println("Eating fish"); }
}

public void example() {
    Animal a = new Cat(); // OK — Cat implements all abstract methods
}
```

## Prevention Checklist

- Never use `new` on an abstract class or interface — always instantiate a concrete subclass
- Ensure all abstract methods are implemented before creating instances
- Use factory methods to encapsulate concrete class creation
- Use lambda expressions for functional interfaces (single abstract method)
- Check for `abstract` keyword on the class/interface you're trying to instantiate
- Consider using dependency injection instead of direct instantiation

## Related Errors

- [cannot find symbol: method (method-not-found)](/languages/java/method-not-found)
- [non-static method cannot be referenced from a static context (non-static-method)](/languages/java/non-static-method)
- [method does not override or implement a method from a supertype (override-methods)](/languages/java/override-methods)
- [invalid method reference (invalid-method-reference)](/languages/java/invalid-method-reference)
