---
title: "Gradle Enterprise Server Error"
description: "Gradle build fails because the Gradle Enterprise or Develocity server returns an error or rejects the build data submission."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Gradle Enterprise Server Error

Gradle Enterprise provides build caching, build scans, and analytics. A server error occurs when the build cannot communicate with or receive a valid response from the Gradle Enterprise server.

## Common Causes

- The Gradle Enterprise server URL is incorrect or the server is down
- The server version is incompatible with the installed plugin version
- Authentication token or access key is invalid
- The server has reached its build scan storage limit

## How to Fix

1. Verify server availability:

```bash
curl -I https://gradle-enterprise.example.com
```

2. Check plugin and server version compatibility:

```groovy
// settings.gradle
plugins {
    id 'com.gradle.enterprise' version '3.16' // must match server version
}

gradleEnterprise {
    server = 'https://gradle-enterprise.example.com'
}
```

3. Validate authentication credentials:

```bash
export GRADLE_ENTERPRISE_ACCESS_KEY=gradle-enterprise.example.com=access-key-id:secret
```

4. Test the build with the server in offline mode:

```bash
./gradlew build -Dgradle.enterprise.buildscan.publish=false
```

## Examples

```bash
# Error output
Failed to send build scan to Gradle Enterprise: 
  Server returned HTTP 500 Internal Server Error
```

```groovy
// Gradle Enterprise configuration
gradleEnterprise {
    server = 'https://gradle-enterprise.example.com'
    buildScan {
        publishAlways()
        publishIf { !gradle.startParameter.taskNames.any { it.contains('test') } }
    }
}
```

## Related Errors

- [Build Scan Upload Failed]({{< relref "/tools/gradle/gradle-build-scan-upload-error" >}}) -- scan upload issues
- [Develocity Plugin Error]({{< relref "/tools/gradle/gradle-develocity-plugin-error" >}}) -- plugin configuration errors
