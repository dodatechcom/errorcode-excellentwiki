---
title: "[Solution] Stripe Charge Has Been Disputed Error — How to Fix"
description: "Fix Stripe charge disputed errors by submitting evidence, preventing disputes with fraud detection, responding within deadlines, and managing chargeback workflows"
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["warning"]
weight: 5
comments: true
---

# Stripe Charge Has Been Disputed Error

This error means a customer or card issuer has initiated a dispute (chargeback) against one of your charges. The funds are automatically debited from your Stripe balance while the dispute is being resolved.

## Why It Happens

- The customer does not recognize the charge on their statement
- The product or service was not delivered as expected
- The customer is attempting friendly fraud (claiming they did not make the purchase)
- A duplicate charge was accidentally created
- The billing descriptor is unclear or does not match the business name
- No receipt or proof of delivery was provided to the customer
- The transaction was made without proper authentication (3D Secure)

## Common Error Messages

```
{
  "type": "event",
  "data": {
    "object": {
      "id": "dp_xxx",
      "status": "needs_response",
      "reason": "product_not_received",
      "amount": 5000
    }
  }
}
```

```
{
  "error": {
    "type": "invalid_request_error",
    "message": "Charge has already been disputed."
  }
}
```

```
{
  "status": "warning",
  "message": "Your Stripe account has a high dispute rate."
}
```

## How to Fix It

### 1. Retrieve the Dispute Details

```javascript
const dispute = await stripe.disputes.retrieve('dp_abc123');

console.log('Reason:', dispute.reason);
console.log('Amount:', dispute.amount);
console.log('Status:', dispute.status);
console.log('Evidence due by:', dispute.evidence_details.due_by);
```

### 2. Submit Evidence for the Dispute

```javascript
const dispute = await stripe.disputes.update('dp_abc123', {
  evidence: {
    customer_email_address: 'customer@example.com',
    customer_purchase_ip: '192.168.1.1',
    shipping_tracking_number: '1Z999AA10123456784',
    shipping_carrier: 'UPS',
    receipt_url: 'https://example.com/receipts/12345',
    service_date: '2025-01-15',
    service_detail: 'Digital subscription activated on 2025-01-15',
    billing_address: '123 Main St, City, State 12345',
    uncategorized_text: 'Customer accessed the service 47 times since purchase'
  },
  submit: true
});
```

### 3. Accept the Dispute (When Customer Is Right)

```javascript
// If the dispute is valid, accept it to avoid additional fees
await stripe.disputes.close('dp_abc123');
```

### 4. Prevent Future Disputes

```javascript
// Use Stripe Radar for fraud prevention
const paymentIntent = await stripe.paymentIntents.create({
  amount: 5000,
  currency: 'usd',
  payment_method: 'pm_card_visa',
  confirm: true,
  radar_options: {
    risk_score: '65'  // Custom risk threshold
  }
});

// Use 3D Secure for high-risk transactions
const paymentIntent = await stripe.paymentIntents.create({
  amount: 5000,
  currency: 'usd',
  payment_method: 'pm_card_visa',
  confirm: true,
  payment_method_options: {
    card: {
      request_three_d_secure: 'any'
    }
  }
});
```

## Common Scenarios

- **Subscription dispute**: Customer claims they cancelled but was still charged. Check the subscription status and cancellation timestamp in Stripe before responding.
- **Digital goods dispute**: Customer claims the product was not received. Provide delivery confirmation, IP logs, and usage records as evidence.
- **Fraudulent card use**: A stolen card was used. Cooperate with the issuer and provide AVS/CVV match results.

## Prevent It

- Use a clear billing descriptor that matches your business name so customers recognize charges
- Send receipts immediately after every charge using Stripe's receipt emails
- Enable 3D Secure for transactions above a risk threshold to shift liability to the issuer

## Related Pages

- [Stripe Account Restricted](/tools/stripe/stripe-account-restricted)
- [Stripe Charge Disputed](/tools/stripe/stripe-charge-disputed)
- [Stripe Balance Error](/tools/stripe/stripe-balance-error)
