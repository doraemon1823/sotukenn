import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys,os

df=pd.read_csv("df_mix2.csv")
df=df[1:]
df=df.drop("Unnamed: 0",axis=1)
df=df.reset_index()
df=df.drop("index",axis=1)
list_a = list(range(199))
df.columns=list_a

ID=df[0]
id_num=0
list_edge=[]
print("START !!!!")
for loc_num in range(500):
    print(loc_num,"/500")
    for next_num in range(198):
        for id_num in range(2000):
            if df.loc[loc_num][next_num+1]==ID[id_num]:
                print(loc_num,"==like=>>",id_num)
                case=([loc_num,id_num])
                list_edge.append(case)
            else:
                pass
df_networt=pd.Dataframe(case)
df_network.to_csv("df_network.csv")
