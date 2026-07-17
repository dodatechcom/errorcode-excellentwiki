---
title: "[Solution] Scala OutOfMemoryError"
description: "Fix Scala OutOfMemoryError when JVM heap is exhausted. Learn memory management, streaming, and GC tuning."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["out-of-memory", "heap", "memory", "gc", "jvm", "scala"]
weight: 5
---

## What This Error Means

An `OutOfMemoryError` occurs when the JVM cannot allocate more memory because the heap is full. This happens when processing large datasets or holding too many objects in memory.

## Common Causes

- Loading entire large dataset into memory
- Memory leaks (retained references)
- Infinite recursion building stack frames
- Large collection operations (e.g., `groupBy` on large data)
- JVM heap size too small

## How to Fix

```scala
// WRONG: Loading everything into memory
val largeFile = Source.fromFile("huge.csv").getLines().toList  // OOM

// CORRECT: Process line by line
val source = Source.fromFile("huge.csv")
try {
  source.getLines().foreach { line =>
    processLine(line)
  }
} finally {
  source.close()
}
```

```scala
// WRONG: Building large intermediate collections
val result = (1 to 10000000).map(_ * 2).filter(_ > 100).toList

// CORRECT: Use views (lazy collections)
val result = (1 to 10000000).view.map(_ * 2).filter(_ > 100).toList

// Or use iterators
val result = Iterator.from(1).map(_ * 2).filter(_ > 100).take(1000).toList
```

```scala
// WRONG: Not increasing heap for large jobs
// java -cp app.jar MainClass

// CORRECT: Increase JVM heap
// java -Xmx4g -Xms2g -cp app.jar MainClass
// Or in build.sbt:
// javaOptions += "-Xmx4g"
```

```scala
// WRONG: Grouping large dataset into memory
val grouped = hugeDataset.groupBy(_.category)  // May OOM

// CORRECT: Use Spark or streaming for big data
import org.apache.spark.sql.SparkSession
val spark = SparkSession.builder().getOrCreate()
val df = spark.read.csv("huge.csv")
```

## Examples

```scala
// Example 1: Monitor memory usage
def withMemoryLogging[T](name: String)(f: => T): T = {
  val rt = Runtime.getRuntime
  val before = rt.totalMemory() - rt.freeMemory()
  val result = f
  val after = rt.totalMemory() - rt.freeMemory()
  println(s"$name used ${(after - before) / 1024} KB")
  result
}

// Example 2: Streaming processing
import scala.io.Source
Source.fromFile("big.csv")
  .getLines()
  .sliding(1000)  // Process in batches of 1000
  .foreach(processBatch)

// Example 3: Lazy evaluation
lazy val hugeComputation = {
  (1 to 10000000).map(computeExpensive).toList
}
// Only computed when accessed
```

## Related Errors

- [scala-stackoverflow]({{< relref "/languages/scala/scala-stackoverflow" >}}) — stack overflow in recursion
- [scala-nullpointer]({{< relref "/languages/scala/scala-nullpointer" >}}) — null pointer
- [scala-matcherror]({{< relref "/languages/scala/scala-matcherror" >}}) — pattern match failed
