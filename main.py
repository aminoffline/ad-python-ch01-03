# movie genres

#movie_genres = {'Horror':0, 'Romance':0, 'Comedy':0, 'History':0 , 'Adventure':0 , 'Action':0}

def INPUT(n):
    movie_genres = {'Horror': 0, 'Romance': 0, 'Comedy': 0, 'History': 0, 'Adventure': 0, 'Action': 0}
    for i in range(0,n):
        name,choice1,choice2,choice3 =input().split(sep=" ")
        if choice1 in movie_genres.keys():
            movie_genres[f'{choice1}'] += 1
        if choice2 in movie_genres.keys():
            movie_genres[f'{choice2}'] += 1
        if choice3 in movie_genres.keys():
            movie_genres[f'{choice3}'] += 1
    return movie_genres
repetition = int(input())
A = INPUT(repetition)
A = dict(sorted(A.items(),key=lambda item : (-item[1],item[0])))

for k , v in A.items():
    print(f'{k}:{v}', end='\n')




