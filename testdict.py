from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

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

    return data
   
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = parse_multi_form(request.form)
      return render_template("result.html",result = result)
	  
if __name__ == '__main__':
   app.run(debug = True)
