---
title: "[Solution] Scala ScoverageError - Brief Description"
description: "Fix Scoverage coverage errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1070
---

An scoverage error occurs when code coverage instrumentation fails.

## Common Causes

- Scoverage version incompatible with Scala
- Exclusion annotations not working
- Coverage report not generating

## How to Fix

Configure in build.sbt:

```scala
coverageEnabled := true
coverageMinimumStmtTotal := 80
coverageFailOnMinimum := true
```

Exclude code:

```scala
coverageExcludedPackages := ".*Test.*;.*Spec.*"
```

## Examples

```scala
// sbt clean coverage test coverageReport
```

## Related Errors

- [Scala WartRemoverError](/languages/scala/scala-wartremover-error)
- [Scala ScalacheckError](/languages/scala/scala-scalacheck-error)
