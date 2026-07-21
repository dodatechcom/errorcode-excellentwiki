---
title: "[Solution] UIKit UIListContentView Configuration Error"
description: "Fix UIListContentView content configuration application errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIListContentView Configuration Error

List content view configuration fails when the configuration is not applied in cellForRow, when the configuration type does not match the cell, or when the cell is reused with incorrect content.

## Common Causes
- Configuration not applied in cellForRow
- Cell reused with wrong configuration
- Image and text not matching expected content
- Configuration conflicts with storyboard

## How to Fix
1. Apply configuration in cellForRowAt
2. Use correct configuration type
3. Reset configuration before applying new
4. Test cell reuse scenarios

```swift
func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
    var content = cell.defaultContentConfiguration()
    content.text = items[indexPath.row].title
    content.secondaryText = items[indexPath.row].subtitle
    cell.contentConfiguration = content
    return cell
}
```

## Examples
```swift
// Cell with image and subtitle:
var content = cell.defaultContentConfiguration()
content.text = item.title
content.secondaryText = item.description
content.image = UIImage(systemName: item.icon)
content.imageProperties.tintColor = .systemBlue
content.secondaryTextProperties.color = .secondaryLabel
cell.contentConfiguration = content
```
