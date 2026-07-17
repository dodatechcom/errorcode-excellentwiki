---
title: "[Solution] Stripe Customer Error — No Such Customer Found"
description: "Fix Stripe no such customer errors. Resolve customer ID lookup failures and deletion issues in Stripe API."
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["error"]
weight: 6
---

A Stripe customer error occurs when you reference a customer ID that does not exist, has been deleted, or is formatted incorrectly. Every customer operation requires a valid customer ID that starts with `cus_`.

## What This Error Means

When Stripe cannot find the customer, it returns:

```json
{
  "error": {
    "type": "invalid_request_error",
    "param": "customer",
    "code": "resource_missing",
    "message": "No such customer: cus_invalid123"
  }
}
```

This means the customer ID passed to the API does not match any customer in your Stripe account.

## Why It Happens

- The customer was deleted but the ID is still in your database
- The customer ID is mistyped or corrupted
- You are using a test key but referencing a live customer ID (or vice versa)
- The customer ID belongs to a different Stripe account
- The ID format is wrong (e.g., missing the `cus_` prefix)

## How to Fix It

### Verify Customer Exists

```javascript
try {
  const customer = await stripe.customers.retrieve('cus_abc123');
  console.log('Customer found:', customer.email);
} catch (error) {
  if (error.code === 'resource_missing') {
    console.log('Customer does not exist. Creating new one...');
    const newCustomer = await stripe.customers.create({
      email: 'user@example.com',
    });
  }
}
```

### Safe Customer Lookup

```javascript
async function getOrCreateCustomer(email, metadata = {}) {
  const existing = await stripe.customers.list({
    email: email,
    limit: 1,
  });

  if (existing.data.length > 0) {
    return existing.data[0];
  }

  return stripe.customers.create({
    email,
    metadata,
  });
}

// Usage
const customer = await getOrCreateCustomer('user@example.com', {
  source: 'registration',
});
```

### Clean Up Deleted Customers

```python
import stripe

# Check if customer still exists
def safe_retrieve_customer(customer_id):
    try:
        return stripe.Customer.retrieve(customer_id)
    except stripe.error.InvalidRequestError as e:
        if e.code == 'resource_missing':
            # Customer was deleted, create new one
            return stripe.Customer.create(
                email="user@example.com"
            )
        raise
```

### Sync Customer Data

```javascript
// Periodically verify customer IDs in your database
async function validateCustomerIds(customerIds) {
  const valid = [];
  const invalid = [];

  for (const id of customerIds) {
    try {
      await stripe.customers.retrieve(id);
      valid.push(id);
    } catch (error) {
      if (error.code === 'resource_missing') {
        invalid.push(id);
      }
    }
  }

  return { valid, invalid };
}
```

## Common Mistakes

- Storing customer IDs without validating they exist first
- Not handling deleted customers in subscription flows
- Mixing test and live customer IDs across environments
- Using `cus_` IDs from webhooks that reference deleted customers
- Not implementing fallback logic for missing customers

## Related Pages

- [Stripe Payment Intent Failed]({{< relref "/tools/stripe/stripe-payment-intent-failed" >}}) — PaymentIntent confirmation failed
- [Stripe Authentication Error]({{< relref "/tools/stripe/stripe-authentication-error" >}}) — No API key provided or invalid key
