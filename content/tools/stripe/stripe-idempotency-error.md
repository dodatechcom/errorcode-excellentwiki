---
title: "[Solution] Stripe Idempotency Key Mismatch Error — Fix Request Conflicts"
description: "Fix Stripe idempotency key mismatch errors. Resolve duplicate request prevention and key management issues."
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["error"]
weight: 9
---

A Stripe idempotency key mismatch error occurs when you reuse an idempotency key but send a different request body. Idempotency keys prevent duplicate charges by caching the response for a given key.

## What This Error Means

When the idempotency key is reused with a different request, Stripe returns:

```json
{
  "error": {
    "type": "invalid_request_error",
    "code": "idempotency_mismatch",
    "message": "There was a conflict in the request"
  }
}
```

The key was already used for a successful request with different parameters, so Stripe refuses to execute a conflicting request.

## Why It Happens

- Reusing an idempotency key with different amounts or currencies
- The same key is sent from multiple servers with different data
- Retrying a failed request without changing the key
- Copying keys between different types of API calls
- The key expired (keys are valid for 24 hours) and was reused

## How to Fix It

### Generate Unique Idempotency Keys

```javascript
const { v4: uuidv4 } = require('uuid');

// Generate a unique key for each request
const idempotencyKey = uuidv4();

const paymentIntent = await stripe.paymentIntents.create(
  {
    amount: 2000,
    currency: 'usd',
    payment_method: 'pm_card_visa',
  },
  {
    idempotencyKey: idempotencyKey,
  }
);
```

### Use Meaningful Keys

```javascript
// Better: use descriptive keys for debugging
const key = `order_${orderId}_${Date.now()}`;
// e.g., "order_12345_1699900000000"

const payment = await stripe.charges.create(
  {
    amount: 2000,
    currency: 'usd',
    source: 'tok_visa',
  },
  {
    idempotencyKey: key,
  }
);
```

### Handle Key Conflicts Gracefully

```javascript
async function safeCharge(amount, currency, key) {
  try {
    return await stripe.charges.create(
      { amount, currency },
      { idempotencyKey: key }
    );
  } catch (error) {
    if (error.code === 'idempotency_mismatch') {
      // Generate a new key and retry once
      const newKey = `${key}_${Date.now()}`;
      return await stripe.charges.create(
        { amount, currency },
        { idempotencyKey: newKey }
      );
    }
    throw error;
  }
}
```

### Python Example

```python
import stripe
import uuid

# Generate unique key per request
idempotency_key = str(uuid.uuid4())

payment = stripe.PaymentIntent.create(
    amount=2000,
    currency='usd',
    idempotency_key=idempotency_key,
)
```

### Key Rotation Strategy

```javascript
function generateIdempotencyKey(operation, entityId) {
  // Combine operation type, entity ID, and timestamp
  const timestamp = Math.floor(Date.now() / 1000);
  return `${operation}_${entityId}_${timestamp}`;
}

// Usage
const key = generateIdempotencyKey('charge', 'order_123');
// "charge_order_123_1699900000"
```

## Common Mistakes

- Reusing the same key for different payment amounts
- Hardcoding idempotency keys in source code
- Not using idempotency keys at all (risk of duplicate charges)
- Sharing keys across different microservices
- Using sequential keys that could be guessed

## Related Pages

- [Stripe Rate Limit Error]({{< relref "/tools/stripe/stripe-rate-limit" >}}) — Too Many Requests (429)
- [Stripe Payment Intent Failed]({{< relref "/tools/stripe/stripe-payment-intent-failed" >}}) — PaymentIntent confirmation failed
