from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

target_star = db.movies.find_one({'title':'사운드 오브 뮤직'})['star']


same_star_movies = list(db.movies.find({'star': target_star}))
db.movies.update_many({'star': target_star},{'$set':{'star': 0}})

for movie in same_star_movies:
    print(movie['star'])


# 튜터님 코드
#target_star = db.movies.find_one({'title':'사운드 오브 뮤직'})['star']
#seacrh_result = list(db.movies.fomt({'star':target_star}))

# for movie in search_result:
#     print(movie['title'])

#search_query = {'star': target_star}
#update_quety = {'$set': {'star':0}}

#db.movies.update_many(search_query,update_query)//