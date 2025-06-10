# Scapy ile gelişmiş IP paket işleme
from scapy.all import *
import socket
import struct

class NetworkProcessor:
    def __init__(self):
        self.fragment_size = 1024
        self.ttl_value = 64
        
    def create_custom_packet(self, data, dst_ip, dst_port, fragment_id=0):
        """Manuel IP başlığı ile paket oluşturma"""
        # IP başlığı parametreleri
        ip_header = IP(
            dst=dst_ip,
            ttl=self.ttl_value,
            id=fragment_id,
            flags="DF" if len(data) <= self.fragment_size else "MF"
        )
        
        # UDP başlığı
        udp_header = UDP(dport=dst_port)
        
        # Paket oluşturma
        packet = ip_header / udp_header / Raw(load=data)
        
        # Manuel checksum hesaplama
        packet = self.calculate_checksum(packet)
        
        return packet
    
    def fragment_data(self, data):
        """Veriyi parçalara ayırma"""
        fragments = []
        for i in range(0, len(data), self.fragment_size):
            fragment = data[i:i + self.fragment_size]
            fragments.append({
                'data': fragment,
                'seq_num': i // self.fragment_size,
                'is_last': i + self.fragment_size >= len(data)
            })
        return fragments