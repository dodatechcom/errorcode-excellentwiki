---
title: "Maven Wrapper Download Failed"
description: "Maven wrapper fails to download the required Maven distribution."
tools: ["maven"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["maven", "wrapper", "download", "distribution", "network"]
weight: 5
---

# Maven Wrapper Download Failed

This error occurs when the Maven wrapper cannot download the Maven distribution specified in `.mvn/wrapper/maven-wrapper.properties`. The wrapper ensures consistent Maven versions across builds.

## Common Causes

- Network connectivity issues or proxy blocking
- Distribution URL is incorrect or unreachable
- Disk space insufficient for download
- SSL certificate verification failure

## How to Fix

### Check Wrapper Properties

```properties
# .mvn/wrapper/maven-wrapper.properties
distributionUrl=https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/3.9.6/apache-maven-3.9.6-bin.zip
```

### Download Manually

```bash
curl -L -o /tmp/maven.zip https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/3.9.6/apache-maven-3.9.6-bin.zip
# Place in ~/.m2/wrapper/dists/
```

### Use Local Maven Installation

```bash
export M2_HOME=/usr/local/apache-maven-3.9.6
export PATH=$M2_HOME/bin:$PATH
mvn clean install
```

### Configure Proxy for Wrapper

```properties
# .mvn/jvm.config
-Dhttps.proxyHost=proxy.example.com
-Dhttps.proxyPort=8080
```

### Regenerate Wrapper

```bash
mvn wrapper:wrapper -Dmaven=3.9.6
```

### Skip Wrapper Validation

```bash
./mvnw clean install
# No skip option — fix the underlying network issue
```

## Examples

```text
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-wrapper-plugin:3.2.0:wrapper
  Error downloading Maven distribution:
  Connection timed out (ConnectException)
```

## Related Errors

- [Maven Repository Error]({{< relref "/tools/maven/maven-repository-error" >}}) — repository connection failure
- [Maven Build Error]({{< relref "/tools/maven/maven-build-error" >}}) — general build failure
- [Maven Compiler Error]({{< relref "/tools/maven/maven-compiler-error" >}}) — compiler configuration
