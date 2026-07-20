---
title: "[Solution] Scala MacroParadiseError - Brief Description"
description: "Fix macro paradise errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1074
---

A macro paradise error occurs when macro annotations fail to expand.

## Common Causes

- Plugin not added to compiler
- Annotation not properly defined
- Version mismatch

## How to Fix

Add plugin:

```scala
addCompilerPlugin("org.scalamacros" % "paradise" % "2.1.1" cross CrossVersion.full)
```

Define annotations:

```scala
import scala.annotation.StaticAnnotation
import scala.language.experimental.macros
import scala.reflect.macros.whitebox

class myAnnotation extends StaticAnnotation {
  def macroTransform(annottees: Any*): Any = macro MyAnnotationMacro.impl
}
```

## Examples

```scala
@myAnnotation
def myMethod(): Unit = ()
```

## Related Errors

- [Scala MacroError](/languages/scala/scala-macro-error)
- [Scala SBTPluginError](/languages/scala/scala-sbt-plugin-error)
