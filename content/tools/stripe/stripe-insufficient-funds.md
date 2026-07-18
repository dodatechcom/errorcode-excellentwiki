---
title: "[Solution] Stripe Insufficient Funds Error - Fix Card Has Insufficient Funds"
description: "Fix Stripe insufficient funds errors when charges fail. Implement retry logic, soft decline handling, and payment recovery strategies."
tools: ["stripe"]
error-types: ["insufficient-funds"]
severities: ["error"]
weight: 5
---

This error means the customer's card does not have enough available balance to complete the charge. Stripe declines the transaction due to insufficient funds.

## What This Error Means

When a charge exceeds the available balance on the card, Stripe returns:

```
CardError: Your card has insufficient funds.
```

The decline code is `insufficient_funds`. This is one of the most common card decline reasons and may be temporary if the customer has pending deposits.

## Why It Happens

- The card's available balance is less than the charge amount
- The customer's bank has placed a hold on some funds
- A pending transaction has not yet cleared
- The charge amount includes currency conversion that exceeds the balance
- Pre-authorization holds are consuming available credit
- The customer's daily spending limit has been reached

## How to Fix It

### Handle the error gracefully

```javascript
try {
  await stripe.paymentIntents.create({
    amount: 5000,
    currency: 'usd',
    customer: 'cus_xxx',
    payment_method: 'pm_xxx',
    confirm: true,
  });
} catch (error) {
  if (error.decline_code === 'insufficient_funds') {
    // Ask customer to use a different payment method
  }
}
```

### Implement smart retries

```python
# Stripe automatically retries with smart timing
stripe.PaymentIntent.create(
    amount=2000,
    currency='usd',
    customer='cus_xxx',
    payment_method='pm_xxx',
    confirm=True,
    error_on_requires_action=True,
    payment_behavior='error_if_incomplete'
)
```

### Allow customers to use a different payment method

```javascript
// Redirect to payment method update flow
const paymentMethod = await stripe.paymentMethods.create({
  type: 'card',
  card: { token: 'tok_new_card' },
});

await stripe.paymentIntents.update('pi_xxx', {
  payment_method: 'pm_new_card',
});
```

### Handle subscription payment failures

```python
# Enable failed payment handling on subscriptions
stripe.Subscription.modify(
    'sub_xxx',
    payment_behavior='default_incomplete',
    payment_settings={
        'save_default_payment_method': 'on_subscription'
    },
    pending_invoice_item_interval={
        'interval': 'month'
    }
)
```

### Use Stripe's retry logic

```python
# Configure automatic retries for soft declines
stripe.PaymentIntent.create(
    amount=2000,
    currency='usd',
    customer='cus_xxx',
    off_session=True,
    confirm=True,
    payment_behavior='allow_incomplete'
)
```

### Offer alternative payment methods

```javascript
const paymentMethods = await stripe.paymentMethods.list({
  customer: 'cus_xxx',
  type: 'card',
});
```

Suggest the customer try a different card if available.

## Common Mistakes

- Not distinguishing between hard declines (permanent) and soft declines (temporary)
- Not retrying failed charges at different times
- Failing to notify customers about failed subscription payments
- Assuming insufficient funds means the card is permanently invalid
- Not offering alternative payment methods when a card fails repeatedly

## Related Pages

- [Stripe Card Declined]({{< relref "/tools/stripe/stripe-card-declined" >}}) -- card decline errors
- [Stripe Payment Intent Failed]({{< relref "/tools/stripe/stripe-payment-intent-failed" >}}) -- payment processing
- [Stripe Subscription Error]({{< relref "/tools/stripe/stripe-subscription-error" >}}) -- subscription issues
