from airbnb_analysis_service import AirbnbAnalysisService
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

if __name__ == "__main__":

    # create service class
    airbnbAnalysis = AirbnbAnalysisService()

    # get all tables in form of a list
    listings = airbnbAnalysis.get_listings()
    reviews = airbnbAnalysis.get_reviews()
    neighbourhoods = airbnbAnalysis.get_neighbourhoods()

listings_df = pd.DataFrame(listings)

plt.figure(figsize=(8, 5))
listings_df['room_type'].value_counts().plot(kind='bar')
plt.title('Anzahl der Angebote pro Zimmertyp')
plt.xlabel('Zimmertyp')
plt.ylabel('Anzahl')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Stelle sicher, dass price numerisch ist
listings_df['price'] = pd.to_numeric(listings_df['price'], errors='coerce')

# Entferne Zeilen mit fehlenden Preisen
valid_prices = listings_df['price'].dropna()

# Plotten
plt.figure(figsize=(10, 6))
plt.hist(valid_prices, bins=50, edgecolor='black')
plt.title("Verteilung der Airbnb-Preise in Zürich (alle Daten)")
plt.xlabel("Preis (CHF)")
plt.ylabel("Anzahl der Listings")
plt.grid(True)
plt.tight_layout()
plt.show()