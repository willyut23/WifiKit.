# WifiKit.
<div align="center">

```
 █     █░ ██▓  █████▒██▓   ▄▄▄█████▓ ▒█████   ▒█████   ██▓     ██ ▄█▀ ██▓▄▄▄█████▓
 ▓█░ █ ░█░▓██▒▓██   ▒▓██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒     ██▄█▒ ▓██▒▓  ██▒ ▓▒
 ▒█░ █ ░█ ▒██▒▒████ ░▒██▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ▓███▄░ ▒██▒▒ ▓██░ ▒░
 ░█░ █ ░█ ░██░░▓█▒  ░░██░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    ▓██ █▄ ░██░░ ▓██▓ ░ 
 ░░██▒██▓ ░██░░▒█░   ░██░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██▒ █▄░██░  ▒██▒ ░ 
 ░ ▓░▒ ▒  ░▓   ▒ ░   ░▓       ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▒ ▓▒░▓    ▒ ░░  
   ▒ ░ ░   ▒ ░ ░      ▒ ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒ ▒░ ▒ ░    ░   
   ░   ░   ▒ ░ ░ ░    ▒ ░     ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░ ░░ ░  ▒ ░  ░     
     ░     ░          ░                  ░ ░      ░ ░      ░  ░░  ░    ░             
```

**Router fix and network diagnostics toolkit**

![Python](https://img.shields.io/badge/python-3.6%2B-blue?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

</div>

---

## Overview

WifiKit is a command-line toolkit for diagnosing and fixing common network issues. It covers DNS management, IP renewal, TCP/IP resets, Wi-Fi tools, and more — all from a single clean menu.

---

## Requirements

- Python 3.6+
- Administrator / sudo privileges for most features
- No third-party packages needed

---

## Usage

**Windows** — run as Administrator:
```bash
python wifitoolkit.py
```

**Linux / macOS:**
```bash
sudo python3 wifitoolkit.py
```

---

## Features

### 🔄 Network Reset
| # | Tool | Description |
|---|------|-------------|
| 01 | Flush DNS Cache | Clears stored DNS entries that may cause connection issues |
| 02 | Release & Renew IP | Gets a fresh IP address from your router |
| 03 | Reset TCP/IP Stack | Resets core network protocols to defaults |
| 04 | Reset Winsock | Repairs corrupted socket settings (Windows) |
| 05 | Restart Network Adapter | Cycles your network adapter off and on |

### 🔍 Diagnostics
| # | Tool | Description |
|---|------|-------------|
| 06 | Ping Gateway | Tests connection to your router |
| 07 | Ping Google DNS | Tests whether you have internet access |
| 08 | Show IP Configuration | Displays full network adapter info |
| 09 | Trace Route | Shows the path packets take to reach Google |
| 10 | Check Internet Connectivity | Checks multiple servers for connectivity |

### 🌐 DNS Tools
| # | Tool | Description |
|---|------|-------------|
| 11 | Set DNS to Google | Uses `8.8.8.8` / `8.8.4.4` |
| 12 | Set DNS to Cloudflare | Uses `1.1.1.1` / `1.0.0.1` — recommended for low latency |
| 13 | Restore Automatic DNS | Reverts DNS back to your ISP's default |
| 14 | Show Current DNS | Displays your active DNS servers |

### 📶 Wi-Fi Management
| # | Tool | Description |
|---|------|-------------|
| 15 | Show Available Networks | Scans and lists nearby Wi-Fi networks |
| 16 | Show Wi-Fi Password | Reveals the password for saved networks |
| 17 | Disconnect & Reconnect | Cycles your Wi-Fi connection |
| 18 | Signal Strength | Shows your current Wi-Fi signal info |

### ⚙️ Advanced
| # | Tool | Description |
|---|------|-------------|
| 19 | Full Auto-Fix | Runs all resets in sequence — best starting point |
| 20 | Open Router Admin | Opens your router's admin page in the browser |
| 21 | Show ARP Table | Lists devices mapped on your local network |
| 22 | Show Active Connections | Displays open ports and active connections |

---

## Quick Fix for High Ping

Run these in order:

```
12 → Switch to Cloudflare DNS
 1 → Flush DNS Cache
 3 → Reset TCP/IP Stack
 2 → Release & Renew IP
```

Then restart your PC. Or just run **`19` (Full Auto-Fix)** to do it all at once.

---

## Notes

- Actions that modify network settings require admin/sudo — the script will warn you if privileges are missing
- A system restart is recommended after running TCP/IP or Winsock resets on Windows
- Cloudflare DNS (`1.1.1.1`) generally offers lower latency than Google DNS for most regions

---

## License

MIT
