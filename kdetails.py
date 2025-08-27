import numpy as np
import matplotlib.pyplot as plt

# Trục thời gian chi tiết 2020-2030
years = np.linspace(2020, 2030, 300)
wave6_detail = np.sin((years-2020)/30*np.pi/2)  # đoạn đầu sóng 6

fig, ax = plt.subplots(figsize=(14,6))

# Vẽ đoạn sóng
ax.plot(years, wave6_detail, color="seagreen", linewidth=2)
ax.fill_between(years, 0, wave6_detail, color="lightgreen", alpha=0.3)

# Các dòng chảy công nghệ
ax.text(2021, 0.05, "AI thế hệ đầu\n(Deep Learning bùng nổ)", fontsize=9, color="darkblue")
ax.text(2024, 0.2, "Big Data, Cloud,\nỨng dụng diện rộng", fontsize=9, color="darkblue")
ax.text(2028, 0.4, "AI tích hợp IoT,\nTự động hóa nâng cao", fontsize=9, color="darkblue")

# Kinh tế - xã hội
ax.text(2021, 0.15, "Tự động hóa trong sản xuất", fontsize=9, color="brown")
ax.text(2025, 0.3, "Dịch vụ AI phổ biến,\nNền kinh tế gig mở rộng", fontsize=9, color="brown")
ax.text(2029, 0.5, "Chuyển dịch lao động\nsang ngành tri thức", fontsize=9, color="brown")

# Sự kiện lớn
events_detail = {
    2023: "AI tạo sinh (Generative AI)\nbùng nổ toàn cầu",
    2025: "Ứng dụng AI trong sản xuất &\ndịch vụ y tế",
    2027: "AI tham gia điều hành\nkinh tế - xã hội",
    2030: "Ngưỡng công nghệ hội tụ\n(AI + IoT + Năng lượng sạch)"
}

for year, label in events_detail.items():
    y_val = np.sin((year-2020)/30*np.pi/2)
    ax.plot(year, y_val, "ro")
    ax.text(year, y_val+0.05, label, fontsize=9, ha="center", color="red")

# Vạch năm hiện tại
ax.axvline(2025, color="red", linestyle="--", linewidth=1.5)
ax.text(2025, -0.05, "2025\nHiện tại", color="red", ha="center", fontsize=9, fontweight="bold")

# Cấu hình
ax.set_xlim(2020, 2030)
ax.set_ylim(-0.1, 0.7)
ax.set_xticks(range(2020, 2031, 1))
ax.set_yticks([])
ax.set_xlabel("Năm")
ax.set_title("Chi tiết Sóng Kondratieff thứ 6 (2020–2030) – Giai đoạn đi lên", fontsize=13, fontweight="bold")

plt.show()
