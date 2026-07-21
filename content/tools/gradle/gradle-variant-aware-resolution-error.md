---
title: "Gradle Variant Selection Error"
description: "Gradle variant-aware dependency resolution fails because no matching variant is found for the consumer's requirements."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Gradle Variant Selection Error

Gradle uses variant-aware dependency resolution to select the best artifact for a consumer. A selection error occurs when no variant matches the consumer's requested attributes.

## Common Causes

- The producer does not expose a variant matching the requested `usage` attribute
- The producer variant has incompatible `org.gradle.category` attributes
- Custom attributes are misconfigured on the consumer or producer
- A metadata rule incorrectly modifies variant attributes

## How to Fix

1. Inspect available variants of the dependency:

```bash
./gradlew :app:dependencies --configuration runtimeClasspath
./gradlew :app:dependencyInsight --dependency com.example:library --configuration runtimeClasspath
```

2. Check variant attributes on the producer:

```groovy
// Producer build.gradle
javaLibrary {
    withVariantsFromConfiguration(configurations.runtimeElements) {
        attributes {
            attribute(Usage.USAGE_ATTRIBUTE, objects.named(Usage, Usage.JAVA_RUNTIME))
        }
    }
}
```

3. Match consumer attributes in the dependency declaration:

```groovy
dependencies {
    implementation('com.example:library') {
        attributes {
            attribute(Attribute.of('org.gradle.category', String), 'library')
        }
    }
}
```

4. Use dependency capabilities to resolve ambiguity:

```groovy
dependencies {
    implementation('com.example:library') {
        capabilities {
            requireCapability('com.example:library-impl')
        }
    }
}
```

## Examples

```bash
# Error output
Could not resolve com.example:library:1.0.0
  Cannot select variant with usage 'java-api' from variants
    - runtimeElements: java-runtime
    - apiElements: java-api
  No variant with attribute 'org.gradle.category' = 'library'
```

```groovy
// Producer exposing correct variants
javaLibrary {
    withVariantsFromConfiguration(configurations.apiElements) {
        attributes {
            attribute(Category.CATEGORY_ATTRIBUTE, objects.named(Category, Category.LIBRARY))
        }
    }
}
```

## Related Errors

- [Capability Conflict]({{< relref "/tools/gradle/gradle-capability-conflict" >}}) -- variant capability conflicts
- [Forced Dependency Conflict]({{< relref "/tools/gradle/gradle-forced-dependency-conflict" >}}) -- forced version conflicts
