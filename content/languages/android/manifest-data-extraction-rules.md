---
title: "Data Extraction Rules Error"
description: "Configure Android 12+ data extraction rules and backup rules in manifest"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Backup or data transfer fails because extraction rules are not configured

## Common Causes

- android:dataExtractionRules not defined in manifest
- android:fullBackupContent deprecated and not migrated
- Missing cloud backup rules for Android 12+
- No device transfer rules configured

## Fixes

- Add android:dataExtractionRules for Android 12+
- Keep android:fullBackupContent for older versions
- Define include/exclude rules for files and databases
- Test backup with adb shell bmgr

## Code Example

```kotlin
<!-- AndroidManifest.xml -->
<application
    android:dataExtractionRules="@xml/data_extraction_rules"
    android:fullBackupContent="@xml/backup_rules"
    ...>
```

<!-- res/xml/data_extraction_rules.xml -->
<?xml version="1.0" encoding="utf-8"?>
<data-extraction-rules>
    <cloud-backup>
        <include domain="sharedpref" path="." />
        <exclude domain="database" path="temp.db" />
    </cloud-backup>
</data-extraction-rules>
