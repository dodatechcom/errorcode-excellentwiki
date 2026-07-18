---
title: "[Solution] Erlang Fun Clause Error in Anonymous Functions"
description: "Fix Erlang no function clause error in fun expressions. Handle argument mismatches in anonymous functions."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `function_clause` error occurs when an anonymous function (fun) receives arguments that do not match any of its defined clauses. The Erlang runtime cannot find a matching clause for the provided arguments, resulting in this error.

## Why It Happens

- Wrong number of arguments passed to the fun: The fun expects a specific arity but receives a different number.
- Argument types do not match expected patterns: The fun may expect a tuple but receives an atom.
- Fun defined with limited patterns for dynamic input: The fun handles only specific cases but the caller provides unexpected data.
- Callback fun receives unexpected data from higher-order function: Functions like `lists:map/2` pass each element to the fun, and if the fun cannot handle certain elements, this error occurs.
- Recursive fun has incorrect base case pattern: A recursive fun may not handle the termination condition properly.

## How to Fix It

Define fun clauses with pattern matching for all expected inputs. Use multiple clauses to handle different cases:

```erlang
Fun = fun
    (0) -> base_case;
    (N) when N > 0 -> recursive_call(N - 1);
    (N) -> {error, {invalid_input, N}}
end,
Fun(5).
```

Use multi-clause funs to handle different argument shapes. This is particularly useful for processing results from other functions:

```erlang
Processor = fun
    ({ok, Data}) -> process(Data);
    ({error, Reason}) -> handle_error(Reason);
    (Other) -> {error, {unexpected, Other}}
end,
Processor(fetch_result()).
```

Add guards to validate argument ranges and types:

```erlang
SafeDiv = fun
    (A, 0) -> {error, division_by_zero};
    (A, B) when is_number(A), is_number(B) -> A / B;
    (A, B) -> {error, {type_mismatch, A, B}}
end.
```

Debug by printing received arguments. This helps you understand what the fun is actually receiving:

```erlang
DebugFun = fun(Args) ->
    io:format("Fun received: ~p~n", [Args]),
    handle(Args)
end.
```

Use anonymous functions with `fun Module:Function/Arity` syntax for better error messages:

```erlang
%% Instead of:
lists:map(fun(X) -> X * 2 end, List)

%% Use:
lists:map(fun my_module:double/1, List)
```

## Common Mistakes

- Assuming fun accepts any argument without pattern matching. Always define clauses for expected inputs.
- Not handling edge cases like zero, nil, or empty lists. These are common inputs that may not match your expected patterns.
- Forgetting that fun clause order matters like case branches. The first matching clause is executed, so order your clauses from most specific to most general.
- Passing wrong tuple arity to callback functions. Ensure the tuple structure matches what the fun expects.
- Not using guards to validate argument types and ranges. Guards provide early validation before processing.

## Related Pages

- [function-clause]({{< relref "/languages/erlang/erlang-functionclause" >}}) - named function clause error
- [badmatch]({{< relref "/languages/erlang/erlang-badmatch" >}}) - pattern match failure
- [case-clause]({{< relref "/languages/erlang/case-clause" >}}) - case clause error
- [badarg]({{< relref "/languages/erlang/badarg" >}}) - bad argument error
