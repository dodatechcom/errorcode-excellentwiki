---
title: "[Solution] Lua Pattern Match Error Invalid Pattern Fix"
description: "Fix Lua pattern match errors from invalid patterns. Learn why pattern compilation fails and how to write correct Lua patterns."
languages: ["lua"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A Lua pattern error occurs when a pattern string passed to functions like `string.match`, `string.find`, `string.gsub`, or `string.gmatch` is syntactically invalid. Lua patterns are not full regular expressions and have their own syntax rules. An invalid pattern causes `stringfunctionname: bad argument` with details about the malformed pattern.

## Why It Happens

- Unclosed brackets in character classes (`[` without `]`)
- Unbalanced parentheses in captures
- Using regular expression syntax not supported in Lua patterns
- Escaping characters incorrectly with `%` in patterns
- Empty pattern where a non-empty one is expected
- Pattern string containing embedded null bytes
- Using special characters like `(` without escaping as `%(`

## How to Fix It

### Escape special characters correctly

```lua
-- WRONG: Unescaped special characters
local pattern = "(hello)"  -- treated as capture group, not literal
local result = string.match("say (hello) now", pattern)

-- CORRECT: Escape with %
local pattern = "%(hello%)"
local result = string.match("say (hello) now", pattern)
print(result)  -- (hello)
```

### Fix unbalanced character classes

```lua
-- WRONG: Unclosed bracket
local pattern = "[aeiou"  -- missing ]
local result = string.match("hello", pattern)  -- error

-- CORRECT: Close the character class
local pattern = "[aeiou]"
local result = string.match("hello", pattern)
print(result)  -- e
```

### Use correct Lua pattern syntax instead of regex

```lua
-- WRONG: Using regex-only syntax
local pattern = "\\d+"  -- Lua does not use backslash d
local result = string.match("abc123", pattern)  -- error

-- CORRECT: Use Lua pattern syntax
local pattern = "%d+"
local result = string.match("abc123", pattern)
print(result)  -- 123
```

### Escape user-provided patterns safely

```lua
-- WRONG: User input used directly as pattern
local userInput = "(test)"
local result = string.find("some text", userInput)  -- error

-- CORRECT: Escape all pattern special characters
local function escapePattern(str)
    return str:gsub("([%(%)%.%%%+%-%*%?%[%]%^%$])", "%%%1")
end
local safe = escapePattern(userInput)
local result = string.find("some text", safe)
```

### Validate patterns before using them

```lua
-- WRONG: Pattern may be invalid
local function search(text, pattern)
    return string.find(text, pattern)  -- crashes on bad pattern
end

-- CORRECT: Wrap in pcall to catch pattern errors
local function search(text, pattern)
    local ok, result, finish = pcall(string.find, text, pattern)
    if ok then
        return result, finish
    else
        print("Invalid pattern: " .. tostring(result))
        return nil
    end
end
```

## Common Mistakes

- Confusing Lua patterns with PCRE regular expressions
- Not knowing that Lua patterns do not support alternation (`|`)
- Using `\b` or `\w` which are not valid in Lua patterns
- Forgetting that `%` is the escape character in Lua patterns, not `\`
- Not escaping `-` in character classes where it means "zero or more shortest"

## Related Pages

- [Lua String Concat Nil](lua-string-concat-nil) - concatenation nil error
- [Lua Argument Type Error](lua-argument-type-error) - wrong argument type
- [Lua Encoding Error](lua-encoding-error) - encoding and UTF-8 issues
- [Lua I/O Error](lua-io-error) - file read/write error
