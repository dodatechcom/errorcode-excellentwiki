---
title: "[Solution] Stripe Payment Intent Unexpected State"
description: "Fix Stripe payment intent state errors. Handle payment intent lifecycle and state transitions."
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
comments: true
---

## Error Description

The Stripe API returned a `unexpected_state` error. This error occurs when a payment or API operation fails due to a specific condition that must be addressed.

A typical error:

```
{
  "error": {
    "type": "card_error",
    "code": "unexpected_state",
    "message": "Your card was declined.",
    "param": "source"
  }
}
```

## Common Causes

- **Invalid input**: The data sent to the API does not meet validation requirements.
- **Authentication failure**: The API key is invalid, expired, or lacks required permissions.
- **Resource not found**: The requested object does not exist or was deleted.
- **Rate limiting**: Too many requests sent in a short time period.
- **Processing failure**: The payment network or bank rejected the transaction.

## How to Fix It

**Step 1: Check the error response**

```python
import stripe
stripe.api_key = "sk_test_..."

try:
    charge = stripe.Charge.create(
        amount=2000,
        currency="usd",
        source="tok_visa",
    )
except stripe.error.CardError as e:
    print(f"Card declined: {e.user_message}")
    print(f"Error code: {e.code}")
except stripe.error.RateLimitError:
    print("Too many requests - retry later")
except stripe.error.InvalidRequestError as e:
    print(f"Invalid parameters: {e}")
except stripe.error.AuthenticationError:
    print("Authentication failed - check API key")
except stripe.error.APIConnectionError:
    print("Network error - check connectivity")
except stripe.error.StripeError as e:
    print(f"General error: {e}")
```

**Step 2: Implement proper error handling**

```python
import time

def create_charge_with_retry(amount, currency, source, max_retries=3):
    for attempt in range(max_retries):
        try:
            return stripe.Charge.create(
                amount=amount,
                currency=currency,
                source=source,
            )
        except stripe.error.RateLimitError:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
                continue
            raise
        except stripe.error.CardError:
            raise
```

**Step 3: Validate inputs before sending**

```python
def validate_charge_params(amount, currency):
    if amount < 50:
        raise ValueError("Amount must be at least 50 cents")
    if currency not in ["usd", "eur", "gbp"]:
        raise ValueError("Unsupported currency")
    return True
```

## Common Scenarios

**Testing with test mode.**
Use Stripe test cards like `4242 4242 4242 4242` for testing. Different card numbers trigger different error scenarios.

**Production payments.**
Always validate customer input on the client and server side. Handle errors gracefully and provide clear feedback to customers.

## Prevention

1. Use Stripe.js and Elements for secure card collection
2. Validate inputs on both client and server
3. Implement idempotency keys for all create operations
4. Monitor Stripe dashboard for error rate increases
