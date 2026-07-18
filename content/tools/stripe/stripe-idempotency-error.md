---
title: "[Solution] Stripe Idempotency Key Reusage Error — How to Fix"
description: "Fix Stripe idempotency key errors by generating unique keys per request, understanding key expiration rules, and handling key reuse correctly"
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
comments: true
---

# Stripe Idempotency Key Reusage Error

This error means you are reusing an idempotency key for a request that differs from the original. Stripe caches the result of the first request and returns it for any subsequent request with the same key, but only if the request parameters match exactly.

## Why It Happens

- The same idempotency key is used for requests with different parameters
- The idempotency key has not expired and you are retrying with changed data
- Two different code paths accidentally use the same key generator
- The idempotency key is hardcoded instead of being generated per-operation
- A retry mechanism reuses the key but the original request already succeeded
- The key was used more than 24 hours ago and Stripe purged the cached response

## Common Error Messages

```
{
  "error": {
    "type": "invalid_request_error",
    "code": "idempotency_mismatch",
    "message": "Idempotency key parameters differ from original request."
  }
}
```

```
{
  "error": {
    "type": "invalid_request_error",
    "code": "idempotency_mismatch",
    "message": "Keys must be unique strings."
  }
}
```

```
{
  "error": {
    "type": "invalid_request_error",
    "code": "idempotency_mismatch",
    "message": "An idempotency key was used with a different request."
  }
}
```

## How to Fix It

### 1. Generate Unique Idempotency Keys Per Request

```javascript
const { v4: uuidv4 } = require('uuid');

// Generate a unique key for every new operation
const idempotencyKey = uuidv4();

const paymentIntent = await stripe.paymentIntents.create(
  {
    amount: 2000,
    currency: 'usd',
    customer: 'cus_abc123'
  },
  {
    idempotencyKey: idempotencyKey
  }
);
```

### 2. Use Meaningful Idempotency Keys

```python
import stripe
import uuid

def create_subscription(customer_id, price_id):
    # Use a key that ties to the specific business operation
    idempotency_key = f"sub-{customer_id}-{price_id}-{uuid.uuid4()}"

    return stripe.Subscription.create(
        customer=customer_id,
        items=[{"price": price_id}],
        idempotency_key=idempotency_key
    )
```

### 3. Never Reuse Keys for Different Data

```javascript
// WRONG: Reusing key for different amounts
const key = 'payment-001';

await stripe.paymentIntents.create({ amount: 2000, currency: 'usd' }, { idempotencyKey: key });
await stripe.paymentIntents.create({ amount: 5000, currency: 'usd' }, { idempotencyKey: key }); // ERROR!

// RIGHT: Generate a new key for each payment
await stripe.paymentIntents.create({ amount: 2000, currency: 'usd' }, { idempotencyKey: uuidv4() });
await stripe.paymentIntents.create({ amount: 5000, currency: 'usd' }, { idempotencyKey: uuidv4() });
```

### 4. Safe Retry with Idempotency

```javascript
async function safeCharge(amount, customerId) {
  // Check if a charge was already made for this order
  const existing = await stripe.paymentIntents.list({
    customer: customerId,
    limit: 1
  });

  if (existing.data.length > 0 && existing.data[0].status !== 'failed') {
    return existing.data[0]; // Return existing, don't create new
  }

  // Create new with unique key
  return stripe.paymentIntents.create({
    amount,
    currency: 'usd',
    customer: customerId
  }, {
    idempotencyKey: `charge-${customerId}-${Date.now()}`
  });
}
```

## Common Scenarios

- **Retry after network timeout**: The first request succeeded but the client got a timeout. On retry, use the same key and identical parameters — Stripe returns the cached result safely.
- **Webhook + API overlap**: A webhook creates a subscription while the customer also clicks "subscribe" on the frontend. Each path should use a different idempotency key.
- **Load balancer retries**: The load balancer retries a request to a different backend. The idempotency key must be present in the request body, not just headers.

## Prevent It

- Generate idempotency keys using UUIDs or ULIDs, never hardcoded values
- Include the operation type, resource ID, and timestamp in the key for debugging
- Store the idempotency key with the transaction record so retries can reuse it safely

## Related Pages

- [Stripe Rate Limit Error](/tools/stripe/stripe-rate-limit-error)
- [Stripe Webhook Error](/tools/stripe/stripe-webhook-error)
- [Stripe Charge Disputed](/tools/stripe/stripe-charge-disputed)
