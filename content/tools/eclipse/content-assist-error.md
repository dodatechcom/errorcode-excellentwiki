---
title: "[Solution] Eclipse Content assist error"
description: "Content assist error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "eclipse"
tags: ["eclipse", "ide", "content-assist", "proposals", "completion"]
severity: "error"
---

# Content assist error

## Error Message

```
An internal error occurred during code completion. java.lang.NullPointerException at org.eclipse.jdt.internal.codeassist.InternalCompletionProposal...
```

## Common Causes

- A JDT bug causes a NullPointerException when processing completion proposals in certain code patterns.
- The source file contains syntactically incomplete code that confuses the completion engine.
- A corrupted JDT cache is causing the content assist engine to return invalid proposals.

## Solutions

### Solution 1: Clean and Rebuild the Project

Go to **Project > Clean** and clean all projects. Then close and reopen the source file where content assist fails. If the issue persists, close all projects and reopen them one at a time to isolate the problem. Check the **Error Log** view for detailed stack traces.

```java
# Check Eclipse error log for content assist exceptions
# Navigate to: <workspace>/.metadata/.log
# Search for "codeassist" or "CompletionProposal" errors

# Example log entry:
# !ENTRY org.eclipse.jdt.core 4 0 2026-07-15 10:30:00
# !MESSAGE java.lang.NullPointerException
#   at org.eclipse.jdt.internal.codeassist.InternalCompletionProposal
```

### Solution 2: Adjust Content Assist Settings

Open **Window > Preferences > Java > Editor > Content Assist** and adjust the settings to reduce the scope of completion proposals. Disable **Insert common prefixes automatically** and reduce the **Auto activation delay** to minimize the impact of the bug on daily workflow.

```bash
# Preferences path for content assist tuning
# Window > Preferences > Java > Editor > Content Assist
#   Auto activation delay: 200ms
#   Auto activation triggers for Java: .abcdefghijklmnopqrstuvwxyz
# Window > Preferences > Java > Editor > Content Assist > Advanced
#   Disable unnecessary proposal categories
```

## Prevention Tips

- File a bug report at bugs.eclipse.org if the NullPointerException is reproducible.
- As a workaround, type a few characters of the class name before triggering content assist.
- Disable third-party content assist plugins to check if they conflict with JDT proposals.

## Related Errors

- [code-completion-error]({{< relref "/tools/eclipse/code-completion-error" >}})
- [jdt-error]({{< relref "/tools/eclipse/jdt-error" >}})
- [quick-fix-error]({{< relref "/tools/eclipse/quick-fix-error" >}})
