import pandas as pd
import os

def waterLevelFind(x,y):
    loc = r"C:\Users\Lakshya Agrawal\Desktop\fontend\up_data"
    files = os.listdir(loc)
    level_dict = {}
    freq = {}
    avg_level_dict = {}
    print(type(level_dict))

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

    input_lat = 1
    input_lan = 1
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
    for key,value in nearest_5levels.items():
        nearest_levels_array.append((key,value))
        total_distance+=key
        i+=1
        if(i>5):
            break

    print(nearest_levels_array)
    for key,value in nearest_levels_array:
        output_val+=(1-key/total_distance)*value

    print(output_val/4)