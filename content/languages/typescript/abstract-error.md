---
title: "[Solution] TypeScript Cannot Instantiate Abstract Class — Abstract Class Usage Fix"
description: "Fix TypeScript 'Cannot instantiate abstract class' errors. Understand abstract classes, abstract methods, and proper instantiation patterns."
languages: ["typescript"]
severities: ["error"]
error-types: ["type-error"]
tags: ["abstract-class", "abstract-method", "instantiation", "polymorphism", "type-error"]
weight: 5
---

# TypeScript: Cannot instantiate abstract class

This error occurs when you try to use `new` to create an instance of an abstract class. Abstract classes are designed to be base classes that cannot be instantiated directly — they must be subclassed by a concrete class that implements all abstract methods.

## Common Causes

- **Directly instantiating an abstract class** — `new AbstractClass()` is not allowed
- **Missing abstract method implementations** — a subclass hasn't implemented all abstract methods
- **Confusing abstract class with interface** — trying to instantiate an abstract class like a concrete one
- **Factory function returning abstract type** — factory returns the abstract base type

## How to Fix

```typescript
// Cause 1: Direct instantiation of abstract class
abstract class Animal {
  abstract speak(): string;

  describe() {
    return `Animal: ${this.speak()}`;
  }
}

const a = new Animal();  // TS2511: Cannot create an instance of an abstract class

// Fix: create a concrete subclass
class Dog extends Animal {
  speak() {
    return "Woof!";
  }
}

const dog = new Dog();
console.log(dog.describe());  // "Animal: Woof!"

// Cause 2: Subclass missing abstract method
class Cat extends Animal {
  // TS2515: Non-abstract class 'Cat' does not implement all abstract members
}

// Fix: implement all abstract methods
class Cat extends Animal {
  speak() {
    return "Meow!";
  }
}
```

```typescript
// Example: Abstract class with multiple abstract methods
abstract class Shape {
  abstract area(): number;
  abstract perimeter(): number;

  describe() {
    return `Area: ${this.area()}, Perimeter: ${this.perimeter()}`;
  }
}

class Circle extends Shape {
  constructor(private radius: number) {
    super();
  }

  area() {
    return Math.PI * this.radius ** 2;
  }

  perimeter() {
    return 2 * Math.PI * this.radius;
  }
}

class Rectangle extends Shape {
  constructor(private width: number, private height: number) {
    super();
  }

  area() {
    return this.width * this.height;
  }

  perimeter() {
    return 2 * (this.width + this.height);
  }
}

function printShapeInfo(shape: Shape) {
  console.log(shape.describe());
}

printShapeInfo(new Circle(5));
printShapeInfo(new Rectangle(4, 6));
```

## Examples

```typescript
// Example 1: Abstract class as type (allowed)
abstract class Vehicle {
  abstract start(): void;
  abstract stop(): void;
}

// This is fine — using abstract class as a type annotation
function processVehicle(v: Vehicle) {
  v.start();
  v.stop();
}

// Example 2: Abstract class in factory pattern
abstract class Logger {
  abstract log(message: string): void;

  static create(type: "console" | "file"): Logger {
    if (type === "console") return new ConsoleLogger();
    return new FileLogger();
  }
}

class ConsoleLogger extends Logger {
  log(message: string) {
    console.log(message);
  }
}

class FileLogger extends Logger {
  log(message: string) {
    // write to file
  }
}

// Example 3: Abstract class with constructor
abstract class Repository<T> {
  protected items: T[] = [];

  abstract findById(id: number): T | undefined;

  add(item: T) {
    this.items.push(item);
  }

  getAll() {
    return [...this.items];
  }
}

class UserRepository extends Repository<{ id: number; name: string }> {
  findById(id: number) {
    return this.items.find(item => item.id === id);
  }
}
```

## Related Errors

- [TS2515: Non-abstract class does not implement abstract members]({{< relref "/languages/typescript/abstract-error" >}}) — missing implementation
- [TS2345: Argument type not assignable]({{< relref "/languages/typescript/ts2345" >}}) — abstract type passed where concrete expected
- [TS2322: Type not assignable]({{< relref "/languages/typescript/type-assignment" >}}) — abstract class assigned to concrete type
