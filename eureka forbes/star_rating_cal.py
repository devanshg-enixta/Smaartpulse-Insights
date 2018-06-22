import pandas as pd
read = pd.read_csv("eureka_forbes_reviews_8_1_18.csv")
product_id = read.source_product_id.unique()
col=['source_product_id','source','1star_count','2star_count','3star_count','4star_count','5star_count','total_count','average_5star','average_pct']
for ids in product_id:
    total = 0
    avg_5=0.0
    avg_pct=0.0 
    rev1 = read[read.source_product_id==ids]
    product_source= rev1.source.unique()
    for source in product_source:
        total = 0
        avg_5=0.0
        avg_pct=0.0 
        rev = rev1[rev1.source ==source]
        star_5 = rev[rev.star_rating == 5]
        star_4 = rev[rev.star_rating == 4]
        star_3 = rev[rev.star_rating == 3]
        star_2 = rev[rev.star_rating == 2]
        star_1 = rev[rev.star_rating == 1]
        total = len(star_1.index)+len(star_2.index)+len(star_3.index)+len(star_4.index)+len(star_5.index)
        if total > 0:
            avg_5= round(float((1*len(star_1.index)+2*len(star_2.index)+3*len(star_3.index)+4*len(star_4.index)+5*len(star_5.index))/float(total)),3)
            avg_pct = round(float((avg_5-1)*25),3)
            row = [ids,source,len(star_1.index),len(star_2.index),len(star_3.index),len(star_4.index),len(star_5.index),total,avg_5,avg_pct]
            out.append(row)
out=pd.DataFrame(out)
out.columns = col
out.to_csv("rating_test.csv",index=False)
    

    
    

