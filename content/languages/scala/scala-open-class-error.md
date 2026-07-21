---
title: "[Solution] Scala Open Class Error"
description: "Fix Scala 3 open class errors when allowing extension for specific classes."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Open class errors occur when the open modifier is used incorrectly or when open classes have conflicting extensions.

## Common Causes

- Class not marked open but extended
- Open class with final members
- Open class name conflicting
- Missing open for inheritance

## How to Fix

### 1. Mark class as open

```scala
open class Container(val items: List[Int]) {
  def add(item: Int): Container = new Container(items :+ item)
}
```

### 2. Use open for library classes

```scala
open class BaseRepository[T](tableName: String) {
  def findAll(): List[T] = List.empty
}

class UserRepository extends BaseRepository[User]("users") {
  override def findAll(): List[User] = List(User("Alice"))
}
```

## Examples

```scala
open class Animal(val name: String) {
  def speak: String = "..."
}

class Dog(name: String) extends Animal(name) {
  override def speak: String = "Woof!"
}

class Cat(name: String) extends Animal(name) {
  override def speak: String = "Meow!"
}

val animals: List[Animal] = List(new Dog("Rex"), new Cat("Whiskers"))
animals.foreach(a => println(s"${a.name}: ${a.speak}"))
```

## Related Errors

- [Type error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
- [Trait parameter error](/languages/scala/scala-trait-parameter-error)
