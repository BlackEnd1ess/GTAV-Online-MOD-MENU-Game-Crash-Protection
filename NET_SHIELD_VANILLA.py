##info: check custom rules or create your own
from collections import Counter
import json,time,pydivert

with pydivert.WinDivert("outbound and udp and udp.DstPort == 61456") as w:
	for pkt in w:
		payload=pkt.payload or b""
		if len(payload) > 750:##example rule
			continue
		w.send(pkt)