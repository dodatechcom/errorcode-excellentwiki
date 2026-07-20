---
title: "[Solution] Java InvalidMidiDataException — Invalid MIDI Data"
description: "Fix Java InvalidMidiDataException by verifying MIDI format, checking sequence data, and validating MIDI events before processing."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 18
---

# InvalidMidiDataException — Invalid MIDI Data

An `InvalidMidiDataException` is thrown when MIDI data is invalid, malformed, or does not conform to the MIDI specification. This occurs when constructing MIDI messages, loading sequences, or setting properties that violate MIDI format constraints.

## Description

MIDI has strict format requirements for messages, sequences, and timing data. `InvalidMidiDataException` is a checked exception thrown when any of these requirements are violated — such as invalid note values, out-of-range velocities, or malformed MIDI files.

Common message variants:

- `javax.sound.midi.InvalidMidiDataException: invalid event type`
- `javax.sound.midi.InvalidMidiDataException: note value out of range`
- `javax.sound.midi.InvalidMidiDataException: invalid MIDI file format`
- `javax.sound.midi.InvalidMidiDataException: invalid channel`
- `javax.sound.midi.InvalidMidiDataException: resolution must be > 0`

## Common Causes

```java
// Cause 1: Invalid note value (must be 0-127)
ShortMessage msg = new ShortMessage();
msg.setMessage(ShortMessage.NOTE_ON, 0, 200, 100);  // note 200 > 127
// InvalidMidiDataException

// Cause 2: Invalid velocity (must be 0-127)
ShortMessage msg = new ShortMessage();
msg.setMessage(ShortMessage.NOTE_ON, 0, 60, 300);  // velocity 300 > 127
// InvalidMidiDataException

// Cause 3: Invalid channel (must be 0-15)
ShortMessage msg = new ShortMessage();
msg.setMessage(ShortMessage.NOTE_ON, 20, 60, 100);  // channel 20 > 15
// InvalidMidiDataException

// Cause 4: Invalid MIDI file data
byte[] badMidiData = {0x4D, 0x54, 0x68, 0x64};  // Incomplete header
InputStream is = new ByteArrayInputStream(badMidiData);
Sequence seq = MidiSystem.getMidiSequence(is);  // InvalidMidiDataException

// Cause 5: Invalid resolution
Sequence seq = new Sequence(Sequence.PPQ, 0);  // resolution must be > 0
// InvalidMidiDataException
```

## Solutions

### Fix 1: Validate MIDI parameters before creating messages

```java
import javax.sound.midi.*;

public class SafeMidiMessage {
    public static ShortMessage createNoteOn(int channel, int note, int velocity)
            throws InvalidMidiDataException {
        if (channel < 0 || channel > 15) {
            throw new IllegalArgumentException("Channel must be 0-15, got: " + channel);
        }
        if (note < 0 || note > 127) {
            throw new IllegalArgumentException("Note must be 0-127, got: " + note);
        }
        if (velocity < 0 || velocity > 127) {
            throw new IllegalArgumentException("Velocity must be 0-127, got: " + velocity);
        }

        ShortMessage msg = new ShortMessage();
        msg.setMessage(ShortMessage.NOTE_ON, channel, note, velocity);
        return msg;
    }

    public static ShortMessage createNoteOff(int channel, int note)
            throws InvalidMidiDataException {
        return createNoteOn(channel, note, 0);  // NOTE_OFF with velocity 0
    }
}
```

### Fix 2: Validate MIDI file before loading

```java
import javax.sound.midi.*;
import java.io.*;

public class MidiFileValidator {
    public static boolean isValidMidiFile(File file) {
        if (!file.exists()) {
            return false;
        }

        try (FileInputStream fis = new FileInputStream(file)) {
            byte[] header = new byte[4];
            if (fis.read(header) != 4) {
                return false;
            }

            // Check MIDI file magic number: MThd
            return header[0] == 'M' && header[1] == 'T' &&
                   header[2] == 'h' && header[3] == 'd';
        } catch (IOException e) {
            return false;
        }
    }

    public static Sequence loadMidiFile(File file)
            throws InvalidMidiDataException, IOException {
        if (!isValidMidiFile(file)) {
            throw new InvalidMidiDataException("Not a valid MIDI file: " + file.getName());
        }

        return MidiSystem.getMidiSequence(file);
    }
}
```

### Fix 3: Use safe sequence creation

