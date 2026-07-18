---
title: "[Solution] F# Assertion Failure in Test — How to Fix"
description: "Fix F# assertion failures in tests. Learn how to use Assert, Expecto, and xUnit assertions correctly, and debug why test assertions fail unexpectedly."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

Test assertions in F# fail when the actual result does not match the expected result. While assertion failures are expected behavior in testing, unexpected failures indicate bugs in the code or incorrect test expectations.

The most common cause is the function under test returning a different value than expected. This may be due to a logic error, an off-by-one mistake, or an incorrect algorithm.

Another frequent cause of assertion failures is floating-point comparison. Comparing `0.1 + 0.2 = 0.3` fails because of floating-point precision issues. The assertion shows the values are almost equal but not exactly equal.

Timing-dependent tests fail intermittently. If a test depends on the current time, network response, or async completion, the result may vary between runs.

Test setup or teardown issues cause assertions to fail. If the test database is not reset between tests, or if test fixtures are shared between tests, the assertions may be checking against stale data.

Exception handling in tests can mask assertion failures. If a test catches an exception before the assertion runs, the assertion is never evaluated and the test passes when it should fail.

Assertion messages that are too vague make debugging difficult. Without a clear description of what was expected and what was received, finding the root cause of a failure is time-consuming.

## Common Error Messages

```
Assert.Fail: Expected: 42, Actual: 41
```

```
Expecto.AssertException: Expected string to be equal, but they are not.
  Expected: "hello world"
  Actual: "Hello World"
```

```
xUnit.Assert.Equal() Failure: Values differ
  Expected: 3.14159
  Actual: 3.14159265
```

```
NUnit.Framework.AssertionException: Expected: True, Actual: False
```

## How to Fix It

### Use precise floating-point comparisons

```fsharp
// Wrong — floating-point comparison fails
Assert.AreEqual(0.3, 0.1 + 0.2)

// Correct — compare with tolerance
let inline approximatelyEqual (a: float) (b: float) (tolerance: float) =
    abs (a - b) < tolerance

Assert.IsTrue(approximatelyEqual 0.3 (0.1 + 0.2) 1e-10)
```

### Use Expecto for more informative failures

```fsharp
open Expecto

let tests = testList "MyTests" [
    test "addition works" {
        let result = 2 + 2
        Expect.equal result 4 "2 + 2 should equal 4"
    }

    test "string comparison" {
        let result = "hello" + " " + "world"
        Expect.equal result "hello world" "Concatenated strings should match"
    }

    test "floating point with tolerance" {
        let result = 0.1 + 0.2
        Expect.floatClose Accuracy.medium result 0.3 "Floating point sum should be approximately 0.3"
    }
]
```

### Test exception cases explicitly

```fsharp
// Wrong — test may not actually call the function
test "division by zero" {
    let result = divide 10 0
    Assert.AreEqual(0, result)
}

// Correct — test that the exception is raised
test "division by zero throws" {
    Expect.throws (fun () -> divide 10 0 |> ignore) "Should throw DivideByZeroException"
}
```

### Use descriptive assertion messages

```fsharp
// Wrong — no description
Assert.AreEqual(expected, actual)

// Correct — clear description
Assert.AreEqual(
    expected, 
    actual, 
    sprintf "Expected list length to be %d but was %d" expectedLength actualLength
)
```

### Test async operations properly

```fsharp
// Wrong — async assertion may not execute
test "async result" {
    let result = async { return 42 } |> Async.RunSynchronously
    Assert.AreEqual(42, result)
}

// Correct — use async test
testAsync "async result" {
    let! result = async { return 42 }
    Expect.equal result 42 "Async should return 42"
}
```

## Common Scenarios

- Unit tests that fail due to floating-point precision issues
- Integration tests that fail because of database state not being reset
- Async tests that pass because the assertion is never reached

## Prevent It

- Use `Expecto` or a similar framework that provides detailed assertion failure messages
- Always compare floating-point values with a tolerance rather than exact equality
- Write test fixtures that properly set up and tear down state between tests
