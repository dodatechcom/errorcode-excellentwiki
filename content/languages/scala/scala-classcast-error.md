---
title: "[Solution] Scala ClassCastException — Invalid Type Cast in Pattern Match"
description: "Fix Scala ClassCastException during pattern matching and type casting. Learn safe casting with isInstanceOf, match types, and Option."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `ClassCastException` is thrown when you attempt to cast an object to a type that it is not an instance of. In Scala this commonly occurs during pattern matching with type patterns, when using `asInstanceOf`, or when Java interop returns a type that does not match expectations.

## Why It Happens

The most frequent cause is a type pattern match that assumes a runtime type which does not match the actual object. For example, matching `case s: String =>` on a value that is actually an `Int` will succeed in the compiler but fail at runtime with a `ClassCastException`.

Another common cause is generic type erasure. When you match on `List[String]`, the JVM runtime only sees `List`, so the type parameter check is skipped. This means a `List[Int]` will match `List[String]` at runtime, leading to a `ClassCastException` when you try to use the elements as strings.

Java interop is another source. If a Java library returns `Object` and you cast it to a specific type without checking, the cast can fail. This is especially common with collections from Java libraries.

Finally, using `asInstanceOf` for downcasting without a preceding `isInstanceOf` check will throw this error if the types are incompatible.

## How to Fix It

### Use pattern matching with type checks

```scala
def process(x: Any): String = x match {
  case s: String => s.toUpperCase
  case i: Int    => i.toString
  case _         => "unknown"
}
```

### Avoid generic type matching due to erasure

```scala
// Wrong — type erasure means this matches any List
def headString(list: List[_]): String = list match {
  case List(s: String) => s
  case _               => "not a string list"
}

// Correct — check element type at runtime
def headString(list: List[_]): Option[String] = list.headOption.collect {
  case s: String => s
}
```

### Use isInstanceOf before asInstanceOf

```scala
def safeCast[A](x: Any, tag: ClassTag[A]): Option[A] = {
  if (tag.runtimeClass.isInstance(x)) Some(x.asInstanceOf[A])
  else None
}
```

### Use ClassTag for generic type checks

```scala
import scala.reflect.ClassTag

def processItem[T: ClassTag](item: Any): Option[T] = item match {
  case t: T => Some(t)
  case _    => None
}
```

### Avoid asInstanceOf when possible

```scala
// Wrong
val s = obj.asInstanceOf[String]

// Correct
val s = obj match {
  case s: String => s
  case _         => throw new IllegalArgumentException(s"Expected String, got ${obj.getClass}")
}
```

## Common Mistakes

- Using `asInstanceOf` without first verifying the type with `isInstanceOf`
- Assuming generic type parameters are checked at runtime (type erasure)
- Matching on `List[String]` when the list may contain `Int` values
- Trusting Java return types without validation
- Casting between unrelated types in inheritance hierarchies

## Related Pages

- [Scala MatchError](/languages/scala/match-error/)
- [Scala Unsafe Cast](/languages/scala/scala-unsafe-cast/)
- [Scala Type Mismatch](/languages/scala/scala-type-mismatch/)
