---
title: "[Solution] StoreKit Product Request Error"
description: "Fix StoreKit product request failures when fetching in-app purchase products."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# StoreKit Product Request Error

Product requests fail when the product identifiers are incorrect, the App Store Connect configuration is incomplete, or the sandbox environment is not configured.

## Common Causes
- Product identifier does not match App Store Connect
- App not configured for in-app purchases in App Store Connect
- Sandbox tester account not set up
- SKProductsRequest delegate not implemented

## How to Fix
1. Verify product identifiers match exactly in App Store Connect
2. Complete in-app purchase setup in App Store Connect
3. Create sandbox tester accounts
4. Implement both SKProductsRequestDelegate methods

```swift
let productIDs: Set<String> = ["com.app.premium"]
let request = SKProductsRequest(productIdentifiers: productIDs)
request.delegate = self
request.start()

func productsRequest(_ request: SKProductsRequest, didReceive response: SKProductsResponse) {
    for product in response.products {
        print("Product: \(product.productIdentifier) - \(product.localizedTitle)")
    }
}
```

## Examples
```swift
// Complete StoreKit product fetch:
class StoreManager: NSObject, SKProductsRequestDelegate {
    var products: [SKProduct] = []

    func fetchProducts() {
        let ids: Set<String> = ["com.app.monthly", "com.app.yearly"]
        let request = SKProductsRequest(productIdentifiers: ids)
        request.delegate = self
        request.start()
    }

    func productsRequest(_ request: SKProductsRequest, didReceive response: SKProductsResponse) {
        products = response.products
    }

    func request(_ request: SKRequest, didFailWithError error: Error) {
        print("Product request failed: \(error)")
    }
}
```
