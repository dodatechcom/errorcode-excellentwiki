---
title: "[Solution] react-native Hermes Engine Error"
description: "Hermes engine not working."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Hermes engine not working.

## Common Causes

Not enabled.

## How to Fix

Enable in build.gradle.

## Example

```groovy
project.ext.react = [enableHermes: true]
```
