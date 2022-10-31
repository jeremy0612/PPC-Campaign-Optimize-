from pprint import pprint

class Data:
	def __init__(self):
		self.impression = None
		self.clicks = None
		self.CTR = None
		self.spend = None
		self.sales = None
		self.orders = None
		self.units = None
		self.CR = None
		self.ACOS = None
		self.CPC = None
		self.ROAS = None
	def assign(self,pack):
		self.impression, self.clicks, self.CTR = [pack[i] for i in range(3)]
		self.spend, self.sales, self.orders = [pack[i] for i in (3,4,5)]
		self.units, self.CR, self.ACOS, self.CPC, self.ROAS = [pack[i] for i in (6,7,8,9,10)]
				

	def show_data(self):
		attrs = vars(self)
		print("\t",', '.join(" %s : %s " % item for item in attrs.items()))
		#for k,v in attrs.items():
		#	print(k,":",v)
		pass


class Keyword:
	def __init__(self):
		#--------- Properties
		self.keyword_id = None
		self.text = None
		self.match_type = None
		self.default_bid = None
		self.bid = None
		self.data = Data()
	#	-------- Setter for properties-----------
	def set_data(self,pack,pack2):
		self.keyword_id, self.text, self.match_type, self.default_bid, self.bid = [pack[i] for i in (0,1,2,3,4)]
		self.data.assign(pack2)


class Product_targeting:
	def __init__(self):
		self.ProductTarget_ID = None
		self.state = None
		self.bid = None
		self.ASIN = None
		self.rASIN = None
		self.data = Data()
	def set_data(self,pack,pack2):
		self.ProductTarget_ID, self.state, self.bid, self.ASIN, self.rASIN = [pack[i] for i in (0,1,2,3,4)]
		self.data.assign(pack2)
		pass

class Product_Ad:
	def __init__(self):
		#Porperties
		self.productAd_ID = None
		self.SKU = None
		self.ASIN = None
		self.eligibility = None
		#Metrics
		self.data = Data()
	def set_data(self,pack,pack2):
		self.productAd_ID, self.SKU, self.ASIN, self.eligibility = [pack[i] for i in (0,1,2,3)]
		self.data.assign(pack2)

class Ad_group:
	def __init__(self):
		# Properties
		self.adgroup_ID = None
		self.name = None
		self.state = None
		self.default_bid = None
		# Metrics
		self.data = Data()
	def set_data(self,pack,pack2):
		# Assign values of properties
		self.adgroup_ID = pack[0]
		self.name = pack[1]
		self.state = pack[2]
		self.default_bid = pack[3]
		# Assign values of Metrics
		self.data.assign(pack2)


class Bidding_adjustment:
	def __init__(self):
		# Properties
		self.placement = None
		self.Percentage = None
		#Metrics
		self.data = Data()
	def set_data(self,pack,pack2):
		self.placement, self.Percentage = pack[0],pack[1]
		# Assign values of Metrics
		self.data.assign(pack2)
class Campaign:
	def __init__(self):
		# Properties of campaign 
		self.campID = None
		self.type = None
		self.state = None
		self.daily_budget = None
		self.bidding_strategy = None
		self.name = None
		# Campaign containing components
		self.bid_adjust = []
		self.ad_group = []
		self.product_ad = []
		self.product_targeting = []
		self.keyword = []
		#Metrics
		self.data = Data()

	def set_data(self,pack,pack2):	 # Respective Order: campID, name, type, state,daily budget, bidding strategy 
		self.campID = pack[0]
		self.name = pack[1]
		self.type = pack[2]
		self.state = pack[3]
		self.daily_budget = pack[4]
		self.bidding_strategy = pack[5]
		# Assign values of Metrics
		self.data.assign(pack2)
	def show_data(self):
		# Properties of Campaign
		print("====================================")
		print("ID:",self.campID,"|","Name:",self.name)	 						
		print("Type:",self.type,"|","State:",self.state)	 						
		print("Daily budget:",self.daily_budget,"|","Bidding strategy:",self.bidding_strategy)	 						
		#------------ Bidding Adjustments ---------------
		for adjust in self.bid_adjust:
			print("Bidding adjustment:",adjust.placement,"|","percentage:",adjust.Percentage)	 						
			adjust.data.show_data()
			
		#--------- Ad Groups -----------
		for group in self.ad_group:
			# Show properties
			print("	AD Group ID:",group.adgroup_ID,"|","Name:",group.name)
			print("	State:",group.state,"|","Bid default:",group.default_bid)
			group.data.show_data()
		#--------- Product Ads-----------
		for group in self.product_ad:
			# Show properties
			print("	Product Ad ID:",group.productAd_ID,"|","ASIN:",group.ASIN)
			print("	SKU:",group.SKU,"|","Eligibility:",group.eligibility)
			group.data.show_data()			

		print("====================================")
		