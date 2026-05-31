#!/usr/bin/env python3
"""
WIFITOOLKIT - Router Fix & Diagnostics Toolkit
Works on Windows, macOS, and Linux
"""

import os
import sys
import time
import subprocess
import platform
import socket

# ─── Color codes ────────────────────────────────────────────────────────────
class C:
    RED     = '\033[91m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    CYAN    = '\033[96m'
    WHITE   = '\033[97m'
    DIM     = '\033[2m'
    BOLD    = '\033[1m'
    RESET   = '\033[0m'

OS = platform.system()  # 'Windows', 'Linux', 'Darwin'

def run(cmd, shell=True, capture=True):
    """Run a shell command and return output."""
    try:
        result = subprocess.run(
            cmd, shell=shell, capture_output=capture,
            text=True, timeout=30
        )
        return result.stdout.strip(), result.returncode
    except subprocess.TimeoutExpired:
        return "Command timed out.", 1
    except Exception as e:
        return str(e), 1

def clear():
    os.system('cls' if OS == 'Windows' else 'clear')

def pause():
    input(f"\n{C.DIM}  Press ENTER to return to menu...{C.RESET}")

def banner():
    print(f"{C.CYAN}{C.BOLD}")
    print(r" █     █░ ██▓  █████▒██▓   ▄▄▄█████▓ ▒█████   ▒█████   ██▓     ██ ▄█▀ ██▓▄▄▄█████▓")
    print(r" ▓█░ █ ░█░▓██▒▓██   ▒▓██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒     ██▄█▒ ▓██▒▓  ██▒ ▓▒")
    print(r" ▒█░ █ ░█ ▒██▒▒████ ░▒██▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ▓███▄░ ▒██▒▒ ▓██░ ▒░")
    print(r" ░█░ █ ░█ ░██░░▓█▒  ░░██░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    ▓██ █▄ ░██░░ ▓██▓ ░ ")
    print(r" ░░██▒██▓ ░██░░▒█░   ░██░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██▒ █▄░██░  ▒██▒ ░ ")
    print(r" ░ ▓░▒ ▒  ░▓   ▒ ░   ░▓       ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▒ ▓▒░▓    ▒ ░░  ")
    print(r"   ▒ ░ ░   ▒ ░ ░      ▒ ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒ ▒░ ▒ ░    ░   ")
    print(r"   ░   ░   ▒ ░ ░ ░    ▒ ░     ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░ ░░ ░  ▒ ░  ░     ")
    print(r"     ░     ░          ░                  ░ ░      ░ ░      ░  ░░  ░    ░             ")
    print(f"{C.RESET}")
    print(f"{C.DIM}  {'─'*85}{C.RESET}")
    print(f"  {C.YELLOW}Router Fix & Diagnostics Toolkit{C.RESET}  {C.DIM}│  OS: {OS}  │  Python {sys.version.split()[0]}{C.RESET}")
    print(f"{C.DIM}  {'─'*85}{C.RESET}\n")

def menu():
    clear()
    banner()
    cats = [
        ("NETWORK RESET",    "91"),
        ("DIAGNOSTICS",      "93"),
        ("DNS TOOLS",        "92"),
        ("WIFI MANAGEMENT",  "96"),
        ("ADVANCED",         "95"),
    ]
    options = [
        # (display_num, category_idx, label)
        ( 1, 0, "Flush DNS Cache"),
        ( 2, 0, "Release & Renew IP Address"),
        ( 3, 0, "Reset TCP/IP Stack"),
        ( 4, 0, "Reset Winsock / Network Socket"),
        ( 5, 0, "Restart Network Adapter"),
        ( 6, 1, "Ping Gateway (Router)"),
        ( 7, 1, "Ping Google DNS (8.8.8.8)"),
        ( 8, 1, "Show IP Configuration"),
        ( 9, 1, "Trace Route to Google"),
        (10, 1, "Check Internet Connectivity"),
        (11, 2, "Change DNS to Google (8.8.8.8)"),
        (12, 2, "Change DNS to Cloudflare (1.1.1.1)"),
        (13, 2, "Restore Automatic DNS"),
        (14, 2, "Show Current DNS Servers"),
        (15, 3, "Show Available Wi-Fi Networks"),
        (16, 3, "Show Wi-Fi Password (current network)"),
        (17, 3, "Disconnect & Reconnect Wi-Fi"),
        (18, 3, "Show Wi-Fi Signal Strength"),
        (19, 4, "Run Full Auto-Fix (All Resets)"),
        (20, 4, "Open Router Admin Page"),
        (21, 4, "Show ARP Table"),
        (22, 4, "Show Active Connections / Ports"),
    ]

    last_cat = -1
    for num, cat_idx, label in options:
        if cat_idx != last_cat:
            cat_name, cat_color = cats[cat_idx]
            print(f"  \033[{cat_color}m{'─── ' + cat_name + ' '+'─'*(30-len(cat_name))}{C.RESET}")
            last_cat = cat_idx
        print(f"    {C.WHITE}[{num:02d}]{C.RESET}  {label}")

    print(f"\n  {C.DIM}{'─'*45}{C.RESET}")
    print(f"    {C.WHITE}[ 0]{C.RESET}  {C.RED}Exit{C.RESET}\n")
    return input(f"  {C.CYAN}Select an option: {C.RESET}").strip()

# ─── Helper: require admin / root ───────────────────────────────────────────
def need_admin():
    if OS == 'Windows':
        import ctypes
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print(f"\n  {C.RED}[!] This action requires Administrator privileges.{C.RESET}")
            print(f"  {C.YELLOW}    Right-click the script and choose 'Run as Administrator'.{C.RESET}")
            return False
    else:
        if os.geteuid() != 0:
            print(f"\n  {C.RED}[!] This action requires root/sudo.{C.RESET}")
            print(f"  {C.YELLOW}    Run: sudo python3 wifitoolkit.py{C.RESET}")
            return False
    return True

def section(title):
    print(f"\n  {C.CYAN}{C.BOLD}{'─── ' + title + ' ─'*max(1,(40-len(title))//2)}{C.RESET}\n")

def ok(msg):  print(f"  {C.GREEN}[✓]{C.RESET} {msg}")
def info(msg):print(f"  {C.YELLOW}[i]{C.RESET} {msg}")
def err(msg): print(f"  {C.RED}[✗]{C.RESET} {msg}")
def out(text):
    for line in text.splitlines():
        print(f"      {C.DIM}{line}{C.RESET}")

# ─── Get default gateway ─────────────────────────────────────────────────────
def get_gateway():
    if OS == 'Windows':
        o, _ = run("ipconfig")
        for line in o.splitlines():
            if "Default Gateway" in line:
                parts = line.split(":")
                if len(parts) > 1:
                    gw = parts[-1].strip()
                    if gw: return gw
    else:
        o, _ = run("ip route | grep default")
        parts = o.split()
        if len(parts) > 2: return parts[2]
    return "192.168.1.1"

def get_wifi_interface():
    if OS == 'Windows':
        return None  # not needed for netsh commands
    elif OS == 'Linux':
        o, _ = run("iw dev | awk '/Interface/{print $2}'")
        return o.strip() or "wlan0"
    else:  # macOS
        return "en0"

# ════════════════════════════════════════════════════════════════════════════
#  ACTIONS
# ════════════════════════════════════════════════════════════════════════════

def flush_dns():
    section("Flush DNS Cache")
    if OS == 'Windows':
        o, c = run("ipconfig /flushdns")
        (ok if c == 0 else err)(o)
    elif OS == 'Darwin':
        o, c = run("sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder")
        ok("DNS cache flushed (macOS)") if c == 0 else err(o)
    else:
        o, c = run("sudo systemd-resolve --flush-caches 2>/dev/null || sudo resolvectl flush-caches 2>/dev/null || sudo /etc/init.d/nscd restart 2>/dev/null")
        ok("DNS cache flushed") if c == 0 else info("Tried multiple methods — check output above")
    pause()

def release_renew():
    section("Release & Renew IP Address")
    if not need_admin(): return pause()
    if OS == 'Windows':
        info("Releasing IP...")
        o, _ = run("ipconfig /release"); out(o)
        time.sleep(1)
        info("Renewing IP...")
        o, _ = run("ipconfig /renew"); out(o)
        ok("IP renewed.")
    elif OS == 'Linux':
        iface = get_wifi_interface()
        run(f"sudo dhclient -r {iface}")
        time.sleep(1)
        o, c = run(f"sudo dhclient {iface}")
        ok(f"DHCP renewed on {iface}") if c == 0 else err(o)
    else:
        iface = get_wifi_interface()
        run(f"sudo ipconfig set {iface} DHCP")
        ok("DHCP renewed (macOS)")
    pause()

def reset_tcpip():
    section("Reset TCP/IP Stack")
    if not need_admin(): return pause()
    if OS == 'Windows':
        cmds = [
            ("netsh int ip reset", "TCP/IP stack reset"),
            ("netsh int ipv6 reset", "IPv6 stack reset"),
        ]
        for cmd, label in cmds:
            o, c = run(cmd)
            ok(label) if c == 0 else err(f"{label} — {o}")
        info("A restart is recommended to complete the reset.")
    else:
        info("TCP/IP stack reset is managed by the OS on Linux/macOS.")
        info("Restarting NetworkManager instead...")
        o, c = run("sudo systemctl restart NetworkManager 2>/dev/null || sudo service networking restart 2>/dev/null")
        ok("Network service restarted") if c == 0 else err(o)
    pause()

def reset_winsock():
    section("Reset Winsock / Network Socket")
    if not need_admin(): return pause()
    if OS == 'Windows':
        o, c = run("netsh winsock reset")
        ok("Winsock reset. Restart required.") if c == 0 else err(o)
        out(o)
    else:
        info("Winsock is Windows-only.")
        info("Resetting socket buffers via sysctl...")
        run("sudo sysctl -w net.core.rmem_default=212992")
        run("sudo sysctl -w net.core.wmem_default=212992")
        ok("Socket buffers reset.")
    pause()

def restart_adapter():
    section("Restart Network Adapter")
    if not need_admin(): return pause()
    if OS == 'Windows':
        o, _ = run("netsh interface show interface")
        info("Detected interfaces:"); out(o)
        name = input(f"\n  {C.CYAN}Enter adapter name (e.g. Wi-Fi): {C.RESET}").strip()
        if not name: name = "Wi-Fi"
        run(f'netsh interface set interface "{name}" disable')
        time.sleep(2)
        o, c = run(f'netsh interface set interface "{name}" enable')
        ok(f"Adapter '{name}' restarted.") if c == 0 else err(o)
    elif OS == 'Linux':
        iface = get_wifi_interface()
        run(f"sudo ip link set {iface} down")
        time.sleep(2)
        run(f"sudo ip link set {iface} up")
        ok(f"Interface {iface} restarted.")
    else:
        iface = get_wifi_interface()
        run(f"sudo ifconfig {iface} down")
        time.sleep(2)
        run(f"sudo ifconfig {iface} up")
        ok(f"Interface {iface} restarted.")
    pause()

def ping_gateway():
    section("Ping Gateway (Router)")
    gw = get_gateway()
    info(f"Gateway detected: {gw}")
    count_flag = "-n 4" if OS == 'Windows' else "-c 4"
    o, c = run(f"ping {count_flag} {gw}")
    out(o)
    ok("Gateway is reachable!") if c == 0 else err("Gateway did NOT respond. Check router power/connection.")
    pause()

def ping_google():
    section("Ping Google DNS (8.8.8.8)")
    count_flag = "-n 4" if OS == 'Windows' else "-c 4"
    o, c = run(f"ping {count_flag} 8.8.8.8")
    out(o)
    ok("Internet is reachable!") if c == 0 else err("8.8.8.8 did NOT respond. No internet connection.")
    pause()

def show_ipconfig():
    section("IP Configuration")
    cmd = "ipconfig /all" if OS == 'Windows' else "ip addr show" if OS == 'Linux' else "ifconfig"
    o, _ = run(cmd)
    out(o)
    pause()

def traceroute():
    section("Trace Route to Google (8.8.8.8)")
    cmd = "tracert 8.8.8.8" if OS == 'Windows' else "traceroute 8.8.8.8"
    info("Running traceroute — this may take a moment...")
    o, c = run(cmd)
    out(o)
    pause()

def check_internet():
    section("Internet Connectivity Check")
    hosts = [("8.8.8.8", "Google DNS"), ("1.1.1.1", "Cloudflare DNS"), ("google.com", "Google (hostname)")]
    for host, label in hosts:
        try:
            socket.setdefaulttimeout(3)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, 53))
            ok(f"{label} ({host})  — REACHABLE")
        except:
            err(f"{label} ({host})  — UNREACHABLE")
    pause()

