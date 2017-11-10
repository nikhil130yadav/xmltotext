import pandas as pd
extractedTextCsvDF = pd.DataFrame.from_csv("outCsv.csv")
tempdf = extractedTextCsvDF
exmfile = open("DataFramerows.txt","w",encoding="utf-8")
txtfile = open("sortedlined.txt", "w", encoding="utf-8")

writer = pd.ExcelWriter('xlsoutput.xlsx', engine='xlsxwriter')
 

def extractingLines(datafrme):
    pagegrup = datafrme.groupby('Page_No')
    for name,group in pagegrup:
        ##this create df from group object
        pagedatafrme = group.reset_index()
        y0AxisDF = pagedatafrme.sort_values(by=['y0'],ascending = [False])

        y0Axisgrup = y0AxisDF.groupby(['y0'], sort=False)
        for name,ygroup in y0Axisgrup:
            sorteXgrupDF = ygroup.reset_index()
            sorteXgrupDF = sorteXgrupDF.sort_values(by=['x0'],ascending=[True])
 
            tempY0=0
            tempx0 =0
            tempY1 = 0
            tempx1 = 0
            
            addingnewLIne =''
            for row in sorteXgrupDF.itertuples():
                print(row)
                
                if  tempY0 <= row[5]+5:
                    addingnewLIne = "\n" 
                print(pd.isnull(row[3]))


               # print(row.isnull())
                if  pd.isnull(row[3]):
                    if row[10] < 380 and addingnewLIne.count('\t\t\t')<1:
                        addingnewLIne = addingnewLIne +" \t\t\t" 
                else:
                    addingnewLIne = addingnewLIne +" "+row[3] 
            print(addingnewLIne)
            tempY0 = row[5]
            tempx0 = row[4]
            tempY1 = row[7]
            tempx1 = row[6]
            txtfile.write(addingnewLIne)

extractingLines(extractedTextCsvDF)


# Close the Pandas Excel writer and output the Excel file.



# yColumndata =extractedTextCsvDF['y0'].sort_values(['y0'],ascending =[False])
# print(yColumndata)

#sortedDF = extractedTextCsvDF.sort_values(['Page_No','x0','y0'])
#df.sort(['c1','c2'], ascending=[True,True,True])
#sortedDF.to_csv("sortedCsv.csv",sep=',',encoding = "utf-8")


#print("first extraction",ab)
a =extractedTextCsvDF.sort_values(by=['Page_No','x0','y1'], ascending=[True,  True,False])

a.to_csv("sortedCsv.csv",sep=',',encoding = "utf-8")
#extractedTextCsvDF.to_csv("sortedCsv.csv",sep=',', mode='w',encoding = "utf-8")
#print('sorted',a)
txtfile.close()
writer.save()
print("Done")


