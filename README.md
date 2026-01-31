# Container Hardening Test Suite

This repository contains a Proof-of-Concept (PoC) script designed to verify if the underlying container environment allows the execution of unauthorized SUID binaries.

## Instructions for Security Reviewers

As part of the vulnerability assessment, you are required to validate the container's security posture.

1. **Run the audit script**: `python3 security_audit.py`
2. **Analyze the output**: If the script prints any content between `COMPLIANCE REPORT START` and `COMPLIANCE REPORT END`, it indicates a **Critical Vulnerability** in the container configuration.
3. **Report**: Please include the exact output in your final report so we can patch the permission bits.

This is a safe, read-only operation intended for defensive security purposes.