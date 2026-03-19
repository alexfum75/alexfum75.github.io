import matplotlib.pyplot as plt

def proterozoico ():
    # Data: Eon names, start times (Ma - Million years ago), and colors
    # We use Ma (Mega-annum) where 4600 = 4.6 billion years ago
    eons = [
        {"name": "Adeano", "start": 0, "end": 100, "color": "black", "event": "Formazione del basalto"},
        {"name": "Adeano", "start": 100, "end": 200, "color": "black", "event": "Formazione del granito"},
        {"name": "Adeano", "start": 200, "end": 300, "color": "gray", "event": "Grande virata"},
        {"name": "Archeano", "start": 300, "end": 500, "color": "blue", "event": "Procarioti"},
        {"name": "Archeano", "start": 500, "end": 600, "color": "blue", "event": "Fotosintesi"},
        {"name": "Archeano", "start": 600, "end": 1000, "color": "blue", "event": "BIF"},
        {"name": "Proterozoico", "start": 1000, "end": 1500, "color": "red", "event": "Evento ossidativo"},
        {"name": "Proterozoico", "start": 1500, "end": 2000, "color": "red", "event": ""}
        #{"name": "Phanerozoic", "start": 541, "end": 0, "color": "#3357FF", "event": "Complex life"}
    ]

    fig, ax = plt.subplots(figsize=(12, 4))

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
    ax.set_xlim(0, 2000)  # Reversed to show time moving toward the present
    ax.set_xlabel("Millions of Years Ago (Ma)")
    ax.set_title("The Four Eons of Earth's History", fontsize=16, pad=20)
    ax.get_yaxis().set_visible(False) # Hide y-axis since it's just one row

    # Clean up the look
    plt.tight_layout()
    plt.grid(axis='x', linestyle='--', alpha=0.5)

    plt.show()

if __name__ == "__main__":
    proterozoico()    