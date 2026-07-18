---
title: "[Solution] macOS App Store Payment Error — Payment Method Rejected"
description: "Fix macOS App Store payment failure: payment method rejected, cannot add payment, billing information error, card declined."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 197
---

# App Store Payment Error — Payment Method Rejected

Fix macOS App Store payment failure: payment method rejected, cannot add payment, billing information error, card declined.

## Common Causes

- Credit or debit card expired or has insufficient funds
- Bank blocking international or digital transaction
- Billing address does not match card issuer records
- Apple payment system temporarily unavailable

## How to Fix

### 1. Update Payment Method

```bash
# System Settings → Apple ID → Payment & Shipping → Edit or add payment method
```

### 2. Verify Billing Address

```bash
# System Settings → Apple ID → Payment & Shipping → Billing Address → Verify
```

### 3. Try Alternative Payment Method

```bash
# Use different card, Apple Pay, or Apple Gift Card balance
```

### 4. Contact Bank

```bash
# Call card issuer to authorize App Store / Apple transactions
```

## Common Scenarios

This error commonly occurs when:

- Payment method shows 'Declined' when attempting purchase
- Cannot add new payment method to Apple ID account
- Payment goes through but purchase not completed
- Apple ID says payment information needs to be updated

## Prevent It

- Keep payment methods and billing addresses current
- Contact bank before large App Store purchases to prevent blocks
- Use Apple Gift Card as alternative payment method
- Ensure billing address matches exactly what card issuer has on file
