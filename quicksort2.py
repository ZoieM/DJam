def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark


if __name__ == "__main__":

  score_list = []
  user_preference = {"artists":{"Justin": 1, "Beyonce": 2, "Rihanna": 3}}
  song_rating = {"Justin":{"hi": 1, "yo": 2, "goodbye": 3 }, "Beyonce":{"a": 1, "b": 2, "c": 3  },"Rihanna": {"i": 1, "like": 2, "food": 3 }}
  for art_info in user_preference["artists"].items():
      for song_val in song_rating[art_info[0]].items():
          score = art_info[1] + song_val[1]
          score_list.append(score)
          song_rating[art_info[0]][song_val[0]] = score
  quickSort(score_list)
  print(score_list)


