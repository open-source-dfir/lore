# Reporting Issues

This short guide provides a recommendations for isolating issues in tools and writing issue
reports that developers can instantly action.

### Troubleshooting Framework

Before filing a report, systematically isolate the failure to determine whether it is an
environmental quirk, a corrupted image, or a genuine code defect.

```text
 [ Tool Failure Detected ]
             │
             ▼
   Verify Hash Integrity ───(Mismatch)──► Recopy/Re-acquire Image
             │
        (Matches)
             ▼
 Isolate Test Artifacts ──(Works elsewhere)─► Environment Issue (OS/RAM)
             │
     (Still Fails)
             ▼
 Check Alternate Tool ────(Fails there too)─► Damaged/Corrupt Evidence
             │
      (Works there)
             ▼
[ Confirmed Tool Issue ] ──► Proceed to Report Issue
```

* **Rule Out Evidence Corruption:** Verify the cryptographic hash (`MD5`/`SHA-256`) of your
  target forensic image against the original acquisition log. If the hashes match, run a validation
  tool like `chkdsk` or `fsck` on a *copy* of the image to ensure the underlying file system
  structural integrity isn't causing the crash.
* **Isolate the Scope:** Test the tool against a known, clean reference image, such as standard
  NIST CFReDS test images. If the tool processes the reference image successfully, the issue is
  specific to the layout or artifacts of your current evidence.
* **Audit Environment & Dependencies:** Tool chains often rely heavily on specific versions of
  external libraries, e.g., Python runtimes, Java environments, or database engines like SQLite.
  Document any version mismatches or permission boundaries, such as restrictive EDR/anti-virus
  agents locking out the tool from parsing raw disk tracks.

### Blueprint for a Reproducible Report

A developer cannot fix an issue they cannot replicate. Because forensic evidence contains highly
sensitive PII/PHI, you must provide comprehensive technical context *without* violating chain of
custody or privacy laws.

#### Title & Executive Summary

Keep the title highly descriptive, objective and factual, referencing the specific module or
parsing engine.

* *Bad:* "Autopsy crashed during ingest."
* *Good:* `[Autopsy v4.21.0] CTPH/SSDEEP Hash Module aborted on zero-byte files inside unallocated
  space`

#### Environment Details

Forensic workstations vary wildly. Document the exact operational footprint:

* **Operating system (OS):** Windows 11 Enterprise (23H2) / Ubuntu 24.04 LTS
* **Tool Architecture:** 64-bit standalone installer, or built via source including the version,
  e.g. 1.0.1 or a git hash 6beb02a016810720486813dcb7b1c827ea833375.
* **Dependencies and their versions:** Python 3.10.12, OpenJDK 17

#### Data Format Context

Specify the exact packaging of the evidence being parsed:

* **Image Type:** E01 (Expert Witness Format), raw `dd`, VMDK, or live memory capture
* **Target Filesystem:** NTFS, APFS, Ext4, or ExFAT.

#### Step-by-Step Breakdown to Reproduce

Enumerate every click or command argument precisely.

1. Launch the application via standard command-line interface to catch early stdout errors.
2. Load an E01 image with a partition table utilizing GPT.
3. Select the "Keyword Search" ingest module.
4. Check the option for "Search Unallocated Space."
5. Click execute and watch the progress bar reach roughly 42%.

#### Expected versus Actual Mismatch

Be explicit about what the tool *should* have done versus what actually occurred.

* **Expected Result:** The ingest module completes processing, flags hits, and appends anomalies to
  the SQLite database backend.
* **Actual Result:** The software throws a `NullPointerException` in
  `KeywordSearchIngestModule.java:312` and terminates abruptly, corrupting the current case file
  database.

#### Sanitized Supporting Evidence

Never upload un-redacted active case data. Instead, provide sanitized diagnostics:

* **Stack Traces & Logs:** Extract the relevant lines from the application's `.log` folder.
* **Hexadecimal data:** If a specific corrupt file or partition table breaks the tool, use a hex
  viewer (or editor) to extract just the offending file headers/metadata, replace any actual
  content strings with dummy characters (`0x41`), and attach the file snippet.
