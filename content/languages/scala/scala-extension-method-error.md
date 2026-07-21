---
title: "[Solution] Scala Extension Method Error"
description: "Fix Scala 3 extension method errors when adding methods to existing types."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Extension method errors occur when extension methods have incorrect type parameters or when they conflict with existing methods.

## Common Causes

- Extension method name conflicts with existing method
- Wrong type parameter syntax
- Extension method not accessible from import
- Extension method on incompatible type

## How to Fix

### 1. Use correct extension syntax

```scala
extension (s: String) {
  def isPalindrome: Boolean = s == s.reverse
}

println("racecar".isPalindrome)  // true
```

### 2. Avoid name conflicts

```scala
extension [A](list: List[A]) {
  def second: Option[A] = list.lift(1)
}

val result = List(1, 2, 3).second  // Some(2)
```

## Examples

```scala
extension (n: Int) {
  def isEven: Boolean = n % 2 == 0
  def factorial: BigInt = (1 to n).map(BigInt(_)).product
}

println(5.isEven)    // false
println(5.factorial) // 120
```

## Related Errors

- [Type error](/languages/scala/scala-type-mismatch)
- [Implicit conversion error](/languages/scala/scala-implicit-conversion-error)
- [Compilation error](/languages/scala/scala-type-inference-error)
