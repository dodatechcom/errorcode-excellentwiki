---
title: "[Solution] Stripe Invoice Error - Fix Invoice Payment Failed"
description: "Fix Stripe invoice payment failures. Resolve automatic payment, manual payment, and invoice collection issues for subscriptions."
tools: ["stripe"]
error-types: ["invoice-error"]
severities: ["error"]
weight: 5
---

This error means a Stripe invoice failed to collect payment. The automatic or manual payment attempt was declined or the invoice configuration is invalid.

## What This Error Means

When an invoice fails to collect payment, you see:

```
InvalidRequestError: Invoice collection failed
# or
CardError: Payment failed for invoice in_xxx
# or
InvalidRequestError: Cannot finalize an invoice with no line items
```

Invoice errors occur during creation, finalization, payment, or voiding of invoices. Failed invoice payments can cause subscription suspensions.

## Why It Happens

- The customer's default payment method is invalid or expired
- The invoice amount exceeds the card's remaining balance
- The invoice was manually created without line items
- The subscription's latest invoice is in an uncollectible state
- The payment intent associated with the invoice requires authentication
- The invoice was finalized but the payment method was removed

## How to Fix It

### Retrieve the failed invoice

```python
invoice = stripe.Invoice.retrieve('in_xxx')
print(invoice.status)  # open, paid, void, uncollectible
print(invoice.attempt_count)
```

### Retry payment on a failed invoice

```python
stripe.Invoice.pay('in_xxx')
```

### Update payment method before retrying

```python
stripe.PaymentMethod.attach('pm_new_card', customer='cus_xxx')
stripe.Customer.modify(
    'cus_xxx',
    invoice_settings={'default_payment_method': 'pm_new_card'}
)
stripe.Invoice.pay('in_xxx')
```

### Manually send an invoice

```python
stripe.Invoice.send_invoice('in_xxx')
```

For manually created invoices, send them to the customer.

### Void an incorrect invoice

```python
stripe.Invoice.void_invoice('in_xxx')
```

Voiding prevents further payment attempts on an invoice.

### Mark an invoice as uncollectible

```python
stripe.Invoice.mark_uncollectible('in_xxx')
```

Use this for invoices that will never be paid.

### Finalize a draft invoice

```python
stripe.Invoice.finalize_invoice('in_xxx')
```

Draft invoices must be finalized before payment can be collected.

### Check invoice payment settings

```python
stripe.Subscription.modify(
    'sub_xxx',
    payment_settings={
        'save_default_payment_method': 'on_subscription'
    },
    collection_method='charge_automatically',
)
```

Ensure the collection method matches your intended payment flow.

## Common Mistakes

- Not monitoring failed invoices which can lead to subscription churn
- Not providing customers a way to update their payment method after failure
- Voiding invoices instead of marking them uncollectible when tracking is needed
- Not setting up webhooks for `invoice.payment_failed` events
- Assuming automatic retries will eventually succeed without customer action

## Related Pages

- [Stripe Subscription Error]({{< relref "/tools/stripe/stripe-subscription-error" >}}) -- subscription issues
- [Stripe Payment Intent Failed]({{< relref "/tools/stripe/stripe-payment-intent-failed" >}}) -- payment processing
- [Stripe Card Declined]({{< relref "/tools/stripe/stripe-card-declined" >}}) -- card decline errors
