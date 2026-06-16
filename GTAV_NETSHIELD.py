##info: block crash packets by ingame cheaters/modders
## can cause connection lost in session
from datetime import datetime
import pydivert,time,os,gc
gc.enable()

RELAY={"185.56.65.167","185.56.65.168","185.56.65.169","185.56.65.170","185.56.65.171","185.56.65.172"}

start=time.time()

SUSPECT_OUT_LEN=875
SUSPECT_IN_LEN=208
OUTPUT_LOG=True

FILTER=("udp and ("
	"(outbound and udp.DstPort == 61456) or "
	"(inbound and udp.SrcPort == 61456 and udp.DstPort == 6672)"
	")")

os.system('cls')
print("-- GTAV Online Net-Shield v1.1 --")
with pydivert.WinDivert(FILTER) as w:
	for pkt in w:
		payload=pkt.payload or b""
		plen=len(payload)
		src=str(pkt.src_addr)
		dst=str(pkt.dst_addr)
		ddt=datetime.now().strftime("%H:%M:%S")
		if pkt.is_outbound and pkt.dst_port == 61456 and plen == SUSPECT_OUT_LEN:
			if OUTPUT_LOG:
				print(f'[INFO] <{ddt}> blocked OUTBOUND crash-packet ::: paket_details: IP_ADDR {src}:{pkt.src_port} -> {dst}:{pkt.dst_port} ::: data={payload[:8].hex()}')
			continue
		if (pkt.is_inbound and src in RELAY and pkt.src_port == 61456 and pkt.dst_port == 6672 and plen == SUSPECT_IN_LEN):
			if OUTPUT_LOG:
				print(f'[INFO] <{ddt}> blocked INBOUND crash-packet ::: paket_details: IP_ADDR {src}:{pkt.src_port} -> {dst}:{pkt.dst_port} ::: data={payload[:8].hex()}')
			continue
		w.send(pkt)
