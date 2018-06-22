import pandas as pd
import matplotlib.pyplot as plt
import random
out_t=pd.read_csv("2_positive_percentage_fragmentswise_for_last_year_lipsticks.csv")
lis= ['maybelline','loreal','lakme','mac','colorbar']
out_t = out_t[out_t['Brand_name'].isin(lis)]
x1 = list(out_t.Month.unique())
br  = out_t.Brand_name.unique()
y1=[]
y2=[]

colors = ['#624ea7', 'g', 'yellow', 'k', 'maroon']
i=0
f , plt1 = plt.subplots(4,1)
plt2 = plt1.flatten()
j=0
n=4
for b1 in br:
    if b1 not in  'loreal':
        b2 = ['loreal',b1]
        for b in b2:
            #print b
            rev = out_t[out_t.Brand_name == b]

            x2 = list(rev.Month.unique())
            y2=[]
            for i in range(1,13):
                if i in x2:
                    for row in rev.to_dict("records"):
                        if row['Month'] == i:
                            y2.append(row['positive'])
                else:
                    y2.append(0)
            print y2,b
            plt2[j].plot(x1, y2, label = b)
        j=j+1
#plt1.xlabel('Months')
# naming the y axis
#plt1.ylabel('Positive percentage')

for ax in plt1.flat:
    ax.set(xlabel='Months', ylabel='%pos')
    ax.legend()
    



    
   
# show a legend on the plot

 
# function to show the plot
plt.show()
