---
title: "[Solution] Elixir Regex Error — Invalid Regular Expression Pattern"
description: "Fix Elixir Regex errors with invalid patterns. Learn about Regex.compile, capture groups, and pattern validation in Elixir."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `Regex` error is raised when a regular expression pattern is invalid or when regex operations fail. The error message shows the pattern that caused the error and the specific issue (like unmatched parentheses or invalid escape sequences).

## Why It Happens

The most common cause is an invalid regex pattern. Unmatched parentheses, invalid escape sequences, or incorrect quantifier syntax cause compilation errors.

Another frequent cause is using regex functions with invalid arguments. Passing `nil` or non-binary values to `Regex.run` or `Regex.match?` causes this error.

Memory exhaustion from catastrophic backtracking occurs with patterns that have exponential time complexity. For example, patterns like `(a+)+` on long input strings can cause the regex engine to consume excessive memory.

Invalid capture group syntax or unnamed groups in functions that expect named groups also cause this error.

Finally, using PCRE-specific syntax that is not supported by Elixir's regex engine (which uses PCRE2) can cause issues.

## How to Fix It

### Validate regex patterns before use

```elixir
def safe_regex(pattern) do
  case Regex.compile(pattern) do
    {:ok, regex} -> {:ok, regex}
    {:error, reason} -> {:error, reason}
  end
end
```

### Test regex patterns with Regex.compile

```elixir
case Regex.compile("^[a-z]+$") do
  {:ok, regex} -> IO.puts("Valid pattern")
  {:error, {reason, _}} -> IO.puts("Invalid: #{reason}")
end
```

### Handle nil inputs

```elixir
def safe_match?(nil, _regex), do: false
def safe_match?(string, regex) when is_binary(string) do
  Regex.match?(regex, string)
end
```

### Avoid catastrophic backtracking

```julia
# Wrong — may cause exponential backtracking
Regex.run(~r/(a+)+b/, "aaaaaaaaaaac")

# Correct — use atomic groups or possessive quantifiers
Regex.run(~r/a++b/, "aaaaaaaaaaac")
```

### Use sigil syntax for clarity

```elixir
# Both are equivalent
regex = ~r/^[a-z]+$/
regex = Regex.compile!("^[a-z]+$")
```

## Common Mistakes

- Not escaping special characters in regex patterns
- Using regex functions without validating input first
- Not considering performance implications of complex patterns
- Using regex when String functions would be simpler
- Not testing regex patterns with edge cases

## Related Pages

- [Elixir ArgumentError](/languages/elixir/elixir-argumenterror-elixir/)
- [Elixir FunctionClauseError](/languages/elixir/elixir-clause-error/)
- [Elixir UnicodeConversionError](/languages/elixir/elixir-unicode-error/)
