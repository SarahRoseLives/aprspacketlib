# APRS Packet Generator and Validator

I had a need for something to help me write raw APRS packets so I wasn't manually writting them by hand.
This simple library allows you to easily import and generate various APRS packets and validates them with the parser from `aprslib`.
## Overview

The `PacketGenerator` class provides methods to create different types of APRS packets. The `validate_packet` function uses `aprslib` to parse and validate these packets.

```python
import aprslib
from aprspacketlib import PacketGenerator

def validate_packet(packet):
    try:
        parsed = aprslib.parse(packet)
        print(f"Valid packet: {parsed}")
    except Exception as e:
        print(f"Invalid packet: {e}")

# Example: Creating and validating a position report without timestamp
position_packet = PacketGenerator.position_report_without_timestamp("AD8NT-9", "4123.45N", "08123.45W", "Example Position")
print(f"Generated Packet: {position_packet}")
validate_packet(position_packet)

# Example: Validating other types of packets
status_packet = PacketGenerator.status_report("AD8NT-9", "Example Status Message")
print(f"Generated Packet: {status_packet}")
validate_packet(status_packet)

message_packet = PacketGenerator.message_packet("AD8NT-9", "AD8NT-5", "Hello from AD8NT")
print(f"Generated Packet: {message_packet}")
validate_packet(message_packet)

# Example: Validating ACK packet creation
raw_packet = "AD8NT-9>APRS::AD8NT-5 :Test message{AB"
ack_packet = PacketGenerator.generate_ack_packet(raw_packet, "AD8NT-9")
print(f"Generated ACK Packet: {ack_packet}")
validate_packet(ack_packet)
```

## Generated Output
```bash
Generated Packet: AD8NT-9>APRS,TCPIP*,qAC,THIRD:=4123.45N/08123.45W>Example Position
Valid packet: {'raw': 'AD8NT-9>APRS,TCPIP*,qAC,THIRD:=4123.45N/08123.45W>Example Position', 'from': 'AD8NT-9', 'to': 'APRS', 'path': ['TCPIP*', 'qAC', 'THIRD'], 'via': 'THIRD', 'messagecapable': True, 'format': 'uncompressed', 'posambiguity': 0, 'symbol': '>', 'symbol_table': '/', 'latitude': 41.39083333333333, 'longitude': -81.39083333333333, 'comment': 'Example Position'}
Generated Packet: AD8NT-9>APRS,TCPIP*,qAC,THIRD:>Example Status Message
Valid packet: {'raw': 'AD8NT-9>APRS,TCPIP*,qAC,THIRD:>Example Status Message', 'from': 'AD8NT-9', 'to': 'APRS', 'path': ['TCPIP*', 'qAC', 'THIRD'], 'via': 'THIRD', 'format': 'status', 'status': 'Example Status Message'}
Generated Packet: AD8NT-9>APRS,TCPIP*,qAC,THIRD::AD8NT-5  :Hello from AD8NT
Valid packet: {'raw': 'AD8NT-9>APRS,TCPIP*,qAC,THIRD::AD8NT-5  :Hello from AD8NT', 'from': 'AD8NT-9', 'to': 'APRS', 'path': ['TCPIP*', 'qAC', 'THIRD'], 'via': 'THIRD', 'addresse': 'AD8NT-5', 'format': 'message', 'message_text': 'Hello from AD8NT'}
Generated ACK Packet: AD8NT-9>APRS::AD8NT-5 ::ackAB}
Valid packet: {'raw': 'AD8NT-9>APRS::AD8NT-5 ::ackAB}', 'from': 'AD8NT-9', 'to': 'APRS', 'path': [], 'via': '', 'format': 'beacon', 'text': ':AD8NT-5 ::ackAB}'}
```