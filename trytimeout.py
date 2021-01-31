"""
[0, 1, None, 3, 4, 5, 6, 7, None, 9, None, 11, None, 13, None, 15, None, 17, None, 19]
[0, 1, 3, 4, 5, 6, 7, 9, 11, 13, 15, 17, 19]
"""

import multiprocessing
from time import sleep

def f(x):
	sl = x if (-1)**x >0 else 1
	print("Start running with x={} and sleep={}".format(x,sl))
	sleep(sl)
	try:
		print("      running finished with x={} and sleep={}, result={}".format(x, sl, 1 / (x-2)))
		return x
	except Exception as e:
		print('\n\nCaught exception {} in worker thread (x = {:d}):'.format(e, x))
		return None

if __name__ == '__main__':
	with multiprocessing.Pool(2) as pool:
		async_results = [pool.apply_async(f, (i,)) for i in range(20)]
		results_collection=[]
		for async_res in async_results:
			try:
				this_res = async_res.get(timeout=5)
				results_collection.append(this_res)
			except Exception as e:
				print("Exception: {}".format(e))
				results_collection.append(None)
				pass
		print(results_collection)
		#Removing unsuccessful ones
		results_collection = [r for r in results_collection if r !=None]
		print(results_collection)
