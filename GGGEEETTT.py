import numpy as np
import sys,os
import config2
CONSUMER_KEY    = config2.CONSUMER_KEY
CONSUMER_SECRET = config2.CONSUMER_SECRET
ACCESS_TOKEN = config2.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = config2.ACCESS_TOKEN_SECRET
import tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit = True)#,wait_on_rate_limit_notify= True #PLOT TIME
#user = sys.argv[1]
import pandas as pd
df=pd.read_csv('df_mix.csv')
df=df.drop("Unnamed: 0", axis=1)
df=df.to_numpy()
df=df.reshape(-1,)
k=0
"""
for i in range(10):
    k+=1
    print(df[k])
"""
df_list=df.astype(str)
len(df_list)
list_real=[]
for i in range(1440):
    list_real.append(df[i])
list_real

follower_list=[]
def skip_func(list):
    cnt=0
    for i in list:
        padd= [0] * 200
        try :
            got=api.followers_ids(i,count=200)
        except :
            print('========NG=============',cnt)# pass (Real code == pass ,Practice code == print(NG))
            follower_list.append(padd)
        else :
            print('==========OK==========',cnt)
            #followerData["Follower_id"] = str(a)
            #followerDatas.append(followerData)
            #followerDatas.append(a)
            follower_list.append(got)
        #print(str(i))
        #print(followerData)
        cnt+=1
skip_func(list_real)

pd.set_option("display.max_rows", 250)
df=pd.DataFrame(follower_list)

df1=df.fillna(0)
df1=df1.astype(int)

df0=pd.DataFrame(list_real,columns=['ID'])
print(df0.head())# core user's follow user

#pd.options.display.precision = 21
df2=pd.concat([df0, df1],axis=1)
df2=df2.fillna(0)
df2=df2.astype(int)

df2.to_csv("Network_moto_2020.csv")

print(df2.head())

