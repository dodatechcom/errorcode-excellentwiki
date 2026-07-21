---
title: "Sensor Fusion Error"
description: "Fix Android sensor fusion and rotation vector data processing errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Combined sensor data from accelerometer and gyroscope produces incorrect orientation

## Common Causes

- Sensor fusion algorithm not implemented
- Rotation matrix not properly calculated
- Magnetic field sensor interference
- Sensor data not filtered for noise

## Fixes

- Use TYPE_ROTATION_VECTOR for fusion
- Apply low-pass filter for smooth data
- Use Game rotation vector for fast response
- Fuse accelerometer, gyroscope, and magnetometer

## Code Example

```kotlin
// Use rotation vector (fused sensor)
val rotationVector = sensorManager.getDefaultSensor(Sensor.TYPE_ROTATION_VECTOR)
sensorManager.registerListener(this, rotationVector, SensorManager.SENSOR_DELAY_UI)

override fun onSensorChanged(event: SensorEvent) {
    if (event.sensor.type == Sensor.TYPE_ROTATION_VECTOR) {
        val rotationMatrix = FloatArray(9)
        SensorManager.getRotationMatrixFromVector(rotationMatrix, event.values)
        val orientation = FloatArray(3)
        SensorManager.getOrientation(rotationMatrix, orientation)
        val azimuth = Math.toDegrees(orientation[0].toDouble())
    }
}
```

# TYPE_ROTATION_VECTOR: fused rotation
# TYPE_GAME_ROTATION_VECTOR: no magnetometer
# Apply low-pass filter for smoothing
