---
title: "[Solution] Scala Abstract Type Needs to Be Instantiated"
description: "Fix Scala abstract type errors. Learn how to instantiate abstract types, use type members, and resolve abstract type constraints."
languages: ["scala"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

An "abstract type needs to be instantiated" compile error occurs when you try to use an abstract type member without providing a concrete type. The compiler knows the type exists in the class hierarchy but does not know what specific type it should be.

## Why It Happens

The most common cause is defining an abstract type member in a trait and then trying to create an instance of it without a concrete implementation. For example, a trait `Repository` with `type Entity` requires a subclass to specify what `Entity` actually is.

Another common cause is using a path-dependent type that has not been bound. When you declare `val repo: Repository`, the type `repo.Entity` is abstract until you provide a concrete implementation that specifies the type.

Type constraints that reference abstract types without refinement also cause this error. If a method signature requires `T#Id` and `T` is abstract, the compiler cannot verify that `T#Id` exists.

Implicit resolution failures involving abstract types are also frequent. When an implicit parameter requires a specific type member, the compiler may not be able to find it if the type is still abstract.

## How to Fix It

### Provide concrete type in extending class

```scala
trait Repository {
  type Entity
  def find(id: Long): Option[Entity]
}

class UserRepository extends Repository {
  type Entity = User
  def find(id: Long): Option[User] = ???
}
```

### Use type aliases for concrete binding

```scala
trait Config {
  type DB <: Database
  val db: DB
}

class PostgresConfig extends Config {
  type DB = PostgresDatabase
  val db: PostgresDatabase = new PostgresDatabase
}
```

### Refine types with structural refinement

```scala
trait Processor {
  type Input
  type Output
  def process(input: Input): Output
}

val processor: Processor { type Input = String; type Output = Int } = ???
```

### Use type parameters instead of type members

```scala
// With type members
trait Repository {
  type Entity
  def find(id: Long): Option[Entity]
}

// With type parameters — more explicit
trait Repository[E] {
  def find(id: Long): Option[E]
}
```

### Add context bounds for abstract type constraints

```scala
trait JsonCodec[T] {
  def encode(value: T): String
  def decode(json: String): T
}

def save[T: JsonCodec](entity: T): Unit = {
  val codec = implicitly[JsonCodec[T]]
  println(codec.encode(entity))
}
```

## Common Mistakes

- Forgetting that abstract type members must be specified in all concrete subclasses
- Confusing type members (`type Foo = Bar`) with type parameters (`class Foo[Bar]`)
- Not realizing that path-dependent types are different for each instance
- Assuming abstract types are resolved at the trait level rather than the concrete class
- Leaving type members abstract in classes that are instantiated directly

## Related Pages

- [Scala Type Mismatch](/languages/scala/scala-type-mismatch/)
- [Scala Variance Error](/languages/scala/scala-variance-error/)
- [Scala Implicit Not Found](/languages/scala/scala-implicit-not-found/)
