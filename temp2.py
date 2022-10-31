from sxl import Workbook
import sys,threading 
from data_structure import *
import json 

def Read_file():
    wb = Workbook("bulksheet.xlsx") #initialize   workbook class
    ws = wb.sheets['Sponsored Products Campaigns'] #initialize sheet class
    
    # ----- Sample for 1 camp ------
    camp1 = Campaign()
    location = "B57:AT68"
    for r in ws.range(location):
            pack = []
            if "Campaign" == r[0]:
                pack.extend([r[2],r[8],r[15],r[16],r[19],r[29]])
                camp1.set_data(pack,r[34:])  
                print(pack)  
            #print(r)
            elif "Bidding Adjustment" == r[0]:
                pack.extend([r[30],r[31]])
                temp = Bidding_adjustment()
                temp.set_data(pack,r[34:])
                camp1.bid_adjust.append(temp)  
                print(pack)  
            elif "Ad Group" == r[0]:
                pack.extend([r[3],r[10],r[17],r[24]])
                temp = Ad_group()
                temp.set_data(pack,r[34:])
                camp1.ad_group.append(temp)  
                print(pack)  
            elif "Product Ad" == r[0]:
                pack.extend([r[5],r[20],r[21],r[22]])
                temp = Product_Ad()
                temp.set_data(pack,r[34:])
                camp1.product_ad.append(temp)  
                print(pack)  
            elif "Product Targeting" == r[0]:
                pack.extend([r[7],r[16],r[26],r[32],r[33]])
                temp = Product_targeting()
                temp.set_data(pack,r[34:])
                camp1.product_targeting.append(temp)  
                print(pack) 
            elif "Keyword" == r[0]:
                pack.extend([r[6],r[27],r[28],r[25],r[26]])
                temp = Keyword()
                temp.set_data(pack,r[34:])
                camp1.keyword = temp  
                print(pack)  
            
    return camp1
            #print(r)
    #camp1.show_data()
    #-------------------------------
    '''
    wb = Workbook("bulksheet.xlsx") #initialize   workbook class
    ws = wb.sheets['Sponsored Products Campaigns'] #initialize sheet class
    print(ws.rows[3])
    init = 0
    for row in ws.rows:
        print("\nROW:",init)
        for cell in row:
            if cell == "":
                    print("hehe",type(cell),end="\t")
                    continue
            print(cell,type(cell),end="\t")   
        if init==2:
            break
        init += 1
    '''

def analyze(camp):
    camp.show_data()
    warning = []
    #---------- Read json -----------
    file = open("config.json",'r')
    data = json.load(file)
    for i in data:
        print(i)
    print("================================")
    pack = data[0]  # profit margin percent & breakeven point
    pack2 = data[1]  # keyword analyzing for auto campaign 
    pack3 = data[2] # campaign's metric warning

    #---------- Analyze from campaigns' metrics --------
    if camp.data.CTR < float(pack3['ctr'][0]):
        warning.append("Poor listing or target wrong keyword lead to low CTR")
        pass
    elif camp.data.CTR > float(pack3['ctr'][1]):
        if camp.data.CR < float(pack3['cr'][0]):
            warning.append("Buyers go to next page , need to check listing ")
    if camp.data.impression < float(pack3['impression'][0]):
        warning.append("Low impression, need more data")                                                   
    #---------- Analyze auto campaigns' keyword --------
    if camp.type == "AUTO":
        if len(camp.keyword) > 1:
            for kw in camp.keyword:
                if kw.data.ACOS < pack['pmp']:
                    pass

    #---------- Pass Warning -------------
    print("Warning !")
    for w in warning:
        print(w)
        

if __name__ =="__main__":
    threading.Thread(target = analyze(Read_file())).start()








