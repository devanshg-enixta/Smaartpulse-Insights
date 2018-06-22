import pandas as pd
read = pd.read_csv("eureka_forbes_reviews_8_1_18.csv")
product_id = read.source_product_id.unique()
out_source=[]
col=['source_product_id','flipkart','amazon_in','snapdeal']
for ids in product_id:
    rev = read[read.source_product_id==ids]
    s1 = rev[rev.source == 'flipkart']
    s3 = rev[rev.source == 'snapdeal']
    s2 = rev[rev.source == 'amazon_in']
    row = [ids,len(s1.index),len(s2.index),len(s3.index)]
#    row.append(df[['Communications','Business']].idxmax(axis=1))
    out_source.append(row)
out_source=pd.DataFrame(out_source)
out_source.columns = col
out_source['Highest'] = out_source[['flipkart','amazon_in','snapdeal']].idxmax(axis=1)
out_source.to_csv("source_counts.csv",index=False)
    
    

