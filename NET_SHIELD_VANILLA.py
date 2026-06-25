##info: check custom rules or create your own
from datetime import datetime
import time,pydivert

BLOCK_LOG=False
PASS_LOG=False

def show_log(p,typ):
	ddt=datetime.now().strftime("%H:%M:%S")
	if typ == 1:
		print(f'[INFO] <{ddt}> BLOCK_OUTBOUND ::: IP_ADDR={p.src_addr}:{p.src_port} -> {p.dst_addr}:{p.dst_port} >>> data[len={len(p.payload)}]={p.payload[:8].hex()}')
		#print(f'BLOCK_DATA >> {p.payload[:8].hex()}')
		return
	print(f'[INFO] <{ddt}> PASS_OUTBOUND ::: IP_ADDR={p.src_addr}:{p.src_port} -> {p.dst_addr}:{p.dst_port} >> len={len(p.payload)} ')
	#print(f'PASS_DATA >> {p.payload[:8].hex()}')

print('GTAV NetShield Vanilla v1.1 OUTBOUND ONLY')
with pydivert.WinDivert("outbound and udp and udp.DstPort == 61456") as w:
	for pkt in w:
		payload=pkt.payload or b""
		if len(payload) == 875:
			if BLOCK_LOG:
				show_log(pkt,typ=1)
			continue
		if PASS_LOG:
			show_log(pkt,typ=0)
		w.send(pkt)
