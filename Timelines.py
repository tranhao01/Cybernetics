import numpy as np
import matplotlib.pyplot as plt

# Trục thời gian
years = np.linspace(1947, 2070, 500)

# Hàm sóng giả lập (sinusoidal cho trực quan, không phải số liệu tuyệt đối)
wave4 = np.sin((years-1947)/35*np.pi) * (years<=1982)
wave5 = np.sin((years-1982)/38*np.pi) * ((years>=1982)&(years<=2020))
wave6 = np.sin((years-2020)/45*np.pi) * (years>=2020)

# Vẽ biểu đồ sóng
fig, ax = plt.subplots(figsize=(14,6))

ax.plot(years, wave4, color="lightgreen", label="Sóng 4 (1947–1982/91)")
ax.plot(years, wave5, color="mediumseagreen", label="Sóng 5 (1982/91–2020)")
ax.plot(years, wave6, color="seagreen", label="Sóng 6 (2020–2060/70)")

# Đường hiện tại
ax.axvline(2025, color='red', linestyle='--', linewidth=2)
ax.text(2025, 1.1, "2025\nHiện tại", color="red", ha="center", fontsize=10, fontweight="bold")

# Cấu hình
ax.set_xlim(1947, 2070)
ax.set_ylim(-1.2, 1.2)
ax.set_xticks(range(1950, 2080, 10))
ax.set_yticks([])
ax.set_xlabel("Năm")
ax.set_title("Biểu đồ sóng Kondratieff (K-Waves) - dạng chu kỳ đi lên & đi xuống", fontsize=13, fontweight="bold")
ax.legend()

plt.show()
