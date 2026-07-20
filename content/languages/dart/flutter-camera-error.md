---
title: "[Solution] Flutter Camera Error — plugin init, controller, image stream, permission"
description: "Fix Flutter Camera plugin errors from initialization, controller management, image stream, and permission handling."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 190
---

Camera errors occur when the camera plugin fails to initialize, permissions are missing, or the controller is used incorrectly.

## Common Causes

1. Camera permission not granted before initialization.
2. `CameraController` not being disposed.
3. `initializeImageStream` called without proper listener.
4. Multiple camera controllers competing for the same camera.
5. `takePicture` called before `initialize` completes.

## How to Fix It

**Solution 1: Initialize camera with permission check**

```dart
import 'package:camera/camera.dart';
import 'package:permission_handler/permission_handler.dart';

late List<CameraDescription> cameras;

Future<void> initCameras() async {
  cameras = await availableCameras();
}

class CameraPage extends StatefulWidget {
  @override
  State<CameraPage> createState() => _CameraPageState();
}

class _CameraPageState extends State<CameraPage> {
  CameraController? _controller;
  
  @override
  void initState() {
    super.initState();
    _initCamera();
  }
  
  Future<void> _initCamera() async {
    final status = await Permission.camera.request();
    if (!status.isGranted) {
      print('Camera permission denied');
      return;
    }
    
    if (cameras.isEmpty) {
      print('No cameras available');
      return;
    }
    
    _controller = CameraController(
      cameras[0],
      ResolutionPreset.high,
    );
    
    await _controller!.initialize();
    
    if (mounted) {
      setState(() {});
    }
  }
  
  @override
  void dispose() {
    _controller?.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    if (_controller == null || !_controller!.value.isInitialized) {
      return Center(child: CircularProgressIndicator());
    }
    
    return CameraPreview(_controller!);
  }
}
```

**Solution 2: Take a picture safely**

```dart
import 'package:camera/camera.dart';

class PictureTaker extends StatefulWidget {
  @override
  State<PictureTaker> createState() => _PictureTakerState();
}

class _PictureTakerState extends State<PictureTaker> {
  CameraController? _controller;
  
  Future<void> _takePicture() async {
    if (_controller == null || !_controller!.value.isInitialized) {
      return;
    }
    
    if (_controller!.value.isTakingPicture) {
      return; // Already taking a picture
    }
    
    try {
      XFile file = await _controller!.takePicture();
      print('Picture saved: ${file.path}');
    } on CameraException catch (e) {
      print('Error: ${e.description}');
    }
  }
  
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: _takePicture,
      child: Text('Take Picture'),
    );
  }
}
```

**Solution 3: Use image stream for processing**

```dart
import 'package:camera/camera.dart';

class ImageStreamWidget extends StatefulWidget {
  @override
  State<ImageStreamWidget> createState() => _ImageStreamWidgetState();
}

class _ImageStreamWidgetState extends State<ImageStreamWidget> {
  CameraController? _controller;
  
  void _startImageStream() {
    _controller?.startImageStream((CameraImage image) {
      // Process each frame
      print('Frame: ${image.width}x${image.height}');
    });
  }
  
  void _stopImageStream() {
    _controller?.stopImageStream();
  }
  
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        ElevatedButton(
          onPressed: _startImageStream,
          child: Text('Start Stream'),
        ),
        ElevatedButton(
          onPressed: _stopImageStream,
          child: Text('Stop Stream'),
        ),
      ],
    );
  }
}
```

**Solution 4: Switch cameras**

```dart
import 'package:camera/camera.dart';

class CameraSwitcher extends StatefulWidget {
  @override
  State<CameraSwitcher> createState() => _CameraSwitcherState();
}

class _CameraSwitcherState extends State<CameraSwitcher> {
  CameraController? _controller;
  int _currentCameraIndex = 0;
  
  Future<void> _switchCamera() async {
    final cameras = await availableCameras();
    if (cameras.length < 2) return;
    
    _currentCameraIndex = (_currentCameraIndex + 1) % cameras.length;
    
    _controller?.dispose();
    _controller = CameraController(
      cameras[_currentCameraIndex],
      ResolutionPreset.high,
    );
    
    await _controller!.initialize();
    setState(() {});
  }
  
  @override
  void dispose() {
    _controller?.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: _switchCamera,
      child: Text('Switch Camera'),
    );
  }
}
```

**Solution 5: Handle camera lifecycle**

```dart
import 'package:camera/camera.dart';

class CameraLifecycleWidget extends StatefulWidget {
  @override
  State<CameraLifecycleWidget> createState() => _CameraLifecycleWidgetState();
}

class _CameraLifecycleWidgetState extends State<CameraLifecycleWidget>
    with WidgetsBindingObserver {
  CameraController? _controller;
  
  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
  }
  
  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    if (_controller == null || !_controller!.value.isInitialized) return;
    
    if (state == AppLifecycleState.inactive) {
      _controller?.dispose();
    } else if (state == AppLifecycleState.resumed) {
      _initCamera();
    }
  }
  
  Future<void> _initCamera() async {
    _controller = CameraController(
      CameraDescription(
        name: '0',
        lensDirection: CameraLensDirection.back,
        sensorOrientation: 0,
      ),
      ResolutionPreset.high,
    );
    await _controller!.initialize();
    if (mounted) setState(() {});
  }
  
  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    _controller?.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return Center(child: Text('Camera'));
  }
}
```

## Examples

Add `camera: ^0.10.0` and `permission_handler: ^10.0.0` to your `pubspec.yaml`. On iOS, add `NSCameraUsageDescription` to `Info.plist`.

## Related Errors

- [Flutter Permission Error](/languages/dart/flutter-permission-error/)
- [Flutter Location Error](/languages/dart/flutter-location-error/)
- [Flutter Image Error](/languages/dart/flutter-image-error/)
