---
title: "[Solution] Ruby Money Gem — Currency Conversion, Rounding, Exchange Rate Errors"
description: "Fix Ruby Money gem errors. Handle currency conversion, rounding, and exchange rate issues."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, money, currency, conversion, rounding"]
severity: "error"
---

# Ruby Currency / Money Gem Errors

## Error Message

```
Money::Currency::UnknownCurrency: Unknown currency: xyz
# or
ArgumentError: can't convert nil to Money
# or
Money::Rates::NoRateTableLoaded: No rate table loaded
```

## Common Causes

- Using an unsupported or misspelled currency code
- Converting between currencies without a loaded exchange rate table
- Rounding errors when using non-decimal currencies
- Nil values in arithmetic operations

## Solutions

### Solution 1: Use Supported Currency Codes

Always use valid ISO 4217 currency codes.

```ruby
require "money"

# BAD: unknown currency
Money.new(100, "XYZ")  # UnknownCurrency

# GOOD: use valid ISO codes
Money.new(100, "USD")  # => #<Money fractional:10000 currency:USD>
Money.new(100, "EUR")  # => #<Money fractional:10000 currency:EUR>

# List available currencies
Money::Currency.all  # => [#<Money::Currency id: usd>, ...]
```

### Solution 2: Load Exchange Rates for Conversion

Set up exchange rates before converting between currencies.

```ruby
require "money"
require "money/bank/google_currency"

# Use Google's exchange rates
bank = Money::Bank::GoogleCurrency.new
bank.update_rates

Money.default_bank = bank

usd = Money.new(100, "USD")
eur = usd.exchange_to("EUR")
puts eur  # => #<Money fractional:92 currency:EUR>
```

### Solution 3: Handle Rounding Correctly

Use proper rounding methods for monetary calculations.

```ruby
require "money"

# BAD: floating point rounding errors
100.00 / 3  # => 33.333333333333336

# GOOD: use Money for precise arithmetic
Money.new(10000, "USD") / 3
# => #<Money fractional:3333 currency:USD>

# Round to nearest cent
amount = Money.new(1555, "USD")
amount.round  # => #<Money fractional:1555 currency:USD>

# Use exchange with rounding
bank = Money::Bank::VariableExchange.new
bank.add_rate("USD", "EUR", 0.92)
bank.exchange Money.new(100, "USD"), "EUR"
# => #<Money fractional:92 currency:EUR>
```

### Solution 4: Format Money for Display

Format monetary values consistently for output.

```ruby
require "money"

money = Money.new(1234567, "USD")

# Default format
money.format  # => "$12,345.67"

# Custom format
money.format(symbol: true, thousands_separator: ",", decimal_mark: ".")
# => "$12,345.67"

# Without symbol
money.format(symbol: false)
# => "12345.67"

# European format
eur = Money.new(1234567, "EUR")
eur.format(thousands_separator: ".", decimal_mark: ",")
# => "12.345,67 €"
```

## Prevention Tips

- Always use valid ISO 4217 currency codes with Money
- Load exchange rates before performing currency conversions
- Use Money for arithmetic instead of floats to avoid rounding errors
- Format amounts consistently using `Money#format`

## Related Errors

- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
- [FloatDomainError]({{< relref "/languages/ruby/float-domain-error" >}})
- [ZeroDivisionError]({{< relref "/languages/ruby/zero-division-error" >}})
