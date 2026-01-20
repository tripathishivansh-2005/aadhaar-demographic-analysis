import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 12))
ax.axis('off')

boxes = {
    "A": (0.5, 0.95, "UIDAI Aadhaar\nDemographic Update Dataset"),
    "B": (0.5, 0.85, "Data Cleaning & Preprocessing"),
    "C": (0.5, 0.75, "Feature Engineering"),
    "D": (0.5, 0.65, "Exploratory Data Analysis"),
    "E1": (0.2, 0.55, "Univariate Analysis"),
    "E2": (0.5, 0.55, "Bivariate Analysis"),
    "E3": (0.8, 0.55, "Trivariate Analysis"),
    "F": (0.5, 0.40, "Visualisation Layer"),
    "G": (0.5, 0.30, "Insights & Interpretation"),
    "H": (0.5, 0.20, "Policy & Administrative Impact")
}

# Draw boxes
for x, y, text in boxes.values():
    ax.text(x, y, text, ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.4"))

# Draw arrows
def arrow(start, end):
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle="->"))

arrow((0.5, 0.93), (0.5, 0.87))
arrow((0.5, 0.83), (0.5, 0.77))
arrow((0.5, 0.73), (0.5, 0.67))

arrow((0.5, 0.63), (0.2, 0.57))
arrow((0.5, 0.63), (0.5, 0.57))
arrow((0.5, 0.63), (0.8, 0.57))

arrow((0.2, 0.53), (0.5, 0.43))
arrow((0.5, 0.53), (0.5, 0.43))
arrow((0.8, 0.53), (0.5, 0.43))

arrow((0.5, 0.37), (0.5, 0.32))
arrow((0.5, 0.27), (0.5, 0.22))


plt.show()
