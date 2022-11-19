from sxl import Workbook
import sys,threading 
from data_structure import *
import time
import random

threading.stack_size(2**27)  # new thread will get stack of such size

def Read_file(file_path,queue):
    if len(file_path) < 1:
        wb = Workbook("sheet/7days.xlsx") #initialize   workbook class
    else:
        wb = Workbook(file_path) #initialize   workbook class    
    ws = wb.sheets['Sponsored Products Campaigns'] #initialize sheet class
    print(ws.num_rows)
    #------- Group each campaign first row number to a list ------- 
    init = 1 
    camps = []
    for row in ws.rows:
        if "Campaign" == row[1]:
            camps.append(init)
        init += 1
    #print(camps)
    #------- Print out each camp in group-----------
    init = 1
    for i in range(len(camps)):
        #print("Camp number",init)
        try:
            location = "B" + str(camps[i]) + ":AT" + str(camps[i+1]-1)
        except:
            location = "B" + str(camps[i]) + ":AT" + str(ws.num_rows)
        camp = Campaign()
        for r in ws.range(location):
            pack = []
            if "Campaign" == r[0]:
                pack.extend([r[2],r[8],r[15],r[16],r[19],r[29]])
                camp.set_data(pack,r[34:])  
            elif "Bidding Adjustment" == r[0]:
                pack.extend([r[30],r[31]])
                temp = Bidding_adjustment()
                temp.set_data(pack,r[34:])
                camp.bid_adjust.append(temp)  
            elif "Ad Group" == r[0]:
                pack.extend([r[3],r[10],r[17],r[24]])
                temp = Ad_group()
                temp.set_data(pack,r[34:])
                camp.ad_group.append(temp)  
            elif "Product Ad" == r[0]:
                pack.extend([r[5],r[20],r[21],r[22]])
                temp = Product_Ad()
                temp.set_data(pack,r[34:])
                camp.product_ad.append(temp)  
            elif "Product Targeting" == r[0]:
                pack.extend([r[7],r[16],r[26],r[32],r[33]])
                temp = Product_targeting()
                temp.set_data(pack,r[34:])
                camp.product_targeting.append(temp)  
            elif "Keyword" == r[0]:
                pack.extend([r[6],r[27],r[28],r[25],r[26]])
                temp = Keyword()
                temp.set_data(pack,r[34:])
                camp.keyword.append(temp)  
        #camp.show_data()
        #print(queue.empty())
        #print(queue.full())
        #while queue.full() == True:
        #    time.sleep(random.random())
        queue.put(camp)
        init += 1
        if init == ws.num_rows:
            break
    queue.put("End")

def Read_file_2():
    wb = Workbook("bulksheet.xlsx") #initialize   workbook class
    ws = wb.sheets['Sponsored Products Campaigns'] #initialize sheet class
    #print(ws.rows[3])
    '''
    for x in ws.range("A21:D26"):
        print(x)
    for y in ws.rows[1][0]:
        print(y)
    '''
    print(ws.num_rows)
    
    #print out each camp in group
    init = 1
    for i in range(ws.num_rows):
        print(ws.rows[i])
        if "Campaign" == ws.rows[i]:
            print("Camp number",init)
            location = "A" + str(camps[i]) + ":D" + str(camps[i+1]-1)
            for r in ws.range(location):
                print(r)
            init += 1



if __name__ =="__main__":
    threading.Thread(target = Read_file).start()
#    threading.Thread(target = Read_file_2).start()
    