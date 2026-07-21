---
title: "Build Scan Upload Failed"
description: "Gradle build scan upload failed because the Develocity or Gradle Enterprise server rejected the connection or the scan data."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Build Scan Upload Failed

Build scans provide a shared, web-based report of your Gradle build. An upload failure means the scan data was generated locally but could not be transmitted to the Develocity or Gradle Enterprise server.

## Common Causes

- The Develocity server URL is misconfigured or unreachable
- Authentication credentials are missing or expired
- The scan data exceeds the server size limit
- Network proxy settings block the upload connection
- The Develocity plugin version is outdated

## How to Fix

1. Verify the Develocity server URL in `settings.gradle`:

```groovy
// settings.gradle
plugins {
    id 'com.gradle.develocity' version '3.17'
}

develocity {
    server = 'https://develocity.example.com'
}
```

2. Check authentication credentials:

```bash
# Set access key via environment variable
export DEVELOCITY_ACCESS_KEY=develocity.example.com=access-key-id:secret

# Or configure in ~/.gradle/gradle.properties
develocity.accessKey=develocity.example.com=access-key-id:secret
```

3. Test connectivity to the server:

```bash
curl -I https://develocity.example.com
```

4. Configure proxy settings if behind a corporate network:

```bash
# In gradle.properties
systemProp.http.proxyHost=proxy.example.com
systemProp.http.proxyPort=8080
systemProp.https.proxyHost=proxy.example.com
systemProp.https.proxyPort=8080
```

5. Build with scan upload and debug logging:

```bash
./gradlew build --scan --info
```

## Examples

```bash
# Error output
 FAILURE: Build failed with an exception.
 * What went wrong:
 Failed to upload build scan to Develocity: Connection refused
```

```groovy
// Correct Develocity configuration
develocity {
    server = 'https://develocity.example.com'
    buildScan {
        publishAlways()
        termsOfServiceUrl = 'https://gradle.com/terms-of-service'
        termsOfServiceAgree = 'yes'
    }
}
```

## Related Errors

- [Develocity Plugin Error]({{< relref "/tools/gradle/gradle-develocity-plugin-error" >}}) -- plugin configuration issues
- [Build Scan Not Created]({{< relref "/tools/gradle/gradle-build-scan-not-created" >}}) -- scan generation failures
