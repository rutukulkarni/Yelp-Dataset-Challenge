import Connection as c

restaurantList = []

class Restaurant:
    def __init__(self,restaurant):
        self.restaurantId = restaurant["business_id"]
        self.name = restaurant["name"]
        self.address = restaurant["full_address"]
        self.latitude = restaurant["latitude"]
        self.longitude = restaurant["longitude"]
        self.stars = restaurant["stars"]
        self.isOpen = restaurant["open"]
        self.reviewCount = restaurant["review_count"]

