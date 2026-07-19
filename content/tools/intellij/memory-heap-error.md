---
title: "[Solution] IntelliJ IDEA OutOfMemoryError: Java heap space"
description: "Fix IntelliJ IDEA OutOfMemoryError Java heap space. Increase JVM heap allocation and optimize IDE memory usage."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "memory", "jvm", "performance", "heap"]
severity: "error"
---

# OutOfMemoryError: Java heap space

## Error Message

```
java.lang.OutOfMemoryError: Java heap space
Increase heap size via Help → Change Memory Settings
or edit vmoptions file manually.

java.lang.OutOfMemoryError: GC overhead limit exceeded
```

## Common Causes

- Default heap allocation is insufficient for the project size
- Too many plugins consuming IDE memory
- Large file operations or indexing on massive codebases
- Memory leak in a third-party plugin
- Insufficient system RAM for IDE + build processes

## Solutions

### Solution 1: Increase IDE Heap Size via Settings

Navigate to **Help → Change Memory Settings** and increase the heap allocation. For large projects, 4096 MB or higher is recommended.

```
Help → Change Memory Settings
# Set Maximum Heap Size to 4096 MB or higher
# Click 'Save and Restart'
```

### Solution 2: Edit VM Options File Directly

Modify the IDE's vmoptions file for more granular memory control.

```bash
# Find vmoptions file:
# Help → Edit Custom VM Options
# Or manually locate:
# Linux: ~/.config/JetBrains/IntelliJIdea<version>/idea64.vmoptions
# macOS: ~/Library/Application Support/JetBrains/IntelliJIdea<version>/idea64.vmoptions
# Windows: C:\Users\<user>\AppData\Roaming\JetBrains\IntelliJIdea<version>\idea64.vmoptions

# Recommended settings:
-Xms2048m
-Xmx8192m
-XX:ReservedCodeCacheSize=2048m
-XX:+UseG1GC
```

### Solution 3: Disable Unnecessary Plugins

Reduce memory usage by disabling plugins you do not actively use.

```
File → Settings → Plugins → Installed
# Disable plugins you don't need:
#   - Plugins for languages you don't use
#   - Unused tool integrations
#   - Redundant code inspection plugins
# Each disabled plugin frees memory resources
```

### Solution 4: Analyze IDE Memory Usage

Use the built-in memory indicator to monitor IDE heap consumption in real-time.

```
# Enable memory indicator:
# View → Appearance → Status Bar Widgets → Memory Indicator
# The indicator shows current/maximum heap usage
# Click it to trigger garbage collection manually

# For detailed analysis:
# Help → Diagnostic Tools → Memory Indicator
```

## Prevention Tips

- Set -Xmx to no more than 75% of available system RAM
- Enable the memory indicator in the status bar for real-time monitoring
- Use Help → Collect Memory and Diagnostic Info for profiling large heap dumps
- Consider splitting very large monorepos into smaller modules

## Related Errors

- [Indexing Error]({{< relref "/tools/intellij/indexing-error" >}})
- [Compilation Failed]({{< relref "/tools/intellij/compilation-error" >}})
- [Terminal Error]({{< relref "/tools/intellij/terminal-error" >}})
