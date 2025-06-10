class RealTimeIDS:
    def __init__(self):
        self.threat_patterns = {
            'port_scan': {'pattern': 'multiple_port_access', 'threshold': 10},
            'ddos': {'pattern': 'high_packet_rate', 'threshold': 1000},
            'data_exfiltration': {'pattern': 'large_outbound', 'threshold': 1024000}
        }
        
    def detect_anomalies(self, network_traffic):
        """ML tabanlı anomali tespiti"""
        # Basit threshold-based detection
        for threat_type, config in self.threat_patterns.items():
            if self._check_pattern(network_traffic, config):
                self._trigger_alert(threat_type)
                return True
        return False