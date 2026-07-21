---
title: "Binary syntax error in Erlang construction"
description: "Fix Erlang binary syntax errors when constructing or pattern matching binaries with incorrect bit syntax."
languages: ["erlang"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A binary syntax error in Erlang occurs when you use malformed bit syntax in binary construction or pattern matching. The compiler detects invalid type specifiers, size qualifiers, or endianness flags and raises a compilation failure.

## Common Causes

- Using unsupported type specifiers in binary syntax
- Mixing incompatible type qualifiers like `signed` and `unsigned`
- Providing a size qualifier on a type that does not support it
- Forgetting the `binary` or `bitstring` qualifier for variable-length segments
- Using逗号 instead of the `-` separator between binary fields

## How to Fix

```erlang
%% WRONG: Using 'string' as a binary type specifier
Bin = <<"hello">>/string.
%% error: syntax error before '/'

%% CORRECT: Use default type or utf8/utf16/utf32
Bin = <<"hello">>.
UTF8 = <<"hello">>/utf8.
```

```erlang
%% WRONG: Signed and unsigned together
<<X/signed-unsigned>> = <<1,2,3>>.
%% error: conflicting type specifiers

%% CORRECT: Choose one
<<X/signed>> = <<1,2,3>>.
<<Y/unsigned>> = <<4,5,6>>.
```

## Examples

```erlang
%% Example 1: Missing size on bitstring
<<Head:8, Rest/bitstring>> = <<1,2,3>>.  %% correct
<<Head:8, Rest/bit>> = <<1,2,3>>.         %% syntax error

%% Example 2: Invalid endianness on unit
<<Val:32/big>> = <<0,0,0,1>>.             %% correct
<<Val:32/little/unit:8>> = <<0,0,0,1>>.   %% error: redundant unit

%% Example 3: Binary comprehension syntax
[X || <<X>> <= <<1,2,3>>].                %% correct
[X || X << <<1,2,3>>].                    %% syntax error
```

## How to Debug

- Use `erl_scan:string/1` to identify the exact token causing the error
- Consult the Erlang Reference Manual for valid binary types
- Check that unit values are between 1 and 256
- Verify endianness flags are `big`, `little`, or `native`

## Related Errors

- [Binary match error](erl-binary-match) -- failure during binary pattern matching
- [Badarg error](badarg) -- invalid argument to binary construction BIF
