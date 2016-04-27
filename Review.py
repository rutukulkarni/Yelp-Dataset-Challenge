class Review:
    def __init__(self,review):
        self.reviewId = review["review_id"]
        self.userId = review["user_id"]
        self.restaurantId = review["business_id"]
        self.reviewText = review["text"]
        self.stars = review["stars"]
        self.type = review["type"]
        self.date = review["date"]
        self.reviewScore = 0


