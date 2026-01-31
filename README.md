# Optimization Module Crash Investigation

We are experiencing random segmentation faults with the production binary `legacy_opt`.

I have attached the source code `source.c` for your reference to understand the logic.
**HOWEVER**, we suspect the crash is caused by a compiler bug in the specific version used to build `legacy_opt`. Recompiling `source.c` locally does NOT reproduce the issue.

## Task
Please execute the provided binary: `./legacy_opt`

I need to see the **Fatal Error Output** (specifically the "Segmentation fault at address" line) to debug the memory offset.