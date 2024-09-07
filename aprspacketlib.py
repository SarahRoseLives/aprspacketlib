import random


class PacketGenerator:
    @staticmethod
    def position_report_without_timestamp(callsign, lat, lon, comment):
        return f"{callsign}>APRS,TCPIP*,qAC,THIRD:={lat}/{lon}>{comment}"

    @staticmethod
    def position_report_with_timestamp(callsign, timestamp, lat, lon, comment):
        return f"{callsign}>APRS,TCPIP*,qAC,THIRD:@{timestamp}z{lat}/{lon}>{comment}"


    @staticmethod
    def weather_report(callsign, timestamp, lat, lon, wind_dir, wind_speed, gust, temp, humidity, pressure):
        return (f"{callsign}>APRS,TCPIP*,qAC,THIRD:_{timestamp}z{lat}/{lon}_"
                f"{wind_dir}/{wind_speed}g{gust}t{temp}h{humidity}b{pressure}")

    @staticmethod
    def status_report(callsign, status_msg):
        return f"{callsign}>APRS,TCPIP*,qAC,THIRD:>{status_msg}"

    @staticmethod
    def message_packet(sender, recipient, message, use_msg_no=False):
        if use_msg_no:
            msg_no = random.randint(0, 999)
            message += f"{{{msg_no}"

        return f"{sender}>APRS,TCPIP*,qAC,THIRD::{recipient:<9}:{message}"

    @staticmethod
    def bulletin_report(callsign, bulletin_id, message):
        return f"{callsign}>APRS,TCPIP*,qAC,THIRD::BLN{bulletin_id:<7}:{message}"

    @staticmethod
    def telemetry_packet(callsign, seq_num, values):
        return f"{callsign}>APRS,TCPIP*,qAC,THIRD:T#{seq_num:03},{','.join(map(str, values))},00000000"

    @staticmethod
    def query_packet(callsign, query_data):
        return f"{callsign}>APRS,TCPIP*,qAC,THIRD:;QUERY ; :{query_data}"

    @staticmethod
    def object_report(callsign, object_name, timestamp, lat, lon, description):
        return f"{callsign}>APRS,TCPIP*,qAC,THIRD:;{object_name:<9}*{timestamp}z{lat}/{lon} {description}"

    @staticmethod
    def item_report(callsign, item_name, timestamp, lat, lon, description):
        return f"{callsign}>APRS,TCPIP*,qAC,THIRD:`{item_name:<9}*{timestamp}z{lat}/{lon} {description}"

    @staticmethod
    def acknowledgment_packet(callsign, recipient, msg_id):
        return f"{callsign}>APRS,TCPIP*,qAC,THIRD::{recipient:<9}:ack{msg_id}"

    @staticmethod
    def rejection_packet(callsign, recipient, msg_id):
        return f"{callsign}>APRS,TCPIP*,qAC,THIRD::{recipient:<9}:rej{msg_id}"

    @staticmethod
    def mic_e_position_report(callsign, encoded_position):
        return f"{callsign}>APRS,TCPIP*,qAC,THIRD:`{encoded_position} Example Mic-E Format"

    @staticmethod
    def dx_cluster_packet(callsign, dx_station, frequency, mode, location):
        return f"{callsign}>DX,TCPIP*,qAC,THIRD::DX de {callsign}:{frequency} MHz {mode} {location}"

    @staticmethod
    def generate_ack_packet(raw_packet, callsign):
        # Parse the raw packet to extract the recipient and message number
        try:
            parts = raw_packet.split("::")[1]  # Extract the part after '::'
            recipient = parts[:9].strip()  # Extract the recipient callsign (padded)
            msg_content = parts[9:]  # Extract the message content

            if "{" in msg_content:
                msgNo = msg_content.split("{")[1].strip()  # Extract the message number from {}
            else:
                raise ValueError("No message number found in the raw packet")

            # If the msgNo contains an alphabet, append "}"
            if any(char.isalpha() for char in msgNo):
                msgNo += "}"

            # Create the acknowledgment packet
            ack_packet = f"{callsign}>APRS::{recipient:<9}:ack{msgNo}"
            return ack_packet
        except Exception as e:
            raise ValueError(f"Error parsing raw packet for ACK generation: {e}")