def set_dns(primary, secondary, label):
    section(f"Set DNS to {label}")
    if not need_admin(): return pause()
    if OS == 'Windows':
        o, _ = run('netsh interface show interface')
        info("Detected interfaces:"); out(o)
        name = input(f"\n  {C.CYAN}Enter adapter name (e.g. Wi-Fi): {C.RESET}").strip() or "Wi-Fi"
        run(f'netsh interface ip set dns "{name}" static {primary}')
        run(f'netsh interface ip add dns "{name}" {secondary} index=2')
        ok(f"DNS set to {label} on '{name}'.")
    elif OS == 'Linux':
        with open("/etc/resolv.conf", "w") as f:
            f.write(f"nameserver {primary}\nnameserver {secondary}\n")
        ok(f"DNS set to {label} in /etc/resolv.conf")
    else:
        iface = get_wifi_interface()
        run(f"sudo networksetup -setdnsservers '{iface}' {primary} {secondary}")
        ok(f"DNS set to {label} on {iface}")
    pause()

def restore_auto_dns():
    section("Restore Automatic DNS")
    if not need_admin(): return pause()
    if OS == 'Windows':
        name = input(f"  {C.CYAN}Adapter name (e.g. Wi-Fi): {C.RESET}").strip() or "Wi-Fi"
        run(f'netsh interface ip set dns "{name}" dhcp')
        ok(f"DNS set back to DHCP on '{name}'.")
    elif OS == 'Linux':
        run("sudo systemctl restart systemd-resolved 2>/dev/null || sudo dhclient 2>/dev/null")
        ok("DNS restored (restarted resolver).")
    else:
        iface = get_wifi_interface()
        run(f"sudo networksetup -setdnsservers '{iface}' 'Empty'")
        ok(f"DNS reset to automatic on {iface}.")
    pause()

