---
title: "[Solution] Stripe Currency Error — Invalid Currency Code"
description: "Fix Stripe invalid currency errors. Resolve currency code format issues and unsupported currency problems in Stripe."
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

A Stripe currency error occurs when you pass an unsupported or incorrectly formatted currency code. Stripe uses lowercase three-letter ISO 4217 currency codes for all transactions.

## What This Error Means

When the currency code is invalid, Stripe returns:

```json
{
  "error": {
    "type": "invalid_request_error",
    "param": "currency",
    "message": "Invalid currency: us-dollar. Stripe currently supports these currencies: usd, aed, afn, ..."
  }
}
```

Stripe requires exact ISO 4217 codes in lowercase with no spaces or special characters.

## Why It Happens

- Using uppercase instead of lowercase (USD vs usd)
- Passing full currency names instead of codes (dollar vs usd)
- Using a code for a currency Stripe does not support
- Passing a currency with extra whitespace
- Using an outdated currency code

## How to Fix It

### Use Correct Currency Codes

```javascript
// WRONG
const payment1 = await stripe.paymentIntents.create({
  amount: 500,
  currency: 'USD',      // uppercase
});

const payment2 = await stripe.paymentIntents.create({
  amount: 500,
  currency: 'dollar',   // full name
});

// RIGHT
const payment = await stripe.paymentIntents.create({
  amount: 500,
  currency: 'usd',      // lowercase ISO 4217
});
```

### Currency Lookup Helper

```javascript
const supportedCurrencies = {
  'USD': 'usd', 'EUR': 'eur', 'GBP': 'gbp',
  'CAD': 'cad', 'AUD': 'aud', 'JPY': 'jpy',
  'INR': 'inr', 'BRL': 'brl', 'MXN': 'mxn',
  'CHF': 'chf', 'SEK': 'sek', 'NOK': 'nok',
};

function normalizeCurrency(input) {
  const normalized = input.trim().toLowerCase();
  if (supportedCurrencies[input.toUpperCase()]) {
    return supportedCurrencies[input.toUpperCase()];
  }
  return normalized;
}

// Usage
const currency = normalizeCurrency('USD'); // returns 'usd'
```

### Validate Currency Before API Call

```javascript
const STRIPE_CURRENCIES = [
  'usd', 'eur', 'gbp', 'cad', 'aud', 'jpy',
  'inr', 'brl', 'mxn', 'chf', 'sek', 'nok',
  'dkk', 'pln', 'czk', 'hkd', 'sgd', 'zar',
];

function validateCurrency(currency) {
  const code = currency.toLowerCase().trim();
  if (!STRIPE_CURRENCIES.includes(code)) {
    throw new Error(`Unsupported currency: ${currency}`);
  }
  return code;
}
```

### Python Example

```python
import stripe

# Always lowercase
payment_intent = stripe.PaymentIntent.create(
    amount=500,
    currency='usd',  # not 'USD'
)
```

### Handle Multi-Currency Payments

```javascript
function getCurrencyConfig(countryCode) {
  const map = {
    'US': { currency: 'usd', decimal_places: 2 },
    'JP': { currency: 'jpy', decimal_places: 0 },
    'HU': { currency: 'huf', decimal_places: 0 },
  };
  return map[countryCode] || { currency: 'usd', decimal_places: 2 };
}
```

## Common Mistakes

- Passing `"USD"` instead of `"usd"`
- Using `"dollar"` or `"euro"` instead of the code
- Forgetting that JPY has no decimal places (amount is in yen, not sen)
- Not checking if the currency is supported in the user's country
- Hardcoding one currency instead of supporting multiple

## Related Pages

- [Stripe Amount Error]({{< relref "/tools/stripe/stripe-amount-error" >}}) — Amount must be at least 50 cents
- [Stripe Payment Intent Failed]({{< relref "/tools/stripe/stripe-payment-intent-failed" >}}) — PaymentIntent confirmation failed
