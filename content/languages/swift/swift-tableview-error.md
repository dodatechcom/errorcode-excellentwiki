---
title: "[Solution] Swift UITableView Error — Dequeue & DataSource"
description: "Fix Swift UITableView errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 126
---

UITableView errors occur when cell dequeue fails, cell identifiers don't match, or datasource reload causes inconsistencies.

## Common Causes

```swift
// Cell identifier mismatch
tableView.register(MyCell.self, forCellReuseIdentifier: "Cell")
let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath) // Crash

// Missing dataSource
tableView.dataSource = nil
tableView.reloadData() // No data source
```

## How to Fix

**1. Register and dequeue correctly**

```swift
tableView.register(MyCell.self, forCellReuseIdentifier: "MyCell")

func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    guard let cell = tableView.dequeueReusableCell(withIdentifier: "MyCell", for: indexPath) as? MyCell else {
        return UITableViewCell()
    }
    cell.configure(with: items[indexPath.row])
    return cell
}
```

**2. Handle section headers**

```swift
func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
    sections[section].title
}

func tableView(_ tableView: UITableView, viewForHeaderInSection section: Int) -> UIView? {
    let header = tableView.dequeueReusableHeaderFooterView(withIdentifier: "Header")
    return header
}
```

**3. Safe reload**

```swift
func updateData(newItems: [Item]) {
    let diff = calculateDiff(old: items, new: newItems)
    items = newItems
    
    tableView.performBatchUpdates({
        tableView.deleteSections(diff.deletes, with: .fade)
        tableView.insertSections(diff.inserts, with: .fade)
        tableView.reloadSections(diff.updates, with: .fade)
    })
}
```

**4. Estimated row height**

```swift
tableView.estimatedRowHeight = 80
tableView.rowHeight = UITableView.automaticDimension
```

**5. Self-sizing cells**

```swift
class MyCell: UITableViewCell {
    @IBOutlet weak var titleLabel: UILabel!
    @IBOutlet weak var bodyLabel: UILabel!
    
    override func awakeFromNib() {
        super.awakeFromNib()
        bodyLabel.numberOfLines = 0
    }
}
```

## Examples

Complete UITableView setup:
```swift
class ListViewController: UITableViewController {
    var items: [String] = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "Cell")
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        items.count
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
        cell.textLabel?.text = items[indexPath.row]
        return cell
    }
}
```

## Related Errors

- [UICollectionView Error](/languages/swift/swift-collectionview-error)
- [Navigation Controller Error](/languages/swift/swift-navigation-controller)
- [ViewController Lifecycle](/languages/swift/swift-view-controller-lifecycle)
