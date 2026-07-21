---
title: "[Solution] Scala Import Selector Error"
description: "Fix Scala import selector errors when using rename, exclude, or wildcards in import statements."
languages: ["scala"]
error-types: ["syntax-error"]
severities: ["error"]
---

Import selector errors occur when import selectors have wrong syntax or when imported names conflict.

## Common Causes

- Wrong rename syntax in import
- Importing non-existent member
- Conflicting imports from different packages
- Wildcard import bringing unwanted names

## How to Fix

### 1. Use correct import selector syntax

```scala
import java.util.{ArrayList => JList, List => JList2}
import scala.collection.mutable.{ListBuffer => _, _}
```

### 2. Avoid conflicts

```scala
import java.util.Date
import java.sql.{Date => SqlDate}

val utilDate = new Date(0)
val sqlDate = new SqlDate(0)
```

## Examples

```scala
import scala.concurrent.{Future, Promise}
import scala.util.{Try, Success, Failure}
import scala.concurrent.ExecutionContext.Implicits.global

val f: Future[Int] = Future.successful(42)
f.onComplete {
  case Success(v) => println(s"Got: $v")
  case Failure(e) => println(s"Error: ${e.getMessage}")
}
```

## Related Errors

- [Import error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
- [Name collision error](/languages/scala/scala-type-inference-error)
