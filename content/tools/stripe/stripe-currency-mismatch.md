---
title: "[Solution] Stripe Currency Mismatch Error - Fix Currency Mismatch for Customer"
description: "Fix Stripe currency mismatch errors when charging customers in the wrong currency. Handle multi-currency payments and balance constraints."
tools: ["stripe"]
error-types: ["currency-mismatch"]
severities: ["error"]
weight: 5
---

This error means the currency of the charge does not match the customer's default currency or the account's supported currencies. Stripe rejects the transaction due to currency constraints.

## What This Error Means

When there is a currency mismatch, Stripe returns:

```
InvalidRequestError: This customer has no attached payment source capable of charging in USD
# or
Currency mismatch: the customer's default currency does not match the charge currency
```

Stripe accounts and customers have currency constraints that must align with the charge.

## Why It Happens

- The charge currency differs from the customer's default currency
- The payment method does not support the requested currency
- The Stripe account does not have the currency enabled
- You are charging in a currency that requires specific configuration
- The customer's bank does not support the charge currency
- A subscription is set to a different currency than the payment method

## How to Fix It

### Check the customer's default currency

```python
customer = stripe.Customer.retrieve('cus_xxx')
print(customer.currency)
```

Ensure the charge currency matches the customer's currency.

### Set the correct currency on the charge

```python
stripe.PaymentIntent.create(
    amount=2000,
    currency='eur',  # Match the customer's currency
    customer='cus_xxx',
    payment_method='pm_xxx',
    confirm=True,
)
```

### Check supported currencies for the account

```python
balance = stripe.Balance.retrieve()
for currency in balance.available:
    print(currency.currency, currency.amount)
```

Your Stripe account must support the currency you are charging in.

### Convert amounts for multi-currency payments

```python
# Customer pays in EUR, your account settles in USD
stripe.PaymentIntent.create(
    amount=2000,  # Amount in cents for EUR
    currency='eur',
    customer='cus_xxx',
    payment_method='pm_xxx',
    confirm=True,
)
```

Stripe handles the conversion automatically.

### Update the customer's currency

```python
stripe.Customer.modify(
    'cus_xxx',
    currency='usd'
)
```

Only certain customer properties can be modified after creation.

### Use the payment currency on the payment method

```python
# List payment methods and check supported currencies
methods = stripe.PaymentMethod.list(
    customer='cus_xxx',
    type='card',
)
```

Different payment methods support different currencies.

### Enable multi-currency in your Stripe dashboard

Go to Settings > Payment Methods and enable the currencies you want to accept.

## Common Mistakes

- Assuming all payment methods support all currencies
- Not checking the customer's default currency before creating charges
- Using the wrong currency code format (must be lowercase ISO 4217)
- Not enabling multi-currency in the Stripe dashboard
- Charging in a currency that the customer's bank does not support

## Related Pages

- [Stripe Currency Error]({{< relref "/tools/stripe/stripe-currency-error" >}}) -- currency configuration
- [Stripe Payment Intent Failed]({{< relref "/tools/stripe/stripe-payment-intent-failed" >}}) -- payment processing
- [Stripe Card Declined]({{< relref "/tools/stripe/stripe-card-declined" >}}) -- card decline errors
