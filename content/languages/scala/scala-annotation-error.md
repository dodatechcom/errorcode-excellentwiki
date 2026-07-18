---
title: "[Solution] Scala Annotation Class Not Found — How to Fix"
description: "Fix Scala annotation class not found errors. Learn about annotation definitions, runtime retention, and how to import custom annotations correctly."
languages: ["scala"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

Scala annotations are applied to code elements like classes, methods, and fields to provide metadata to the compiler or runtime. When the compiler cannot find the annotation class you reference, it raises an "annotation class not found" error.

The most common cause is a missing import. Custom annotations live in specific packages and must be imported before use, just like any other class.

Another frequent cause is annotation retention policy mismatch. Annotations with `AnnotationRetention.Source` are only available at compile time and cannot be accessed via reflection at runtime. If you try to read such an annotation reflectively, the runtime cannot find it.

Version incompatibility between annotation libraries and the Scala compiler can cause annotations to become unresolvable. This happens especially with annotations from macro-based libraries that depend on specific compiler internals.

Annotation arguments that reference non-existent types or classes produce this error. If the annotation constructor expects a class reference and you pass a type that is not in scope, compilation fails.

Finally, annotations defined in a separate compilation unit that has not been compiled yet (such as a circular dependency) cause this error during incremental compilation.

## Common Error Messages

```
Error: (line, col) not found: type MyAnnotation
```

```
Error: (line, col) annotation class MyAnnotation is not found in classpath
```

```
Error: (line, col) class MyAnnotation needs to be a trait to be mixed in
```

```
Error: (line, col) attribute MyAnnotation is not applicable to type Method
```

## How to Fix It

### Import the annotation class explicitly

```scala
import scala.annotation.tailrec
import com.example.annotations.Validated

@Validated
def process(input: String): String = input.trim
```

### Define custom annotations with correct retention

```scala
import scala.annotation.StaticAnnotation

// Source-only annotation (compile time)
class JsonField(name: String) extends StaticAnnotation

// Runtime annotation (requires classfile retention)
import java.lang.annotation.{Retention, RetentionPolicy}
@Retention(RetentionPolicy.RUNTIME)
class MyRuntimeAnnotation extends scala.annotation.StaticAnnotation
```

### Check annotation target applicability

```scala
// Some annotations only apply to certain targets
@volatile var counter: Int = 0    // @volatile applies to vars only
@transient var cache: Map[String, Any] = Map.empty  // @transient applies to vars

// Custom annotation with target
import scala.annotation.meta._

class MyAnnotation extends scala.annotation.StaticAnnotation
// Use @target to restrict where it can be applied
```

### Ensure annotation dependencies are on the classpath

```scala
// In build.sbt, ensure the annotation library is a dependency
libraryDependencies += "org.example" %% "my-annotations" % "1.0.0"
```

### Handle annotation processing in macros correctly

```scala
import scala.quoted._

def myMacroImpl(annottees: Expr[Any])(using Quotes): Expr[Any] = {
  import quotes.reflect._
  val tree = annottees.asTerm
  // Process the annotated tree
  tree
}
```

## Common Scenarios

- Upgrading a library and discovering annotations from the old version are no longer in scope
- Using annotations defined in a different module that is not a dependency
- Attempting to read annotations at runtime that were defined with source-only retention

## Prevent It

- Always import annotation classes explicitly rather than relying on wildcard imports
- Verify annotation retention policy matches your usage (source vs. runtime)
- Include annotation library dependencies in all modules that reference them
