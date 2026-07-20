---
title: "[Solution] Flutter GetX Error — Get.find, Get.put, Get.lazyPut, GetBuilder"
description: "Fix Flutter GetX errors from dependency injection, Get.find failures, Get.put vs Get.lazyPut, and GetBuilder lifecycle."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 184
---

GetX errors occur when dependencies are not registered, `Get.find` is called before `Get.put`, or controllers are not properly managed.

## Common Causes

1. `Get.find` called before the dependency is registered with `Get.put`.
2. Using `Get.put` instead of `Get.lazyPut` for deferred initialization.
3. Controller not being disposed, causing memory leaks.
4. `GetBuilder` used without a registered controller.
5. Multiple instances registered when singleton was intended.

## How to Fix It

**Solution 1: Register and find dependencies**

```dart
import 'package:flutter/material.dart';
import 'package:get/get.dart';

class CounterController extends GetxController {
  var count = 0.obs;
  
  void increment() => count++;
  void decrement() => count--;
}

class MyPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Register the controller
    Get.put(CounterController());
    
    return Scaffold(
      body: Center(
        child: Obx(() => Text(
          'Count: ${Get.find<CounterController>().count}',
        )),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => Get.find<CounterController>().increment(),
        child: Icon(Icons.add),
      ),
    );
  }
}
```

**Solution 2: Use Get.lazyPut for deferred initialization**

```dart
import 'package:flutter/material.dart';
import 'package:get/get.dart';

class ApiClient extends GetxController {
  @override
  void onInit() {
    super.onInit();
    print('ApiClient initialized');
  }
}

void main() {
  // Lazy — only initialized when first found
  Get.lazyPut(() => ApiClient());
  
  runApp(GetMaterialApp(home: HomePage()));
}

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // First access triggers initialization
    final client = Get.find<ApiClient>();
    return Text('API Client ready');
  }
}
```

**Solution 3: Use GetBuilder for state management**

```dart
import 'package:flutter/material.dart';
import 'package:get/get.dart';

class NameController extends GetxController {
  var name = 'Guest'.obs;
  
  void setName(String newName) => name.value = newName;
}

class NamePage extends StatelessWidget {
  final controller = Get.put(NameController());
  
  @override
  Widget build(BuildContext context) {
    return GetBuilder<NameController>(
      builder: (ctrl) {
        return Column(
          children: [
            Obx(() => Text('Name: ${ctrl.name}')),
            ElevatedButton(
              onPressed: () => ctrl.setName('Alice'),
              child: Text('Set Name'),
            ),
          ],
        );
      },
    );
  }
}
```

**Solution 4: Handle controller lifecycle**

```dart
import 'package:flutter/material.dart';
import 'package:get/get.dart';

class TempController extends GetxController {
  var data = ''.obs;
  
  @override
  void onInit() {
    super.onInit();
    loadData();
  }
  
  void loadData() async {
    await Future.delayed(Duration(seconds: 1));
    data.value = 'Loaded';
  }
  
  @override
  void onClose() {
    // Cleanup resources
    super.onClose();
  }
}

// Use Get.put with permanent: false (default) for auto-cleanup
// Get.put(TempController(), permanent: true); // Never disposed
```

**Solution 5: Bindings for clean dependency management**

```dart
import 'package:flutter/material.dart';
import 'package:get/get.dart';

class HomeBinding extends Bindings {
  @override
  void dependencies() {
    Get.lazyPut(() => CounterController());
    Get.lazyPut(() => NameController());
  }
}

void main() {
  runApp(GetMaterialApp(
    initialRoute: '/home',
    binding: HomeBinding(),
    getPages: [
      GetPage(name: '/home', page: () => HomePage()),
    ],
  ));
}
```

## Examples

GetX provides dependency injection, state management, and routing. `Get.put` registers immediately; `Get.lazyPut` defers until first `Get.find`. `Obx` is the reactive widget for `.obs` variables.

## Related Errors

- [Flutter Provider Error](/languages/dart/flutter-provider-error/)
- [Flutter Riverpod Error](/languages/dart/flutter-riverpod-error/)
- [Flutter Bloc Error](/languages/dart/flutter-bloc-error/)
