import pandas as pd
import matplotlib.pyplot as plt
import random
out_t=pd.read_csv("1_task_12_months_review_brand_wise_lipsticks.csv")
lis= ['maybelline','loreal','lakme','mac','colorbar']
out_t = out_t[out_t['Brand_name'].isin(lis)]
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
                    y1.append(row['Total_Number_of_Reviews'])
        else:
            y1.append(0)
    plt.plot(x1, y1, label = b)
plt.xlabel('Months')
# naming the y axis
plt.ylabel('Total_Number_of_Reviews')
plt.legend()
# function to show the plot
plt.show()