```java
import javax.sound.midi.*;

public class SafeSequenceBuilder {
    public static Sequence createSequence(int resolution)
            throws InvalidMidiDataException {
        if (resolution <= 0) {
            throw new IllegalArgumentException("Resolution must be > 0, got: " + resolution);
        }

        return new Sequence(Sequence.PPQ, resolution);
    }

    public static Sequence createTempoSequence(int bpm) throws InvalidMidiDataException {
        Sequence sequence = new Sequence(Sequence.PPQ, 240);
        Track track = sequence.createTrack();

        // Set tempo using meta message
        int microsPerBeat = 60_000_000 / bpm;
        byte[] tempoBytes = new byte[]{
            (byte) ((microsPerBeat >> 16) & 0xFF),
            (byte) ((microsPerBeat >> 8) & 0xFF),
            (byte) (microsPerBeat & 0xFF)
        };

        MetaMessage tempoMsg = new MetaMessage();
        tempoMsg.setMessage(0x51, tempoBytes, 3);
        track.add(new MidiEvent(tempoMsg, 0));

        return sequence;
    }
}
```

### Fix 4: Handle invalid MIDI data in processing loops

```java
import javax.sound.midi.*;

public class MidiEventProcessor {
    public static void processSequence(Sequence sequence) {
        for (Track track : sequence.getTracks()) {
            for (int i = 0; i < track.size(); i++) {
                MidiEvent event = track.get(i);
                MidiMessage message = event.getMessage();

                if (message instanceof ShortMessage) {
                    ShortMessage sm = (ShortMessage) message;
                    try {
                        int command = sm.getCommand();
                        int channel = sm.getChannel();
                        int data1 = sm.getData1();
                        int data2 = sm.getData2();

                        if (command == ShortMessage.NOTE_ON && data2 > 0) {
                            if (channel < 0 || channel > 15 ||
                                data1 < 0 || data1 > 127 ||
                                data2 < 0 || data2 > 127) {
                                System.err.println("Skipping invalid event at tick "
                                    + event.getTick());
                                continue;
                            }
                            System.out.println("Note ON: " + data1
                                + " on channel " + channel);
                        }
                    } catch (InvalidMidiDataException e) {
                        System.err.println("Invalid MIDI data at event "
                            + event.getTick() + ": " + e.getMessage());
                    }
                } else if (message instanceof MetaMessage) {
                    MetaMessage mm = (MetaMessage) message;
                    System.out.println("Meta event type: " + mm.getType());
                }
            }
        }
    }
}
```

### Fix 5: Safe MIDI message factory

```java
import javax.sound.midi.*;

public class MidiMessageFactory {
    public static ShortMessage programChange(int channel, int program)
            throws InvalidMidiDataException {
        if (channel < 0 || channel > 15) {
            throw new IllegalArgumentException("Invalid channel: " + channel);
        }
        if (program < 0 || program > 127) {
            throw new IllegalArgumentException("Invalid program: " + program);
        }

        ShortMessage msg = new ShortMessage();
        msg.setMessage(ShortMessage.PROGRAM_CHANGE, channel, program, 0);
        return msg;
    }

    public static ShortMessage controlChange(int channel, int controller, int value)
            throws InvalidMidiDataException {
        if (channel < 0 || channel > 15) {
            throw new IllegalArgumentException("Invalid channel: " + channel);
        }
        if (controller < 0 || controller > 127) {
            throw new IllegalArgumentException("Invalid controller: " + controller);
        }
        if (value < 0 || value > 127) {
            throw new IllegalArgumentException("Invalid value: " + value);
        }

        ShortMessage msg = new ShortMessage();
        msg.setMessage(ShortMessage.CONTROL_CHANGE, channel, controller, value);
        return msg;
    }
}
```

## Prevention Checklist

- Validate all MIDI parameters (channel 0-15, note 0-127, velocity 0-127).
- Check MIDI file headers before loading (`MThd` magic number).
- Use positive resolution values for `Sequence` creation.
- Handle `InvalidMidiDataException` when loading external MIDI files.
- Validate MIDI events before processing in loops.
- Use factory methods with built-in validation for MIDI messages.

## Related Errors

- [MidiUnavailableException](../midiunavailableexception) — MIDI device not available.
- [IOException](../ioexception) — MIDI file I/O error.
- [IllegalArgumentException](../illegalargumentexception) — invalid method parameters.
