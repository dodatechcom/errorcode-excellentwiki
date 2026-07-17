---
title: "Maven Could Not Transfer from Remote Repository"
description: "Maven fails to download artifacts from a remote repository."
tools: ["maven"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["maven", "repository", "transfer", "network", "remote"]
weight: 5
---

# Maven Could Not Transfer from Remote Repository

This error occurs when Maven cannot download artifacts from a remote repository due to network issues, authentication problems, or repository misconfiguration.

## Common Causes

- Network connectivity issues
- Repository URL is incorrect or down
- Proxy settings not configured
- SSL certificate issues
- Repository requires authentication

## How to Fix

### Check Repository Connectivity

```bash
curl -I https://repo.maven.apache.org/maven2/
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

### Skip SSL Verification (Temporary)

```bash
mvn clean install -Dmaven.wagon.http.ssl.insecure=true
```

### Add Repository with Authentication

```xml
<repositories>
    <repository>
        <id>private-repo</id>
        <url>https://repo.example.com/releases</url>
    </repository>
</repositories>
```

```xml
<!-- ~/.m2/settings.xml -->
<servers>
    <server>
        <id>private-repo</id>
        <username>${env.REPO_USER}</username>
        <password>${env.REPO_PASS}</password>
    </server>
</servers>
```

### Force Update Snapshots

```bash
mvn clean install -U
```

### Use Offline Mode for Local Cache

```bash
mvn clean install -o
```

## Examples

```text
[ERROR] Could not transfer artifact com.example:lib:jar:1.0.0
  from/to central (https://repo.maven.apache.org/maven2):
  Transfer failed for https://repo.maven.apache.org/...
  Connection timed out (ConnectException)
```

## Related Errors

- [Maven Dependency Error]({{< relref "/tools/maven/maven-dependency-error" >}}) — artifact not found
- [Maven Repository Error]({{< relref "/tools/maven/maven-repository-error" >}}) — repository connection failure
- [Maven Wrapper Error]({{< relref "/tools/maven/maven-wrapper-error" >}}) — wrapper download failure
