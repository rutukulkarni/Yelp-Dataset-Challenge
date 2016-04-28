import pickle
import scipy.spatial.distance as scipy_dist
import numpy as np
import User as u
import Connection as c
import Restaurant as r
import Review as rv

#INPUT PARAMETERS
userInput = 9
restInput = 25
k = 100

noOfUsers = 0
noOfRestaurants = 0
userList = []
restaurantList = []
reviewList = []
userIdList = []
restIdList = []
commonMoviesSeen = 0.0

def getDistance(firstUser, secondUser):
    commonRestaurantsVisited = len(firstUser)
    scalingFactor = float(commonRestaurantsVisited)/noOfRestaurants

    distance = 1 / (1 + (float(scipy_dist.euclidean(firstUser,secondUser)) * scalingFactor))
    return distance

# def getNearestFriendRestaurants(nearestFriends):
#     for frnd in nearestFriends:
#         for review in reviewList:

def suggestionModel(user, restaurant, k, distanceMatrix, userRestMatrix):

    nearestUsers = []
    nearestUserIds = []
    distances = list(distanceMatrix[user])

    distances.sort(reverse=True)
    userVector = list(userRestMatrix[user])
    userVector.sort(reverse = True)
    print "distanceMatrixp[user]",distances
    print "vector",userVector

    for i in range(k):
        userIndex = distanceMatrix[user].index(distances[i])
        #print "..",userIndex
        nearestUsers.append(userList[userIndex])
        nearestUserIds.append(userIndex)

    #prediction logic
    predictionList = []
    nearestFriends = []
    for j in range(len(nearestUsers)-1):
        if nearestUsers[j]!=nearestUsers[j+1]:
            print nearestUsers[j].userId
            if userRestMatrix[nearestUserIds[j]].__contains__(userInput):
                print userInput, "is friend of", userRestMatrix[nearestUserIds[j]]
                nearestFriends.append(nearestUsers[j].userId)
            else:
                nearestFriends = list(nearestUsers)
                #getNearestFriendRestaurants(nearestFriends)
        else:
            break


def generateDistanceMatrix(userRestMatrix):

    distanceMatrix = [[0.0 for x in range(noOfUsers)] for x in range(noOfUsers)]

    for user1 in range(noOfUsers-1):
        for user2 in range(user1+1,noOfUsers):
            firstUser = []
            secondUser = []
            if user1 != user2:
                if distanceMatrix[user1][user2] == 0.0:
                    for rest in range(noOfRestaurants):
                        #creating non-zero vectors
                        if userRestMatrix[user1][rest] != 0.0 and userRestMatrix[user2][rest] != 0.0:
                            firstUser.append(userRestMatrix[user1][rest])
                            secondUser.append(userRestMatrix[user2][rest])
                    if(len(firstUser)>0):
                        distanceMatrix[user1][user2] = distanceMatrix[user2][user1] = getDistance(firstUser,secondUser)
                        print "u1: ",user1, " u2: ",user2, " dist: ",distanceMatrix[user1][user2]
                else:
                    distanceMatrix[user2][user1] = distanceMatrix[user1][user2]
    pickle.dump( distanceMatrix, open("distance.p","wb"))

    suggestionModel(userInput, restInput, k, distanceMatrix, userRestMatrix)

def getUserRestMapping():
    userRestMatrix = [[0.0 for x in range(noOfRestaurants)] for x in range(noOfUsers)]

    for review in reviewList:
        if userIdList.__contains__(review.userId) and restIdList.__contains__(review.restaurantId):
            userIndex = userIdList.index(review.userId)
            restaurantIndex = restIdList.index(review.restaurantId)
            if userIndex < noOfUsers and restaurantIndex < noOfRestaurants:
                userRestMatrix[userIndex][restaurantIndex] = (review.stars/5.0 + review.reviewScore)/2.0
                print "user: ", userIndex, "rest: ",restaurantIndex, "review: ",userRestMatrix[userIndex][restaurantIndex]

        #print "dsd"
    generateDistanceMatrix(userRestMatrix)

def getConnection():
    conn = c.Connection()
    db = conn.connect()
    return db

def getReviews():
    db = getConnection()
    collection = db.reviewsWithSentiments
    uniqueId = 0
    for review in collection.find():
        reviewObj = rv.Review(review)
        reviewList.append(reviewObj)
        uniqueId+=1
        #printTop10Data(reviewList)


def getRestaurantData():
    global noOfRestaurants
    db = getConnection()
    collection = db.businesses
    for restaurant in collection.find().limit(500):
        restaurantObj = r.Restaurant(restaurant)
        restaurantList.append(restaurantObj)
        restIdList.append(restaurantObj.restaurantId)
    noOfRestaurants = len(restaurantList)
    #printTop10Data(restaurantList)


def getUserData():
    db = getConnection()
    collection = db.users
    global noOfUsers
    for user in collection.find().limit(500):
        userObj = u.User(user)
        userList.append(userObj)
        #print userObj.userId
        userIdList.append(userObj.userId)
        #append(userObj)
    noOfUsers = len(userList)


def printTop10Data(list):
    for i in range(10):
        print list[i]


#findNeighbors()
getUserData()
getRestaurantData()
getReviews()
getUserRestMapping()