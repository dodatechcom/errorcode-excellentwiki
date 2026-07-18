---
title: "[Solution] Scala Dependency Injection Error — How to Fix"
description: "Fix Scala dependency injection errors. Learn how to resolve missing bindings, circular dependencies, and wiring issues in DI frameworks like MacWire and ZIO."
languages: ["scala"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

Scala dependency injection frameworks like MacWire, Purity, and ZIO Modules use compile-time or runtime mechanisms to wire dependencies together. When the wiring process cannot find a required dependency or encounters a conflict, it raises an error.

The most common cause is a missing implicit or given value for a required dependency. In MacWire, for example, `wire[T]` looks for implicit values in scope that match the constructor parameters of `T`. If any parameter cannot be satisfied, compilation fails.

Another frequent cause is circular dependencies. If service A depends on service B and service B depends on service A, neither can be instantiated first. Compile-time DI frameworks detect this at compile time, while runtime frameworks may fail with a stack overflow.

Ambiguous bindings occur when multiple implementations exist for the same dependency. If you have two different `Database` implementations and the DI framework cannot determine which one to use, it reports ambiguity.

Type mismatch in bindings is common when the actual type of a dependency does not match the type expected by the consumer. This happens when you define a dependency as a trait but the binding provides a concrete class without the correct type annotation.

Module boundary violations occur when a dependency from one module leaks into another, creating unexpected coupling. The DI framework may not be able to resolve dependencies that cross module boundaries without explicit configuration.

## Common Error Messages

```
Error: (line, col) could not find value for constructor parameter db: Database
```

```
Error: (line, col) circular dependency detected between UserService and AuthService
```

```
Error: (line, col) ambiguous implicit values: impl1 and impl2 both match type Repository
```

```
Error: (line, col) type mismatch; expected: Logger; found: ConsoleLogger
```

## How to Fix It

### Provide all required dependencies in scope

```scala
// MacWire example
import com.softwaremill.macwire._

trait Database {
  def query(sql: String): List[Map[String, Any]]
}

class MySqlDatabase extends Database {
  def query(sql: String): List[Map[String, Any]] = Nil
}

class UserRepository(db: Database) {
  def findAll(): List[Map[String, Any]] = db.query("SELECT * FROM users")
}

// Provide the dependency
val db: Database = new MySqlDatabase
val userRepo = wire[UserRepository] // Requires Database in scope
```

### Break circular dependencies with constructor injection

```scala
// Before — circular
class A(b: B)
class B(a: A)

// After — break the cycle
class A(bProvider: () => B)  // Lazy reference
class B(a: A)

val a = new A(() => b)
val b = new B(a)
```

### Disambiguate with named bindings

```scala
import com.softwaremill.macwire._

trait Cache
class RedisCache extends Cache
class MemcachedCache extends Cache

class UserService(cache: Cache)

// Use named vals to disambiguate
val redisCache: Cache = new RedisCache
val memcachedCache: Cache = new MemcachedCache

// Choose which one to inject
val userService = wireWith(UserService.apply _) // Uses redisCache
```

### Use module patterns for organization

```scala
trait DatabaseModule {
  def database: Database
}

trait CacheModule {
  def cache: Cache
}

class AppModule extends DatabaseModule with CacheModule {
  lazy val database: Database = new MySqlDatabase
  lazy val cache: Cache = new RedisCache
}

val app = new AppModule
// All dependencies resolved through module mixing
```

### ZIO dependency injection example

```scala
import zio._

case class UserService(repo: UserRepository) {
  def findUser(id: Int): UIO[Option[User]] = repo.findById(id)
}

object UserService {
  val live: URLayer[UserRepository, UserService] =
    ZLayer.fromFunction UserService.apply _
}

// Wiring
val program = for {
  service <- ZIO.service[UserService]
  user    <- service.findUser(1)
} yield user

program.provide(
  UserRepository.live,
  UserService.live,
  Database.live
)
```

## Common Scenarios

- Setting up a new project with compile-time DI and discovering missing dependency definitions
- Refactoring a service and breaking existing dependency wiring
- Working with a multi-module project where dependencies span module boundaries

## Prevent It

- Define dependencies in traits so the DI framework can verify type compatibility at compile time
- Use lazy evaluation for circular references and break cycles early in the design
- Organize dependencies into modules with clear boundaries and explicit exports
