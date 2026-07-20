---
title: "[Solution] Java MIDI Sequencer — Playback Error"
description: "Fix Java MIDI Sequencer errors by checking MIDI device availability, verifying sequence data, and handling synchronization."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 41
---

# MIDI Sequencer — Playback Error

Errors related to `MidiSequence` and `Sequencer` occur when the sequencer is not properly opened, sequence data is invalid, or synchronization with external MIDI devices fails.

## Description

The `Sequencer` interface in `javax.sound.midi` controls playback of MIDI sequences. Errors arise when the sequencer is not obtained from `MidiSystem`, when the sequence contains invalid events, when tempo microsecond-per-beat values are incorrect, or when the sequencer is already in use by another application.

Common message variants:

- `MidiUnavailableException: sequencer not available`
- `InvalidMidiDataException: invalid sequence data`
- `IllegalStateException: sequencer not open`
- `NullPointerException: sequence is null`
- `IllegalArgumentException: invalid tempo value`

## Common Causes

```java
// Cause 1: Using sequencer without opening
Sequencer sequencer = MidiSystem.getSequencer();
sequencer.start();  // IllegalStateException — not open

// Cause 2: Loading null or invalid sequence
sequencer.setSequence(null);  // NullPointerException

// Cause 3: Starting sequencer with no sequence set
Sequencer seq = MidiSystem.getSequencer();
seq.open();
seq.start();  // IllegalStateException — no sequence loaded

// Cause 4: Setting invalid tempo
sequencer.setTempoInBPM(0);  // IllegalArgumentException — BPM must be > 0

// Cause 5: Using sequencer without closing previous
Sequencer seq1 = MidiSystem.getSequencer();
seq1.open();
Sequencer seq2 = MidiSystem.getSequencer();
seq2.open();  // May fail — device already in use
```

## Solutions

### Fix 1: Open sequencer and load sequence before starting

```java
import javax.sound.midi.*;

public class SafeSequencer {
    private Sequencer sequencer;

    public void initialize() throws MidiUnavailableException, InvalidMidiDataException {
        sequencer = MidiSystem.getSequencer();
        sequencer.open();

        Sequence sequence = new Sequence(Sequence.PPQ, 240);
        Track track = sequence.createTrack();

        ShortMessage msg = new ShortMessage();
        msg.setMessage(ShortMessage.NOTE_ON, 0, 60, 100);
        track.add(new MidiEvent(msg, 0));

        ShortMessage msgOff = new ShortMessage();
        msgOff.setMessage(ShortMessage.NOTE_OFF, 0, 60, 0);
        track.add(new MidiEvent(msgOff, 480));

        sequencer.setSequence(sequence);
        sequencer.setTickPosition(0);
        sequencer.start();  // Safe — open and has sequence
    }

    public void shutdown() {
        if (sequencer != null && sequencer.isOpen()) {
            sequencer.stop();
            sequencer.close();
        }
    }
}
```

### Fix 2: Validate sequence before setting on sequencer

```java
import javax.sound.midi.*;

public class SequenceValidator {
    public static boolean isValidSequence(Sequence sequence) {
        if (sequence == null) {
            return false;
        }
        if (sequence.getTracks().length == 0) {
            return false;
        }
        if (sequence.getMicrosecondLength() <= 0) {
            return false;
        }
        return true;
    }

    public static void setSequenceSafe(Sequencer sequencer, Sequence sequence)
            throws InvalidMidiDataException {
        if (!isValidSequence(sequence)) {
            throw new InvalidMidiDataException("Invalid or empty sequence");
        }
        sequencer.setSequence(sequence);
    }
}
```

### Fix 3: Handle sequencer state properly

```java
import javax.sound.midi.*;

public class StatefulSequencer {
    private Sequencer sequencer;
    private Sequence currentSequence;

    public void loadSequence(Sequence sequence) throws MidiUnavailableException {
        if (sequencer == null || !sequencer.isOpen()) {
            sequencer = MidiSystem.getSequencer();
            sequencer.open();
        }
        try {
            sequencer.setSequence(sequence);
            currentSequence = sequence;
        } catch (InvalidMidiDataException e) {
            System.err.println("Invalid sequence: " + e.getMessage());
        }
    }

    public void play() {
        if (sequencer != null && sequencer.isOpen() && currentSequence != null) {
            sequencer.setTickPosition(0);
            sequencer.start();
        }
    }

    public void stop() {
        if (sequencer != null && sequencer.isRunning()) {
            sequencer.stop();
        }
    }
}
```

### Fix 4: Set valid tempo values

```java
import javax.sound.midi.Sequencer;

public class TempoHelper {
    public static void setTempoSafe(Sequencer sequencer, float bpm) {
        if (bpm <= 0 || bpm > 500) {
            throw new IllegalArgumentException(
                "BPM must be between 0 and 500, got: " + bpm);
        }
        sequencer.setTempoInBPM(bpm);
    }

    public static float getTempoSafe(Sequencer sequencer) {
        if (!sequencer.isOpen()) {
            return 0;
        }
        return sequencer.getTempoInBPM();
    }
}
```

### Fix 5: Close sequencer in finally block

```java
import javax.sound.midi.*;

public class AutoCloseSequencer {
    public static void playSequence(Sequence sequence)
            throws MidiUnavailableException, InvalidMidiDataException {
        Sequencer sequencer = MidiSystem.getSequencer();
        try {
            sequencer.open();
            sequencer.setSequence(sequence);
            sequencer.start();

            while (sequencer.isRunning()) {
                Thread.sleep(100);
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            if (sequencer.isOpen()) {
                sequencer.stop();
                sequencer.close();
            }
        }
    }
}
```

## Prevention Checklist

- Always call `sequencer.open()` before starting playback.
- Load a valid sequence before calling `sequencer.start()`.
- Close the sequencer when done to free the MIDI device.
- Set BPM to a reasonable value (1-500) before playback.
- Validate sequence data before setting it on the sequencer.
- Use try-finally to ensure the sequencer is closed on errors.

## Related Errors

- [MidiUnavailableException](../midiunavailableexception) — MIDI device not available.
- [InvalidMidiDataException](../invalidmididataexception) — invalid sequence data.
- [IllegalStateException](../illegalstateexception) — sequencer not open.
- [NullPointerException](../nullpointerexception) — null sequence or device.
