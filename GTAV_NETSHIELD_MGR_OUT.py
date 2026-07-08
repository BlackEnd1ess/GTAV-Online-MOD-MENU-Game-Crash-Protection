#info: This script is helpful if you have only blocked inbound packets, but are still sending outgoing packets.
from datetime import datetime
import time,pydivert,os

RELAY=('185.56.65.167','185.56.65.168','185.56.65.169','185.56.65.170','185.56.65.171','185.56.65.172','185.56.65.173')

##block outbound to other player without set firewall rule
NAT_SUPERSTRICT_OUT=False

BLOCK_LOG=True
PASS_LOG=True

def show_log(p,typ):
	ddt=datetime.now().strftime("%H:%M:%S")
	payload=p.payload or b""
	log_text={0:f"[INFO] <{ddt}> BLOCK_OUTBOUND ::: IP_ADDR={p.src_addr}:{p.src_port} -> {p.dst_addr}:{p.dst_port} >> data[len={len(payload)}]={payload[:8].hex()}",
			1:f"[INFO] <{ddt}> PASS_OUTBOUND ::: IP_ADDR={p.src_addr}:{p.src_port} -> {p.dst_addr}:{p.dst_port} >> len={len(payload)}",
			2:f"[INFO] <{ddt}> BLOCK_PEER_2_PEER ::: IP_ADDR={p.src_addr}:{p.src_port} -> {p.dst_addr}:{p.dst_port} >> len={len(payload)}"}
	if typ in log_text:
		print(log_text[typ])
		return
	print(f'[INFO] <{ddt}> UNKNOWN ERROR - unrecognize packet')

os.system('cls')
print(f">>> GTAV NetShield - SUPERSTRICT_NAT v2.0 ACTIVE={bool(NAT_SUPERSTRICT_OUT)} <<<")
try:
	with pydivert.WinDivert('udp and outbound and (udp.DstPort == 61456 or udp.SrcPort == 6672)') as w:
		for pkt in w:
			payload=pkt.payload or b""
			plen=len(payload)
			last_relay_out=time.time()
			if NAT_SUPERSTRICT_OUT:
				if pkt.src_port == 6672 and not pkt.dst_addr in RELAY:
					if BLOCK_LOG:
						show_log(pkt,typ=2)
					continue
			if pkt.dst_port == 61456 and plen == 875 and pkt.dst_addr in RELAY:
				if BLOCK_LOG:
					show_log(pkt,typ=0)
				continue
			if PASS_LOG:
				show_log(pkt,typ=1)
			w.send(pkt)
except KeyboardInterrupt:
	pass

finally:
	running=False
	print("\nNetShield stopped.")