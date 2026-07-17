---
title: "[Solution] Stripe Amount Error — Amount Must Be at Least 50 Cents"
description: "Fix Stripe amount validation errors. Resolve minimum amount requirements and currency-specific amount constraints."
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["error"]
weight: 4
---

A Stripe amount error occurs when the payment amount is below the minimum threshold or in an invalid format. Stripe requires amounts in the smallest currency unit (cents for USD) with specific minimums per currency.

## What This Error Means

When you create a charge or payment intent with an amount below the minimum, Stripe returns:

```json
{
  "error": {
    "type": "invalid_request_error",
    "param": "amount",
    "message": "Amount must be at least 50 cents"
  }
}
```

The minimum amount varies by currency. For USD, it is 50 cents (50 in the API). For JPY, it is 50 yen (50 in the API since JPY has no decimal places).

## Why It Happens

- Passing the amount in dollars instead of cents (e.g., 5 instead of 500)
- Forgetting to convert the amount to the smallest currency unit
- Sending zero or negative amounts
- Using floating point numbers that produce unexpected values
- Not accounting for currency-specific minimums

## How to Fix It

### Convert to Smallest Currency Unit

```javascript
// WRONG: Sending dollars
const amountWrong = 5.00;

// RIGHT: Sending cents
const amountCorrect = 500;

const paymentIntent = await stripe.paymentIntents.create({
  amount: amountCorrect, // 500 = $5.00 USD
  currency: 'usd',
});
```

### Safe Conversion Function

```javascript
function dollarsToCents(amount) {
  return Math.round(amount * 100);
}

// Usage
const amount = dollarsToCents(19.99); // 1999
const paymentIntent = await stripe.paymentIntents.create({
  amount,
  currency: 'usd',
});
```

### Python Example

```python
import stripe

# Convert dollars to cents
amount_in_cents = int(19.99 * 100)  # 1999

payment_intent = stripe.PaymentIntent.create(
    amount=amount_in_cents,
    currency='usd',
)
```

### Check Minimum Per Currency

```javascript
const minimumAmounts = {
  usd: 50,   // $0.50
  eur: 50,   // 0.50 EUR
  gbp: 30,   // 0.30 GBP
  jpy: 50,   // 50 JPY (no decimals)
  aud: 50,   // $0.50 AUD
};

function validateAmount(currency, amount) {
  const min = minimumAmounts[currency.toLowerCase()] || 50;
  if (amount < min) {
    throw new Error(`Minimum for ${currency} is ${min}`);
  }
}
```

### Validate Before Sending

```javascript
function createPayment(amountInDollars, currency) {
  const amount = Math.round(amountInDollars * 100);

  if (amount < 50) {
    throw new Error('Payment amount must be at least $0.50');
  }

  return stripe.paymentIntents.create({
    amount,
    currency,
  });
}
```

## Common Mistakes

- Passing 5.00 instead of 500 for a $5.00 charge
- Using `parseFloat` which can produce rounding errors
- Not checking the minimum amount before API calls
- Ignoring currency-specific minimums for international payments
- Sending amounts as strings instead of integers

## Related Pages

- [Stripe Currency Error]({{< relref "/tools/stripe/stripe-currency-error" >}}) — Invalid currency code
- [Stripe Payment Intent Failed]({{< relref "/tools/stripe/stripe-payment-intent-failed" >}}) — PaymentIntent confirmation failed
