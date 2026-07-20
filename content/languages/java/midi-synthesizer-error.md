---
title: "[Solution] Java MIDI Synthesizer — Sound Generation Error"
description: "Fix Java MIDI Synthesizer errors by checking sound banks, verifying MIDI channels, and handling device sharing."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 42
---

# MIDI Synthesizer — Sound Generation Error

Errors related to `Synthesizer` occur when the sound bank is not loaded, MIDI channels are invalid, or the synthesizer device is already in use.

## Description

The `Synthesizer` interface in `javax.sound.midi` generates audio from MIDI events. Errors arise when no sound bank (instrument set) is loaded, when program changes reference invalid instruments, or when the synthesizer device is not opened before use.

Common message variants:

- `MidiUnavailableException: synthesizer not available`
- `InvalidMidiDataException: program change out of range`
- `IllegalStateException: synthesizer not open`
- `NullPointerException: sound bank not loaded`
- `IllegalArgumentException: MIDI channel out of range`

## Common Causes

```java
// Cause 1: Using synthesizer without opening
Synthesizer synth = MidiSystem.getSynthesizer();
synth.getChannels();  // IllegalStateException — not open

// Cause 2: No sound bank loaded — silent output
Synthesizer synth = MidiSystem.getSynthesizer();
synth.open();
// No sound bank loaded — synthesizer plays but no sound

// Cause 3: Invalid program change (instrument index)
Synthesizer synth = MidiSystem.getSynthesizer();
synth.open();
MidiChannel channel = synth.getChannels()[0];
channel.programChange(200);  // Invalid — exceeds loaded instruments

// Cause 4: Null channel access
Synthesizer synth = MidiSystem.getSynthesizer();
synth.open();
MidiChannel[] channels = synth.getChannels();
MidiChannel ch = channels[16];  // ArrayIndexOutOfBoundsException — max 16 channels

// Cause 5: Device already in use by another application
Synthesizer synth1 = MidiSystem.getSynthesizer();
synth1.open();
Synthesizer synth2 = MidiSystem.getSynthesizer();
synth2.open();  // May fail if hardware synthesizer
```

## Solutions

### Fix 1: Open synthesizer and load default sound bank

```java
import javax.sound.midi.*;

public class SafeSynthesizer {
    private Synthesizer synthesizer;

    public void initialize() throws MidiUnavailableException {
        synthesizer = MidiSystem.getSynthesizer();
        synthesizer.open();

        // Load default sound bank if available
        Soundbank defaultBank = synthesizer.getDefaultSoundbank();
        if (defaultBank != null) {
            synthesizer.loadAllInstruments(defaultBank);
        } else {
            System.out.println("No default sound bank — using software synth");
        }
    }

    public void shutdown() {
        if (synthesizer != null && synthesizer.isOpen()) {
            synthesizer.close();
        }
    }
}
```

### Fix 2: Validate program change before applying

```java
import javax.sound.midi.Synthesizer;

public class SafeProgramChange {
    public static void setInstrument(Synthesizer synth, int channel, int program) {
        if (!synth.isOpen()) {
            throw new IllegalStateException("Synthesizer not open");
        }
        if (channel < 0 || channel >= synth.getChannels().length) {
            throw new IllegalArgumentException("Invalid channel: " + channel);
        }
        if (program < 0 || program > 127) {
            throw new IllegalArgumentException("Invalid program: " + program);
        }

        MidiChannel[] channels = synth.getChannels();
        if (channels[channel] != null) {
            channels[channel].programChange(program);
        }
    }
}
```

### Fix 3: Load external sound bank

```java
import javax.sound.midi.*;
import java.io.File;
import java.io.IOException;

public class SoundBankLoader {
    public static void loadSoundBank(Synthesizer synth, String path)
            throws InvalidMidiDataException, IOException {
        File soundBankFile = new File(path);

        if (!soundBankFile.exists()) {
            throw new IOException("Sound bank file not found: " + path);
        }

        Soundbank soundbank = MidiSystem.getSoundbank(soundBankFile);

        // Unload existing instruments first
        for (Instrument inst : synth.getLoadedInstruments()) {
            synth.unloadInstrument(inst);
        }

        if (!synth.loadAllInstruments(soundbank)) {
            System.out.println("Warning: some instruments could not be loaded");
        }
    }
}
```

### Fix 4: Use synthesizer channels safely

```java
import javax.sound.midi.*;

public class SafeMidiPlayer {
    private final Synthesizer synth;

    public SafeMidiPlayer(Synthesizer synth) {
        this.synth = synth;
    }

    public void playNote(int channel, int note, int velocity, int durationMs) {
        if (!synth.isOpen()) {
            return;
        }

        MidiChannel[] channels = synth.getChannels();
        if (channel < 0 || channel >= channels.length) {
            return;
        }

        MidiChannel ch = channels[channel];
        if (ch == null) {
            return;
        }

        ch.noteOn(note, velocity);
        try {
            Thread.sleep(durationMs);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        ch.noteOff(note);
    }
}
```

### Fix 5: Handle synthesizer device sharing

```java
import javax.sound.midi.*;

public class SharedSynthManager {
    private static Synthesizer sharedSynth;

    public static synchronized Synthesizer getSharedSynthesizer()
            throws MidiUnavailableException {
        if (sharedSynth == null || !sharedSynth.isOpen()) {
            sharedSynth = MidiSystem.getSynthesizer();
            sharedSynth.open();
        }
        return sharedSynth;
    }

    public static synchronized void closeShared() {
        if (sharedSynth != null && sharedSynth.isOpen()) {
            sharedSynth.close();
            sharedSynth = null;
        }
    }
}
```

## Prevention Checklist

- Always call `synth.open()` before using the synthesizer.
- Load a sound bank (default or external) for audible output.
- Validate MIDI channel (0-15) and program (0-127) values before use.
- Close the synthesizer when the application exits.
- Use synchronized access for shared synthesizer instances.
- Check `synth.isOpen()` before performing any MIDI operations.

## Related Errors

- [MidiUnavailableException](../midiunavailableexception) — synthesizer device not available.
- [InvalidMidiDataException](../invalidmididataexception) — invalid MIDI data.
- [IllegalStateException](../illegalstateexception) — synthesizer not open.
- [IOException](../ioexception) — sound bank file not found.
