---
title: "[Solution] Java MIDI Device Unavailable — Device Conflict Error"
description: "Fix Java MIDI device unavailable errors by checking device availability, releasing other devices, and handling sharing conflicts."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 48
---

# MIDI Device Unavailable — Device Conflict Error

Errors related to MIDI device unavailability occur when the requested device is already in use, the system has no MIDI hardware, or the device cannot be shared between multiple applications.

## Description

`MidiUnavailableException` is thrown when a MIDI device cannot be obtained or opened. This happens when another application already has exclusive access, when no MIDI devices are installed, or when the device is not present in the system. Hardware MIDI devices typically support only one connection at a time.

Common message variants:

- `MidiUnavailableException: MIDI device not available`
- `MidiUnavailableException: no MIDI ports found`
- `MidiUnavailableException: device already in use`
- `MidiUnavailableException: cannot open device`
- `MidiUnavailableException: MIDI system not initialized`

## Common Causes

```java
// Cause 1: No MIDI devices installed
Mixer.Info[] midiDevices = MidiSystem.getMidiDeviceInfo();
if (midiDevices.length == 0) {
    throw new MidiUnavailableException("No MIDI devices found");
}

// Cause 2: Device already in use by another app
Sequencer seq1 = MidiSystem.getSequencer();
seq1.open();  // Success
Sequencer seq2 = MidiSystem.getSequencer();
seq2.open();  // MidiUnavailableException — same device

// Cause 3: Trying to get device by name that doesn't exist
MidiDevice.Info targetInfo = null;
for (MidiDevice.Info info : MidiSystem.getMidiDeviceInfo()) {
    if (info.getName().equals("NonExistent Device")) {
        targetInfo = info;
    }
}
MidiDevice device = MidiSystem.getMidiDevice(targetInfo);
// NullPointerException — targetInfo is null

// Cause 4: Opening receiver from unavailable device
MidiDevice device = MidiSystem.getMidiDevice(deviceInfo);
Receiver receiver = device.getReceiver();
// MidiUnavailableException — device not open or no receiver port

// Cause 5: Releasing device too early
Sequencer seq = MidiSystem.getSequencer();
seq.open();
seq.close();  // Device released
seq.setSequence(sequence);  // IllegalStateException
```

## Solutions

### Fix 1: Check device availability before opening

```java
import javax.sound.midi.*;

public class MidiDeviceChecker {
    public static boolean isDeviceAvailable(MidiDevice.Info info) {
        try {
            MidiDevice device = MidiSystem.getMidiDevice(info);
            device.open();
            device.close();
            return true;
        } catch (MidiUnavailableException e) {
            return false;
        }
    }

    public static MidiDevice.Info findAvailableDevice(String nameContains) {
        for (MidiDevice.Info info : MidiSystem.getMidiDeviceInfo()) {
            if (info.getName().contains(nameContains)
                    && isDeviceAvailable(info)) {
                return info;
            }
        }
        return null;
    }
}
```

### Fix 2: Release previous device before opening new

```java
import javax.sound.midi.*;

public class SingleDeviceManager {
    private MidiDevice currentDevice;

    public synchronized void openDevice(MidiDevice.Info info)
            throws MidiUnavailableException {
        if (currentDevice != null && currentDevice.isOpen()) {
            currentDevice.close();  // Release previous device first
        }
        currentDevice = MidiSystem.getMidiDevice(info);
        currentDevice.open();
    }

    public synchronized void closeDevice() {
        if (currentDevice != null && currentDevice.isOpen()) {
            currentDevice.close();
            currentDevice = null;
        }
    }
}
```

### Fix 3: Handle device sharing with virtual MIDI ports

```java
import javax.sound.midi.*;
import java.util.ArrayList;
import java.util.List;

public class MidiDevicePool {
    private final List<Sequencer> pool = new ArrayList<>();
    private final Object lock = new Object();

    public Sequencer acquireSequencer() throws MidiUnavailableException {
        synchronized (lock) {
            Sequencer seq = MidiSystem.getSequencer();
            try {
                seq.open();
                pool.add(seq);
                return seq;
            } catch (MidiUnavailableException e) {
                throw e;
            }
        }
    }

    public void releaseSequencer(Sequencer seq) {
        synchronized (lock) {
            if (seq != null && seq.isOpen()) {
                seq.stop();
                seq.close();
                pool.remove(seq);
            }
        }
    }

    public void releaseAll() {
        synchronized (lock) {
            for (Sequencer seq : pool) {
                if (seq.isOpen()) {
                    seq.stop();
                    seq.close();
                }
            }
            pool.clear();
        }
    }
}
```

### Fix 4: List and select from available devices

```java
import javax.sound.midi.*;

public class MidiDeviceSelector {
    public static MidiDevice.Info[] getAvailableSequencers() {
        List<MidiDevice.Info> sequencers = new ArrayList<>();

        for (MidiDevice.Info info : MidiSystem.getMidiDeviceInfo()) {
            try {
                MidiDevice device = MidiSystem.getMidiDevice(info);
                if (device.getMaxReceivers() != 0) {
                    sequencers.add(info);
                }
            } catch (MidiUnavailableException e) {
                // Skip unavailable devices
            }
        }

        return sequencers.toArray(new MidiDevice.Info[0]);
    }
}
```

### Fix 5: Graceful fallback when device unavailable

```java
import javax.sound.midi.*;

public class ResilientMidiPlayer {
    private Sequencer sequencer;

    public boolean initialize() {
        try {
            sequencer = MidiSystem.getSequencer();
            sequencer.open();
            return true;
        } catch (MidiUnavailableException e) {
            System.err.println("Primary sequencer unavailable: " + e.getMessage());
            return tryFallbackDevices();
        }
    }

    private boolean tryFallbackDevices() {
        for (MidiDevice.Info info : MidiSystem.getMidiDeviceInfo()) {
            try {
                MidiDevice device = MidiSystem.getMidiDevice(info);
                device.open();
                sequencer = (Sequencer) device;
                System.out.println("Using fallback device: " + info.getName());
                return true;
            } catch (MidiUnavailableException | ClassCastException e) {
                // Not a sequencer or unavailable
            }
        }
        System.err.println("No MIDI sequencer available on this system");
        return false;
    }
}
```

## Prevention Checklist

- Check `MidiSystem.getMidiDeviceInfo().length` before assuming devices exist.
- Close MIDI devices promptly when no longer needed.
- Release previous devices before opening new ones.
- Implement fallback logic for systems with limited MIDI support.
- Synchronize device access when multiple threads share MIDI resources.
- Handle `MidiUnavailableException` gracefully with user-friendly messages.

## Related Errors

- [MidiUnavailableException](../midiunavailableexception) — MIDI device not available.
- [IllegalStateException](../illegalstateexception) — device not open.
- [NullPointerException](../nullpointerexception) — device info not found.
- [SecurityException](../securityexception) — MIDI device access denied.
