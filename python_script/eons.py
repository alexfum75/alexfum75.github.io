import matplotlib.pyplot as plt

def proterozoico ():
    # Data: Eon names, start times (Ma - Million years ago), and colors
    # We use Ma (Mega-annum) where 4600 = 4.6 billion years ago
    eons = [
        {"name": "Hadean", "start": 4600, "end": 4000, "color": "#4D4D4D", "event": "Earth forms"},
        {"name": "Archean", "start": 4000, "end": 2500, "color": "#FF5733", "event": "First life"},
        {"name": "Proterozoic", "start": 2500, "end": 541, "color": "#33FF57", "event": "Oxygen rise"}
        #{"name": "Phanerozoic", "start": 541, "end": 0, "color": "#3357FF", "event": "Complex life"}
    ]

    fig, ax = plt.subplots(figsize=(8, 4))

    # Create the bars
    for eon in eons:
        duration = eon["start"] - eon["end"]
        ax.barh("Earth History", duration, left=eon["end"], color=eon["color"], edgecolor='white', label=eon["name"])
        
        # Add eon labels in the middle of the bars
        mid_point = eon["end"] + (duration / 2)
        ax.text(mid_point, 0, eon["name"], ha='center', va='center', color='white', fontweight='bold', fontsize=10)
        
        # Add major events
        ax.annotate(eon["event"], xy=(eon["start"], 0.4), xytext=(eon["start"], 0.8),
                    arrowprops=dict(arrowstyle="->", color='black'), ha='center', fontsize=9)

    # Formatting the x-axis
    ax.set_xlim(4600, 541)  # Reversed to show time moving toward the present
    ax.set_xlabel("Millions of Years Ago (Ma)")
    ax.set_title("The Four Eons of Earth's History", fontsize=16, pad=20)
    ax.get_yaxis().set_visible(False) # Hide y-axis since it's just one row

    # Clean up the look
    plt.tight_layout()
    plt.grid(axis='x', linestyle='--', alpha=0.5)

    plt.show()

if __name__ == "__main__":
    proterozoico()    