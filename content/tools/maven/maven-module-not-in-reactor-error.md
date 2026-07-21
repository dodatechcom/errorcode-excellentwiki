---
title: "Maven Module Not In Reactor Error"
description: "Maven build command references a module using -pl that is not included in the reactor build, causing the build to fail."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Module Not In Reactor Error

The Maven reactor builds all modules declared in the parent POM. An error occurs when the `-pl` flag references a module not in the reactor or the module name is incorrect.

## Common Causes

- The module name in `-pl` does not match the `<module>` declaration
- The module was recently added but the build was not re-evaluated
- The module directory exists but is not listed in the parent POM
- A profile-activated module is not active in the current build

## How to Fix

1. List all reactor modules:

```bash
mvn validate -N
```

2. Use the correct module name:

```bash
# List modules first
mvn validate -N | grep "module"

# Then build the specific module
mvn clean install -pl my-module
```

3. Use `-am` to also build required dependencies:

```bash
mvn clean install -pl my-module -am
```

4. Verify the module is declared in the parent POM:

```xml
<modules>
  <module>my-module</module> <!-- must match directory name -->
</modules>
```

## Examples

```bash
# Error output
The project com.example:my-app:1.0-SNAPSHOT does not exist
  in the reactor: [com.example:core:1.0-SNAPSHOT, com.example:lib:1.0-SNAPSHOT]
```

```bash
# Correct build with reactor filtering
mvn clean install -pl core -am
mvn clean install -pl '!app' # exclude app
```

## Related Errors

- [Reactor Build Order]({{< relref "/tools/maven/maven-reactor-build-order" >}}) -- reactor ordering issues
- [Module Not Found]({{< relref "/tools/maven/maven-module-not-found" >}}) -- missing modules
