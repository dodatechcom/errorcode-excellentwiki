---
title: "[Solution] Scala OutOfMemoryError — Java Heap Space Exhausted"
description: "Fix Scala OutOfMemoryError Java heap space. Learn about JVM memory limits, large collections, memory leaks, and heap tuning options."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

An `OutOfMemoryError` with the message "Java heap space" is thrown when the JVM cannot allocate more memory for object creation. The garbage collector has run but could not free enough memory to satisfy the allocation request. This is a fatal error that terminates the current thread or process.

## Why It Happens

The most common cause is processing large collections in memory without streaming. Loading an entire database table into a `List` or `Vector` before processing can easily exhaust the heap if the dataset is millions of rows.

Recursive functions that build up large intermediate data structures without tail-call optimization also cause this error. Each recursive call adds a new stack frame and the data it references grows the heap.

String concatenation in loops is another frequent culprit. Each concatenation creates a new `String` object, and the old ones remain in memory until garbage collected, leading to a buildup of short-lived objects.

Memory leaks from holding references to objects that are no longer needed prevent the garbage collector from reclaiming that memory. This is common when using global caches, static collections, or event listeners that are never removed.

Finally, the default JVM heap size may simply be too small for the application. The default maximum heap is often 256MB or 512MB, which is insufficient for data-intensive applications.

## How to Fix It

### Increase JVM heap size

```bash
# Set minimum and maximum heap size
java -Xms512m -Xmx4g -jar myapp.jar

# For SBT
SBT_OPTS="-Xmx4g" sbt run
```

### Use streaming instead of materializing collections

```scala
// Wrong — loads everything into memory
val results = dataSource.readAll().toList.filter(_.isValid).map(_.transform)

// Correct — streams through data
val results = dataSource.readAll().iterator.filter(_.isValid).map(_.transform)
```

### Use tail recursion for large iterations

```scala
import scala.annotation.tailrec

@tailrec
def sum(list: List[Int], acc: Int = 0): Int = list match {
  case Nil          => acc
  case head :: tail => sum(tail, acc + head)
}
```

### Use lazy collections and views

```scala
// Wrong — creates intermediate list at each step
val result = (1 to 10000000).map(_ * 2).filter(_ % 3 == 0).toList

// Correct — lazy evaluation avoids intermediate collections
val result = (1 to 10000000).view.map(_ * 2).filter(_ % 3 == 0).toList
```

### Process large files line by line

```scala
import scala.io.Source

// Wrong — loads entire file into memory
val lines = Source.fromFile("huge.txt").getLines().toList

// Correct — processes one line at a time
val source = Source.fromFile("huge.txt")
try {
  source.getLines().foreach { line =>
    process(line)
  }
} finally {
  source.close()
}
```

## Common Mistakes

- Using `.toList` on a large stream or database result set
- Building strings with `+` in a loop instead of `StringBuilder`
- Holding strong references in caches without eviction policies
- Using default heap size for production workloads
- Not closing resources like database connections or file handles

## Related Pages

- [Scala StackOverflowError](/languages/scala/stack-overflow3/)
- [Scala Implicit Not Found](/languages/scala/scala-implicit-not-found/)
- [Scala Option.get Error](/languages/scala/scala-option-get-error/)
