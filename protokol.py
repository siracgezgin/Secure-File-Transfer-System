# Dinamik protokol seçimi
class AdaptiveProtocol:
    def __init__(self):
        self.current_protocol = 'TCP'
        self.network_conditions = {}
        
    def analyze_network_conditions(self):
        """Ağ koşullarını analiz ederek optimal protokol seçimi"""
        latency = self.measure_latency()
        packet_loss = self.measure_packet_loss()
        bandwidth = self.measure_bandwidth()
        
        # Karar algoritması
        if packet_loss > 0.5:  # %0.5'ten fazla paket kaybı
            return 'TCP'  # Güvenilir iletim gerekli
        elif latency < 10:  # Düşük gecikme
            return 'UDP'  # Hız öncelikli
        else:
            return 'TCP'  # Varsayılan güvenilir seçim