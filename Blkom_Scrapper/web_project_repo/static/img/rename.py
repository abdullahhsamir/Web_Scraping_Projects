import os

path = 'G:/abdallah/web/web_project_repo/static/img/'


for file in os.listdir(path):
    os.rename(path + file, path + file.lower())
    print("Done !!")