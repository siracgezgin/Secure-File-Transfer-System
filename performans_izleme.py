# Gelişmiş performans izleme modülü
import time
import psutil
import subprocess
import threading
from collections import deque

class PerformanceMonitor:
    def __init__(self):
        self.metrics = {
            'bandwidth': deque(maxlen=100),
            'latency': deque(maxlen=100),
            'packet_loss': deque(maxlen=100),
            'cpu_usage': deque(maxlen=100),
            'memory_usage': deque(maxlen=100)
        }
        self.monitoring = False
        
    def start_monitoring(self):
        """Gerçek zamanlı izleme başlatma"""
        self.monitoring = True
        monitor_thread = threading.Thread(target=self._monitor_loop)
        monitor_thread.daemon = True
        monitor_thread.start()
        
    def measure_bandwidth(self, interface='eth0'):
        """iPerf3 ile bant genişliği ölçümü"""
        try:
            result = subprocess.run([
                'iperf3', '-c', 'localhost', '-t', '5', '-J'
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                import json
                data = json.loads(result.stdout)
                bandwidth = data['end']['sum_received']['bits_per_second']
                return bandwidth / 1_000_000  # Mbps
        except Exception as e:
            print(f"Bandwidth measurement error: {e}")
            return 0