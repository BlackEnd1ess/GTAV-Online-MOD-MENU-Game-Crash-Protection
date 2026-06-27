# GTAV Online NetShield – Experimental Network Protection

## Overview

GTAV Online NetShield is an experimental network filtering project designed to reduce the impact of certain network-based attacks that have been observed in GTA Online public sessions.

The project combines Windows Firewall rules with WinDivert packet filtering to limit direct peer-to-peer communication while allowing Rockstar relay traffic to continue whenever possible.

**This project does not modify GTA V files, memory, or executable code.** It only filters selected network packets locally on the user's computer.

---

# Latest Updates

## GTAV NetShield SUPERSTRICT (27.06.2026)

The **SUPERSTRICT** profile is intended as an emergency protection mode.

When combined with the recommended Windows Firewall rules, direct player-to-player communication is heavily restricted and network traffic is routed primarily through Rockstar's relay servers.

The included relay monitor displays the current relay status:

* 🟢 Green – Relay traffic is active.
* 🟡 Yellow – No relay traffic has been detected for several seconds.
* 🔴 Red – Relay communication appears to have stopped and a disconnect may be imminent.

This mode is intentionally restrictive and should only be used temporarily if you are repeatedly targeted by disruptive players.

Known limitations:

* Increased latency may occur.
* Long loading times are possible.
* Travelling very far away from other players may eventually result in a disconnect.
* Synchronization quality may be reduced in some situations.

---

## Version 2.0 (18.06.2026)

The RELAY_ONLY mode attempts to allow communication only with Rockstar relay servers while preventing direct peer communication wherever possible.

During testing this resulted in:

* Reduced direct peer connectivity.
* Relay traffic remaining active.
* Public sessions remaining playable.
* Increased difficulty for repeated spoofed packet attempts to reach the client.

This behaviour is experimental and may vary depending on session conditions.

---

# Why this project exists

Over the past months many GTA Online players have reported an increase in:

* Unexpected game crashes
* Session kicks
* Forced disconnects
* Unwanted teleports
* Persistent harassment by players using third-party modifications

This project originated from several weeks of analysing GTA Online network traffic in an attempt to better understand these behaviours and investigate possible mitigation techniques.

Some network patterns repeatedly appeared during testing before or during disruptive events. NetShield was created to experimentally filter selected traffic while preserving normal gameplay as much as possible.

Because GTA Online networking is largely controlled by the game itself, complete protection cannot be guaranteed.

---

# Features

* WinDivert-based outbound packet filtering
* Optional RELAY_ONLY firewall configuration
* Experimental SUPERSTRICT protection mode
* Relay activity monitor
* Configurable packet filtering rules
* No modification of GTA V files

---

# Requirements

* Python 3
* WinDivert
* pydivert
* Npcap (recommended)

Installation:

1. Install the latest WinDivert release.
2. Copy the required WinDivert DLL and SYS files into the Python directory or the script directory.
3. Install pydivert:

```bash
pip install pydivert
```

Administrator privileges are required because WinDivert must access the network stack.

---

# Firewall Configuration

The repository also contains optional Windows Firewall configurations.

Depending on the selected profile these rules can:

* Block inbound GTA Online peer traffic.
* Restrict outbound communication to Rockstar relay servers.
* Reduce direct exposure to peer-to-peer connections.

These configurations are optional and should be tested carefully before regular gameplay.

---

# Known Limitations

This project is experimental.

Possible side effects include:

* Higher latency
* Temporary desynchronization
* Empty or sparsely populated sessions
* Host migration issues
* Disconnects after long periods without relay traffic
* Reduced Social Club visibility depending on firewall configuration

Behaviour may vary depending on Rockstar server infrastructure and future game updates.

---

# Disclaimer

This software is provided for educational and research purposes.

It does not bypass, modify or interfere with BattlEye or GTA V game files.

Incorrect firewall or filtering rules may negatively affect network connectivity.

No guarantee is made that the project prevents every network-based attack or disruptive behaviour.

---

# Acknowledgements

Parts of this project were developed with assistance from ChatGPT, which significantly accelerated research, testing and documentation.

---

Best regards,

**BlackEndless**
