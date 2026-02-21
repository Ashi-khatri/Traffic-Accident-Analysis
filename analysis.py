import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# Load dataset
df = pd.read_csv("traffic.csv")

print("Columns:", df.columns)

# Remove missing values
df = df.dropna()

# Convert time into hour (fixed)
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.hour

# ----------------------------
# Accidents by Hour
# ----------------------------
sns.countplot(x='Hour', data=df)
plt.title("Accidents by Hour")
plt.show()

# ----------------------------
# Accidents by Weather
# ----------------------------
sns.countplot(x='Weather', data=df)
plt.title("Accidents by Weather")
plt.xticks(rotation=45)
plt.show()

# ----------------------------
# Accidents by Road Condition
# ----------------------------
sns.countplot(x='Road_Condition', data=df)
plt.title("Accidents by Road Condition")
plt.xticks(rotation=45)
plt.show()

# ----------------------------
# Create Hotspot Map
# ----------------------------
print("Creating map...")

m = folium.Map(
    location=[df['Latitude'].mean(), df['Longitude'].mean()],
    zoom_start=11
)

heat_data = df[['Latitude', 'Longitude']].values.tolist()
HeatMap(heat_data).add_to(m)

m.save("accident_hotspots.html")

print("Hotspot map saved successfully!")