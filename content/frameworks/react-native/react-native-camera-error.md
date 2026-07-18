---
title: "[Solution] React Native Camera Access Error — How to Fix"
description: "Fix React Native camera errors. Resolve camera permission, capture, and camera preview issues."
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

A React Native camera access error occurs when the app cannot open the camera, capture photos/videos, or display the camera preview. Camera functionality requires proper permissions and native setup.

## Why It Happens

Camera access requires runtime permissions on both platforms. Errors occur when camera permissions are not declared or requested, when the camera library is not properly linked, when the camera is already in use by another app, when the device has no camera, or when the camera component props are incorrectly configured.

## Common Error Messages

```
Camera: Camera permission not granted
```

```
Error: Camera not available
```

```
相机: 设备没有摄像头
```

```
Error: Cannot capture while camera is not ready
```

## How to Fix It

### 1. Request Camera Permission

Handle permissions before using the camera:

```typescript
import { Platform, PermissionsAndroid, Alert } from 'react-native';
import { check, request, PERMISSIONS, RESULTS } from 'react-native-permissions';

async function requestCameraPermission() {
    if (Platform.OS === 'android') {
        const granted = await PermissionsAndroid.request(
            PermissionsAndroid.PERMISSIONS.CAMERA,
            {
                title: 'Camera Permission',
                message: 'App needs camera access to take photos',
                buttonPositive: 'Allow',
                buttonNegative: 'Deny',
            }
        );
        return granted === PermissionsAndroid.RESULTS.GRANTED;
    }

    const result = await request(PERMISSIONS.IOS.CAMERA);
    return result === RESULTS.GRANTED;
}
```

### 2. Use react-native-vision-camera

Set up the modern camera library:

```typescript
import { Camera, useCameraDevices, useCameraPermission } from 'react-native-vision-camera';

function CameraScreen() {
    const { hasPermission, requestPermission } = useCameraPermission();
    const devices = useCameraDevices();
    const device = devices.back;

    useEffect(() => {
        if (!hasPermission) {
            requestPermission();
        }
    }, [hasPermission]);

    if (!hasPermission) {
        return <Text>Camera permission not granted</Text>;
    }

    if (!device) {
        return <Text>Loading camera...</Text>;
    }

    return (
        <Camera
            style={{ flex: 1 }}
            device={device}
            isActive={true}
            photo={true}
        />
    );
}
```

### 3. Capture Photos

Take photos with proper error handling:

```typescript
import { Camera } from 'react-native-vision-camera';

function CameraCapture() {
    const camera = useRef<Camera>(null);

    const takePhoto = async () => {
        if (!camera.current) return;

        try {
            const photo = await camera.current.takePhoto({
                flash: 'auto',
                qualityPrioritization: 'quality',
            });
            console.log('Photo taken:', photo.path);
        } catch (error) {
            console.error('Failed to take photo:', error);
        }
    };

    return (
        <View style={{ flex: 1 }}>
            <Camera
                ref={camera}
                style={{ flex: 1 }}
                device={device}
                isActive={true}
                photo={true}
            />
            <Button title="Take Photo" onPress={takePhoto} />
        </View>
    );
}
```

### 4. Handle Camera Errors

Provide fallback behavior:

```typescript
function CameraView() {
    const [error, setError] = useState(null);

    if (error) {
        return (
            <View>
                <Text>Camera Error: {error}</Text>
                <Button
                    title="Retry"
                    onPress={() => setError(null)}
                />
                <Button
                    title="Pick from Gallery"
                    onPress={() => launchImageLibrary({ mediaType: 'photo' })}
                />
            </View>
        );
    }

    return (
        <Camera
            onError={(error) => setError(error.message)}
            // ... other props
        />
    );
}
```

## Common Scenarios

**Scenario 1: Camera permission works in iOS but not Android.**
Android requires both `CAMERA` permission and `WRITE_EXTERNAL_STORAGE` (for older API levels). Use `react-native-permissions` for consistent handling.

**Scenario 2: Camera preview shows black screen.**
Check that the camera device is correctly selected and `isActive` is set to `true`.

**Scenario 3: Photo capture fails silently.**
Ensure the camera ref is not null and the camera has finished initializing before calling `takePhoto`.

## Prevent It

1. **Always request permissions before opening the camera** to avoid runtime crashes.

2. **Use `react-native-vision-camera`** instead of deprecated camera libraries.

3. **Test on physical devices** — camera doesn't work in most simulators.
