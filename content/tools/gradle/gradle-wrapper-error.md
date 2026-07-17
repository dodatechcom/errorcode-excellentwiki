---
title: "Gradle Wrapper Download Failed"
description: "Gradle wrapper cannot download the specified Gradle distribution."
tools: ["gradle"]
error-types: ["build-error"]
severities: ["error"]
tags: ["gradle", "wrapper", "download", "distribution", "network"]
weight: 5
---

# Gradle Wrapper Download Failed

The Gradle wrapper (`gradlew`) attempts to download a specific Gradle distribution when it's not cached locally. A download failure means the wrapper cannot fetch the distribution from the configured URL.

## Common Causes

- Network connectivity issues
- Corporate firewall blocking the download URL
- Proxy configuration missing in Gradle wrapper properties
- Invalid or unavailable distribution URL

## How to Fix

### Check Wrapper Properties

```properties
# gradle/wrapper/gradle-wrapper.properties
distributionUrl=https\://services.gradle.org/distributions/gradle-8.4-bin.zip
```

### Configure Proxy

```properties
# gradle/wrapper/gradle-wrapper.properties
systemProp.http.proxyHost=proxy.example.com
systemProp.http.proxyPort=8080
systemProp.https.proxyHost=proxy.example.com
systemProp.https.proxyPort=8080
```

### Download Manually

```bash
curl -L -o /tmp/gradle.zip https://services.gradle.org/distributions/gradle-8.4-bin.zip
mkdir -p ~/.gradle/wrapper/dists/gradle-8.4-bin/
# Move zip to the appropriate directory
```

### Use Offline Installation

```bash
# Copy gradle-8.4-bin.zip to gradle/wrapper/dists/gradle-8.4-bin/<hash>/
```

### Verify Network Access

```bash
curl -I https://services.gradle.org/distributions/gradle-8.4-bin.zip
```

## Examples

```bash
./gradlew build
# Downloading https://services.gradle.org/distributions/gradle-8.4-bin.zip
# Exception in thread "main" java.io.FileNotFoundException: https://...
```

## Related Errors

- [Wrapper Error]({{< relref "/tools/gradle/gradle-wrapper-error" >}}) — wrapper configuration error
- [Daemon Error]({{< relref "/tools/gradle/gradle-daemon-error" >}}) — daemon startup failure
