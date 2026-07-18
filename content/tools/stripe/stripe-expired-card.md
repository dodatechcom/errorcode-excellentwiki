---
title: "[Solution] Stripe Expired Card Error - Fix Your Card Has Expired"
description: "Fix Stripe expired card errors when payment fails. Handle card expiration, update payment methods, and implement dunning strategies."
tools: ["stripe"]
error-types: ["expired-card"]
severities: ["error"]
weight: 5
---

This error means the customer's card has passed its expiration date. Stripe declines the charge because the card is no longer valid for transactions.

## What This Error Means

When you attempt to charge an expired card, Stripe returns:

```
CardError: Your card has expired.
```

The error includes a decline code of `expired_card`. This is a soft decline that occurs during payment processing when the card's expiration month or year has passed.

## Why It Happens

- The customer's card has expired and they have not updated it
- The expiration date in your stored payment method is outdated
- A test card with an expired date was used in live mode
- The card was reissued by the bank with a new expiration date
- Tokenized card data from a payment element still references the old card

## How to Fix It

### Prompt the customer to update their card

```javascript
const stripe = require('stripe')('sk_test_...');

try {
  await stripe.paymentIntents.create({
    amount: 2000,
    currency: 'usd',
    customer: 'cus_xxx',
    payment_method: 'pm_xxx',
    confirm: true,
  });
} catch (error) {
  if (error.code === 'card_error' && error.decline_code === 'expired_card') {
    // Redirect customer to update payment method
  }
}
```

### Handle the error in your frontend

```javascript
const { error } = await stripe.confirmCardPayment(clientSecret, {
  payment_method: {
    card: cardElement,
    billing_details: { name: 'Customer' }
  }
});

if (error && error.decline_code === 'expired_card') {
  showError('Your card has expired. Please use a different card.');
}
```

### Update the customer's payment method

```python
stripe.PaymentMethod.attach(
    'pm_new_card',
    customer='cus_xxx'
)

stripe.Customer.modify(
    'cus_xxx',
    invoice_settings={
        'default_payment_method': 'pm_new_card'
    }
)
```

### Implement Stripe's automatic card updates

Stripe automatically updates expired cards when banks participate in card account updater programs. Enable this in your Stripe dashboard under Settings > Payment Methods.

### Use SetupIntents for card-on-file

```javascript
const setupIntent = await stripe.setupIntents.create({
  customer: 'cus_xxx',
  payment_method_types: ['card'],
});
```

SetupIntents let customers update their card without charging immediately.

### Send dunning emails for subscription failures

```python
stripe.Subscription.modify(
    'sub_xxx',
    payment_behavior='default_incomplete',
    payment_settings={
        'save_default_payment_method': 'on_subscription'
    }
)
```

## Common Mistakes

- Not providing a way for customers to update expired cards
- Assuming Stripe automatically retries expired card charges
- Not using Stripe's card updater service
- Treating expired card errors as permanent instead of asking for new payment info
- Not sending notifications before subscription cards expire

## Related Pages

- [Stripe Card Declined]({{< relref "/tools/stripe/stripe-card-declined" >}}) -- card decline errors
- [Stripe Payment Intent Failed]({{< relref "/tools/stripe/stripe-payment-intent-failed" >}}) -- payment processing
- [Stripe Subscription Error]({{< relref "/tools/stripe/stripe-subscription-error" >}}) -- subscription issues
