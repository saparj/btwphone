![License](https://img.shields.io/badge/license-GPLv2-blue)
![Platform](https://img.shields.io/badge/platform-Raspberry%20Pi-c51a4a)
![OS](https://img.shields.io/badge/OS-Arch%20Linux%20ARM-1793d1)
![Status](https://img.shields.io/badge/status-v1--in--progress-orange)
![SIP](https://img.shields.io/badge/SIP-pjsip%20%2F%20PJSUA2-blue)
![Python](https://img.shields.io/badge/python-3.x-blue)

# BTW Phone

**Bare-metal Telephony Workbench**

An open-source SIP VoIP desk phone built on Arch Linux ARM and Raspberry Pi hardware.

---

## What is this?

BTW Phone is a project to build a fully functional SIP desk phone from the ground up - running the Linux kernel on commodity hardware, with every layer of the stack open and documented.

Commercial VoIP phones run proprietary firmware. Hobbyist SIP projects are usually software-only or microcontroller-based. BTW Phone aims to be a real desk phone, running a real Linux distribution, with real SIP interoperability.

The name "BTW" stands for **Bare-metal Telephony Workbench**. If it also reminds you of something else, it does run Arch by the way.

## Current Status

**v1 - Proof of Concept - In Progress**

Building on a Raspberry Pi 3 Model B+ with Arch Linux ARM, pjsip (PJSUA2 Python bindings), a USB audio dongle, and a Waveshare 4.3" HDMI touchscreen. The goal: a working SIP phone call over Ethernet with a basic touch UI.

V2 targets a Raspberry Pi 4 with an I2S audio codec, 3D-printed enclosure, and TLS/SRTP encryption.

## License

[GPLv2](LICENSE)
