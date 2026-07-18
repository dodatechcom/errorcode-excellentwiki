---
title: "[Solution] Scala Macro Expansion Error — Compile-Time Macro Failure"
description: "Fix Scala macro expansion errors at compile time. Learn about macro annotations, whitebox/blackbox macros, and debugging macro code."
languages: ["scala"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A macro expansion error occurs when a Scala macro fails during compile-time expansion. The error message shows the macro name and the reason for failure, such as "macro expansion error" or "exception during macro expansion". These errors are compile-time errors that prevent the program from building.

## Why It Happens

The most common cause is a bug in the macro implementation itself. Macros run at compile time and have access to the compiler's type system, but errors in the macro code (such as pattern matching on tree nodes) produce confusing error messages.

Another frequent cause is invalid tree construction. When a macro generates code that violates the compiler's invariants (like creating a type that does not exist or using a symbol from a different universe), the expansion fails.

Version mismatches between the macro library and the Scala compiler version are common. Macros compiled with one compiler version may not work with another, especially between major Scala versions (2.13 vs 3.x).

Implicit resolution failures during macro expansion also cause this error. If the macro expects certain implicits to be available and they are not, the generated code will fail to compile.

Finally, macro annotation order matters. Some macros depend on other annotations being present, and if the order is wrong, the expansion may fail.

## How to Fix It

### Enable verbose macro logging

```bash
# Show macro expansion details
scalac -Ymacro-debug-lite myFile.scala
```

### Check Scala version compatibility

```scala
// In build.sbt
scalaVersion := "3.3.1" // Ensure macro library supports this version
libraryDependencies += "org.typelevel" %% "cats-core" % "2.10.0" cross CrossVersion.for3Use2_13
```

### Verify macro annotations are imported

```scala
import scala.annotation.tailrec // Not a macro, but similar pattern
import com.example.macros.myMacro
```

### Debug with quote matching

```scala
import scala.quoted._

def myMacroImpl(x: Expr[Int])(using Quotes): Expr[Int] = {
  println(s"Macro received: ${x.show}")
  x
}
```

### Use simpler macro implementations

```scala
// Instead of complex tree manipulation, use simpler approaches
inline def myMacro(x: Int): Int = ${ myMacroImpl('x) }

def myMacroImpl(x: Expr[Int])(using Quotes): Expr[Int] = x
```

## Common Mistakes

- Using macros when a simpler compile-time feature (like inline or extension methods) would work
- Not testing macros with different Scala compiler versions
- Assuming macros work across Scala 2 and Scala 3 without changes
- Forgetting that macros run at compile time, not runtime
- Not providing adequate error messages in macro-generated code

## Related Pages

- [Scala SBT Resolution Failed](/languages/scala/scala-sbt-error/)
- [Scala Type Mismatch](/languages/scala/scala-type-mismatch/)
- [Scala Implicit Not Found](/languages/scala/scala-implicit-not-found/)
