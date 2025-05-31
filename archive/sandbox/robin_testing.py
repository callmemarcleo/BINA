from airbnb_analysis_service import AirbnbAnalysisService
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # create service class
    airbnbAnalysis = AirbnbAnalysisService()

    # get all tables in form of a list
    listings = airbnbAnalysis.get_listings()
    selling_prices = airbnbAnalysis.get_selling_prices()

    print(f"selling_prices {len(selling_prices)}")
    print(f"listings {len(listings)}")

    # Schritt 1: Umwandeln in DataFrames
    listings_df = pd.DataFrame([l.__dict__ for l in listings])
    selling_prices_df = pd.DataFrame([s.__dict__ for s in selling_prices])
    #
    # # Schritt 2: Daten aufbereiten
    # listings_df['price'] = pd.to_numeric(listings_df['price'], errors='coerce').fillna(0)
    # listings_df['number_of_reviews'] = pd.to_numeric(listings_df['number_of_reviews'], errors='coerce')
    # listings_df['availability_365'] = pd.to_numeric(listings_df['availability_365'], errors='coerce')
    #
    # # Schritt 3: Gruppieren nach Stadtteil ("neighbourhood_group")
    # grouped = listings_df.groupby('neighbourhood_group').agg({
    #     'price': 'mean',
    #     'availability_365': 'mean',
    #     'number_of_reviews': 'mean',
    #     'id': 'count'
    # }).rename(columns={'id': 'listings_count'}).reset_index()
    #
    # # Schritt 4: Ausgabe der Metriken
    # print("\nDurchschnittswerte pro Stadtteil (neighbourhood_group):\n")
    # print(grouped.sort_values('price', ascending=False))
    #
    # # Schritt 5: Visualisierung
    # plt.figure(figsize=(12, 6))
    # plt.bar(grouped['neighbourhood_group'], grouped['price'])
    # plt.xticks(rotation=45)
    # plt.ylabel("Durchschnittlicher Preis (CHF)")
    # plt.title("⭑ Durchschnittlicher Airbnb Preis je Stadtteil in Zürich")
    # plt.tight_layout()
    # plt.show()
    #
    # plt.figure(figsize=(12, 6))
    # plt.bar(grouped['neighbourhood_group'], grouped['availability_365'], color='orange')
    # plt.xticks(rotation=45)
    # plt.ylabel("Verfügbare Tage pro Jahr")
    # plt.title("📅 Durchschnittliche Verfügbarkeit je Stadtteil")
    # plt.tight_layout()
    # plt.show()