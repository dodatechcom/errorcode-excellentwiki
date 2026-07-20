---
title: "[Solution] Swift UICollectionView Error — Layout & Supplementary"
description: "Fix Swift UICollectionView errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 127
---

UICollectionView errors occur when layout configuration is incorrect, supplementary views aren't registered, or prefetching fails.

## Common Causes

```swift
// Missing layout
let layout = UICollectionViewFlowLayout()
layout.itemSize = CGSize(width: 100, height: 100)
// Missing: layout.scrollDirection = .vertical

// Supplementary view not registered
collectionView.register(HeaderView.self, forSupplementaryViewOfKind: "header", withReuseIdentifier: "Header")
```

## How to Fix

**1. Configure layout properly**

```swift
let layout = UICollectionViewCompositionalLayout { sectionIndex, environment in
    let itemSize = NSCollectionLayoutSize(
        widthDimension: .fractionalWidth(1.0),
        heightDimension: .fractionalHeight(1.0)
    )
    let item = NSCollectionLayoutItem(layoutSize: itemSize)
    
    let groupSize = NSCollectionLayoutSize(
        widthDimension: .fractionalWidth(1.0),
        heightDimension: .absolute(100)
    )
    let group = NSCollectionLayoutGroup.vertical(layoutSize: groupSize, subitems: [item])
    
    return NSCollectionLayoutSection(group: group)
}

let collectionView = UICollectionView(frame: .zero, collectionViewLayout: layout)
```

**2. Register and dequeue cells**

```swift
collectionView.register(MyCell.self, forCellWithReuseIdentifier: "MyCell")

func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
    let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "MyCell", for: indexPath) as! MyCell
    cell.configure(with: items[indexPath.item])
    return cell
}
```

**3. Handle supplementary views**

```swift
collectionView.register(
    HeaderView.self,
    forSupplementaryViewOfKind: UICollectionView.elementKindSectionHeader,
    withReuseIdentifier: "Header"
)

func collectionView(_ collectionView: UICollectionView, viewForSupplementaryElementOfKind kind: String, at indexPath: IndexPath) -> UICollectionReusableView {
    let header = collectionView.dequeueReusableSupplementaryView(
        ofKind: kind,
        withReuseIdentifier: "Header",
        for: indexPath
    ) as! HeaderView
    header.title = sections[indexPath.section].title
    return header
}
```

**4. Compositional layout with sections**

```swift
let layout = UICollectionViewCompositionalLayout { sectionIndex, environment in
    let section = self.sections[sectionIndex]
    // Configure section based on type
    return section.layoutSection
}
```

**5. Diffable data source**

```swift
var dataSource: UICollectionViewDiffableDataSource<Section, Item>!

func configureDataSource() {
    dataSource = UICollectionViewDiffableDataSource(collectionView: collectionView) { collectionView, indexPath, item in
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "Cell", for: indexPath) as! MyCell
        cell.configure(with: item)
        return cell
    }
}

func updateSnapshot() {
    var snapshot = NSDiffableDataSourceSnapshot<Section, Item>()
    snapshot.appendSections([.main])
    snapshot.appendItems(items)
    dataSource.apply(snapshot)
}
```

## Examples

Complete collection view setup:
```swift
class GridViewController: UIViewController {
    var collectionView: UICollectionView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupCollectionView()
    }
    
    private func setupCollectionView() {
        let layout = createLayout()
        collectionView = UICollectionView(frame: view.bounds, collectionViewLayout: layout)
        collectionView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        view.addSubview(collectionView)
        
        collectionView.register(Cell.self, forCellWithReuseIdentifier: "Cell")
        collectionView.dataSource = self
    }
    
    private func createLayout() -> UICollectionViewCompositionalLayout {
        let itemSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(0.5), heightDimension: .absolute(150))
        let item = NSCollectionLayoutItem(layoutSize: itemSize)
        item.contentInsets = NSDirectionalEdgeInsets(top: 5, leading: 5, bottom: 5, trailing: 5)
        
        let groupSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0), heightDimension: .absolute(150))
        let group = NSCollectionLayoutGroup.horizontal(layoutSize: groupSize, subitems: [item])
        
        return UICollectionViewCompositionalLayout(section: NSCollectionLayoutSection(group: group))
    }
}
```

## Related Errors

- [UITableView Error](/languages/swift/swift-tableview-error)
- [Auto Layout Error](/languages/swift/swift-autolayout-error)
- [ViewController Lifecycle](/languages/swift/swift-view-controller-lifecycle)
