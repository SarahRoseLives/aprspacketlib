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

