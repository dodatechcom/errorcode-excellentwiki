---
title: "[Solution] Scala Varargs Error"
description: "Fix Scala varargs (*:Seq) syntax errors when passing variable number of arguments."
languages: ["scala"]
error-types: ["syntax-error"]
severities: ["error"]
---

Varargs errors occur when the * syntax is used incorrectly or when converting between Seq and varargs.

## Common Causes

- Wrong syntax for varargs expansion
- Missing * for unpacking Seq to varargs
- Converting varargs to Seq incorrectly
- Varargs with wrong type

## How to Fix

### 1. Use :* for varargs expansion

```scala
def sum(nums: Int*): Int = nums.sum

val list = List(1, 2, 3)
val total = sum(list: _*)  // expand list as varargs
```

### 2. Create Seq from varargs

```scala
val nums: Seq[Int] = Seq(1, 2, 3)  // or
val nums2 = Seq(1, 2, 3: _*)  // same
```

## Examples

```scala
def greet(names: String*): Unit = {
  names.foreach(name => println(s"Hello, $name!"))
}

val people = List("Alice", "Bob", "Charlie")
greet(people: _*)

greet("Dave", "Eve")
```

## Related Errors

- [Type error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
- [Match error](/languages/scala/scala-match-error)
