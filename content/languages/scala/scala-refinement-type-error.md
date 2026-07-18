---
title: "[Solution] Scala Refinement Type or Self-Type Error — How to Fix"
description: "Fix Scala refinement type and self-type errors. Learn how to properly use structural types, self-type annotations, and type refinements in Scala."
languages: ["scala"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

Refinement types in Scala allow you to narrow a type by adding constraints on its members. Self-type annotations specify the minimum requirements a trait must have when mixed into a class. Errors in either area usually stem from the type system's strict requirements about what members must be available.

The most common cause is a self-type annotation that references a type not available in the mixing class. If a trait declares `self: Database =>` and you try to mix it into a class that does not extend `Database`, the compiler rejects it.

Another frequent cause is structural type member access failures. When you use a refinement type like `Foo { def bar: Int }`, accessing `bar` requires reflection by default, which may fail at runtime or require specific compiler flags.

Refinement type constraints that are unsatisfiable cause compile errors. If you refine a type to require both `A with B` where `A` and `B` have conflicting member types, the compiler reports the conflict.

Circular self-type dependencies cause errors. If trait A has `self: B =>` and trait B has `self: A =>`, mixing them creates an impossible constraint.

Finally, abstract type members with conflicting bounds in refined types cause errors when the compiler cannot find a type that satisfies all constraints simultaneously.

## Common Error Messages

```
Error: (line, col) illegal cyclic inheritance involving trait HasDatabase
```

```
Error: (line, col) self-type App does not conform to trait Database's self-type Database
```

```
Error: (line, col) value foo is not a member of refinement type (Foo { def bar: Int })
```

```
Error: (line, col) type mismatch; expected: A with B; found: A
```

## How to Fix It

### Satisfy self-type requirements in mixing classes

```scala
trait Database {
  def connection: Connection
}

trait Repository {
  self: Database =>  // Requires Database to be mixed in
  
  def findAll(): List[Entity] = {
    val conn = connection // Works — Database is guaranteed
    conn.query("SELECT * FROM entities")
  }
}

class MyService extends Database with Repository {
  def connection: Connection = new Connection("jdbc:...")
}
```

### Remove circular self-type dependencies

```scala
// Before — circular dependency
trait A { self: B => }
trait B { self: A => }

// After — break the cycle with a common trait
trait Base
trait A { self: Base with B => }
trait B { self: Base => }
```

### Use structural types with proper reflection settings

```scala
import scala.language.reflectiveCalls

def process(obj: { def name: String; def age: Int }): String =
  s"${obj.name} is ${obj.age}"

// Enable reflective access for structural types
// scalac -language:reflectiveCalls
```

### Refine types with compatible constraints

```scala
trait Animal {
  def sound: String
}

trait Pet {
  def name: String
}

// Compatible refinement
type FriendlyAnimal = Animal with Pet { def friendly: Boolean }

class Dog extends Animal with Pet {
  def sound = "Woof"
  def name = "Rex"
  def friendly = true
}

val dog: FriendlyAnimal = new Dog
```

### Use path-dependent types with self-type

```scala
class App {
  class Config {
    val timeout: Int = 30
  }
  
  val config = new Config
  
  trait HasConfig {
    self: App =>
    def getTimeout: Int = self.config.timeout
  }
}
```

## Common Scenarios

- Building a trait-based architecture where traits depend on capabilities from the mixing class
- Using structural types to accept any object with specific methods without defining a formal interface
- Working with cake pattern or dependency injection patterns that rely on self-type annotations

## Prevent It

- Keep self-type hierarchies simple and avoid circular dependencies between traits
- Use formal traits instead of structural types when performance is critical
- Test that all classes mixing in self-typed traits provide the required capabilities
