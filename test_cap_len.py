from collections import Counter
import json,time,pydivert

DRY_RUN = True
DROP_MODE = True

PORT_MIN = 61450
PORT_MAX = 61460

LOG_FILE = "relay_61450_61460.jsonl"

FILTER = ("outbound and udp and "
	"udp.DstPort == 61456")

type_counter = Counter()
len_counter = Counter()
dst_counter = Counter()

def msg_type(payload: bytes) -> str:
	if len(payload) >= 2:
		return payload[:2].hex()
	return "short"

with pydivert.WinDivert(FILTER) as w:
	print(f"LOG outbound UDP dst {PORT_MIN}-{PORT_MAX}")
	for pkt in w:
		payload = pkt.payload or b""
		now = time.time()
		rec = {"t": now,
			"src": str(pkt.src_addr),
			"sport": pkt.src_port,
			"dst": str(pkt.dst_addr),
			"dport": pkt.dst_port,
			"raw_len": len(pkt.raw),
			"payload_len": len(payload),
			"type": msg_type(payload),
			"head64": payload[:64].hex()}
		type_counter[rec["type"]] += 1
		len_counter[rec["payload_len"]] += 1
		dst_counter[(rec["dst"], rec["dport"])] += 1
		#with open(LOG_FILE, "a", encoding="utf-8") as f:
		#	f.write(json.dumps(rec)+"\n")
		#print(f"{now:.3f} "
		#	f"{rec['src']}:{rec['sport']} -> {rec['dst']}:{rec['dport']} "
		#	f"raw={rec['raw_len']} payload={rec['payload_len']} "
		#	f"type={rec['type']} "
		#	f"hex={rec['head64']}")
		if DROP_MODE:
			if len(payload) > 600:
				#print('drop-> ',payload[:4])
				continue
		w.send(pkt)