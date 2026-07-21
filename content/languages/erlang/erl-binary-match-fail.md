---
title: "Binary pattern match failure in Erlang"
description: "Fix Erlang binary pattern matching errors when a binary does not match the expected structure."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A binary pattern match failure occurs at runtime when you attempt to match a binary against a pattern that does not fit the binary's actual structure. This raises a `badmatch` error if not caught.

## Common Causes

- Binary is shorter than the pattern expects
- Using a fixed-size segment on a variable-length binary
- Header bytes do not match the expected literal values
- Incorrect byte order when matching multi-byte integers
- Pattern requires a specific bit length that the binary does not have

## How to Fix

```erlang
%% WRONG: Assuming binary has at least 4 bytes
<<Size:32, _/binary>> = ShortBinary.
%% error: badmatch if ShortBinary has fewer than 4 bytes

%% CORRECT: Use size prefix or guard
<<Size:32, Rest/binary>> when byte_size(Rest) >= Size -> 
    process(Rest);
_ ->
    {error, invalid_packet}
```

```erlang
%% WRONG: Matching specific magic bytes on wrong data
<<16#DE, 16#AD, Rest/binary>> = <<1, 2, 3>>.
%% error: no match

%% CORRECT: Use case expression for safe matching
case Bin of
    <<16#DE, 16#AD, Rest/binary>> -> process(Rest);
    <<_, _/binary>> -> {error, bad_magic};
    _ -> {error, too_short}
end.
```

## Examples

```erlang
%% Example 1: Network packet parsing
parse_packet(<<1:8, Len:16/big, Payload:Len/binary, Rest/binary>>) ->
    {Payload, Rest};
parse_packet(_) ->
    {error, malformed}.

%% Example 2: Matching bit-level protocol
<<Flags:4/bits, Rest/bitstring>> = <<42>>.

%% Example 3: Recursive binary processing
process_all(<<>>) -> ok;
process_all(<<Len:16, Data:Len/binary, Rest/binary>>) ->
    handle(Data),
    process_all(Rest).
```

## Related Errors

- [Binary syntax error](erl-binary-syntax) -- compile-time syntax problems
- [Badmatch error](badmatch) -- general pattern match failures
