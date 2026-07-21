---
title: "Sensor Not Available Error"
description: "Fix Android sensor availability and accelerometer/gyroscope errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Sensor data not available or returns incorrect values

## Common Causes

- Sensor not available on device
- Sensor manager not properly obtained
- Sensor listener not registered
- Sensor delay too fast or too slow

## Fixes

- Check sensor availability with hasSystemFeature
- Get SensorManager from SYSTEM_SERVICE
- Register listener with appropriate delay
- Use SENSOR_DELAY_NORMAL for UI updates

## Code Example

```kotlin
val sensorManager = getSystemService(Context.SENSOR_SERVICE) as SensorManager
val accelerometer = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER)

if (accelerometer != null) {
    sensorManager.registerListener(
        this,
        accelerometer,
        SensorManager.SENSOR_DELAY_NORMAL
    )
} else {
    // Sensor not available on this device
}

override fun onSensorChanged(event: SensorEvent) {
    if (event.sensor.type == Sensor.TYPE_ACCELEROMETER) {
        val x = event.values[0]
        val y = event.values[1]
        val z = event.values[2]
    }
}
```

# SENSOR_DELAY_FASTEST: 0ms (testing)
# SENSOR_DELAY_GAME: 20ms
# SENSOR_DELAY_UI: 60ms
# SENSOR_DELAY_NORMAL: 200ms
