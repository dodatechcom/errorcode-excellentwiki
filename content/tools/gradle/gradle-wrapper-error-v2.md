---
title: "Gradle Wrapper Download Failed"
description: "Gradle wrapper fails to download the required Gradle distribution."
tools: ["gradle"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Gradle Wrapper Download Failed

This error occurs when the Gradle wrapper cannot download the Gradle distribution specified in `gradle-wrapper.properties`. The wrapper is responsible for ensuring the correct Gradle version is used.

## Common Causes

- Network connectivity issues or proxy blocking
- Distribution URL is incorrect or unreachable
- Disk space insufficient for download
- SSL certificate verification failure
- Corporate firewall blocking downloads

## How to Fix

### Check the Wrapper Properties

```properties
# gradle-wrapper.properties
distributionUrl=https\://services.gradle.org/distributions/gradle-8.5-bin.zip
distributionSha256Sum=abc123...
```

### Download Manually

```bash
# Download the distribution zip manually
curl -L -o gradle-8.5-bin.zip https://services.gradle.org/distributions/gradle-8.5-bin.zip
# Place in ~/.gradle/wrapper/dists/gradle-8.5-bin/<hash>/
```

### Skip Wrapper Validation

```bash
./gradlew build --no-wrapper-validation
```

### Use Local Gradle Installation

```bash
export GRADLE_HOME=/usr/local/gradle-8.5
export PATH=$GRADLE_HOME/bin:$PATH
gradle build
```

### Configure Proxy Settings

```properties
# gradle.properties
systemProp.http.proxyHost=proxy.example.com
systemProp.http.proxyPort=8080
systemProp.https.proxyHost=proxy.example.com
systemProp.https.proxyPort=8080
```

### Regenerate the Wrapper

```bash
gradle wrapper --gradle-version 8.5
```

## Examples

```text
Downloading https://services.gradle.org/distributions/gradle-8.5-bin.zip
Exception in thread "main" java.io.FileNotFoundException:
  https://services.gradle.org/distributions/gradle-8.5-bin.zip
```

## Related Errors

- [Gradle Version Error]({{< relref "/tools/gradle/gradle-version-error" >}}) — version compatibility issues
- [Gradle Cache Error]({{< relref "/tools/gradle/gradle-cache-error" >}}) — corrupted cache entries
- [Gradle Plugin Error]({{< relref "/tools/gradle/gradle-plugin-error" >}}) — plugin not found