def show_dns():
    section("Current DNS Servers")
    if OS == 'Windows':
        o, _ = run("ipconfig /all")
        for line in o.splitlines():
            if "DNS" in line: print(f"      {C.DIM}{line}{C.RESET}")
    elif OS == 'Linux':
        o, _ = run("cat /etc/resolv.conf")
        out(o)
    else:
        iface = get_wifi_interface()
        o, _ = run(f"networksetup -getdnsservers {iface}")
        out(o)
    pause()

def show_wifi_networks():
    section("Available Wi-Fi Networks")
    if OS == 'Windows':
        o, _ = run("netsh wlan show networks mode=bssid")
    elif OS == 'Linux':
        o, _ = run("nmcli dev wifi list 2>/dev/null || iwlist scan 2>/dev/null | grep ESSID")
    else:
        o, _ = run("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s")
    out(o)
    pause()

def show_wifi_password():
    section("Wi-Fi Password (Current Network)")
    if OS == 'Windows':
        o, _ = run("netsh wlan show profiles")
        info("Saved profiles:"); out(o)
        name = input(f"\n  {C.CYAN}Enter network name: {C.RESET}").strip()
        o, _ = run(f'netsh wlan show profile name="{name}" key=clear')
        for line in o.splitlines():
            if "Key Content" in line:
                ok(line.strip())
                break
        else:
            info("No password found or not saved.")
    elif OS == 'Darwin':
        ssid = input(f"  {C.CYAN}Enter SSID: {C.RESET}").strip()
        o, _ = run(f'security find-generic-password -wa "{ssid}"')
        ok(f"Password: {o}") if o else err("Password not found in keychain.")
    else:
        o, _ = run("nmcli -s -g 802-11-wireless.ssid,802-11-wireless-security.psk connection show --active 2>/dev/null")
        out(o) if o else info("Use: sudo cat /etc/NetworkManager/system-connections/<name>.nmconnection")
    pause()

