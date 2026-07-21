---
title: "[Solution] UIKit UICollectionView Diffable Data Source Error"
description: "Fix UICollectionView diffable data source snapshot errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionView Diffable Data Source Error

Diffable data source errors occur when snapshots contain duplicate identifiers, when the data source is applied on a background thread, or when the snapshot does not match the current state.

## Common Causes
- Duplicate identifiers in snapshot
- Applying snapshot on non-main thread
- Snapshot references items not in current data source
- Section identifiers mismatch between snapshots

## How to Fix
1. Ensure all identifiers in snapshot are unique
2. Apply snapshots on the main thread
3. Build snapshots from current data source state
4. Use consistent section identifiers

```swift
// Apply snapshot on main thread:
var snapshot = NSDiffableDataSourceSnapshot<Section, Item>()
snapshot.appendSections([.main])
snapshot.appendItems(items, toSection: .main)

DispatchQueue.main.async {
    self.dataSource.apply(snapshot)
}
```

## Examples
```swift
// Diffable data source setup:
typealias Section = Int
typealias Item = String

let dataSource = UICollectionViewDiffableDataSource<Section, Item>(collectionView: collectionView) { collectionView, indexPath, item in
    let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "Cell", for: indexPath)
    cell.textLabel.text = item
    return cell
}

var snapshot = NSDiffableDataSourceSnapshot<Section, Item>()
snapshot.appendSections([0, 1, 2])
snapshot.appendItems(["A", "B"], toSection: 0)
snapshot.appendItems(["C", "D"], toSection: 1)
dataSource.apply(snapshot)
```
