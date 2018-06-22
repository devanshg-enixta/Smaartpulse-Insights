import pandas as pd
import matplotlib.pyplot as plt
import random
out_t=pd.read_csv("Brand_trend_water_purifiers_11_01_2018_month_v2_top_5.csv")
x1 = list(out_t.Month.unique())
br  = out_t.Brand_name.unique()
y1=[]
y2=[]

plt.figure(1)
for b in br:
    rev = out_t[out_t.Brand_name == b]
    x2 = list(rev.Month.unique())
    y1=[]
    y2=[]
    for i in range(1,13):
        if i in x2:
            for row in rev.to_dict("records"):
                if row['Month'] == i:
                    y1.append(row['Trend_Total_Reviews'])
        else:
            y1.append(0)
    plt.plot(x1, y1, label = b)
plt.xlabel('Months')
# naming the y axis
plt.ylabel('Trend_Total_Reviews')
plt.legend()
colors = ['#624ea7', 'g', 'yellow', 'k', 'maroon']
i=0
f , plt1 = plt.subplots(4,2)
plt2 = plt1.flatten()
j=0
n=4
for b1 in br:
    if b1 not in  'Eureka Forbes':
        b2 = ['Eureka Forbes',b1]
        for b in b2:
            #print b
            rev = out_t[out_t.Brand_name == b]

            x2 = list(rev.Month.unique())
            y2=[]
            for i in range(1,13):
                if i in x2:
                    for row in rev.to_dict("records"):
                        if row['Month'] == i:
                            y2.append(row['per_positive'])
                else:
                    y2.append(0)
            print y2,b
            plt2[j].plot(x1, y2, label = b)
        j=j+1
#plt1.xlabel('Months')
# naming the y axis
#plt1.ylabel('Positive percentage')

for ax in plt1.flat:
    ax.set(xlabel='Months', ylabel='per_positive')
    ax.legend()
    



    
   
# show a legend on the plot

 
# function to show the plot
plt.show()
