   # create service class
    airbnbAnalysis = AirbnbAnalysisService()

    # get all tables in form of a list
    listings = airbnbAnalysis.get_listings()

    print(f"listings {listings}")

    # Schritt 1: Umwandeln in DataFrames
    listings_df = pd.DataFrame([l.__dict__ for l in listings])
    #
    # # Schritt 2: Daten aufbereiten
    # listings_df['price'] = pd.to_numeric(listings_df['price'], errors='coerce').fillna(0)
    # listings_df['number_of_reviews'] = pd.to_numeric(listings_df['number_of_reviews'], errors='coerce')
    # listings_df['availability_365'] = pd.to_numeric(listings_df['availability_365'], errors='coerce')