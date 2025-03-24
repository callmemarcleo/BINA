from airbnb_analysis_service import AirbnbAnalysisService

if __name__ == "__main__":

    # create service class
    airbnbAnalysis = AirbnbAnalysisService()

    # get all tables in form of a list
    listings = airbnbAnalysis.get_listings()
    reviews = airbnbAnalysis.get_reviews()
    neighbourhoods = airbnbAnalysis.get_neighbourhoods()

    # examples
    for review in reviews:
        print("------------------ REVIEWS -----------------------\n")
        print(f"review date: {review.date}\n")
        print(f"review listing_id: {review.listing_id}\n")

    for neighbourhood in neighbourhoods:
        print("------------------ NEIGHBOURHOODS -----------------------\n")
        print(f"neighbourhood.neighbourhood_group: {neighbourhood.neighbourhood_group}\n")
        print(f"neighbourhood.neighbourhood: {neighbourhood.neighbourhood}\n")

    for listing in listings:
        print("------------------ LISTINGS ----------------------- \n")
        print(f"listing.name {listing.name}\n")
        print(f"listing.host_name {listing.host_name}\n")
        print(f"listing.price {listing.price}\n")