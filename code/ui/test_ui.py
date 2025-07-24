import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Các hàm xử lý dữ liệu (giả lập)
def get_historical_prices():
    """Trả về dữ liệu giá lịch sử (ngẫu nhiên)"""
    dates = [f"2023-{m:02d}-{d:02d}" for m in range(1, 13) for d in range(1, 29, 7)]
    prices = [100 + i*2 + np.random.rand()*10 for i in range(len(dates))]
    return dates, prices

def get_latest_price():
    """Trả về giá mới nhất (ngẫu nhiên)"""
    return round(150 + np.random.rand()*20, 2)

# Tạo giao diện
class StockPriceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Price Analyzer")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Thiết lập phong cách
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12), padding=10)
        self.style.configure('Header.TLabel', font=('Helvetica', 16, 'bold'))
        self.style.configure('Result.TLabel', font=('Helvetica', 14))
        
        # Tạo header
        header = ttk.Label(
            root, 
            text="STOCK PRICE ANALYSIS TOOL", 
            style='Header.TLabel',
            foreground="#2E86C1",
            background="#EAECEE",
            padding=10
        )
        header.pack(fill=tk.X, pady=(0, 20))
        
        # Tạo frame cho các nút
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=20)
        
        # Nút Get Historical Prices
        self.hist_btn = ttk.Button(
            button_frame,
            text="Get All Historical Prices",
            command=self.show_historical_prices,
            style='TButton'
        )
        self.hist_btn.grid(row=0, column=0, padx=20)
        
        # Nút Get Latest Price
        self.latest_btn = ttk.Button(
            button_frame,
            text="Get Latest Price",
            command=self.show_latest_price,
            style='TButton'
        )
        self.latest_btn.grid(row=0, column=1, padx=20)
        
        # Khu vực hiển thị kết quả
        self.result_frame = ttk.Frame(root)
        self.result_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Label kết quả
        self.result_label = ttk.Label(
            self.result_frame,
            text="Select a function to analyze stock prices",
            style='Result.TLabel',
            foreground="#2E86C1"
        )
        self.result_label.pack(pady=20)
        
        # Khu vực đồ thị
        self.graph_frame = ttk.Frame(self.result_frame)
        self.graph_frame.pack(fill=tk.BOTH, expand=True)
    
    def show_historical_prices(self):
        dates, prices = get_historical_prices()
        
        # Hiển thị thông báo
        self.result_label.config(text=f"Historical Prices ({len(prices)} records)")
        
        # Vẽ đồ thị
        self.draw_graph(dates, prices)
        
        # Hiển thị thông tin thêm
        min_price = min(prices)
        max_price = max(prices)
        current_price = prices[-1]
        info_text = f"Current: ${current_price:.2f} | Min: ${min_price:.2f} | Max: ${max_price:.2f}"
        ttk.Label(self.result_frame, text=info_text, font=('Helvetica', 12)).pack(pady=10)
    
    def show_latest_price(self):
        latest_price = get_latest_price()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Cập nhật kết quả
        self.result_label.config(text=f"Latest Stock Price")
        
        # Hiển thị giá cả
        price_display = ttk.Label(
            self.result_frame,
            text=f"${latest_price}",
            font=('Helvetica', 32, 'bold'),
            foreground="#27AE60"
        )
        price_display.pack(pady=20)
        
        # Hiển thị thời gian cập nhật
        time_label = ttk.Label(
            self.result_frame,
            text=f"Updated at: {current_time}",
            font=('Helvetica', 10),
            foreground="#7F8C8D"
        )
        time_label.pack()
    
    def draw_graph(self, dates, prices):
        # Xóa đồ thị cũ
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
        
        # Tạo đồ thị mới
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(dates, prices, marker='o', linestyle='-', color='#3498DB')
        ax.set_title('Historical Stock Prices', fontsize=14)
        ax.set_xlabel('Date', fontsize=10)
        ax.set_ylabel('Price ($)', fontsize=10)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.tick_params(axis='x', rotation=45)
        
        # Nhúng đồ thị vào Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def on_close(self):
        plt.close('all')  # Đóng tất cả figure matplotlib
        self.root.quit()  # Thoát mainloop
        self.root.destroy()  # Hủy cửa sổ

if __name__ == "__main__":
    root = tk.Tk()
    app = StockPriceApp(root)
    root.mainloop()
    plt.close('all')