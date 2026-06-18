##info: block crash packets by ingame cheaters/modders
## can cause connection lost in session
from datetime import datetime
import pydivert,time,os,gc
gc.enable()

RELAY={"185.56.65.167","185.56.65.168","185.56.65.169","185.56.65.170","185.56.65.171","185.56.65.172"}
MY_IP="192.168.2.218"
start=time.time()

############## CONFIG ##########
SUSPECT_OUT_LEN=875
SUSPECT_IN_LEN=208
RELAY_ONLY=True

BLOCK_LOG=False
PASS_LOG=False
################################

FILTER=("udp and ("
	# Relay
	"(outbound and udp.DstPort == 61456) or "
	"(inbound and udp.SrcPort == 61456 and udp.DstPort == 6672) or "
	# Peer <-> MY_IP
	"(outbound and udp.SrcPort == 6672) or "
	"(inbound and udp.DstPort == 6672)"
	")")

os.system('cls')
print("-- GTAV Online Net-Shield v2.0 --")

def pass_log_info(p):
	if p.is_inbound:
		print(f'[INBOUND ALLOW] <{ddt}> IP_ADDR={src}:{pkt.src_port} -> {dst}:{pkt.dst_port} >>> data[len={plen}]={payload[:8].hex()}')
	if p.is_outbound:
		print(f'[OUTBOUND ALLOW] <{ddt}> IP_ADDR={src}:{pkt.src_port} -> {dst}:{pkt.dst_port} >>> data[len={plen}]={payload[:8].hex()}')

with pydivert.WinDivert(FILTER) as w:
	for pkt in w:
		payload=pkt.payload or b""
		plen=len(payload)
		src=str(pkt.src_addr)
		dst=str(pkt.dst_addr)
		ddt=datetime.now().strftime("%H:%M:%S")
		if RELAY_ONLY and pkt.is_inbound:
			if pkt.dst_port == 6672 and src not in RELAY:
				if BLOCK_LOG:
					print(f'[INBOUND BLOCK] <{ddt}> REASON=STRICT_NAT_TYPE >>> IP_ADDR={src}:{pkt.src_port} -> {dst}:{pkt.dst_port} >>> data[len={plen}]={payload[:8].hex()}')
				continue
		if pkt.is_outbound and pkt.dst_port == 61456 and plen == SUSPECT_OUT_LEN:
			if BLOCK_LOG:
				print(f'[OUTBOUND BLOCK] <{ddt}> REASON=MALICIOUS_PAYLOAD >>> IP_ADDR={src}:{pkt.src_port} -> {dst}:{pkt.dst_port} >>> data[len={plen}]={payload[:8].hex()}')
			continue
		if pkt.is_inbound and src in RELAY and pkt.src_port == 61456 and pkt.dst_port == 6672 and plen == SUSPECT_IN_LEN:
			if BLOCK_LOG:
				print(f'[INBOUND BLOCK] <{ddt}> REASON=MALICIOUS_PAYLOAD >>> IP_ADDR={src}:{pkt.src_port} -> {src}:{pkt.src_port} >>> data[len={plen}]={payload[:8].hex()}')
			continue
		if PASS_LOG:
			pass_log_info(pkt)
		w.send(pkt)
