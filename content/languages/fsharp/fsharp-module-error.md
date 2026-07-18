---
title: "[Solution] F# Module or Namespace Error — How to Fix"
description: "Fix F# module and namespace errors. Learn how to organize code with modules, resolve namespace conflicts, and fix module visibility and access issues."
languages: ["fsharp"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

F# uses modules and namespaces to organize code into logical groups. When modules are not properly defined, have conflicting names, or are not accessible from where they are referenced, the compiler raises an error.

The most common cause is missing `open` statements. If you use a function from module `MyApp.Utils` without opening the module first, the compiler does not know where to find the function.

Another frequent cause is circular module dependencies. If module A references module B and module B references module A, the compiler cannot determine the compilation order and raises an error.

Module naming conflicts occur when two modules in different namespaces have the same name. Without explicit qualification or `open` statements, the compiler cannot decide which module to use.

Hidden module members cause access errors. If a module member is defined with `private` or is not in a module that has been `open`ed, attempts to access it fail.

The order of `open` statements matters. If two modules define functions with the same name, the last opened module takes precedence. This can cause unexpected function resolution.

Namespace declarations that do not match the file structure cause compilation errors. F# requires that namespace and module declarations align with the project structure.

## Common Error Messages

```
error FS0039: The namespace/module 'MyApp' is not defined
```

```
error FS0039: The value 'helper' is not defined in 'MyApp.Utils'
```

```
error FS0122: The module 'MyApp.Internal' is not accessible from this code location
```

```
error FS0039: The namespace 'MyApp' is not defined in the assembly
```

## How to Fix It

### Open modules correctly

```fsharp
// Define modules
module MyApp.Utils =
    let helper x = x * 2
    let processValue x = x + 1

module MyApp.Main =
    open MyApp.Utils  // Now Utils functions are in scope

    let result = helper 5      // Works
    let processed = processValue 10  // Works
```

### Use qualified names to resolve conflicts

```fsharp
module ModuleA =
    let process x = x + 1

module ModuleB =
    let process x = x * 2

// Both modules have 'process' — use qualified names
let result1 = ModuleA.process 5  // 6
let result2 = ModuleB.process 5  // 10

// Or use aliases
module A = ModuleA
module B = ModuleB
let result3 = A.process 5
```

### Define namespaces and modules correctly

```fsharp
// Namespace declaration
namespace MyApp.Types

type Person = {
    Name: string
    Age: int
}

// Module declaration (after namespace)
namespace MyApp

module Utils =
    let helper x = x * 2
```

### Control module visibility

```fsharp
// Public module — accessible everywhere
module public MyApp.PublicApi =
    let publicFunction x = x + 1

// Internal module — only accessible within the project
module internal MyApp.Internal =
    let privateSecret = 42
    let publicHelper x = x + privateSecret
```

### Handle circular dependencies

```fsharp
// Wrong — circular dependency
// module A = let x = B.y
// module B = let y = A.x

// Correct — break the cycle with a shared base module
module Shared =
    type CommonType = { Value: int }

module A =
    open Shared
    let processValue (c: CommonType) = c.Value * 2

module B =
    open Shared
    let createValue n = { Value = n }
```

### Use module aliases for convenience

```fsharp
open MyApp.Utils as U
open MyApp.Types as T

let result = U.helper 5
let person: T.Person = { Name = "Alice"; Age = 30 }
```

## Common Scenarios

- Organizing a large F# project into logical modules
- Resolving naming conflicts between modules from different libraries
- Building a public API with controlled visibility of internal modules

## Prevent It

- Use `open` statements at the top of files to bring needed modules into scope
- Prefer qualified names over `open` when there is a risk of name conflicts
- Keep module definitions small and focused to avoid circular dependencies
