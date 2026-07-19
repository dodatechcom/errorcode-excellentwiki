---
title: "[Solution] Eclipse Plugin installation failed"
description: "Plugin error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "eclipse"
tags: ["eclipse", "ide", "plugin", "marketplace", "installation"]
severity: "error"
---

# Plugin installation failed

## Error Message

```
An error occurred while collecting items to be installed. No repository found containing: org.eclipse.some.feature.group/2.3.1.v20230101
```

## Common Causes

- The update site URL is outdated or the plugin has been removed from the repository.
- A dependency conflict exists between the new plugin and already installed plugins.
- Network issues or proxy settings prevent Eclipse from reaching the update site.

## Solutions

### Solution 1: Use Eclipse Marketplace Instead

Open **Help > Eclipse Marketplace**, search for the desired plugin, and click **Install**. Marketplace resolves dependencies automatically and uses curated plugin metadata. If Marketplace fails, try the **Help > Install New Software** dialog with a verified update site URL.

```java
# Check available update sites in Eclipse configuration
cat ~/.eclipse/org.eclipse.platform_<version>/configuration/org.eclipse.equinox.simpleconfigurator/bundles.info
```

### Solution 2: Install via Command Line

Use the Eclipse command-line installer or the p2 director to install plugins headlessly, which bypasses the UI and gives you more detailed error output.

```bash
# Install plugin via p2 director
eclipse -application org.eclipse.equinox.p2.director \
  -repository https://download.eclipse.org/releases/latest/ \
  -installIU org.eclipse.some.feature.group/2.3.1.v20230101
```

## Prevention Tips

- Back up your Eclipse workspace before installing new plugins.
- Check plugin compatibility with your Eclipse version at the **Eclipse Marketplace** page.
- Run Eclipse with the `-clean` flag to clear the plugin cache if installation corruption is suspected.

## Related Errors

- [workspace-corruption]({{< relref "/tools/eclipse/workspace-corruption" >}})
- [gradle-integration-error]({{< relref "/tools/eclipse/gradle-integration-error" >}})
- [maven-integration-error]({{< relref "/tools/eclipse/maven-integration-error" >}})
