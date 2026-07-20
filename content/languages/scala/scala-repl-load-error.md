---
title: "[Solution] Scala REPLLoadError - Brief Description"
description: "Fix REPL :load errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1064
---

A REPL :load error occurs when the Scala REPL cannot load a file.

## Common Causes

- File path with spaces or special characters
- Encoding issues
- Syntax that REPL cannot handle

## How to Fix

Use proper paths:

```scala
:load /path/to/file.scala
```

Use :paste mode:

```scala
:paste
// Paste or type code here
// Press Ctrl+D when done
```

## Examples

```scala
:paste mycode.scala
```

## Related Errors

- [Scala ScaladocError](/languages/scala/scala-scaladoc-error)
- [Scala SBTPluginError](/languages/scala/scala-sbt-plugin-error)
