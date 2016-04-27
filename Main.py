import math
import scipy.spatial.distance as scipy_dist
from sklearn.neighbors import NearestNeighbors
import numpy as np
import User as u
import Connection as c
import Restaurant as r
import Review as rv

noOfUsers = 0
noOfRestaurants = 0
userList = []
restaurantList = []
reviewList = []

def getUserRestMapping():
    userRestMatrix = [[0.0 for x in range(noOfRestaurants)] for x in range(noOfUsers)]
    score = 0.0
    count = 0
    sum = 0
    count=0
    for user in range(noOfUsers):
        for restaurant in range(noOfRestaurants):
            for review in reviewList:
                userIndex = userList.index(review.userId)

def getConnection():
    conn = c.Connection()
    db = conn.connect()
    return db

def getReviews():
    db = getConnection()
    collection = db.reviews
    for review in collection.find():
        reviewObj = rv.Review(review)
        reviewList.append(reviewObj)
    noOfRestaurants = len(reviewList)
    #printTop10Data(reviewList)


def getRestaurantData():
    db = getConnection()
    collection = db.businesses

    for restaurant in collection.find():
        restaurantObj = r.Restaurant(restaurant)
        restaurantList.append(restaurantObj)
    noOfRestaurants = len(restaurantList)
    printTop10Data(restaurantList)

def getUserData():
    db = getConnection()
    collection = db.users

    for user in collection.find():
        userObj = u.User(user)
        userList.append(userObj)
    noOfUsers = len(userList)
    printTop10Data(userList)



def printTop10Data(list):
    for i in range(10):
        print list[i]


def findNeighbors():
    X = np.array([[-1, -1,0], [-2, -1,0], [-3, -2,8], [1, 1,5], [2, 1,3], [3, 2,3]])
    nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
    distances, indices = nbrs.kneighbors(X)
    print distances,'....',indices

findNeighbors()
#getUserData()
#getRestaurantData()
#getReviews()
#getUserRestMapping()