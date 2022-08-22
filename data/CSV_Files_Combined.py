import pandas
import csv   


sg2=""
sg5=""
count5=0
df = pandas.read_csv('daily_sales_data_0.csv')   

with open('daily_sales_data_1_2_3_combined.csv', 'w',newline='') as csvfile:    
    fieldnames = ['Sales', 'Date', 'Region']    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  

    writer.writeheader()    
    print("Wait the file is being processed")
    for x in range(len(df.index)):

        if df.loc[x][0]=="pink morsel":
              
              sg2 = df.loc[x][1];
              floa5= float(sg2[1:])

              writer.writerow({'Sales':"$"+str((floa5*(df.loc[x][2]))),'Date': df.loc[x][3],'Region': df.loc[x][4]})
        if(x==(len(df.index)-1)):
            count5=count5+1
            df = pandas.read_csv('daily_sales_data_1.csv')
            for x in range(len(df.index)):
                if df.loc[x][0]=="pink morsel":
                    sg2 = df.loc[x][1];
                    floa5= float(sg2[1:])
                    writer.writerow({'Sales':"$"+str((floa5*(df.loc[x][2]))),'Date': df.loc[x][3],'Region': df.loc[x][4]})
        if(count5==1):
            df = pandas.read_csv('daily_sales_data_2.csv')
            for x in range(len(df.index)):
                if df.loc[x][0]=="pink morsel":
                    sg2 = df.loc[x][1];
                    floa5= float(sg2[1:])
                    writer.writerow({'Sales':"$"+str((floa5*(df.loc[x][2]))),'Date': df.loc[x][3],'Region': df.loc[x][4]})
            print("Task is completed")

            
              





                  
                  
                 
              

    



   
