---
title: "[Solution] Scala SBT Resolution Failed — Dependency Conflict Error"
description: "Fix SBT dependency resolution failures and conflicts. Learn about eviction, version overrides, and transitive dependency management."
languages: ["scala"]
error-types: ["build-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

An SBT resolution failure occurs when the dependency resolver cannot find a compatible version of a library or when transitive dependencies conflict. The error typically shows which dependencies are pulling in incompatible versions and which version was evicted.

## Why It Happens

The most common cause is two or more libraries depending on different major versions of the same transitive dependency. For example, if library A depends on `cats-core 2.9.0` and library B depends on `cats-core 3.0.0`, SBT cannot automatically resolve the conflict.

Another frequent cause is a missing artifact. If the library version does not exist in Maven Central or your configured repositories, resolution fails. This happens frequently after typos in version strings or when using snapshot versions that have been deleted.

Repository configuration issues also cause resolution failures. If a private repository is required but not configured, or if the resolver order causes conflicts, SBT cannot download the needed artifacts.

Version range specifications like `[1.0,2.0)` can cause unexpected resolutions. SBT resolves ranges by picking the latest version, which may not be compatible with your other dependencies.

Finally, cross-compilation suffix mismatches (e.g., looking for `_2.13` when only `_3` artifacts are published) cause resolution failures.

## How to Fix It

### Use dependencyOverrides to force a version

```scala
dependencyOverrides ++= Seq(
  "com.typesafe.akka" %% "akka-actor" % "2.8.0",
  "org.typelevel"     %% "cats-core"   % "2.10.0"
)
```

### Exclude transitive dependencies

```scala
libraryDependencies += "com.example" %% "lib" % "1.0" exclude("org.unwanted", "unwanted-lib")
```

### Use evictedWarnings to see what is being resolved

```scala
evictionWarningOptions in update := EvictionWarningOptions.default
  .withWarnTransitiveEvictions(true)
  .withWarnDirectEvictions(true)
```

### Pin versions with dependency locks

```scala
// In project/plugins.sbt
addSbtPlugin("com.github.sbt" % "sbt-pgp" % "2.2.1")

// Run dependencyLockWrite to create a lock file
// Run dependencyLockCheck to verify
```

### Check for cross-compilation issues

```scala
// Ensure you are using the correct Scala version suffix
libraryDependencies += "org.typelevel" %% "cats-core" % "2.10.0"
// For Scala 3: use %% not %%
```

## Common Mistakes

- Not checking `sbt update` output for eviction warnings
- Using `latest.integration` as a version, which is non-deterministic
- Not using `dependencyOverrides` when transitive conflicts are known
- Publishing artifacts with version ranges instead of exact versions
- Forgetting that `exclude` removes all transitive dependencies of that group

## Related Pages

- [Scala Macro Expansion Error](/languages/scala/scala-macro-error/)
- [Scala Implicit Not Found](/languages/scala/scala-implicit-not-found/)
- [Scala Play Framework Error](/languages/scala/scala-play-error/)
