from collections import Counter
import json,time,pydivert

FILTER="outbound and udp and udp.DstPort == 61456"
def msg_type(payload: bytes) -> str:
	if len(payload) >= 2:
		return payload[:2].hex()
	return "short"

with pydivert.WinDivert(FILTER) as w:
	for pkt in w:
		payload=pkt.payload or b""
		if len(payload) > 700:
			continue
		w.send(pkt)