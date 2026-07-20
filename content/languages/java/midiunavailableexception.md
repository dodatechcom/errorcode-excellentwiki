---
title: "[Solution] Java MidiUnavailableException — MIDI Device Unavailable"
description: "Fix Java MidiUnavailableException by checking MIDI device availability, releasing MIDI resources, and handling device conflicts properly."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 17
---

# MidiUnavailableException — MIDI Device Unavailable

A `MidiUnavailableException` is thrown when a MIDI device (synthesizer, sequencer, or MIDI port) cannot be opened or is not available. This commonly occurs when MIDI resources are already in use or when no MIDI device is present on the system.

## Description

Java Sound MIDI API provides access to MIDI devices through `Synthesizer`, `Sequencer`, and `MidiDevice` interfaces. Each device requires exclusive access to system MIDI resources. When a device is already open by another application or thread, `MidiUnavailableException` is thrown.

Common message variants:

- `javax.sound.midi.MidiUnavailableException: MIDI device not available`
- `javax.sound.midi.MidiUnavailableException: Synthesizer not available`
- `javax.sound.midi.MidiUnavailableException: Sequencer not available`
- `javax.sound.midi.MidiUnavailableException: cannot open device`

## Common Causes

```java
// Cause 1: Opening sequencer twice
import javax.sound.midi.*;

Sequencer seq1 = MidiSystem.getSequencer();
seq1.open();  // First open succeeds

Sequencer seq2 = MidiSystem.getSequencer();
seq2.open();  // MidiUnavailableException — sequencer already in use

// Cause 2: No MIDI device on system
// Headless server without MIDI support
Synthesizer synth = MidiSystem.getSynthesizer();
synth.open();  // MidiUnavailableException

// Cause 3: Opening device without checking availability
MidiDevice.Info[] infos = MidiSystem.getMidiDeviceInfo();
MidiDevice device = MidiSystem.getMidiDevice(infos[0]);
device.open();  // May throw if device unavailable

// Cause 4: Sequencer not loaded with sequence
Sequencer sequencer = MidiSystem.getSequencer();
sequencer.open();
// Sequence not loaded — some operations may fail
sequencer.start();  // May behave unexpectedly

// Cause 5: MIDI device closed while in use
MidiDevice device = MidiSystem.getMidiDevice(info);
device.open();
device.close();
// Subsequent operations fail
```

## Solutions

### Fix 1: Check device availability before opening

```java
import javax.sound.midi.*;

public class SafeMidiDevice {
    public static MidiDevice openDevice(MidiDevice.Info info)
            throws MidiUnavailableException {
        MidiDevice device = MidiSystem.getMidiDevice(info);

        if (device.isOpen()) {
            System.out.println("Device already open: " + info.getName());
            return device;
        }

        try {
            device.open();
            return device;
        } catch (MidiUnavailableException e) {
            System.err.println("Cannot open MIDI device: " + info.getName());
            throw e;
        }
    }
}
```

### Fix 2: Use try-with-resources for MIDI devices

```java
import javax.sound.midi.*;

public class MidiPlayer {
    public static void playSequence(Sequence sequence) {
        try (Sequencer sequencer = MidiSystem.getSequencer()) {
            sequencer.open();
            sequencer.setSequence(sequence);
            sequencer.start();

            while (sequencer.isRunning()) {
                Thread.sleep(100);
            }
        } catch (MidiUnavailableException e) {
            System.err.println("Sequencer unavailable: " + e.getMessage());
        } catch (InvalidMidiDataException e) {
            System.err.println("Invalid MIDI data: " + e.getMessage());
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } catch (Exception e) {
            System.err.println("MIDI error: " + e.getMessage());
        }
    }
}
```

### Fix 3: Handle MIDI device conflicts with retry

```java
import javax.sound.midi.*;

public class ResilientMidiPlayer {
    private Sequencer sequencer;

    public void initialize() {
        try {
            sequencer = MidiSystem.getSequencer();
            if (sequencer == null) {
                System.err.println("No sequencer available");
                return;
            }

            if (!sequencer.isOpen()) {
                sequencer.open();
            }
        } catch (MidiUnavailableException e) {
            System.err.println("Sequencer unavailable, trying synthesizer");
            try {
                Synthesizer synth = MidiSystem.getSynthesizer();
                synth.open();
                sequencer = synth.getSequencer();
                if (sequencer != null && !sequencer.isOpen()) {
                    sequencer.open();
                }
            } catch (MidiUnavailableException ex) {
                System.err.println("No MIDI device available: " + ex.getMessage());
            }
        }
    }

    public void close() {
        if (sequencer != null && sequencer.isOpen()) {
            sequencer.stop();
            sequencer.close();
        }
    }
}
```

### Fix 4: List available MIDI devices

```java
import javax.sound.midi.*;

public class MidiDeviceLister {
    public static void main(String[] args) {
        MidiDevice.Info[] infos = MidiSystem.getMidiDeviceInfo();

        System.out.println("Available MIDI devices:");
        for (MidiDevice.Info info : infos) {
            System.out.println("  Name: " + info.getName());
            System.out.println("  Vendor: " + info.getVendor());
            System.out.println("  Version: " + info.getVersion());
            System.out.println("  Description: " + info.getDescription());

            try {
                MidiDevice device = MidiSystem.getMidiDevice(info);
                System.out.println("  Max Transmitters: " + device.getMaxTransmitters());
                System.out.println("  Max Receivers: " + device.getMaxReceivers());
                System.out.println("  Open: " + device.isOpen());
            } catch (MidiUnavailableException e) {
                System.out.println("  Status: Unavailable");
            }
            System.out.println();
        }
    }
}
```

### Fix 5: Proper MIDI lifecycle management

```java
import javax.sound.midi.*;

public class MidiLifecycleManager {
    private MidiDevice device;
    private Receiver receiver;

    public void openDevice(MidiDevice.Info info) throws MidiUnavailableException {
        device = MidiSystem.getMidiDevice(info);
        device.open();
        receiver = device.getReceiver();
    }

    public void sendNote(int channel, int note, int velocity) {
        if (receiver == null) {
            System.err.println("MIDI receiver not initialized");
            return;
        }

        try {
            ShortMessage msg = new ShortMessage();
            msg.setMessage(ShortMessage.NOTE_ON, channel, note, velocity);
            receiver.send(msg, -1);
        } catch (InvalidMidiDataException e) {
            System.err.println("Invalid MIDI message: " + e.getMessage());
        }
    }

    public void close() {
        try {
            if (receiver != null) {
                receiver.close();
            }
        } finally {
            if (device != null && device.isOpen()) {
                device.close();
            }
        }
    }

    @Override
    protected void finalize() throws Throwable {
        close();
        super.finalize();
    }
}
```

## Prevention Checklist

- Always check `device.isOpen()` before calling `device.open()`.
- Use try-with-resources or try-finally to ensure MIDI devices are closed.
- Provide fallback MIDI devices (sequencer vs. synthesizer).
- List available devices before attempting to open specific ones.
- Implement graceful degradation when MIDI is unavailable.
- Close MIDI devices in shutdown hooks or `finalize()`.

## Related Errors

- [LineUnavailableException](../lineunavailableexception) — audio line cannot be opened.
- [InvalidMidiDataException](../invalidmididataexception) — MIDI data is invalid or malformed.
- [IllegalArgumentException](../illegalargumentexception) — invalid MIDI parameters.
