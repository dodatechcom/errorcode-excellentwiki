---
title: "[Solution] Flutter Draggable DragTarget Error"
description: "Fix Flutter Draggable and DragTarget errors when drag-and-drop fails or items are not accepted by the target."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A Draggable DragTarget error in Flutter occurs when the drag-and-drop interaction between a `Draggable` and `DragTarget` fails because the data types do not match or the `onWillAccept` callback rejects the data.

## Common Causes

- `Draggable.data` type does not match `DragTarget` expected type
- `onWillAccept` callback returns `false` for valid data
- `feedback` widget is too large or positioned incorrectly
- `DragTarget` is obscured by another widget
- `LongPressDraggable` used but user taps instead of long-pressing

## How to Fix

1. Match data types between Draggable and DragTarget:

```dart
Draggable<String>(
  data: 'item-1',
  feedback: Material(child: Card(child: Padding(
    padding: const EdgeInsets.all(8),
    child: Text('Dragging'),
  ))),
  childWhenDragging: Opacity(
    opacity: 0.3,
    child: Card(child: ListTile(title: Text('Item 1'))),
  ),
  child: Card(child: ListTile(title: Text('Item 1'))),
)

DragTarget<String>(
  onWillAccept: (data) => data != null,
  onAccept: (data) {
    setState(() => _acceptedItems.add(data));
  },
  builder: (context, candidateData, rejectedData) {
    return Container(
      height: 200,
      color: candidateData.isNotEmpty ? Colors.green.shade100 : Colors.grey.shade200,
      child: const Center(child: Text('Drop here')),
    );
  },
)
```

2. Use `onWillAcceptWithDetails` for more control:

```dart
DragTarget<Photo>(
  onWillAcceptWithDetails: (details) {
    return details.data.size < 1024 * 1024; // Accept only small images
  },
  onAcceptWithDetails: (details) {
    addPhoto(details.data);
  },
  builder: (context, candidateData, rejectedData) {
    return Container(
      decoration: BoxDecoration(
        border: Border.all(
          color: candidateData.isNotEmpty ? Colors.blue : Colors.grey,
          width: 2,
        ),
      ),
      child: const Center(child: Text('Drop photo here')),
    );
  },
);
```

## Examples

```dart
// Bug: data type mismatch
Draggable<int>(data: 42, child: Text('Drag me'))
DragTarget<String>(onAccept: (data) => print(data)); // Never accepts int

// Fixed: match types
Draggable<String>(data: 'hello', child: Text('Drag me'))
DragTarget<String>(onAccept: (data) => print(data));
```

```text
A DragTarget widget was used with a type that does not match the Draggable data type.
```
