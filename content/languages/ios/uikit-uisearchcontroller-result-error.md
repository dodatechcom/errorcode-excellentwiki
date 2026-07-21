---
title: "[Solution] UIKit UISearchController Result Error"
description: "Fix UISearchController search result display and interaction errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UISearchController Result Error

Search controller results fail to display when the search results updater is not set, when results are not updated on the main thread, or when the search bar is not properly connected.

## Common Causes
- Search results updater not set
- Results updated on background thread
- Search bar not added to navigation item
- Results controller not properly configured

## How to Fix
1. Set searchResultsUpdater to the view controller
2. Update results on the main thread
3. Set searchController.searchBar in navigationItem
4. Configure search controller lifecycle properly

```swift
// Setup search controller:
let searchController = UISearchController(searchResultsController: nil)
searchController.searchResultsUpdater = self
searchController.obscuresBackgroundDuringPresentation = false
searchController.searchBar.placeholder = "Search"
navigationItem.searchController = searchController

// Update results:
func updateSearchResults(for searchController: UISearchController) {
    let query = searchController.searchBar.text ?? ""
    filteredItems = items.filter { $0.name.localizedCaseInsensitiveContains(query) }
    tableView.reloadData()
}
```

## Examples
```swift
// Search with separate results controller:
let resultsVC = ResultsViewController()
let searchController = UISearchController(searchResultsController: resultsVC)
searchController.searchResultsUpdater = resultsVC

// In results controller:
func updateSearchResults(for searchController: UISearchController) {
    guard let query = searchController.searchBar.text else { return }
    results = allItems.filter { $0.name.contains(query) }
    collectionView.reloadData()
}
```
