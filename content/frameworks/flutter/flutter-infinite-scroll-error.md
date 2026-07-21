---
title: "[Solution] Flutter Infinite Scroll Pagination Error"
description: "Fix Flutter infinite scroll pagination errors when loading more items does not trigger or duplicates items."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

An infinite scroll pagination error in Flutter occurs when the scroll listener does not detect when the user has scrolled near the bottom, preventing additional data from loading, or causing the same data to be loaded repeatedly.

## Common Causes

- `ScrollController` not attached to the `ListView`
- Threshold for triggering load-more is too small or too large
- Loading flag not reset after data is fetched
- Page number not incremented after successful load
- `hasMore` flag not set correctly when end of data is reached

## How to Fix

1. Set up a scroll listener with proper threshold:

```dart
class _PaginatedListState extends State<PaginatedList> {
  final _scrollController = ScrollController();
  List<Item> _items = [];
  int _page = 1;
  bool _isLoading = false;
  bool _hasMore = true;

  @override
  void initState() {
    super.initState();
    _scrollController.addListener(_onScroll);
    _loadMore();
  }

  void _onScroll() {
    if (_scrollController.position.pixels >=
        _scrollController.position.maxScrollExtent - 200) {
      _loadMore();
    }
  }

  Future<void> _loadMore() async {
    if (_isLoading || !_hasMore) return;

    setState(() => _isLoading = true);

    try {
      final newItems = await api.fetchItems(page: _page);
      setState(() {
        _items.addAll(newItems);
        _page++;
        _hasMore = newItems.length >= 20; // Assume 20 per page
      });
    } finally {
      setState(() => _isLoading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      controller: _scrollController,
      itemCount: _items.length + (_hasMore ? 1 : 0),
      itemBuilder: (context, index) {
        if (index == _items.length) {
          return const Center(child: CircularProgressIndicator());
        }
        return ListTile(title: Text(_items[index].name));
      },
    );
  }

  @override
  void dispose() {
    _scrollController.dispose();
    super.dispose();
  }
}
```

2. Use `NotificationListener` as an alternative:

```dart
NotificationListener<ScrollNotification>(
  onNotification: (notification) {
    if (notification is ScrollEndNotification &&
        notification.metrics.pixels >= notification.metrics.maxScrollExtent - 200) {
      _loadMore();
    }
    return false;
  },
  child: ListView.builder(...),
);
```

## Examples

```dart
// Bug: isLoading not reset -- only loads once
Future<void> _loadMore() async {
  setState(() => _isLoading = true);
  final items = await api.fetchItems(page: _page);
  _items.addAll(items);
  _page++;
  // Missing: setState(() => _isLoading = false);
}

// Fixed
Future<void> _loadMore() async {
  if (_isLoading || !_hasMore) return;
  setState(() => _isLoading = true);
  try {
    final items = await api.fetchItems(page: _page);
    setState(() {
      _items.addAll(items);
      _page++;
      _hasMore = items.isNotEmpty;
    });
  } finally {
    setState(() => _isLoading = false);
  }
}
```

```text
RangeError (index): Invalid value
```
