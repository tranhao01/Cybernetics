import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(14, 6))

# --- Cybernetic Revolution timeline ---
ax.broken_barh([(1955, 40), (1995, 35), (2030, 30)], (20, 9),
               facecolors=('lightblue', 'skyblue', 'deepskyblue'))

ax.text(1955+20, 24.5, "Giai đoạn đầu tiên\n1955–1995", ha='center', va='center', fontsize=9)
ax.text(1995+17, 24.5, "Giai đoạn giữa\n1995–2030/40", ha='center', va='center', fontsize=9)
ax.text(2030+15, 24.5, "Giai đoạn cuối\n2030/40–2055/70", ha='center', va='center', fontsize=9)

ax.text(1947, 30, "Cybernetic Revolution", fontsize=11, fontweight='bold')

# --- K-Wave timeline ---
ax.broken_barh([(1947, 35), (1982, 38), (2020, 40)], (5, 9),
               facecolors=('lightgreen', 'mediumseagreen', 'seagreen'))

ax.text(1947+17, 9.5, "Sóng 4\n1947–1982/91", ha='center', va='center', fontsize=9)
ax.text(1982+19, 9.5, "Sóng 5\n1982/91–2020", ha='center', va='center', fontsize=9)
ax.text(2020+20, 9.5, "Sóng 6\n2020–2060/70", ha='center', va='center', fontsize=9)

ax.text(1947, 15, "K-Waves (Kondratieff)", fontsize=11, fontweight='bold')

# --- Vạch năm hiện tại (2025) ---
ax.axvline(2025, color='red', linestyle='--', linewidth=2)
ax.text(2025, 34, "2025\n(Hiện tại)", color='red', ha='center', va='bottom', fontsize=10, fontweight='bold')

# --- Cấu hình trục ---
ax.set_ylim(0, 40)
ax.set_xlim(1945, 2075)
ax.set_xlabel("Năm")
ax.set_yticks([])
ax.set_xticks(range(1950, 2080, 10))
ax.grid(axis='x', linestyle=':', alpha=0.6)

plt.title("Timeline: Cybernetic Revolution & K-Waves (1947–2070)", fontsize=13, fontweight='bold')
plt.show()
