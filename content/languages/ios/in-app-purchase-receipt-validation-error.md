---
title: "[Solution] In-App Purchase Receipt Validation Error"
description: "Fix StoreKit receipt validation failures for in-app purchases in iOS apps."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# In-App Purchase Receipt Validation Error

Receipt validation fails when the receipt is corrupted, expired, or the validation endpoint returns an error code.

## Common Causes
- Receipt not sent to validation server
- Sandbox receipt validated against production endpoint
- Receipt expired or malformed
- Apple server temporarily unavailable

## How to Fix
1. Verify the receipt data is base64-encoded correctly
2. Use the appropriate endpoint (sandbox vs production)
3. Implement retry logic for server unavailability
4. Handle all StoreKit receipt validation error codes

```swift
// Validate receipt:
func validateReceipt(receiptData: Data) {
    let base64Receipt = receiptData.base64EncodedString()
    let body = ["receipt-data": base64Receipt]
    let url = URL(string: "https://buy.itunes.apple.com/verifyReceipt")!
    // Send to your server for validation
}
```

## Examples
```swift
// Receipt validation helper:
func fetchReceipt() -> String? {
    guard let url = Bundle.main.appStoreReceiptURL,
          let data = try? Data(contentsOf: url) else {
        return nil
    }
    return data.base64EncodedString()
}
```
