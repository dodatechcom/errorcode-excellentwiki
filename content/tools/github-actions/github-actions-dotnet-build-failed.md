---
title: "[Solution] GitHub Actions DotNet Build Failed"
description: "Fix GitHub Actions .NET build failures in CI workflow."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

dotnet build failures occur during .NET compilation:

```
Error: error CS0246: The type or namespace name 'Serilog' could not be found
```

## Common Causes

- .NET SDK version mismatch.
- NuGet package restore failed.

## How to Fix

**Set up .NET properly:**

```yaml
steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-dotnet@v4
    with:
      dotnet-version: '8.0.x'
  - run: dotnet restore
  - run: dotnet build --no-restore
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-dotnet@v4
    with:
      dotnet-version: '8.0.x'
      cache: true
  - run: dotnet restore
  - run: dotnet build --configuration Release
```
