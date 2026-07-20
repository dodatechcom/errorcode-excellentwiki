---
title: "[Solution] Scala SBTPluginError - Brief Description"
description: "Fix SBT plugin errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1062
---

An SBT plugin error occurs when plugins fail to load or resolve.

## Common Causes

- Plugin not found in repositories
- Version conflict between plugins
- Incompatible SBT version

## How to Fix

Check plugin compatibility:

```scala
// project/plugins.sbt
addSbtPlugin("org.scoverage" % "sbt-scoverage" % "2.0.9")
```

Resolve conflicts:

```scala
dependencyOverrides += "org.scala-sbt" %% "sbt" % "1.9.7"
```

## Examples

```scala
addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "2.1.5")
addSbtPlugin("org.scalameta" % "sbt-scalafmt" % "2.5.2")
```

## Related Errors

- [Scala SBTTaskError](/languages/scala/scala-sbt-task-error)
- [Scala ScaladocError](/languages/scala/scala-scaladoc-error)
