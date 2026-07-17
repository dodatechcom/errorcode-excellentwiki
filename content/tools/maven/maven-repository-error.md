---
title: "Maven Repository Connection Error"
description: "Maven cannot connect to a configured repository due to network or authentication issues."
tools: ["maven"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

# Maven Repository Connection Error

A Maven repository connection error occurs when Maven cannot reach a configured repository. This can be caused by network issues, incorrect URLs, firewall restrictions, or authentication failures.

## Common Causes

- Network connectivity issues
- Incorrect repository URL in `pom.xml` or `settings.xml`
- Corporate firewall blocking repository access
- Repository requires authentication but credentials are missing
- SSL certificate issues

## How to Fix

### Test Repository Connectivity

```bash
curl -I https://repo.maven.apache.org/maven2/
```

### Check Repository Configuration

```xml
<repositories>
    <repository>
        <id>central</id>
        <url>https://repo.maven.apache.org/maven2</url>
    </repository>
</repositories>
```

### Configure Proxy Settings

```xml
<!-- ~/.m2/settings.xml -->
<proxies>
    <proxy>
        <id>http-proxy</id>
        <active>true</active>
        <protocol>http</protocol>
        <host>proxy.example.com</host>
        <port>8080</port>
    </proxy>
</proxies>
```

### Configure Authentication

```xml
<servers>
    <server>
        <id>private-repo</id>
        <username>your-username</username>
        <password>your-password</password>
    </server>
</servers>
```

### Check SSL Certificate

```bash
# If using internal CA
mvn clean install -Dmaven.wagon.http.ssl.insecure=true
```

### Use Offline Mode After Initial Download

```bash
mvn clean install -o
```

## Examples

```bash
mvn clean install
[ERROR] Could not transfer artifact from/to central:
Failed to transfer https://repo.maven.apache.org/maven2/
ConnectException: Connection refused
```

## Related Errors

- [Dependency Error]({{< relref "/tools/maven/maven-dependency-error" >}}) — artifact not found
- [Build Failed]({{< relref "/tools/maven/maven-build-error" >}}) — general build failure
