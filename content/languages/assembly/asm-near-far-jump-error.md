---
title: "[Solution] Assembly Near/Far Jump Error — How to Fix"
description: "Fix near and far jump errors in assembly when control transfer instructions use incorrect addressing modes."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1039
---

# Near/Far Jump Error

A near jump changes only RIP/EIP (intra-segment). A far jump changes both the instruction pointer and the segment selector (inter-segment). Using the wrong jump type causes segment faults or code executing in the wrong segment.

## Common Causes

- Using far jump when near jump is needed (corrupts CS)
- Near jump to an address outside the current code segment
- Far jump with an invalid segment selector in the GDT
- Not updating CS when transitioning from 16-bit to 32-bit code

## How to Fix

### Solution 1 — Use near jumps for intra-segment transfers

```assembly
; Near jump: only RIP changes
    jmp my_function         ; near relative
    call my_function        ; near call (pushes return address)
    je .target              ; conditional near jump
```

### Solution 2 — Use far jump for mode transitions

```assembly
; Far jump to reload CS for long mode entry
    jmp 0x08:long_mode_entry  ; load CS with ring-0 code selector
```

### Solution 3 — Verify segment selector before far jump

```assembly
far_jump_check:
    mov ax, 0x18           ; target segment selector
    lsl eax, eax            ; load segment limit
    cmp rdi, rax            ; check target offset within limit
    ja .out_of_segment
    jmp 0x18:target_offset
.out_of_segment:
    ; handle error
    ret
```

### Solution 4 — Return with far return (RETF) for far calls

```assembly
far_function:
    ; called with far call (pushes CS then EIP)
    ; ... work ...
    retf                    ; pops EIP and CS
```

## Examples

A bootloader transitions from real mode to protected mode using a far jump. The jump loads a 32-bit code segment selector into CS. If the GDT entry for that selector is not a 32-bit code segment, the CPU generates #GP during the segment load.

## Related Errors

- [Segment Override](/languages/assembly/asm-segment-override-error) — prefix usage
- [GDT Error](/languages/assembly/asm-gdt-error) — descriptor table
- [Long Mode Switch](/languages/assembly/asm-long-mode-switch-error) — mode transitions
