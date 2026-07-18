---
title: "[Solution] Scala NoSuchElementException — Call on Empty Collection"
description: "Fix Scala NoSuchElementException when calling .head or .last on an empty collection. Use safe alternatives like Option and pattern matching."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `NoSuchElementException` is thrown when you call `.head`, `.last`, `.tail`, or `.init` on an empty collection. The error message reads "Next on empty iterator" or "empty.head". This is a runtime error that occurs because these methods have no valid return value for an empty collection.

## Why It Happens

The primary cause is calling `.head` or `.tail` on a collection that was expected to have elements but ended up empty. This frequently happens when filtering produces no results, when a database query returns an empty list, or when reading from a file yields no lines.

Another common scenario is calling `.next()` on an iterator that has been fully consumed. Once an iterator is exhausted, calling `.next()` again throws this error immediately.

Using `.find()` without checking the result can also lead to this issue. The `.find()` method returns an `Option`, and calling `.get` on `None` will not throw `NoSuchElementException` directly, but code that assumes `.find()` always returns a value will fail.

Finally, partitioning a collection and accessing the wrong half without verifying it is non-empty is a frequent source of this error in data processing pipelines.

## How to Fix It

### Use Option instead of .head

```scala
val list = List.empty[Int]
// Wrong: list.head throws NoSuchElementException
// Correct:
list.headOption match {
  case Some(value) => println(s"First: $value")
  case None        => println("Empty list")
}
```

### Check isEmpty before accessing elements

```scala
val items = getResults()
if (items.nonEmpty) {
  val first = items.head
  process(first)
}
```

### Use pattern matching on collections

```scala
val list = getResults()
list match {
  case head :: tail => println(s"First: $head, rest: $tail")
  case Nil          => println("Empty list")
}
```

### Use safe defaults with .headOption

```scala
val config = Map("timeout" -> "30")
val timeout = config.get("timeout").map(_.toInt).getOrElse(30)
```

### Handle empty iterators properly

```scala
val iter = getSource().iterator
while (iter.hasNext) {
  val item = iter.next()
  process(item)
}
```

## Common Mistakes

- Using `.head` without first checking `.nonEmpty`
- Assuming `.find()` always returns a `Some`
- Calling `.tail` on a single-element list without checking length
- Not handling empty results from database queries or API calls
- Using `.get` on an `Option` returned from `.headOption`

## Related Pages

- [Scala MatchError](/languages/scala/match-error/)
- [Scala ClassCastException](/languages/scala/class-cast/)
- [Scala NullPointerException](/languages/scala/null-pointer6/)
