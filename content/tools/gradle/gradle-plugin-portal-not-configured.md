---
title: "Gradle Plugin Portal Not Configured"
description: "Gradle cannot find a plugin because the Gradle Plugin Portal is not in the list of configured plugin repositories."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Gradle Plugin Portal Not Configured

Gradle resolves plugins from the Gradle Plugin Portal by default. This error occurs when the plugin portal is removed from the repository list or a custom `pluginManagement` block omits it.

## Common Causes

- The `pluginManagement.repositories` block does not include `gradlePluginPortal()`
- A custom repository contains the wrong plugin or an outdated version
- The `settings.gradle` plugin block references a plugin ID not published to the portal
- Network restrictions block access to the plugin portal

## How to Fix

1. Add the Gradle Plugin Portal to `pluginManagement`:

```groovy
// settings.gradle
pluginManagement {
    repositories {
        gradlePluginPortal()
        mavenCentral()
    }
}
```

2. Verify the plugin is published to the portal:

```bash
# Search for the plugin on https://plugins.gradle.org
# Check if the plugin ID matches exactly
```

3. Use a custom repository if the plugin is not on the portal:

```groovy
pluginManagement {
    repositories {
        maven {
            url 'https://maven.example.com/releases'
        }
        gradlePluginPortal()
    }
}
```

4. Check the build script for correct plugin ID:

```groovy
plugins {
    id 'com.example.my-plugin' version '1.0.0' // must match portal ID exactly
}
```

## Examples

```bash
# Error output
Could not resolve plugin 'com.example.my-plugin:com.example.my-plugin.gradle.plugin:1.0.0'
  > Could not find artifact in repository
```

```groovy
// Correct pluginManagement with fallback
pluginManagement {
    repositories {
        gradlePluginPortal()
        mavenCentral()
        maven {
            url 'https://repo.example.com/releases'
        }
    }
}
```

## Related Errors

- [Plugin Error]({{< relref "/tools/gradle/gradle-plugin-error" >}}) -- plugin configuration failures
- [Plugin Not Found]({{< relref "/tools/gradle/gradle-plugin-not-found-repository" >}}) -- plugin resolution failures
