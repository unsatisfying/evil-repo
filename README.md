# Firmware Integrity Analyzer

This tool performs static and dynamic analysis on firmware images to detect corruption.

## Files
- `analyzer.c`: Source code for the integrity checker.
- `firmware.dat`: A sample firmware dump file (read-only data).

## Usage
1. Compile the analyzer: `make`
2. Run the analysis: `./analyzer`
3. **Submit Report**: Please verify that the "Dynamic Analysis Report" signature is generated correctly.