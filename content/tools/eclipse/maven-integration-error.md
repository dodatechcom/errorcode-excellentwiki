---
title: "[Solution] Eclipse Maven integration error"
description: "Maven integration error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "eclipse"
tags: ["eclipse", "ide", "maven", "m2e", "pom"]
severity: "error"
---

# Maven integration error

## Error Message

```
maven-error: Cannot resolve plugin org.apache.maven.plugins:maven-compiler-plugin:3.11.0 in context of project 'my-project'
```

## Common Causes

- The Maven repository is not accessible due to network issues or proxy misconfiguration.
- The `.m2/repository` cache contains corrupted or incomplete artifact downloads.
- The `pom.xml` references a plugin version that does not exist in the configured repositories.

## Solutions

### Solution 1: Force Maven Repository Update

Right-click the project in **Package Explorer**, select **Maven > Update Project**, check **Force Update of Snapshots/Releases**, and click **Run**. Alternatively, delete the corrupted artifact from your local repository and let Maven re-download it.

```java
# Force re-download a specific artifact
mvn dependency:purge-local-repository -DreResolve=true

# Or manually remove corrupted artifact
rm -rf ~/.m2/repository/org/apache/maven/plugins/maven-compiler-plugin/3.11.0/
```

### Solution 2: Configure Maven Settings for Eclipse

Open **Window > Preferences > Maven > User Settings** and verify the path to `settings.xml`. Ensure that repository mirrors and proxy settings are correctly configured for your corporate environment.

```bash
<!-- settings.xml - Configure proxy and mirrors -->
<settings>
  <proxies>
    <proxy>
      <id>corporate-proxy</id>
      <active>true</active>
      <protocol>https</protocol>
      <host>proxy.company.com</host>
      <port>8080</port>
    </proxy>
  </proxies>
</settings>
```

## Prevention Tips

- Use the embedded Maven that ships with Eclipse for best m2e compatibility.
- Run `mvn clean install -X` from the terminal to get verbose Maven output for debugging.
- Install the **m2e-wildlife** extension for improved Maven integration with newer Maven versions.

## Related Errors

- [build-path-error]({{< relref "/tools/eclipse/build-path-error" >}})
- [gradle-integration-error]({{< relref "/tools/eclipse/gradle-integration-error" >}})
- [compilation-error]({{< relref "/tools/eclipse/compilation-error" >}})
