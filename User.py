import Connection as c


class User:
    def __init__(self,user):
        self.userId = user["user_id"]
        self.name = user["name"]
        self.avgRating = user["average_stars"]
        self.yelpingSince = user["yelping_since"]
        self.elite = user["elite"]
        self.friends = user["friends"]




