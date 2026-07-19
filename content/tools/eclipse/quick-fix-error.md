---
title: "[Solution] Eclipse Quick fix error"
description: "Quick fix error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "eclipse"
tags: ["eclipse", "ide", "quick-fix", "correction", "assist"]
severity: "error"
---

# Quick fix error

## Error Message

```
No quick fixes available for the current selection. The problem at the cursor position does not have automated corrections.
```

## Common Causes

- The error or warning under the cursor is a type of issue that does not have an automated fix in JDT.
- The quick fix proposals engine is not loaded due to a corrupted plugin cache.
- The error is a compilation error that requires manual code changes rather than automated assistance.

## Solutions

### Solution 1: Navigate to the Problem First

Ensure the cursor is positioned exactly on the error marker (red wavy underline) in the editor. Click the lightbulb icon in the left margin or press **Ctrl+1** to open the quick fix proposals. If the cursor is not on the error, no proposals will be shown. Use the **Problems** view to double-click and navigate to each error.

```java
// Example: Quick fix for unhandled exception
// Cursor must be on the line with the error
public void readFile() throws IOException {
    // Place cursor on IOException error marker
    // Press Ctrl+1 to see quick fixes:
    // 1. Add throws declaration
    // 2. Surround with try/catch
}
```

### Solution 2: Use Source > Organize Imports

Many common quick fixes are related to missing imports. Instead of using quick fix, use **Source > Organize Imports (Ctrl+Shift+O)** to automatically add all missing imports. For static imports, use **Source > Add Static Import** and search for the method.

```bash
# Quick fix keyboard shortcuts
# Ctrl+1      - Quick Fix
# Ctrl+Shift+O - Organize Imports
# Ctrl+Shift+F - Format Code
# Ctrl+D      - Delete Line
```

## Prevention Tips

- Enable **Window > Preferences > Java > Editor > Hints** to see inline suggestions beyond errors.
- Some quick fixes support multiple proposals; use the arrow keys to cycle through them.
- You can create custom quick fix proposals using the JDT extension point API.

## Related Errors

- [compilation-error]({{< relref "/tools/eclipse/compilation-error" >}})
- [refactoring-error]({{< relref "/tools/eclipse/refactoring-error" >}})
- [content-assist-error]({{< relref "/tools/eclipse/content-assist-error" >}})
