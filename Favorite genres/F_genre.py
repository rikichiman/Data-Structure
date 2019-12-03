genre={
    'Drama':['book1','book2','book3'],
    'history':['book4','book5','book6'],
    'action':['book7','book8']
}

users={
    'jhon':['book1','book2','book7'],
    'amine':['book4','book5','book7','book8','book3']
}

def findMax(listg):
    max=0
    for fg in listg:
        for v in fg.values():
            if v > max:
                max = v
    return max

def genre_list(lg,max):
    fav_list=[]
    for fg in lg:
            for k, v in fg.items():
                if v == max:
                    fav_list.append(k)
    return fav_list

def favorite_genres(users,genre):
    usrF={}
    Finalusr={}
    for user in users.keys():
        #get list of books
        usr_book=users[user]
        if user not in usrF.keys():
            usrF[user]=[]    #Empty array of genres {'genre':count} ..
        for g in genre.keys():
            genre_book=genre[g]
            ng=0
            for gb in genre_book:
                for ub in usr_book:
                    if gb == ub:
                        ng=ng+1
            usrF[user].append({g:ng})
        
        max=findMax(usrF[user])
        Finalusr[user]=genre_list(usrF[user],max)   
    return Finalusr

print(favorite_genres(users,genre))