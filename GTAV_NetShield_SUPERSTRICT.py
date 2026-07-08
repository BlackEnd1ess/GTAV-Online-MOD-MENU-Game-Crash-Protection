##info: Before using the script, ensure that the firewall rules are set as described in EXTENDED_PROTECTION.txt
from colorama import init,Fore,Style
import time,pydivert,threading,os
from datetime import datetime

init()
BLOCK_LOG=True
PASS_LOG=False

WINDOW_SECONDS=60
MAX_RELAY=3

CONNECT_WARNING=2
CONNECT_CRITICAL=5

relay_hits=[]
last_relay_out=time.time()
running=True

def relay_state():
	age=time.time()-last_relay_out
	if age < CONNECT_WARNING:
		return Fore.GREEN+"● GREEN"+Style.RESET_ALL,"Relay traffic active"
	if age < CONNECT_CRITICAL:
		return Fore.YELLOW+"● YELLOW" + Style.RESET_ALL,"No relay packets for a few seconds"
	return Fore.RED+"● RED"+Style.RESET_ALL,"No relay traffic - session may become unstable"

def status_loop():
	while running:
		state,msg=relay_state()
		age=time.time()-last_relay_out
		print(f"\r[{state}] last_out={age:05.1f}s | {msg}   ",
			end="",
			flush=True)
		time.sleep(.1)

def show_log(p,typ):
	ddt=datetime.now().strftime("%H:%M:%S")
	payload=p.payload or b""
	if typ == 1:
		print(f"[INFO] <{ddt}> BLOCK_OUTBOUND ::: "
			f"IP_ADDR={p.src_addr}:{p.src_port} -> {p.dst_addr}:{p.dst_port} "
			f">>> data[len={len(payload)}]={payload[:8].hex()}")
	else:
		print(f"[INFO] <{ddt}> PASS_OUTBOUND ::: "
			f"IP_ADDR={p.src_addr}:{p.src_port} -> {p.dst_addr}:{p.dst_port} "
			f">> len={len(payload)}")

os.system('cls')
print(">>> GTAV NetShield - SUPERSTRICT_NAT (IN/OUT) <<<")
print("Relay INFO: GREEN=RUNNING | YELLOW=IDLE | RED=DISCONNECTED")

threading.Thread(target=status_loop,daemon=True).start()
try:
	with pydivert.WinDivert("outbound and udp and udp.DstPort == 61456") as w:
		for pkt in w:
			payload=pkt.payload or b""
			plen=len(payload)
			last_relay_out=time.time()
			if plen == 875:
				now=time.time()
				relay_hits=[t for t in relay_hits if now - t < WINDOW_SECONDS]
				relay_hits.append(now)
				if len(relay_hits) > MAX_RELAY:
					if BLOCK_LOG:
						show_log(pkt,typ=1)
						print(f"[RATE_LIMIT_875] {len(relay_hits)} hits in {WINDOW_SECONDS}s")
					continue
			if PASS_LOG:
				show_log(pkt,typ=0)
			w.send(pkt)

except KeyboardInterrupt:
	pass

finally:
	running=False
	print("\nNetShield stopped.")
