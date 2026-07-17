---
title: "[Solution] Stripe PaymentIntent Failed — Payment Confirmation Error"
description: "Fix Stripe PaymentIntent confirmation failures. Resolve payment processing errors and failed charge attempts."
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["error"]
weight: 7
---

A Stripe PaymentIntent failed error occurs when a payment cannot be confirmed or processed. PaymentIntent is Stripe's recommended way to accept payments, and failures can happen at multiple stages of the payment flow.

## What This Error Means

When a PaymentIntent fails, the response includes details about the failure:

```json
{
  "error": {
    "type": "invalid_request_error",
    "code": "payment_intent_unexpected_state",
    "message": "The payment intent could not be confirmed"
  }
}
```

The PaymentIntent status will be `requires_payment_method`, `requires_action`, or `requires_confirmation` depending on where the failure occurred.

## Why It Happens

- The payment method attached is invalid or expired
- The customer did not complete 3D Secure authentication
- The card was declined by the issuing bank
- The amount exceeds the card's limit
- The PaymentIntent is in an unexpected state
- Required parameters are missing from the confirmation call
- The payment method does not match the currency

## How to Fix It

### Handle PaymentIntent Lifecycle

```javascript
async function processPayment(amount, currency, paymentMethodId) {
  // Step 1: Create the PaymentIntent
  const paymentIntent = await stripe.paymentIntents.create({
    amount,
    currency,
    payment_method: paymentMethodId,
    confirm: false, // Don't confirm immediately
  });

  // Step 2: Confirm when ready
  try {
    const confirmed = await stripe.paymentIntents.confirm(
      paymentIntent.id
    );

    // Step 3: Handle the result
    if (confirmed.status === 'succeeded') {
      return { success: true, paymentIntent: confirmed };
    }

    if (confirmed.status === 'requires_action') {
      return {
        success: false,
        requiresAction: true,
        clientSecret: confirmed.client_secret,
      };
    }

    return { success: false, status: confirmed.status };
  } catch (error) {
    return { success: false, error: error.message };
  }
}
```

### Handle 3D Secure

```javascript
const stripe = Stripe('sk_test_your_key');

async function handleCardPayment(clientSecret) {
  const { error, paymentIntent } = await stripe.confirmCardPayment(
    clientSecret,
    {
      payment_method: {
        card: cardElement,
        billing_details: {
          name: 'Jenny Rosen',
        },
      },
    }
  );

  if (error) {
    console.error('Payment failed:', error.message);
  } else if (paymentIntent.status === 'succeeded') {
    console.log('Payment succeeded!');
  }
}
```

### Python Example

```python
import stripe
stripe.api_key = "sk_test_your_key"

try:
    intent = stripe.PaymentIntent.create(
        amount=2000,
        currency='usd',
        payment_method='pm_card_visa',
        confirm=True,
    )
    print(f"Status: {intent.status}")
except stripe.error.CardError as e:
    print(f"Card declined: {e.user_message}")
except stripe.error.InvalidRequestError as e:
    print(f"Invalid request: {e}")
```

### Retry Failed Confirmations

```javascript
async function confirmWithRetry(paymentIntentId, maxAttempts = 3) {
  for (let i = 0; i < maxAttempts; i++) {
    try {
      return await stripe.paymentIntents.confirm(paymentIntentId);
    } catch (error) {
      if (error.code !== 'payment_intent_unexpected_state') {
        throw error;
      }
      await new Promise(r => setTimeout(r, 1000 * (i + 1)));
    }
  }
  throw new Error('Failed to confirm after retries');
}
```

## Common Mistakes

- Not handling the `requires_action` status for 3D Secure
- Confirming a PaymentIntent that is already confirmed
- Using the wrong payment method ID
- Not updating the PaymentIntent when the customer changes cards
- Forgetting to handle network errors during confirmation

## Related Pages

- [Stripe Card Declined]({{< relref "/tools/stripe/stripe-card-declined" >}}) — Your card was declined
- [Stripe Amount Error]({{< relref "/tools/stripe/stripe-amount-error" >}}) — Amount must be at least 50 cents
