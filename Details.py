import matplotlib.pyplot as plt
import numpy as np

# Thời gian từ 2020 đến 2055 (giai đoạn đi lên sóng 6)
years = np.linspace(2020, 2055, 300)
wave6_up = np.sin((years-2020)/30*np.pi/2)  # Nửa chu kỳ sin (đi lên)

fig, ax = plt.subplots(figsize=(14,7))

# Vẽ sóng đi lên
ax.plot(years, wave6_up, color="seagreen", linewidth=2)
ax.fill_between(years, 0, wave6_up, color="lightgreen", alpha=0.3)

# Nhãn dòng chảy chính
ax.text(2022, 0.2, "AI, Big Data, Năng lượng tái tạo", fontsize=9, color="darkblue")
ax.text(2032, 0.55, "AI tự điều chỉnh, Sinh học tổng hợp,\nY học cá nhân hóa", fontsize=9, color="darkblue")
ax.text(2042, 0.85, "Siêu hệ thống tự thích nghi,\nNăng lượng sạch phổ cập", fontsize=9, color="darkblue")

# Nhãn kinh tế - xã hội
ax.text(2022, 0.05, "Tự động hóa sản xuất,\nDịch vụ AI", fontsize=9, color="brown")
ax.text(2034, 0.35, "Kinh tế tri thức,\nĐô thị tự vận hành", fontsize=9, color="brown")
ax.text(2045, 0.65, "Kinh tế tự điều chỉnh,\nXã hội mạng lưới toàn cầu", fontsize=9, color="brown")

# Các sự kiện lớn (chấm đỏ)
events = {
    2027: "Bùng nổ ứng dụng AI",
    2035: "Bước ngoặt y tế AI\n& sinh học tổng hợp",
    2040: "Xã hội tự động hóa",
    2050: "Đỉnh Sóng 6"
}

for year, label in events.items():
    y_val = np.sin((year-2020)/30*np.pi/2)
    ax.plot(year, y_val, "ro")
    ax.text(year, y_val+0.07, label, fontsize=9, ha="center", color="red")

# Vạch năm hiện tại
ax.axvline(2025, color="red", linestyle="--", linewidth=1.5)
ax.text(2025, -0.05, "2025\nHiện tại", color="red", ha="center", fontsize=9, fontweight="bold")

# Cấu hình
ax.set_xlim(2020, 2055)
ax.set_ylim(-0.1, 1.2)
ax.set_xticks(range(2020, 2060, 5))
ax.set_yticks([])
ax.set_xlabel("Năm")
ax.set_title("Dòng chảy Sóng Kondratieff thứ 6 (giai đoạn đi lên ~2020–2050)", fontsize=13, fontweight="bold")

plt.show()
