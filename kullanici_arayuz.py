# Tkinter tabanlı GUI
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SecureTransferGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Secure File Transfer System")
        self.root.geometry("800x600")
        self.setup_interface()
        
    def setup_interface(self):
        """Ana arayüz bileşenlerini oluşturma"""
        # File selection frame
        file_frame = ttk.LabelFrame(self.root, text="File Selection", padding=10)
        file_frame.pack(fill="x", padx=10, pady=5)
        
        # Network monitoring frame
        monitor_frame = ttk.LabelFrame(self.root, text="Network Monitoring", padding=10)
        monitor_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Real-time graphs
        self.setup_monitoring_graphs(monitor_frame)