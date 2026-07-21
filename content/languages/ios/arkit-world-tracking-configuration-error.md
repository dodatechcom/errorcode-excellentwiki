---
title: "[Solution] ARKit World Tracking Configuration Error"
description: "Fix ARKit world tracking session configuration and failure errors."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# ARKit World Tracking Configuration Error

World tracking fails when the configuration is incompatible with the device, when camera access is denied, or when tracking quality degrades.

## Common Causes
- Device does not support world tracking
- Camera permission not granted
- ARKit session fails to start
- Tracking quality too low for reliable tracking

## How to Fix
1. Check ARWorldTrackingConfiguration.isSupported
2. Request camera permission before starting session
3. Handle session failure in delegate
4. Monitor tracking quality and provide feedback

```swift
// Setup AR session:
if ARWorldTrackingConfiguration.isSupported {
    let configuration = ARWorldTrackingConfiguration()
    configuration.planeDetection = [.horizontal, .vertical]
    sceneView.session.run(configuration)
}

// Handle failures:
func session(_ session: ARSession, didFailWithError error: Error) {
    print("Session failed: \(error)")
}
```

## Examples
```swift
// AR session management:
class ARViewController: UIViewController, ARSCNViewDelegate {
    @IBOutlet var sceneView: ARSCNView!

    override func viewDidLoad() {
        super.viewDidLoad()
        sceneView.delegate = self
        guard ARWorldTrackingConfiguration.isSupported else {
            showError("Device does not support AR")
            return
        }
    }

    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        let config = ARWorldTrackingConfiguration()
        config.planeDetection = .horizontal
        sceneView.session.run(config, options: [.resetTracking, .removeExistingAnchors])
    }

    func sessionWasInterrupted(_ session: ARSession) {
        print("Session interrupted")
    }
}
```
