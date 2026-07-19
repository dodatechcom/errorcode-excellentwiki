---
title: "[Solution] Eclipse Code completion error"
description: "Code completion error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "eclipse"
tags: ["eclipse", "ide", "content-assist", "autocomplete", "jdt"]
severity: "error"
---

# Code completion error

## Error Message

```
Content assist not available. The Java content assist engine failed to initialize. Check the Error Log for details.
```

## Common Causes

- The JDT indexing process has not completed or has failed, preventing content assist from working.
- A large number of open projects or library dependencies has overwhelmed the content assist engine.
- A corrupted workspace metadata file is blocking the JDT indexer.

## Solutions

### Solution 1: Rebuild the Workspace Index

Go to **Project > Clean**, select **Clean all projects**, and click **OK**. This forces JDT to rebuild its indexes. After cleaning, wait for the **Building workspace** progress bar to complete before using content assist. You can also use **Ctrl+Space** to manually trigger content assist.

```java
# Verify JDT indexing is working
# Check the Progress view for "Building workspace" activity
# If stuck, try restarting Eclipse with:
eclipse -clean
```

### Solution 2: Configure Content Assist Settings

Navigate to **Window > Preferences > Java > Editor > Content Assist** and ensure **Enable auto activation** is checked. Set the auto activation delay to a lower value (e.g., 200ms). Also check **Window > Preferences > Java > Editor > Content Assist > Advanced** to enable all proposal categories.

```bash
# Key bindings for content assist
# Default: Ctrl+Space (trigger content assist)
# Ctrl+Shift+Space (parameter hints)
# Ctrl+1 (quick fix)
```

## Prevention Tips

- Close unused projects in the workspace to reduce the index size and speed up content assist.
- Check the **Error Log** view for JDT-related errors when content assist fails.
- Use **Window > Preferences > Java > Editor > Content Assist > Sort & Filter** to customize proposal order.

## Related Errors

- [jdt-error]({{< relref "/tools/eclipse/jdt-error" >}})
- [compilation-error]({{< relref "/tools/eclipse/compilation-error" >}})
- [outline-error]({{< relref "/tools/eclipse/outline-error" >}})
