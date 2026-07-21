---
title: "[Solution] Flutter ListView Item Height Error"
description: "Fix Flutter ListView item height errors when list items have inconsistent or unbounded heights."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A ListView item height error in Flutter occurs when items in a `ListView.builder` have unbounded or inconsistent heights, causing the scroll view to calculate incorrect offsets or display items with visual glitches.

## Common Causes

- `itemExtent` set to a value smaller than the actual item height
- Items with dynamic content that changes height after render
- `ListView` with `itemExtent` but items use `Expanded` or `Flexible`
- `SliverList` delegate returns items with unconstrained height
- Missing `key` on list items causing incorrect recycling

## How to Fix

1. Let items determine their own height:

```dart
ListView.builder(
  itemCount: items.length,
  itemBuilder: (context, index) {
    final item = items[index];
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(item.title, style: Theme.of(context).textTheme.titleMedium),
            const SizedBox(height: 8),
            Text(item.description),
          ],
        ),
      ),
    );
  },
);
```

2. Use `itemExtent` only when all items have the same height:

```dart
ListView.builder(
  itemExtent: 72, // Fixed height for all items
  itemCount: items.length,
  itemBuilder: (context, index) => ListTile(
    leading: CircleAvatar(child: Text('${index + 1}')),
    title: Text(items[index].name),
  ),
);
```

3. Use `prototypeItem` instead of `itemExtent` for similar heights:

```dart
ListView.builder(
  prototypeItem: ListTile(title: Text('Prototype')),
  itemCount: items.length,
  itemBuilder: (context, index) => ListTile(title: Text(items[index].name)),
);
```

## Examples

```dart
// Bug: itemExtent too small
ListView.builder(
  itemExtent: 40, // Items need 80+ pixels
  itemCount: items.length,
  itemBuilder: (context, index) => Card(
    child: Padding(
      padding: const EdgeInsets.all(16),
      child: Column(children: [Text('Title'), Text('Subtitle')]),
    ),
  ),
);

// Fixed: remove itemExtent or set correct value
ListView.builder(
  itemCount: items.length,
  itemBuilder: (context, index) => Card(...),
);
```

```text
RangeError (index): Invalid value -- layout offset out of bounds
```
