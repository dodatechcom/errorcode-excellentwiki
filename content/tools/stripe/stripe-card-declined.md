---
title: "[Solution] Stripe Card Declined Error — Your Card Was Declined"
description: "Fix Stripe card declined errors. Resolve payment failures caused by insufficient funds, expired cards, or bank declines."
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["error"]
weight: 2
---

A Stripe card declined error occurs when the customer's card is rejected by the issuing bank during a payment attempt. Stripe passes through the decline reason from the card network so you can display an appropriate message.

## What This Error Means

When Stripe attempts to charge a card and the bank rejects it, you receive a `card_declined` error. The full error response looks like:

```json
{
  "error": {
    "type": "card_error",
    "code": "card_declined",
    "decline_code": "insufficient_funds",
    "message": "Your card has insufficient funds."
  }
}
```

The `decline_code` field tells you exactly why the card was declined.

## Why It Happens

- The card has insufficient funds
- The card is expired or has an incorrect CVC
- The bank does not allow the transaction type
- The card has reached its credit limit
- The bank suspects fraud and blocks the transaction
- The card is not enabled for international or online purchases
- The cardholder's bank is temporarily unavailable

## How to Fix It

### Handle Decline Codes in Code

```javascript
try {
  const paymentIntent = await stripe.paymentIntents.create({
    amount: 2000,
    currency: 'usd',
    payment_method: 'pm_card_visa',
    confirm: true,
  });
} catch (error) {
  if (error.type === 'card_error') {
    const declineCode = error.decline_code;
    switch (declineCode) {
      case 'insufficient_funds':
        showCustomerMessage('Your card has insufficient funds.');
        break;
      case 'expired_card':
        showCustomerMessage('Your card has expired. Please use a different card.');
        break;
      case 'incorrect_cvc':
        showCustomerMessage('The CVC number is incorrect.');
        break;
      default:
        showCustomerMessage('Your card was declined. Please try another card.');
    }
  }
}
```

### Common Decline Codes

| Decline Code | Meaning |
|---|---|
| `insufficient_funds` | Not enough money on the card |
| `expired_card` | Card expiration date has passed |
| `incorrect_cvc` | CVC verification failed |
| `lost_card` | Card reported lost |
| `stolen_card` | Card reported stolen |
| `generic_decline` | Bank gave no specific reason |
| `do_not_honor` | Bank declined without explanation |

### Retry with Different Payment Method

```javascript
// Offer the customer a different payment method
const paymentIntent = await stripe.paymentIntents.create({
  amount: 2000,
  currency: 'usd',
  payment_method_types: ['card', 'us_bank_account'],
});
```

## Common Mistakes

- Displaying raw error messages to customers instead of user-friendly text
- Not retrying with a different payment method
- Treating all decline codes the same way
- Not logging decline codes for analytics
- Failing to distinguish between soft declines (retryable) and hard declines (permanent)

## Related Pages

- [Stripe Payment Intent Failed]({{< relref "/tools/stripe/stripe-payment-intent-failed" >}}) — PaymentIntent confirmation failed
- [Stripe Balance Insufficient]({{< relref "/tools/stripe/stripe-balance-insufficient" >}}) — Insufficient funds in Stripe balance