def reconnect_wifi():
    section("Disconnect & Reconnect Wi-Fi")
    if not need_admin(): return pause()
    iface = get_wifi_interface()
    if OS == 'Windows':
        run('netsh wlan disconnect')
        time.sleep(2)
        run('netsh wlan connect name=""')  # reconnect last
        ok("Wi-Fi reconnected.")
    elif OS == 'Linux':
        run(f"sudo ip link set {iface} down"); time.sleep(2)
        run(f"sudo ip link set {iface} up")
        run(f"sudo dhclient {iface}")
        ok(f"Reconnected {iface}.")
    else:
        run(f"networksetup -setairportpower {iface} off"); time.sleep(2)
        run(f"networksetup -setairportpower {iface} on")
        ok("Wi-Fi reconnected.")
    pause()

def wifi_signal():
    section("Wi-Fi Signal Strength")
    if OS == 'Windows':
        o, _ = run("netsh wlan show interfaces")
        for line in o.splitlines():
            if any(k in line for k in ["Signal", "SSID", "BSSID", "Radio", "Channel"]):
                print(f"      {C.DIM}{line.strip()}{C.RESET}")
    elif OS == 'Linux':
        iface = get_wifi_interface()
        o, _ = run(f"iwconfig {iface} 2>/dev/null || iw dev {iface} link")
        out(o)
    else:
        o, _ = run("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I")
        out(o)
    pause()

