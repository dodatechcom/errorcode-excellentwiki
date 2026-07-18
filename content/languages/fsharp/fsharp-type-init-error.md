---
title: "[Solution] F# TypeInitializationException — Static Constructor Failure"
description: "Fix F# TypeInitializationException when a type's static constructor fails. Learn static initialization order, circular dependencies, and lazy patterns."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `TypeInitializationException` is thrown when the static constructor (or type initializer) of a type fails. The .NET runtime calls the static constructor the first time any member of the type is accessed. If it throws an exception, every subsequent access to the type wraps the original exception in `TypeInitializationException`.

## Why It Happens

The most common cause is an exception thrown in a `static let` binding or `static do` statement. In F#, top-level bindings in a module or static members with initializers run as part of the type's static constructor.

Another frequent cause is accessing a type whose static constructor depends on another type whose static constructor also fails. This creates a chain of `TypeInitializationException` exceptions.

Circular dependencies between types with static constructors can cause this error. If type A's static constructor accesses type B, and type B's static constructor accesses type A, the runtime detects the cycle and throws.

Reading environment variables or configuration files that do not exist during static initialization is another common source. If the application reads `System.Configuration.ConfigurationManager.AppSettings` before the config file is loaded, it may throw.

Finally, accessing a static member of a type in a different assembly whose static constructor failed will surface as `TypeInitializationException` in the calling code.

## How to Fix It

### Use lazy initialization instead of static constructors

```fsharp
// Wrong — static constructor may fail
type Config() =
    static let settings = System.Configuration.ConfigurationManager.AppSettings
    static member Settings = settings

// Correct — lazy initialization with error handling
type Config() =
    static let mutable settings = None
    static member Settings =
        match settings with
        | Some s -> s
        | None   ->
            let s = System.Configuration.ConfigurationManager.AppSettings
            settings <- Some s
            s
```

### Handle exceptions in static initializers

```fsharp
type Database() =
    static let connection =
        try
            Some (new SqlConnection("..."))
        with
        | ex ->
            printfn "Failed to connect: %s" ex.Message
            None
    static member Connection = connection
```

### Use Module-level functions instead of static constructors

```fsharp
module Config =
    let private loadSettings () =
        System.Configuration.ConfigurationManager.AppSettings

    let settings = lazy loadSettings ()

    let getValue key =
        settings.Value.[key]
```

### Avoid circular static dependencies

```fsharp
// Wrong — circular dependency
type A() =
    static do printfn "%s" B.Name
and B() =
    static do printfn "%s" A.Name

// Correct — break the cycle with a function
type A() =
    static member GetName () = "A"

type B() =
    static member GetName () = "B"
```

### Check inner exception for root cause

```fsharp
try
    let _ = typeof<MyType>.Name
with
| :? TypeInitializationException as ex ->
    printfn "Root cause: %A" ex.InnerException
```

## Common Mistakes

- Putting potentially failing operations in static constructors without error handling
- Creating circular dependencies between types with static initializers
- Not checking `InnerException` when catching `TypeInitializationException`
- Assuming static constructors run in a specific order across assemblies
- Using `let` bindings at module level that execute at load time without lazy evaluation

## Related Pages

- [F# NullReferenceException](/languages/fsharp/fsharp-nullreference/)
- [F# OutOfMemoryException](/languages/fsharp/fsharp-out-of-memory/)
- [F# InvalidOperation](/languages/fsharp/fsharp-invalidoperation/)
