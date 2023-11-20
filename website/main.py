from flask import Flask, redirect,url_for,render_template,request

import pandas as pd
import os

def waterLevelFind(input_lat,input_lan):
    loc = r".\up_data"
    files = os.listdir(loc)
    level_dict = {}
    freq = {}
    avg_level_dict = {}
    # print(type(level_dict))

    for file in files:
        st = loc+"\\"+file
        df = pd.read_csv(st)
        for i in range(len(df)):
            lat_long = (df["lat"][i],df["long"][i])
            if(lat_long in level_dict):
                level_dict[lat_long]+=df["level"][i]
            else:
                level_dict[lat_long]=df["level"][i]
            level_dict[lat_long]+=df["level"][i]
            if(lat_long in freq):
                freq[lat_long]+=1
            else:
                freq[lat_long]=1
    for p in level_dict:
        avg_level_dict[p]=level_dict[p]/freq[p]

   
    loc1 = (input_lat,input_lan)
    import haversine as hs   
    from haversine import Unit
    nearest_5levels = {}
    for key in avg_level_dict:
        loc2 = key
        result=hs.haversine(loc1,loc2,unit=Unit.KILOMETERS)
        nearest_5levels[result] = avg_level_dict[key]

    output_val = 0
    i = 0
    nearest_levels_array = []
    total_distance = 0
    sorted_dict_by_keys = {k: nearest_5levels[k] for k in sorted(nearest_5levels.keys())}
    # print(sorted_dict_by_keys)
    nearest_5levels = sorted_dict_by_keys
    for key,value in nearest_5levels.items():
        nearest_levels_array.append((key,value))
        total_distance+=key
        i+=1
        if(i>5):
            break

    # print(nearest_levels_array)
    for key,value in nearest_levels_array:
        output_val+=(1-key/total_distance)*value

    # print(output_val/4)
    return output_val/4


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/waterLevel",methods=["POST","GET"])
def waterLevel():
    # return render_template("index.html")
    if request.method == "POST":
        Latitude = request.form["lat"]
        Longitude = request.form["lng"]
        # print(type(Latitude))
        lat = float(Latitude)
        lon = float(Longitude)
        groundLevel = waterLevelFind(lat,lon)
        stri =  str(groundLevel)
        return render_template("ans.html",data=[stri])
        # return stri
    else:
        return render_template("index.html")
    

if __name__ == "__main__":
    app.run(debug=True)