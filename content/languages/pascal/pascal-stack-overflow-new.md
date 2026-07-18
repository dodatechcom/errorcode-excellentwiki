---
title: "[Solution] Pascal: stack overflow runtime error"
description: "Fix Pascal stack overflow by eliminating deep recursion and converting to iterative algorithms."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["critical"]
weight: 5
---

## What This Error Means

A Pascal stack overflow occurs when the call stack exceeds its allocated size, typically due to excessive recursion or very large local variables. Each function call pushes a stack frame containing parameters, local variables, and return addresses. When recursion is too deep or stack frames are too large, the stack pointer runs into protected memory, triggering Runtime error 202 or a segmentation fault. This is a critical runtime error that immediately terminates the program.

## Why It Happens

Stack overflow in Pascal most commonly results from unbounded recursion. A recursive function that does not have a proper base case, or whose base case is never reached, will recurse until the stack is exhausted. Factorial, Fibonacci, and tree traversal implementations are frequent culprits. Deep recursion on large data structures, such as processing a linked list with millions of elements recursively, can also overflow the stack. Functions with large local variables, such as large arrays allocated on the stack, consume significant stack space per call. Mutual recursion, where two or more functions call each other, can be harder to detect but produces the same problem. Tail recursion that is not optimized by the compiler still consumes stack space.

## How to Fix It

**Convert recursion to iteration:**

```pascal
{ WRONG: recursive factorial, stack overflow for large n }
function Factorial(n: Integer): Int64;
begin
  if n <= 1 then
    Factorial := 1
  else
    Factorial := n * Factorial(n - 1);
end;

{ CORRECT: iterative factorial }
function Factorial(n: Integer): Int64;
var
  result: Int64;
  i: Integer;
begin
  result := 1;
  for i := 2 to n do
    result := result * i;
  Factorial := result;
end;
```

**Use an explicit stack for tree traversal:**

```pascal
type
  PNode = ^TNode;
  TNode = record
    value: Integer;
    left, right: PNode;
  end;

{ WRONG: recursive traversal }
procedure Traverse(node: PNode);
begin
  if node <> nil then
  begin
    Traverse(node^.left);
    Write(node^.value, ' ');
    Traverse(node^.right);
  end;
end;

{ CORRECT: iterative with explicit stack }
procedure TraverseIterative(root: PNode);
var
  stack: array[1..1000] of PNode;
  top: Integer;
  current: PNode;
begin
  top := 0;
  current := root;
  while (top > 0) or (current <> nil) do
  begin
    while current <> nil do
    begin
      Inc(top);
      stack[top] := current;
      current := current^.left;
    end;
    current := stack[top];
    Dec(top);
    Write(current^.value, ' ');
    current := current^.right;
  end;
end.
```

**Increase stack size for legitimate deep recursion:**

```bash
# Turbo Pascal / Free Pascal
{ $M 65536,0,1000000 }  { Min stack, max stack }

# Free Pascal command line
fpc -Cm 1000000 source.pas
```

**Use tail recursion when possible:**

```pascal
{ Tail-recursive: can be optimized by some compilers }
function SumList(list: array of Integer; index, acc: Integer): Integer;
begin
  if index > High(list) then
    SumList := acc
  else
    SumList := SumList(list, index + 1, acc + list[index]);
end;


## Common Mistakes

- Not having a base case in recursive functions, or having a base case that is unreachable
- Allocating large arrays as local variables instead of using heap allocation
- Not realizing that mutual recursion also consumes stack space
- Assuming the compiler automatically optimizes all tail recursion
- Forgetting that each recursive call multiplies the stack usage of local variables

## Related Pages

- [Range check error in Pascal](/languages/pascal/pascal-index-error-new)
- [Out of heap space in Pascal](/languages/pascal/pascal-heap-error-new)
- [Invalid pointer operation in Pascal](/languages/pascal/pascal-invalid-pointer-v2)
- [Runtime error in Pascal](/languages/pascal/pascal-runtime-error-v2)
