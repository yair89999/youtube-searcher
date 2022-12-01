from flask import Flask,redirect,url_for, render_template, request, session, flash
import os,urllib.request,re

app = Flask(__name__)

def search_in_youtube(what_to_search):
    search_keyword = what_to_search # get everything except the "$search "
    fixed_search_keywod = ""
    for letter in search_keyword: # will get all the letters in the fixed_search_keywod vairable
        if letter.isalpha() == True:
            fixed_search_keywod += letter
    try:
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + fixed_search_keywod) # search in youtube the word and save the html file
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        print("searched: " + "https://www.youtube.com/watch?v=" + video_ids[0])
        return "https://www.youtube.com/watch?v=" + video_ids[0]
    except: # couldnt Encode the URL
        print(f"couldnt find {search_keyword}","\n")
        return "cant find"


@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        what_to_search = request.form["video name"]
        print("search for: "+what_to_search)
        url2 = search_in_youtube(what_to_search)
        if url2 == "cant find":
            flash("I am sorry but we couldn't find" + what_to_search)
        else:
            return render_template("after_search.html", url=url2)
        print(url2)
    return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True)