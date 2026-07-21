---
title: "[Solution] Core Audio AudioUnit Configuration Error"
description: "Fix AudioUnit configuration and initialization errors in iOS audio apps."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Core Audio AudioUnit Configuration Error

AudioUnit setup fails when the component description is incorrect, when audio session category conflicts, or when the unit is not properly initialized.

## Common Causes
- Wrong AudioComponentDescription for desired unit
- Audio session not configured before unit creation
- Unit not initialized before use
- Format mismatch between input and output

## How to Fix
1. Use correct AudioComponentDescription for the unit type
2. Configure audio session before creating AudioUnit
3. Initialize the unit after configuration
4. Verify format compatibility between connected units

```swift
// Create AudioUnit:
var desc = AudioComponentDescription(
    componentType: kAudioUnitType_Output,
    componentSubType: kAudioUnitSubType_RemoteIO,
    componentManufacturer: kAudioUnitManufacturer_Apple,
    componentFlags: 0,
    componentFlagsMask: 0
)

let component = AudioComponentFindNext(nil, &desc)
var unit: AudioUnit?
AudioComponentInstanceNew(component!, &unit)
```

## Examples
```swift
// Audio unit setup:
func setupAudioUnit() {
    var desc = AudioComponentDescription(
        componentType: kAudioUnitType_Output,
        componentSubType: kAudioUnitSubType_VoiceProcessingIO,
        componentManufacturer: kAudioUnitManufacturer_Apple,
        componentFlags: 0,
        componentFlagsMask: 0
    )
    guard let component = AudioComponentFindNext(nil, &desc) else { return }
    var unit: AudioUnit?
    AudioComponentInstanceNew(component, &unit)
    guard let audioUnit = unit else { return }

    var enableIO: UInt32 = 1
    AudioUnitSetProperty(audioUnit, kAudioOutputUnitProperty_EnableIO, kAudioUnitScope_Input, 1, &enableIO, UInt32(MemoryLayout<UInt32>.size))
}
```
