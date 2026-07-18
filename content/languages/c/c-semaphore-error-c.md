---
title: "[Solution] C Semaphore Error — How to Fix"
description: "Fix C semaphore initialization, wait/post errors, and use in producer-consumer patterns."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Semaphore Error — How to Fix

Semaphores control access to shared resources. Common errors include not initializing semaphores, using post instead of wait (inverted logic), integer overflow from excessive post, and not handling EINTR from interrupted waits.

## Common Error Messages

- `sem_wait: Interrupted system call`
- `Semaphore not initialized — undefined behavior`
- `sem_post causes count overflow`
- `Deadlock from semaphore misuse`

## How to Fix It

### Initialize semaphore correctly

```c
#include <semaphore.h>
#include <stdio.h>

sem_t sem;

int main(void) {
    if (sem_init(&sem, 0, 1) == -1) {
        perror("sem_init");
        return 1;
    }
    sem_wait(&sem);
    printf("In critical section\n");
    sem_post(&sem);
    sem_destroy(&sem);
    return 0;
}
```

### Handle EINTR from sem_wait

```c
#include <semaphore.h>
#include <errno.h>

void wait_safe(sem_t *sem) {
    while (sem_wait(sem) == -1) {
        if (errno != EINTR) {
            perror("sem_wait");
            return;
        }
    }
}
```

### Use semaphores for producer-consumer

```c
#include <semaphore.h>
#include <stdio.h>

sem_t empty, full;
#define BUFFER_SIZE 10
int buffer[BUFFER_SIZE];

void producer(int item) {
    sem_wait(&empty);
    buffer[0] = item;
    sem_post(&full);
}

int consumer(void) {
    sem_wait(&full);
    int item = buffer[0];
    sem_post(&empty);
    return item;
}
```

### Use named semaphores for cross-process

```c
#include <semaphore.h>
sem_t *sem = sem_open("/mysem", O_CREAT, 0644, 1);
if (sem == SEM_FAILED) { perror("sem_open"); return 1; }
sem_wait(sem);
// ... critical section ...
sem_post(sem);
sem_close(sem);
sem_unlink("/mysem");
```

## Common Scenarios

### Scenario 1: Using sem_post instead of sem_wait — inverts the logic

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Forgetting to initialize semaphore before first wait

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Not handling EINTR when sem_wait is interrupted by signal

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always initialize semaphores with sem_init
- **Tip 2:** Handle EINTR by retrying sem_wait
- **Tip 3:** Use separate semaphores for empty/full in producer-consumer
