---
title: "[Solution] UIKit UIListContentConfiguration Error"
description: "Fix UIListContentConfiguration cell configuration errors in UIKit."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIListContentConfiguration Error

List content configuration fails when the configuration is not properly applied, when content types do not match, or when the configuration conflicts with the cell's existing content.

## Common Causes
- Content configuration not applied to cell
- Cell reused with wrong configuration type
- Image or text not matching expected content
- Configuration conflicts with storyboards

## How to Fix
1. Apply content configuration in cellForRow
2. Use correct configuration type for the cell
3. Clear previous configuration before applying new
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
// Cell with subtitle configuration:
var content = cell.defaultContentConfiguration()
content.text = "Title"
content.secondaryText = "Subtitle"
content.image = UIImage(systemName: "star")
content.imageProperties.tintColor = .systemYellow
content.textProperties.font = .preferredFont(forTextStyle: .headline)
content.secondaryTextProperties.font = .preferredFont(forTextStyle: .subheadline)
cell.contentConfiguration = content
cell.accessories = [.disclosureIndicator]
```
