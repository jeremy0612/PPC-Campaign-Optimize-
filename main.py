import sys,threading 
from data_structure import *
from queue import Queue
from get_data import Read_file
from analyze_data import *

threading.stack_size(2**27)  # new thread will get stack of such size

campaign_queue = Queue(maxsize = 100)

def read_file():
	Read_file("",campaign_queue)

def analyze():
	Analyze(campaign_queue)
	

if __name__ == "__main__":
	thread1 = threading.Thread(target = read_file)
	thread2 = threading.Thread(target = analyze)
	thread1.start()
	thread2.start()
	thread1.join()
	thread2.join()
	

