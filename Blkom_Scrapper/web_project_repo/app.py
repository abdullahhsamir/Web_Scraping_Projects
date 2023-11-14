from flask import Flask,render_template,request
import json
import os
from flask.helpers import url_for

from werkzeug.utils import redirect


#from static.get_names import get_names

app = Flask(__name__, static_url_path='/static')
#app.run(host='0.0.0.0',port='5000')

@app.route("/")
def homepage():
    search = request.args.get('search')

    if search == '':
        return redirect(url_for('search',search = search))
    if search == 'None':
        return render_template("index.html")
    if search != None:
 
        return redirect(url_for('search',search = search))
    return render_template("index.html", pagetitle ='أنمي سكرابر| الرئيسية')

@app.route("/search")
def search(): 
    search = str(request.args.get('search')).casefold().replace("(", "").replace(")","")
    os.chdir(r"/home/asamir/Desktop/web_project_repo/json_data/all_data")
    f = open('all_data.json')
    data = json.load(f)
    if search == "":
        render_template('search.html', search_animes = data)
    search_animes = []
    for i in range(len(data)):
        if str(data[i]['name']).replace("-", " ").startswith(search) or str(data[i]['name']) == search :
            search_animes.append(str(data[i]['name']))
    search_animes = list(dict.fromkeys(search_animes))
    
    

    return render_template('search.html', search_animes = search_animes, pagetitle ='أنمي سكرابر| البحث')

@app.route("/anime-list/")
def anime_list_():
        return redirect(url_for('anime_list_pagniation',page = 1))

@app.route("/anime-list/page/")
def anime_list():
        return redirect(url_for('anime_list_pagniation',page = 1))

@app.route("/anime-list/page/<int:page>")
def anime_list_pagniation(page):
    os.chdir(r"/home/asamir/Desktop/web_project_repo/json_data")
    file = "data-series%d.json"%page
    f = open(file)
    lst = json.load(f)
    json_files = [f for f in os.listdir() if f.endswith('.json')]
    indexing  = len(json_files)

    backward = page - 1
    forward = page + 1

    if page == 1:
        backward = 1
    
    if page == len(json_files) -1  :
        forward = page
        
    
    return render_template("anime-list.html", lst = lst , indexing = indexing , backward = backward, forward = forward, pagetitle ='أنمي سكرابر| قائمة الأنمي' )

@app.route("/anime/<name>")
def anime(name = None):
    os.chdir(r"/home/asamir/Desktop/web_project_repo/json_data/all_data")
    f = open('all_data.json')
    lst = json.load(f)

    json_files = [f for f in os.listdir() if f.endswith('.json')]
    indexing  = len(json_files)

    

    for i in range(len(lst)):
        if lst[i]['name'] == name:
            lst2=[]
            for j in range(len(lst[i]['episodes'])):
                d = lst[i]['episodes'][j]
                d = {int(k):[i for i in v] for k,v in d.items()}
                lst2.append(d)
            link = lst2
            return render_template("anime-details.html", data = lst[i] , link = link, pagetitle ='أنمي سكرابر| {}'.format(name))
            
    #return render_template("anime-list.html", indexing = indexing)
    return "Not Found!"

@app.route("/about-us/")
def about_us():
    return render_template("about-us.html", pagetitle ='أنمي سكرابر| من نحن')

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")