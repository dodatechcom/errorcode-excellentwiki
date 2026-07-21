---
title: "[Solution] Swift Compiler Error: Cannot Use Mutating Member on Immutable Value"
description: "Fix mutating member errors on immutable values in Swift."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Swift Compiler Error: Cannot Use Mutating Member on Immutable Value

This error occurs when trying to call a mutating method on an immutable value, such as a let constant or a non-mutating function return.

## Common Causes
- Calling mutating method on let constant
- Trying to modify array through non-mutating subscript
- Calling mutating method on protocol existential
- Modifying struct returned from a function

## How to Fix
1. Use var instead of let for values that need mutation
2. Assign the result of mutating operation back to the variable
3. Use mutating methods on var properties only
4. Consider if the value should be a class instead of struct

```swift
// WRONG: Mutating method on let
let numbers = [1, 2, 3]
numbers.append(4)  // Error - let is immutable

// RIGHT: Use var
var numbers = [1, 2, 3]
numbers.append(4)  // OK

// WRONG: Mutating method on immutable return
func getArray() -> [Int] { return [1, 2, 3] }
getArray().append(4)  // Error

// RIGHT: Store in var first
var arr = getArray()
arr.append(4)
```

## Examples
```swift
// Example: Mutating vs non-mutating operations
struct Point {
    var x: Int
    var y: Int

    // Non-mutating - returns new value
    func moved(by delta: Point) -> Point {
        return Point(x: x + delta.x, y: y + delta.y)
    }

    // Mutating - modifies self
    mutating func move(by delta: Point) {
        x += delta.x
        y += delta.y
    }
}

var point = Point(x: 0, y: 0)
point.move(by: Point(x: 1, y: 1))  // OK - point is var

let constPoint = Point(x: 0, y: 0)
// constPoint.move(by: ...)  // Error - constPoint is let
let moved = constPoint.moved(by: Point(x: 1, y: 1))  // OK
```
