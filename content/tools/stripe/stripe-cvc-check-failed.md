---
title: "[Solution] Stripe CVC Check Failed - Fix Security Code Incorrect"
description: "Fix Stripe CVC check failed errors when the card security code is incorrect. Handle CVC validation and implement verification strategies."
tools: ["stripe"]
error-types: ["cvc-check-failed"]
severities: ["error"]
weight: 5
---

This error means the CVC (Card Verification Code) the customer entered does not match what the issuing bank has on file. Stripe declines the transaction due to CVC mismatch.

## What This Error Means

When a CVC check fails, Stripe returns:

```
CardError: Your card's security code is incorrect.
```

The decline code is `incorrect_cvc`. This is a security measure to prevent fraud when the physical card or its details are not available.

## Why It Happens

- The customer typed the CVC incorrectly
- The CVC on the back of the card is being misread
- The card was recently reissued with a new CVC
- The customer is using a stored CVC from an old card
- A test card's CVC does not match the test number
- The issuing bank's CVC database is out of sync

## How to Fix It

### Validate CVC format on the frontend

```javascript
const cardElement = elements.create('card', {
  style: {
    base: {
      fontSize: '16px',
    },
  },
});

// Stripe Elements validates CVC format automatically
const { error, paymentMethod } = await stripe.createPaymentMethod({
  type: 'card',
  card: cardElement,
});
```

Stripe Elements automatically validates CVC length and format before submission.

### Handle the error with a retry option

```javascript
try {
  await stripe.paymentIntents.confirm('pi_xxx', {
    payment_method: 'pm_xxx',
  });
} catch (error) {
  if (error.decline_code === 'incorrect_cvc') {
    // Show message asking customer to check their CVC
    showError('The security code you entered is incorrect. Please try again.');
  }
}
```

### Use CVC check results for fraud prevention

```python
payment_intent = stripe.PaymentIntent.retrieve('pi_xxx')
cvc_check = payment_intent.charges.data[0].payment_method_details.card.cvc_check
# 'pass', 'fail', 'unavailable', 'unchecked'
```

### Do not store CVC

```python
# Never store CVC after payment
# Stripe does not allow CVC storage
```

CVC must never be stored after authorization per PCI DSS.

### Provide clear error messages

```javascript
if (error.decline_code === 'incorrect_cvc') {
  showMessage('The security code (CVV) on your card is incorrect. Please check the 3-digit code on the back of your card.');
}
```

### Use 3D Secure to shift liability

```javascript
const { error } = await stripe.confirmCardPayment(clientSecret, {
  payment_method: {
    card: cardElement,
    billing_details: { name: 'Customer' },
  },
  three_d_secure: {
    create: 'if_supported',
  },
});
```

3D Secure authentication shifts fraud liability to the issuing bank.

## Common Mistakes

- Storing CVC values, which violates PCI DSS
- Not using Stripe Elements which validates CVC before submission
- Showing cryptic error messages instead of helpful guidance
- Not distinguishing CVC failures from other card declines
- Not using 3D Secure for high-risk transactions

## Related Pages

- [Stripe Card Declined]({{< relref "/tools/stripe/stripe-card-declined" >}}) -- card decline errors
- [Stripe Expired Card]({{< relref "/tools/stripe/stripe-expired-card" >}}) -- card expiration
- [Stripe Payment Intent Failed]({{< relref "/tools/stripe/stripe-payment-intent-failed" >}}) -- payment processing
