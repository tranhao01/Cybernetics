# Vẽ lại bảng với độ rộng lớn hơn nữa để tránh bị chồng chữ

fig, ax = plt.subplots(figsize=(18, 8))  # Tăng kích thước hình
ax.axis('tight')
ax.axis('off')
table = ax.table(
    cellText=df.values, 
    colLabels=df.columns, 
    cellLoc='center', 
    loc='center'
)

# Điều chỉnh font và scale để dễ đọc
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(2.0, 2.2)  # Tăng cả chiều ngang và chiều cao

plt.show()
