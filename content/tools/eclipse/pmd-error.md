---
title: "[Solution] Eclipse PMD error"
description: "PMD error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "eclipse"
tags: ["eclipse", "ide", "pmd", "static-analysis", "code-quality"]
severity: "error"
---

# PMD error

## Error Message

```
PMD Rule Violation: UnusedLocalVariable - Avoid unused local variables. Found: unusedVar in method process() at line 23 of MyClass.java
```

## Common Causes

- The code contains local variables that are declared but never used, triggering a PMD rule.
- The PMD ruleset is too strict for the project's coding standards.
- A refactoring left behind dead code that was not cleaned up.

## Solutions

### Solution 1: Install and Configure PMD Plugin

Install the **PMD Eclipse Plugin** from **Help > Eclipse Marketplace**. After installation, configure the ruleset via **Window > Preferences > PMD**. You can enable or disable individual rules and set the severity level for each rule category.

```java
// Before: unused variable triggers PMD violation
public void process(String input) {
    String unusedVar = "not needed";  // PMD: UnusedLocalVariable
    String result = input.trim();
    System.out.println(result);
}

// After: remove the unused variable
public void process(String input) {
    String result = input.trim();
    System.out.println(result);
}
```

### Solution 2: Run PMD from the Command Line

Run PMD directly from the command line to get detailed violation reports that you can cross-reference with the Eclipse violations. This is useful for CI integration and verifying that the Eclipse plugin matches the build pipeline.

```bash
# Run PMD from command line
pmd check -d src/main/java/ \
  -R rulesets/java/quickstart.xml \
  -f text \
  -language java

# Generate HTML report
pmd check -d src/main/java/ \
  -R rulesets/java/quickstart.xml \
  -f html \
  -R report.html
```

## Prevention Tips

- Right-click a PMD violation in the **Problems** view and select **Quick Fix** to apply automated corrections.
- Use @SuppressWarnings('PMD.RuleName') annotations to suppress specific violations where appropriate.
- Configure PMD incremental analysis in Eclipse to speed up repeated scans on large projects.

## Related Errors

- [checkstyle-error]({{< relref "/tools/eclipse/checkstyle-error" >}})
- [compilation-error]({{< relref "/tools/eclipse/compilation-error" >}})
- [problems-view-error]({{< relref "/tools/eclipse/problems-view-error" >}})
