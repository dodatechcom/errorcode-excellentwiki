---
title: "[Solution] Scala Intersection Type Error"
description: "Fix Scala 3 intersection type errors when using & to combine multiple types."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Intersection type errors occur when intersection types combine incompatible traits or when the intersection is too restrictive.

## Common Causes

- Intersection of incompatible traits
- No common implementation for intersection
- Using intersection where union is needed
- Intersection type causing ambiguous implicits

## How to Fix

### 1. Ensure compatible traits

```scala
trait Readable {
  def read(): String
}
trait Writable {
  def write(data: String): Unit
}

type ReadWritable = Readable & Writable
```

### 2. Use intersection correctly

```scala
trait Logger {
  def log(msg: String): Unit
}
trait Formatter {
  def format(data: String): String
}

def process(data: String)(using logger: Logger & Formatter): Unit = {
  logger.log(logger.format(data))
}
```

## Examples

```scala
trait Named {
  def name: String
}
trait Aged {
  def age: Int
}

type Person = Named & Aged

class Employee(val name: String, val age: Int) extends Named with Aged

def greet(p: Person): Unit = println(s"Hello ${p.name}, age ${p.age}")
greet(new Employee("Alice", 30))
```

## Related Errors

- [Type error](/languages/scala/scala-type-mismatch)
- [Implicit ambiguity error](/languages/scala/scala-implicits-ambiguity)
- [Compilation error](/languages/scala/scala-type-inference-error)
