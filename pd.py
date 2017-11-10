import pandas as pd
import csv
import xml.etree.ElementTree as ET
tree = ET.parse('PDFtestOUTPUT.xml')
root = tree.getroot()

exmfile = open("extracted text.txt","w",encoding="utf-8")
newlineexmfile = open("newlin text.txt","w",encoding="utf-8")
outcsv  = open("outCsv.csv","w",encoding="utf-8")  
fieldnames = ['S.No','Text', 'x0','y0','x1','y1','Page_No','height','width']
csvwriter = csv.DictWriter(outcsv, fieldnames=fieldnames)   
csvwriter.writeheader()
  
page_number =None 
row_number =1          
for item in root:
        #print(item.attrib)
        page_number = item.attrib['pageid']
        temp_x = 0
        temp_y = 0
        temp_text = ''
        print("Page Number",page_number)
        # if str(page_number) == '3':
        #     break
        childitem = list(item)
        for subElement in item:
            subelementIter = subElement.iter()
            for child in subelementIter:
                elementText = child.text
                
                if elementText is not None :
                #if elementText is not None :
                    

                    attributDic = child.attrib 
                    ''' 
                     code to make rows
                     '''
                    if int(float(attributDic['y0'])) == temp_y:
                        if temp_x <int(float(attributDic['x0'])):
                            #temp_text += elementText.strip()
                            temp_text += elementText
                            
                            print('nested if:',temp_text)
                            newlineexmfile.write("\n"+temp_text)
                        else:
                            temp_text = elementText.rstrip()+temp_text
                            newlineexmfile.write("\n"+temp_text)
                            print('nest else:',temp_text)   
                    else:
                       # temp_text = ''
                        temp_text2 = elementText.lstrip()
                        print('else:',temp_text2)  
                        newlineexmfile.write("\n"+temp_text2)    

                    x0 = int(float(attributDic['x0']))
                    y0 = int(float(attributDic['y0']))
                    x1 = int(float(attributDic['x1']))
                    y1 = int(float(attributDic['y1']))
                    height = int(float(attributDic['height']))
                    width = int(float(attributDic['width']))
                    temp_text =elementText.strip()
                    temp_y= y0 
                    temp_x =x0
                   # print("Data from Tag",elementText.strip(),'x0',attributDic['x0'],'y0',attributDic['y0'])
                    csvwriter.writerow({'S.No':row_number,'Text':elementText.strip(), 'x0':x0,'y0':y0,'x1':x1,'y1':y1,'Page_No':page_number,
                    'height':height,'width':width})
                    exmfile.write("\n"+elementText)
                    row_number +=1
               
         
exmfile.close()
outcsv.close()
##---taking a out a dataframe from csv file to perform actions
extractedTextCsvDF = pd.DataFrame.from_csv("outCsv.csv")

print(extractedTextCsvDF)
print("first extracgted------------------------------------------------------")
print(extractedTextCsvDF.loc[extractedTextCsvDF['Page_No'] == 1])

a =extractedTextCsvDF.sort_values(['x0','y0','Page_No','x1'], ascending=[True, False, True,False])
#a.to_csv("sortedCsv.csv",sep=',',encoding = "utf-8")

print('sorted',a)
print("Done")


