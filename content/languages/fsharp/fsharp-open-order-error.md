---
title: "[Solution] F# Open Order Error -- Initialization Ordering"
description: "Fix F# open order errors when module open statements cause type initialization failures."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Open Order Error

This error occurs when the order of `open` statements or module references causes type initialization to fail.

## Common Causes

- Circular module references where A opens B and B opens A
- Opening a module before its dependencies are compiled
- Type providers failing due to missing open statements
- Auto-open modules causing name collisions

## How to Fix

### Check compilation order in project file

```xml
<!-- WRONG: files compiled in wrong order -->
<ItemGroup>
  <Compile Include="Types.fs" />
  <Compile Include="Services.fs" />  <!-- depends on Types.fs -->
  <Compile Include="App.fs" />  <!-- depends on both -->
</ItemGroup>

<!-- CORRECT: dependent files last -->
<ItemGroup>
  <Compile Include="Types.fs" />
  <Compile Include="Services.fs" />
  <Compile Include="App.fs" />
</ItemGroup>
```

### Use qualified names to avoid open conflicts

```fsharp
// Instead of opening conflicting namespaces
// Use qualified access
let userList = FSharp.Collections.List.empty
```

## Examples

```fsharp
// File1.fs
namespace MyApp.Types
type Config = { Name: string }

// File2.fs
namespace MyApp.Services
open MyApp.Types
let getConfig () = { Name = "default" }
```
