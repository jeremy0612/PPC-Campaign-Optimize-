from sxl import Workbook
import sys,threading 
from data_structure import *
import json 
import time
import random

def Analyze(queue):
	while True:
		#print("thread2")
		camp = queue.get()
		if camp == "End":
			break
	    #camp.show_data()
		warning = []
		#---------- Read json -----------
		file = open("config.json",'r')
		data = json.load(file)
		#for i in data:
		    #print(i)
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
		print("Camp ID:",camp.campID)
		print("Warning !")
		for w in warning:
		    print(w)
		#if queue.empty() == True:
		#	Analyze(queue)    









