---
title: "Maven Wrapper Error"
description: "Maven wrapper fails to download or execute the configured Maven distribution."
tools: ["maven"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

# Maven Wrapper Error

The Maven wrapper (`mvnw`) is a script that downloads and runs a specific Maven version. A wrapper error means the wrapper cannot download the distribution or execute Maven correctly.

## Common Causes

- Network issues preventing Maven distribution download
- Incorrect distribution URL in wrapper configuration
- Corrupted local Maven wrapper cache
- Permission issues on the wrapper script

## How to Fix

### Check Wrapper Configuration

```properties
# .mvn/wrapper/maven-wrapper.properties
distributionUrl=https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/3.9.5/apache-maven-3.9.5-bin.zip
```

### Regenerate Wrapper

```bash
mvn wrapper:wrapper -Dmaven=3.9.5
```

### Configure Proxy

```properties
# .mvn/jvm.config
-Dhttp.proxyHost=proxy.example.com -Dhttp.proxyPort=8080
-Dhttps.proxyHost=proxy.example.com -Dhttps.proxyPort=8080
```

### Download Manually

```bash
curl -L -o /tmp/maven.zip https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/3.9.5/apache-maven-3.9.5-bin.zip
unzip /tmp/maven.zip -d ~/.m2/wrapper/dists/
```

### Check Permissions

```bash
chmod +x mvnw
chmod +x .mvn/wrapper/maven-wrapper.jar
```

### Verify Network Access

```bash
curl -I https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/3.9.5/apache-maven-3.9.5-bin.zip
```

## Examples

```bash
./mvnw clean install
Exception in thread "main" java.io.FileNotFoundException:
https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/3.9.5/apache-maven-3.9.5-bin.zip
```

## Related Errors

- [Repository Error]({{< relref "/tools/maven/maven-repository-error" >}}) — repository connection failure
- [Version Error]({{< relref "/tools/maven/maven-version-error" >}}) — version mismatch
