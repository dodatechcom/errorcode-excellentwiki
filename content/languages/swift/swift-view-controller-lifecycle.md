---
title: "[Solution] Swift ViewController Lifecycle Override Error"
description: "Fix Swift ViewController lifecycle errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 129
---

ViewController lifecycle errors occur when methods are overridden incorrectly, `super` calls are missing, or view manipulation happens at wrong lifecycle points.

## Common Causes

```swift
// Not calling super
override func viewDidLoad() {
    // Missing: super.viewDidLoad()
    setupViews()
}

// Manipulating view before it loads
init() {
    super.init(coder: coder) // Wrong: view not ready
    view.backgroundColor = .red // Crash
}
```

## How to Fix

**1. Always call super**

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    setupViews()
}

override func viewWillAppear(_ animated: Bool) {
    super.viewWillAppear(animated)
    refreshData()
}
```

**2. Setup views in viewDidLoad**

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    
    let label = UILabel()
    label.translatesAutoresizingMaskIntoConstraints = false
    view.addSubview(label)
    
    NSLayoutConstraint.activate([
        label.centerXAnchor.constraint(equalTo: view.centerXAnchor),
        label.centerYAnchor.constraint(equalTo: view.centerYAnchor)
    ])
}
```

**3. Handle view lifecycle properly**

```swift
override func viewWillAppear(_ animated: Bool) {
    super.viewWillAppear(animated)
    // Refresh data that might change
    tableView.reloadData()
}

override func viewDidAppear(_ animated: Bool) {
    super.viewDidAppear(animated)
    // Start animations or tracking
}

override func viewWillDisappear(_ animated: Bool) {
    super.viewWillDisappear(animated)
    // Save state
}
```

**4. Programmatic init**

```swift
class DetailVC: UIViewController {
    let item: Item
    
    init(item: Item) {
        self.item = item
        super.init(nibName: nil, bundle: nil)
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
```

**5. View layout callbacks**

```swift
override func viewDidLayoutSubviews() {
    super.viewDidLayoutSubviews()
    // Update frames based on actual layout
    gradientLayer.frame = view.bounds
}
```

## Examples

Complete lifecycle usage:
```swift
class ProfileViewController: UIViewController {
    @IBOutlet weak var avatarImageView: UIImageView!
    @IBOutlet weak var nameLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        loadProfile()
    }
    
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        animateEntrance()
    }
    
    private func setupUI() {
        avatarImageView.layer.cornerRadius = avatarImageView.bounds.width / 2
    }
    
    private func loadProfile() {
        // Fetch latest profile data
    }
    
    private func animateEntrance() {
        UIView.animate(withDuration: 0.3) {
            self.nameLabel.alpha = 1
        }
    }
}
```

## Related Errors

- [Navigation Controller Error](/languages/swift/swift-navigation-controller)
- [UITableView Error](/languages/swift/swift-tableview-error)
- [Auto Layout Error](/languages/swift/swift-autolayout-error)
