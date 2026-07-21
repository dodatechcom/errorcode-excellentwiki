---
title: "Maven Reactor Non-Sequential Build"
description: "Maven reactor build fails because modules are not in the correct build order or a module dependency is missing from the reactor."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Reactor Non-Sequential Build

The Maven reactor determines build order based on inter-module dependencies. A non-sequential error occurs when the reactor cannot find a valid build order for the declared modules.

## Common Causes

- A module depends on another module not included in the reactor
- Circular dependencies between modules break the build order
- A module's groupId or artifactId does not match the reactor
- The `-pl` option references a module not in the reactor

## How to Fix

1. List the reactor modules:

```bash
mvn validate -N
mvn validate --recursive
```

2. Verify all module dependencies are included:

```bash
mvn dependency:tree -pl app
```

3. Check for circular dependencies between modules:

```bash
mvn validate 2>&1 | grep -i "cycle\|circular"
```

4. Build specific modules with their dependencies:

```bash
mvn clean install -pl app -am  # -am includes dependencies
```

## Examples

```bash
# Error output
[ERROR] The reactor build order is non-sequential:
  [ERROR]   com.example:app:1.0-SNAPSHOT
  [ERROR]   com.example:core:1.0-SNAPSHOT (depends on :app)
  [ERROR]   :core cannot be built before :app
```

```bash
# Fix -- build with also-make to resolve order
mvn clean install -pl core -am
```

## Related Errors

- [Reactor Build Order]({{< relref "/tools/maven/maven-reactor-build-order" >}}) -- reactor ordering issues
- [Multi Module Reactor]({{< relref "/tools/maven/maven-multi-module-reactor" >}}) -- multi-module reactor
