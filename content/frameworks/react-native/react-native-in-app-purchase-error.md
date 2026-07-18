---
title: "[Solution] React Native In-App Purchase Error — How to Fix"
description: "Fix React Native in-app purchase errors. Resolve IAP initialization, billing, and receipt validation issues."
frameworks: ["react-native"]
error-types: ["connection-error"]
severities: ["error"]
weight: 5
comments: true
---

A React Native in-app purchase error occurs when the billing system fails to initialize, products cannot be fetched, or purchase transactions are not completed. IAP requires platform-specific setup for Google Play and App Store.

## Why It Happens

In-app purchases require proper configuration on both the app and store console. Errors occur when the product IDs don't match between code and store, when the store account is not configured for testing, when the billing library version is outdated, when the app is not published (sandbox testing), or when receipt validation fails.

## Common Error Messages

```
ERR_IAP_NOT_INITIALIZED
```

```
Billing is not available on this device
```

```
Product not found: com.app.premium
```

```
Purchase failed: The payment is invalid
```

## How to Fix It

### 1. Initialize IAP Correctly

Set up the billing connection:

```typescript
import { Platform } from 'react-native';
import RNIap, {
    endConnection,
    initConnection,
    getProducts,
    requestPurchase,
    finishTransaction,
    purchaseUpdatedListener,
    purchaseErrorListener,
} from 'react-native-iap';

const productIds = Platform.select({
    android: ['com.app.premium', 'com.app.coins_100'],
    ios: ['premium_upgrade', 'coins_100'],
});

let purchaseUpdateSubscription;
let purchaseErrorSubscription;

async function initializeIAP() {
    try {
        const result = await initConnection();
        console.log('IAP connected:', result);

        // Fetch products
        const products = await getProducts({ skus: productIds });
        console.log('Products:', products);

        // Listen for purchases
        purchaseUpdateSubscription = purchaseUpdatedListener(
            async (purchase) => {
                console.log('Purchase:', purchase);
                // Verify receipt on server
                await verifyPurchase(purchase);
                // Finish the transaction
                await finishTransaction({ purchase, isConsumable: false });
            }
        );

        purchaseErrorSubscription = purchaseErrorListener((error) => {
            console.error('Purchase error:', error);
        });

        return products;
    } catch (error) {
        console.error('IAP initialization failed:', error);
    }
}

// Cleanup
function cleanupIAP() {
    if (purchaseUpdateSubscription) purchaseUpdateSubscription.remove();
    if (purchaseErrorSubscription) purchaseErrorSubscription.remove();
    endConnection();
}
```

### 2. Request Purchases

Handle the purchase flow:

```typescript
async function buyProduct(productId: string) {
    try {
        await requestPurchase({
            sku: productId,
            ...(Platform.OS === 'android' && { isOfferPersonalized: false }),
        });
    } catch (error) {
        if (error.code === 'E_USER_CANCELLED') {
            console.log('User cancelled purchase');
        } else {
            console.error('Purchase failed:', error);
        }
    }
}

// Display products
function ProductList({ products }) {
    return (
        <View>
            {products.map((product) => (
                <TouchableOpacity
                    key={product.productId}
                    onPress={() => buyProduct(product.productId)}
                >
                    <Text>{product.title}: {product.localizedPrice}</Text>
                </TouchableOpacity>
            ))}
        </View>
    );
}
```

### 3. Validate Receipts on Server

Verify purchases server-side:

```typescript
// Server-side validation
async function verifyPurchase(purchase) {
    const response = await fetch('https://your-server.com/api/verify-purchase', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            receipt: purchase.transactionReceipt,
            platform: Platform.OS,
            productId: purchase.productId,
        }),
    });

    const result = await response.json();
    if (result.valid) {
        // Grant access
        await grantUserAccess(purchase.userId, purchase.productId);
    }
}
```

### 4. Test with Sandbox Accounts

Set up test accounts:

```bash
# iOS: Create sandbox tester in App Store Connect
# Android: Add test accounts in Google Play Console

# Test purchases
# Use sandbox account to make test purchases
# No real charges in sandbox environment
```

## Common Scenarios

**Scenario 1: Products not found in store.**
Verify product IDs match exactly between code and store console. Products must be "active" in the store.

**Scenario 2: Purchase works in sandbox but not production.**
Ensure the app version and product IDs are correct in the production store listing.

**Scenario 3: Purchase not delivered after payment.**
The `finishTransaction` call may have failed. Check server logs for receipt validation errors.

## Prevent It

1. **Always validate receipts on the server** — never trust client-side validation.

2. **Use sandbox/test accounts** for testing and never test with real purchases.

3. **Handle all purchase states** including pending, failed, and restored purchases.
