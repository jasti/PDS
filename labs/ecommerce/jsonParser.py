import json
import users
import listings
import shop
import csv

user_file = "users.json"
listings_file = "listings.json"
shop_file ="shops.json"

user_file = open(user_file,'r')
all_users = []

for line in user_file: 
    user = users.fromJson(line)
    all_users.append(user)

print len(all_users)

user_file.close()

listing_file = open(listings_file,'r')
all_listings= []
for line in listing_file:
    listing = listings.fromJson(line)
    all_listings.append(listing)

print len(all_listings)

all_shops= []
for line in open(shop_file, 'r'):
    shops = shop.fromJson(line)
    all_shops.append(shops)

print len(all_shops)


num_friends  = dict()
num_favorites= dict()
num_purchases = dict()

for a_user in all_users:
    num_favorite = len(a_user.favorites)
   
    if num_favorites.has_key(num_favorite): 
       num_favorites[num_favorite]=1
    else:
       value = num_favorites[num_favorite]
       num_favorites[num_favorite] = value+ 1

print num_favorites        
