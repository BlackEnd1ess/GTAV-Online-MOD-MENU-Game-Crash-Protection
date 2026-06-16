##info: block crash packets by ingame cheaters/modders
## can cause connection lost in 
import pydivert

RELAY={"185.56.65.167","185.56.65.168","185.56.65.169","185.56.65.170","185.56.65.171","185.56.65.172"}
FILTER=("udp and ("
	"(outbound and udp.DstPort == 61456) or "
	"(inbound and udp.SrcPort == 61456 and udp.DstPort == 6672)"
	")")

print('GTAV Online Net-Shield')
with pydivert.WinDivert(FILTER) as w:
	for pkt in w:
		payload = pkt.payload or b""
		plen = len(payload)
		src = str(pkt.src_addr)
		dst = str(pkt.dst_addr)
		if pkt.is_outbound and pkt.dst_port == 61456:
			if plen == 875:
				continue
		if (pkt.is_inbound and src in RELAY and pkt.src_port == 61456 and pkt.dst_port == 6672 and plen == 208):
			continue
		w.send(pkt)
