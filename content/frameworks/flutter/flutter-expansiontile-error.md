---
title: "[Solution] Flutter ExpansionTile Error"
description: "Fix Flutter ExpansionTile errors when tiles do not expand or collapse correctly on tap."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

An ExpansionTile error in Flutter occurs when `ExpansionTile` does not expand on tap, stays permanently open, or the `children` list does not display because the tile is not inside a scrollable parent.

## Common Causes

- `initiallyExpanded` set to `true` but tile should start collapsed
- `onExpansionChanged` callback prevents state changes by returning false
- `ExpansionTile` inside a non-scrollable `Column` without proper height
- Multiple tiles expanded simultaneously when only one should be
- `childrenPadding` not applied causing content to clip

## How to Fix

1. Control expanded state manually:

```dart
class _ExpandableListState extends State<ExpandableList> {
  int? _expandedIndex;

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: sections.length,
      itemBuilder: (context, index) {
        return ExpansionTile(
          key: PageStorageKey('section_$index'),
          title: Text(sections[index].title),
          initiallyExpanded: _expandedIndex == index,
          onExpansionChanged: (expanded) {
            setState(() {
              _expandedIndex = expanded ? index : null;
            });
          },
          children: sections[index].items.map((item) {
            return ListTile(
              title: Text(item),
              onTap: () => selectItem(item),
            );
          }).toList(),
        );
      },
    );
  }
}
```

2. Use Key to prevent incorrect state recycling:

```dart
ExpansionTile(
  key: ValueKey(category.id), // Unique key prevents state mixing
  title: Text(category.name),
  children: category.items.map((item) {
    return ListTile(title: Text(item.name));
  }).toList(),
);
```

3. Handle nested ExpansionTiles:

```dart
ExpansionTile(
  title: Text('Category'),
  children: [
    ExpansionTile(
      title: Text('Subcategory'),
      children: [
        ListTile(title: Text('Item 1')),
        ListTile(title: Text('Item 2')),
      ],
    ),
  ],
);
```

## Examples

```dart
// Bug: ExpansionTile in Column (not scrollable)
Column(
  children: [
    ExpansionTile(title: Text('Section 1'), children: [...]), // May overflow
    ExpansionTile(title: Text('Section 2'), children: [...]),
  ],
);

// Fixed: use ListView
ListView(
  children: [
    ExpansionTile(title: Text('Section 1'), children: [...]),
    ExpansionTile(title: Text('Section 2'), children: [...]),
  ],
);
```

```text
RenderFlex overflowed by pixels on the bottom
```
