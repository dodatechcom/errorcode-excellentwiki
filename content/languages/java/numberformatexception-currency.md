---
title: "[Solution] Java NumberFormatException — Currency String Parsing Fix"
description: "Fix Java NumberFormatException when parsing currency strings by using NumberFormat.getCurrencyInstance(), stripping currency symbols, and handling locale-specific formats."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 8
---

# NumberFormatException — Currency String Parsing Fix

A `NumberFormatException` when parsing currency strings is thrown because `Double.parseDouble()` or `Integer.parseInt()` cannot handle currency symbols, thousands separators, or locale-specific formatting. Currency strings like `$1,234.56` or `€1.234,56` are not valid numeric literals.

## Description

Java's `Double.parseDouble()` and `Long.parseLong()` expect raw numeric strings without formatting. Currency strings include symbols (`$`, `€`, `£`), thousands separators (`,` or `.`), and locale-specific decimal separators. Passing these directly to parse methods throws `NumberFormatException`.

Message variants:

- `java.lang.NumberFormatException: For input string: "$1,234.56"`
- `java.lang.NumberFormatException: For input string: "€1.234,56"`
- `java.lang.NumberFormatException: For input string: "1,000,000"`
- `java.lang.NumberFormatException: For input string: "$0.00"`

## Common Causes

```java
// Cause 1: Parsing currency string with Double.parseDouble
double amount = Double.parseDouble("$1,234.56");  // NumberFormatException

// Cause 2: Parsing locale-formatted number
double amount = Double.parseDouble("1.234,56");  // German format — NumberFormatException

// Cause 3: Parsing number with thousands separator
long count = Long.parseLong("1,000,000");  // NumberFormatException

// Cause 4: Parsing empty or whitespace currency string
double amount = Double.parseDouble("");  // NumberFormatException
double amount = Double.parseDouble("$");  // NumberFormatException

// Cause 5: Parsing currency from API response
String price = "\"$29.99\"";  // includes quotes
double amount = Double.parseDouble(price);  // NumberFormatException
```

## Solutions

### Fix 1: Use NumberFormat.getCurrencyInstance() for parsing

```java
import java.text.NumberFormat;
import java.text.ParseException;
import java.util.Locale;

// Parse US currency
NumberFormat format = NumberFormat.getCurrencyInstance(Locale.US);
Number number = format.parse("$1,234.56");
double amount = number.doubleValue();  // 1234.56

// Parse European currency
NumberFormat germanFormat = NumberFormat.getCurrencyInstance(Locale.GERMANY);
Number number = germanFormat.parse("1.234,56 €");
double amount = number.doubleValue();  // 1234.56

// Parse any locale
NumberFormat format = NumberFormat.getCurrencyInstance(Locale.forLanguageTag("ja-JP"));
Number number = format.parse("¥1,234");
double amount = number.doubleValue();
```

### Fix 2: Strip currency symbols before parsing

```java
public static double parseCurrencyString(String currencyStr) {
    if (currencyStr == null || currencyStr.isBlank()) {
        return 0.0;
    }

    // Remove currency symbols, whitespace, and thousands separators
    String cleaned = currencyStr
        .replaceAll("[£€$¥\\s]", "")     // remove currency symbols and spaces
        .replaceAll(",", "");              // remove thousands separators

    // Handle European format (1.234,56 → 1234.56)
    if (cleaned.matches(".*\\d+\\.\\d{3},\\d{2}")) {
        cleaned = cleaned.replace(".", "").replace(",", ".");
    }

    return Double.parseDouble(cleaned);
}

// Usage
double amount = parseCurrencyString("$1,234.56");   // 1234.56
double amount = parseCurrencyString("€1.234,56");   // 1234.56
double amount = parseCurrencyString("$0.00");       // 0.0
```

### Fix 3: Use DecimalFormat with locale

```java
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.text.ParseException;

// US format
DecimalFormatSymbols usSymbols = DecimalFormatSymbols.getInstance(Locale.US);
DecimalFormat usFormat = new DecimalFormat("$#,##0.00", usSymbols);
Number number = usFormat.parse("$1,234.56");
double amount = number.doubleValue();

// European format
DecimalFormatSymbols euSymbols = DecimalFormatSymbols.getInstance(Locale.GERMANY);
DecimalFormat euFormat = new DecimalFormat("#,##0.00 €", euSymbols);
Number number = euFormat.parse("1.234,56 €");
double amount = number.doubleValue();
```

### Fix 4: Parse currency with safe error handling

```java
import java.text.NumberFormat;
import java.text.ParseException;
import java.util.Locale;
import java.util.Optional;

public class CurrencyParser {
    public static Optional<Double> tryParseCurrency(String input, Locale locale) {
        if (input == null || input.isBlank()) {
            return Optional.empty();
        }
        try {
            NumberFormat format = NumberFormat.getCurrencyInstance(locale);
            format.setParseIntegerOnly(false);
            return Optional.of(format.parse(input.trim()).doubleValue());
        } catch (ParseException e) {
            // Try without currency symbols
            try {
                String cleaned = input.replaceAll("[^\\d.,\\-]", "").trim();
                return Optional.of(Double.parseDouble(cleaned));
            } catch (NumberFormatException nfe) {
                return Optional.empty();
            }
        }
    }
}

// Usage
Optional<Double> amount = CurrencyParser.tryParseCurrency("$1,234.56", Locale.US);
amount.ifPresent(a -> System.out.println("Amount: " + a));
```

## Prevention Checklist

- Never use `Double.parseDouble()` on currency strings — use `NumberFormat.getCurrencyInstance()`.
- Always specify the correct `Locale` when parsing currency.
- Strip non-numeric characters before falling back to `Double.parseDouble()`.
- Handle European format (dot as thousands separator, comma as decimal).
- Use `Optional<Double>` or null returns for fallible parsing.
- Test with multiple locales (US, EU, JP, UK) for international applications.

## Related Errors

- [NumberFormatException](../numberformatexception) — general numeric parsing failure
- [NumberFormatException Hex](../nfe-hex) — hex parsing failure
- [NumberFormatException Empty](../nfe-empty) — empty string parsing
- [ParseException](../datetimeparseexception) — date/time parsing failure
