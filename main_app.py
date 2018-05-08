from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

class ItemTable(Table):
    song_name = Col('Song Name')
    artist = Col('Artist')

class Item(object):
    def __init__(self, song_name, artist):
        self.song_name = song_name
        self.artist = artist


class Artist: 
    def __init__(self, artist_name, artist_rate):
      self.artist_name = artist_name
      self.artist_rate = artist_rate

class Song: 
    def __init__(self, song_name, song_rate):
      self.song_name = song_name
      self.song_rate = song_rate

#class to intialize Stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def check_recent(self, victim):
        if victim in self.items:
            return True
        else: 
            return False
    
    def print_items(self):
        for i in self.items:
            print(i)


#helper function for quicksort
def partition(song_list,start,end):
    i = ( start-1 )
    pivot = song_list[end][1].song_rate    
 
    for j in range(start , end):
 
     
        if song_list[j][1].song_rate <= pivot: #compare element to see if smaller
         
            i = i+1 #increment index
            song_list[i], song_list[j] = song_list[j],song_list[i]
 
    song_list[i+1],song_list[end] = song_list[end],song_list[i+1]
    return ( i+1 )
 
 
# Function to do Quick sort
def quickSort(song_list,start,end):
    if start < end:
 
        p = partition(song_list,start,end) #partitions the index at a specific point
 
        #sorting the elements before and after partition
        quickSort(song_list, start, p-1)
        quickSort(song_list, p+1, end)

def get_sorted_songs(song_list):
    res = []
    song_ordered = Stack()
    for song in song_list:
        song_ordered.push(song)
    
    for i, x in enumerate(song_list):
        res.append(song_ordered.pop())

    return res

def shuffle_sort(song_list):
    song_queue = queue.Queue()
    recently_added = Stack()
    increment_count = 0
    
    while(increment_count < 20):
        end = (len(song_list) - 1)
        print(end)
        rand_index = random.randint(0, end)
        print(rand_index)

        if recently_added.check_recent(song_list[rand_index][0].artist_name):
            increment_count = increment_count + 1
            pass
        else:
            increment_count = 0 
            song_queue.put(song_list[rand_index])
            recently_added.push(song_list[rand_index][0].artist_name)
            song_list.remove(song_list[rand_index])
            recently_added.print_items()
            if recently_added.size() > 4:
                recently_added.pop()
    
    while(len(song_list) != 0):
        end = (len(song_list) - 1)
        rand_index = random.randint(0, end)
        song_queue.put(song_list[rand_index])
        song_list.remove(song_list[rand_index])
       
    final_list = []
    while(song_queue.empty() != True):
        final_list.append(song_queue.get())

    for artist in final_list:
        print(artist[0].artist_name)
    print(len(final_list))

    return final_list

def parse_multi_form(form):
    data = {}
    for url_k in form:
        v = form[url_k]
        ks = []
        while url_k:
            if '[' in url_k:
                k, r = url_k.split('[', 1)
                ks.append(k)
                if r[0] == ']':
                    ks.append('')
                url_k = r.replace(']', '', 1)
            else:
                ks.append(url_k)
                break
        sub_data = data
        for i, k in enumerate(ks):
            if k.isdigit():
                k = int(k)
            if i+1 < len(ks):
                if not isinstance(sub_data, dict):
                    break
                if k in sub_data:
                    sub_data = sub_data[k]
                else:
                    sub_data[k] = {}
                    sub_data = sub_data[k]
            else:
                if isinstance(sub_data, dict):
                    sub_data[k] = v
    data_l = []
    for key, val in data.items(): 
        data_l.append(val)     
    
    artist_list = []    
    for i in range(0,10):
        artist = data_l[0][i]
        processed_text = artist.replace(" ", "")
        artist_list.append(artist)
    
    artist_info = []
    for value in form.items():
        artist_info.append(value)
    print(artist_info)

    artist_ratings = []
    for value in artist_info:
        if value[1].isdigit():
            artist_ratings.append(value[1])
    print(artist_ratings)


    info_list = []
    for i, artist in enumerate(artist_list): 
        for x, songs in enumerate(last_fm_api(artist)):
            info_list.append((Artist(artist_name= artist, artist_rate= artist_ratings[i]),Song(song_name= songs, song_rate= ((10 -x) + int(artist_ratings[i])))))
    
    result = []

    sorted_songs = info_list.copy()
    shuffled = info_list.copy()

    end = len(sorted_songs) - 1
    quickSort(sorted_songs, 0, end)

    shuffled = shuffle_sort(shuffled)

    temp = get_sorted_songs(sorted_songs)

    table_sorted = generate_table(temp) 
    table_shuffled = generate_table(shuffled)  
    
    result.append(table_sorted)
    result.append(table_shuffled)

    return result
   
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = parse_multi_form(request.form)
      return render_template("result.html",result = result)
	  
if __name__ == '__main__':
   app.run(debug = True)
