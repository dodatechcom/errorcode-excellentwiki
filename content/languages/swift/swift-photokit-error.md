---
title: "[Solution] Swift PhotoKit Error — Authorization & Asset Fetch"
description: "Fix Swift PhotoKit errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 142
---

PhotoKit errors occur when authorization isn't properly requested, asset fetching fails, or change requests are misconfigured.

## Common Causes

```swift
// Not checking authorization status
PHPhotoLibrary.requestAuthorization { status in
    // Not handling all status cases
}

// Fetching without authorization
let fetchResult = PHAsset.fetchAssets(with: .image, options: nil)
```

## How to Fix

**1. Check and request authorization**

```swift
import Photos

func checkPhotoAccess() async -> PHAuthorizationStatus {
    let status = PHPhotoLibrary.authorizationStatus(for: .readWrite)
    
    if status == .notDetermined {
        return await PHPhotoLibrary.requestAuthorization(for: .readWrite)
    }
    
    return status
}
```

**2. Fetch assets safely**

```swift
func fetchPhotos() -> [PHAsset] {
    let options = PHFetchOptions()
    options.sortDescriptors = [NSSortDescriptor(key: "creationDate", ascending: false)]
    options.fetchLimit = 20
    
    let result = PHAsset.fetchAssets(with: .image, options: options)
    
    var assets: [PHAsset] = []
    result.enumerateObjects { asset, _, _ in
        assets.append(asset)
    }
    return assets
}
```

**3. Request image from asset**

```swift
func loadImage(from asset: PHAsset, completion: @escaping (UIImage?) -> Void) {
    let options = PHImageRequestOptions()
    options.deliveryMode = .highQualityFormat
    options.isNetworkAccessAllowed = true
    
    PHImageManager.default().requestImage(
        for: asset,
        targetSize: PHImageManagerMaximumSize,
        contentMode: .aspectFit,
        options: options
    ) { image, _ in
        completion(image)
    }
}
```

**4. Save image to library**

```swift
func saveImage(_ image: UIImage) async throws {
    try await PHPhotoLibrary.shared().performChanges {
        PHAssetChangeRequest.creationRequestForAsset(from: image)
    }
}
```

**5. Delete assets**

```swift
func deleteAssets(_ assets: [PHAsset]) async throws {
    try await PHPhotoLibrary.shared().performChanges({
        PHAssetChangeRequest.deleteAssets(assets as NSFastEnumeration)
    })
}
```

## Examples

Complete PhotoKit manager:

```swift
class PhotoManager {
    func requestAccess() async -> Bool {
        let status = await PHPhotoLibrary.requestAuthorization(for: .readWrite)
        return status == .authorized || status == .limited
    }
    
    func fetchLatest(count: Int) -> [PHAsset] {
        let options = PHFetchOptions()
        options.sortDescriptors = [NSSortDescriptor(key: "creationDate", ascending: false)]
        options.fetchLimit = count
        
        let result = PHAsset.fetchAssets(with: .image, options: options)
        var assets: [PHAsset] = []
        result.enumerateObjects { asset, _, _ in
            assets.append(asset)
        }
        return assets
    }
}
```

## Related Errors

- [LocalAuthentication Error](/languages/swift/swift-localauthentication-error)
- [ViewController Lifecycle](/languages/swift/swift-view-controller-lifecycle)
- [Navigation Controller Error](/languages/swift/swift-navigation-controller)
