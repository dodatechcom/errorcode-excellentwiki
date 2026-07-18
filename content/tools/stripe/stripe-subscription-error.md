---
title: "[Solution] Stripe Subscription Error - Fix Subscription Update Failed"
description: "Fix Stripe subscription update failures. Resolve proration, plan changes, payment method, and subscription lifecycle errors."
tools: ["stripe"]
error-types: ["subscription-error"]
severities: ["error"]
weight: 5
---

This error means a subscription operation failed. Updating, creating, or canceling a subscription encountered an error with pricing, payment, or subscription state.

## What This Error Means

When a subscription operation fails, Stripe returns:

```
InvalidRequestError: No such subscription: sub_xxx
# or
CardError: This payment method does not support the requested currency
# or
InvalidRequestError: You cannot update a subscription that is already canceled
```

Subscription errors span multiple categories: invalid subscription ID, payment failures, plan incompatibilities, and state conflicts.

## Why It Happens

- The subscription ID does not exist or belongs to a different account
- The subscription is already canceled and cannot be updated
- The new plan is incompatible with the current subscription
- The payment method attached to the subscription is expired or invalid
- Proration calculations failed due to billing cycle issues
- The subscription update requires customer confirmation but none was provided
- The plan price does not exist or has been deleted

## How to Fix It

### Verify the subscription exists

```python
subscription = stripe.Subscription.retrieve('sub_xxx')
print(subscription.status)
```

Check the subscription status and ensure it is active.

### Update subscription items

```python
stripe.Subscription.modify(
    'sub_xxx',
    items=[{
        'id': 'si_xxx',
        'price': 'price_new',
    }],
    proration_behavior='create_prorations',
)
```

### Handle failed payment on subscription update

```python
subscription = stripe.Subscription.modify(
    'sub_xxx',
    items=[{
        'id': 'si_xxx',
        'price': 'price_new',
    }],
    payment_behavior='error_if_incomplete',
)
```

### Cancel a subscription safely

```python
stripe.Subscription.modify(
    'sub_xxx',
    cancel_at_period_end=True,
)
```

Canceling at period end avoids immediate proration.

### Update the payment method first

```python
stripe.PaymentMethod.attach('pm_new_card', customer='cus_xxx')
stripe.Customer.modify(
    'cus_xxx',
    invoice_settings={'default_payment_method': 'pm_new_card'}
)
```

### Handle trial subscriptions

```python
stripe.Subscription.modify(
    'sub_xxx',
    trial_end='now',
    items=[{'price': 'price_new'}],
)
```

### Delete an outdated price

```python
stripe.Product.modify('prod_xxx', active=False)
```

Deactivating a product stops new subscriptions but preserves existing ones.

## Common Mistakes

- Trying to update a canceled subscription instead of creating a new one
- Not checking if the subscription is in a trial period before modifying
- Deleting prices that are still used by active subscriptions
- Not providing a payment method when switching to a paid plan
- Assuming proration is automatic without setting `proration_behavior`

## Related Pages

- [Stripe Payment Intent Failed]({{< relref "/tools/stripe/stripe-payment-intent-failed" >}}) -- payment processing
- [Stripe Invoice Error]({{< relref "/tools/stripe/stripe-invoice-error" >}}) -- invoice failures
- [Stripe Customer Error]({{< relref "/tools/stripe/stripe-customer-error" >}}) -- customer management
