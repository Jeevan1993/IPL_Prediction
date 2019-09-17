#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import json
from espncricinfo.match import Match
from espncricinfo.player import Player
import pandas as pd
dataset=pd.DataFrame()
 
m=np.load('/home/g1/Documents/Cricket/Batting data/IPL_2008-2019_match_ids.npy')
count_main=0
size=m.size
while(1):#[count_main:]:#[1:2]: 
    if count_main==size:
        break
    
    print("Bowl Match ID=",count_main)
    match_no=m[count_main]
    print("Match no",match_no)
    
    try:
        mm = Match(match_no)
        
        pp=np.zeros([2,11])
        for i in range(2):
            print(" Team:",i)
            for j in range(11):
                pp[i,j]=mm.json['team'][i]['player'][j]['object_id']
        
        pba=np.zeros([2,11])
        pbs=np.zeros([2,11])   
        pbe=np.zeros([2,11])             
        for i in range(2):
            for j in range(11):
                p = Player(int(pp[i,j]))
                count=0
                count1=0
                count2=0
                count3=0
                a=0;b=0;c=0;d=0;e=0;f=0;g=0;h=0;k=0;sum1=0;sum2=0;sum3=0;
                #if dictionary contains t20 then get from t20, else 5
                if ('T20Is' in p.bowling_averages.keys()):
                    a=p.bowling_averages['T20Is']['bowling_average']
                    if a==''or a=='-': a='0'
                    #if a.replace('.','').isdigit():
                    a=a.replace('*','')
                    if a!='0':
                        count1+=1
                    b=p.bowling_averages['T20Is']['strike_rate']
                    if b=='' or b=='-': b='0'
                    b=b.replace('*','')
                    if b!='0':
                    #if b.replace('.','').isdigit():
                        count2+=1
                    g=p.bowling_averages['T20Is']['economy']
                    if g=='' or g=='-': g='0'
                    g=g.replace('*','')
                    if g!='0':
                    #if b.replace('.','').isdigit():
                        count3+=1
                    count+=1
                    
                if ('T20s' in p.bowling_averages.keys()):
                    c=p.bowling_averages['T20s']['bowling_average']
                    if c=='' or c=='-': c='0'
                    c=c.replace('*','')
                    #if c.replace('.','').isdigit():
                    if c!='0':
                        count1+=1
                    d=p.bowling_averages['T20s']['strike_rate']
                    if d==''or d=='-': d='0'
                    d=d.replace('*','')
                    if d!='0':
                    #if d.replace('.','').isdigit():
                        count2+=1
                    h=p.bowling_averages['T20s']['economy']
                    if h=='' or h=='-': h='0'
                    h=h.replace('*','')
                    if h!='0':
                        count3+=1
                    count+=1
                    
                    
                    
                if count1==2:
                    sum1=(float(a)+float(c))/count1
                else:
                    if ('List A' in p.bowling_averages.keys()):
                        e=p.bowling_averages['List A']['bowling_average']
                        if e==''or e=='-': e='0'
                        e=e.replace('*','')
                        #if e.replace('.','').isdigit():
                        if e!='0':
                            count1+=1
                            sum1=(float(a)+float(c)+float(e)/1.5)/count1
                            
                        elif count1!=0:
                            sum1=(float(a)+float(c))/count1
                            
                            
                    
                if count2==2:    
                    sum2=(float(b)+float(d))/count2
                else:
                    if ('List A' in p.bowling_averages.keys()):
                        f=p.bowling_averages['List A']['strike_rate']
                        if f=='' or f=='-': f='0'
                        f=f.replace('*','')
                        if f!='0':
                        #if f.replace('.','').isdigit():
                            count2+=1
                            sum2=(float(b)+float(d)+float(f)/1.5)/count2
                            
                        elif count2!=0:
                            sum2=(float(b)+float(d))/count2
                           
                            
                if count3==2:    
                    sum3=(float(b)+float(d))/count3
                else:
                    if ('List A' in p.bowling_averages.keys()):
                        k=p.bowling_averages['List A']['economy']
                        if k=='' or k=='-': k='0'
                        k=k.replace('*','')
                        if k!='0':
                        #if f.replace('.','').isdigit():
                            count3+=1
                            sum3=(float(g)+float(h)+float(k)*1.5)/count3
                            
                        elif count3!=0:
                            sum3=(float(g)+float(h))/count3
                            
    #            print("i=",i,"j=",j, "Passed")
                pba[i,j]=sum1
                pbs[i,j]=sum2
                pbe[i,j]=sum3
    #            print("Avg=",pba[i,j],"strrate=",pbs[i,j],"econ",pbe[i,j])
                    
        
        x=np.hstack(pba)
        y=np.hstack(pbs)
        z=np.hstack(pbe)
        xyz=[np.hstack([match_no,x,y,z])]
        dataset=dataset.append(xyz)
        print("Done with:",match_no)
        print("\n")
        count_main+=1
    except:
        print("Retring:",match_no)
        #dataset = pd.DataFrame({'Column1':data[:,0],'Column2':data[:,1]})
dataset.to_csv(r'bowl.csv',index=False)
print("Done Saving",count_main)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        