def full_auto_fix():
    section("Full Auto-Fix — Running All Resets")
    if not need_admin(): return pause()
    steps = []
    if OS == 'Windows':
        steps = [
            ("ipconfig /flushdns",        "Flush DNS"),
            ("ipconfig /release",         "Release IP"),
            ("ipconfig /renew",           "Renew IP"),
            ("netsh int ip reset",        "Reset TCP/IP"),
            ("netsh int ipv6 reset",      "Reset IPv6"),
            ("netsh winsock reset",       "Reset Winsock"),
        ]
    elif OS == 'Linux':
        steps = [
            ("sudo systemd-resolve --flush-caches 2>/dev/null || true", "Flush DNS"),
            ("sudo dhclient -r 2>/dev/null; sudo dhclient 2>/dev/null", "Renew DHCP"),
            ("sudo systemctl restart NetworkManager 2>/dev/null || true", "Restart NetworkManager"),
        ]
    else:
        steps = [
            ("sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder", "Flush DNS"),
            ("sudo ifconfig en0 down; sleep 2; sudo ifconfig en0 up", "Restart Interface"),
        ]

    for cmd, label in steps:
        info(f"Running: {label}...")
        o, c = run(cmd)
        ok(label) if c == 0 else err(f"{label} returned code {c}")
        time.sleep(0.5)

    print()
    ok("All fixes applied!")
    if OS == 'Windows':
        info("A system restart is recommended for full effect.")
    pause()

def open_router_admin():
    section("Open Router Admin Page")
    gw = get_gateway()
    url = f"http://{gw}"
    info(f"Router admin URL: {C.CYAN}{url}{C.RESET}")
    if OS == 'Windows':
        os.startfile(url)
    elif OS == 'Darwin':
        run(f"open {url}")
    else:
        run(f"xdg-open {url} 2>/dev/null || sensible-browser {url} 2>/dev/null || echo 'Open manually: {url}'")
    ok("Opened in default browser (if supported).")
    pause()

def show_arp():
    section("ARP Table")
    o, _ = run("arp -a")
    out(o)
    pause()

def show_connections():
    section("Active Connections & Listening Ports")
    cmd = "netstat -ano" if OS == 'Windows' else "ss -tulnp 2>/dev/null || netstat -tulnp"
    o, _ = run(cmd)
    out(o)
    pause()

# ─── Dispatch ────────────────────────────────────────────────────────────────
def dispatch(choice):
    actions = {
        '1':  flush_dns,
        '2':  release_renew,
        '3':  reset_tcpip,
        '4':  reset_winsock,
        '5':  restart_adapter,
        '6':  ping_gateway,
        '7':  ping_google,
        '8':  show_ipconfig,
        '9':  traceroute,
        '10': check_internet,
        '11': lambda: set_dns("8.8.8.8", "8.8.4.4", "Google DNS"),
        '12': lambda: set_dns("1.1.1.1", "1.0.0.1", "Cloudflare DNS"),
        '13': restore_auto_dns,
        '14': show_dns,
        '15': show_wifi_networks,
        '16': show_wifi_password,
        '17': reconnect_wifi,
        '18': wifi_signal,
        '19': full_auto_fix,
        '20': open_router_admin,
        '21': show_arp,
        '22': show_connections,
    }
    fn = actions.get(choice)
    if fn:
        clear()
        banner()
        fn()
    elif choice == '0':
        clear()
        print(f"\n  {C.CYAN}Goodbye.{C.RESET}\n")
        sys.exit(0)
    else:
        err("Invalid option.")
        time.sleep(1)

# ─── Enable ANSI on Windows ──────────────────────────────────────────────────
if OS == 'Windows':
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except:
        pass

# ─── Main loop ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    while True:
        try:
            choice = menu()
            dispatch(choice)
        except KeyboardInterrupt:
            clear()
            print(f"\n  {C.CYAN}Goodbye.{C.RESET}\n")
            sys.exit(0)
