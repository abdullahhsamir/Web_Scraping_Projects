import os
import json
import requests # request img from web
import shutil # save img locally


os.chdir(r"G:\abdallah\web\web_project_repo\json_data")
def get_imgs(url, name_to_save):
  link = url[  url.find("/img/") :  ]
  f_link = "https://animeblkom.net" + link

  res = requests.get(f_link, stream = True)


  
  i =f_link.rfind("/")

  j = f_link.find("-poster")
  #file_name =  f_link[i+1:j]

  
  if res.status_code == 200:
    os.chdir(r"G:\abdallah\web\web_project_repo\static\img")
    with open(str(name_to_save)+'.jpeg','wb') as f:
        shutil.copyfileobj(res.raw, f) 
    print('Image sucessfully Downloaded: ',name_to_save)
  else:
      print('Image Couldn\'t be retrieved')





json_files = [ f for f in os.listdir() if f.endswith('.json') ]
for i in range(50, len(json_files)+1 ):
  os.chdir(r"G:\abdallah\web\web_project_repo\json_data")
  f = open('data-series{}.json'.format(i))
  lst = json.load(f)


  for j in range(len(lst)):
    os.chdir(r"G:\abdallah\web\web_project_repo\json_data")
    get_imgs(lst[j]['src-img'], lst[j]['name'])

