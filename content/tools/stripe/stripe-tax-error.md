---
title: "[Solution] Stripe Tax Calculation Error — How to Fix"
description: "Fix Stripe tax calculation errors by configuring tax settings, validating addresses, handling tax-exempt customers, and resolving calculation edge cases"
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
comments: true
---

# Stripe Tax Calculation Error

This error means Stripe could not calculate tax for a transaction due to missing configuration, invalid addresses, or unsupported tax jurisdictions. Stripe Tax requires specific setup and valid location data to compute correct tax amounts.

## Why It Happens

- Stripe Tax is not enabled on the account
- The customer or business address is missing or invalid
- The product tax category is not assigned
- The transaction occurs in a jurisdiction where Stripe does not calculate tax
- The currency does not match the country's expected currency
- Automatic tax collection is disabled for the Stripe account
- The product is tax-exempt but was not marked as such
- The API request is missing required address fields for tax calculation

## Common Error Messages

```
{
  "error": {
    "type": "invalid_request_error",
    "message": "Automatic tax calculation is not enabled."
  }
}
```

```
{
  "error": {
    "type": "invalid_request_error",
    "message": "Tax calculation requires a valid shipping address."
  }
}
```

```
{
  "automatic_tax": "requires_location_inputs",
  "tax_amount": 0
}
```

## How to Fix It

### 1. Verify Stripe Tax Is Enabled

```bash
# Check via Stripe API
stripe settings retrieve

# Or check in the Dashboard:
# Settings > Tax > Automatic tax collection
```

### 2. Provide Complete Address Information

```javascript
const session = await stripe.checkout.sessions.create({
  mode: 'payment',
  line_items: [
    {
      price: 'price_abc123',
      quantity: 1
    }
  ],
  // Provide shipping address for tax calculation
  shipping_address_collection: {
    allowed_countries: ['US', 'CA', 'GB']
  },
  // Or provide customer address directly
  customer_address: {
    line1: '123 Main St',
    city: 'San Francisco',
    state: 'CA',
    postal_code: '94105',
    country: 'US'
  },
  automatic_tax: {
    enabled: true
  }
});
```

### 3. Assign Product Tax Categories

```python
import stripe

# Set the tax category on a product
stripe.Product.modify(
    'prod_abc123',
    tax_code='txcd_99999999',  # General tangible goods
)

# Common tax codes:
# txcd_10000000 - Software as a Service
# txcd_99999999 - General tangible goods
# txcd_30080000 - Books and periodicals
```

### 4. Handle Tax-Exempt Customers

```javascript
// Mark a customer as tax-exempt
const customer = await stripe.customers.create({
  email: 'nonprofit@example.com',
  tax_exempt: 'exempt',
  metadata: {
    tax_exemption_reason: 'nonprofit_organization'
  }
});

// Create a tax-exempt checkout session
const session = await stripe.checkout.sessions.create({
  customer: customer.id,
  mode: 'payment',
  line_items: [{ price: 'price_abc123', quantity: 1 }],
  automatic_tax: {
    enabled: true
  }
});
```

### 5. Retrieve Tax Calculation Results

```javascript
// Check the tax status of a payment intent
const paymentIntent = await stripe.paymentIntents.retrieve('pi_abc123');

console.log('Automatic tax:', paymentIntent.automatic_tax);
console.log('Tax collected:', paymentIntent.amount_details?.tax_amount);

// Check a checkout session
const session = await stripe.checkout.sessions.retrieve('cs_abc123');
console.log('Tax status:', session.automatic_tax?.status);
```

## Common Scenarios

- **Cross-border sale**: A US company sells to a customer in the EU. Stripe needs both addresses to determine VAT obligations. Provide complete shipping addresses.
- **Digital goods in EU**: Selling digital products to EU customers requires VAT collection. Ensure the product has the correct tax code and the customer address is provided.
- **Marketplace with tax-exempt buyers**: Some buyers (governments, nonprofits) are tax-exempt. Mark these customers as exempt in Stripe to skip tax calculation.

## Prevent It

- Enable automatic tax collection in the Stripe Dashboard before processing any taxable transactions
- Always collect complete shipping addresses in Checkout or PaymentIntent flows
- Use Stripe's `tax_code` on every product to ensure correct tax categorization

## Related Pages

- [Stripe Rate Limit Error](/tools/stripe/stripe-rate-limit-error)
- [Stripe Identity Error](/tools/stripe/stripe-identity-error)
- [Stripe Balance Error](/tools/stripe/stripe-balance-error)
