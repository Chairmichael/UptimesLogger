# logger.py


def main():
	for proc in psutil.process_iter():
		# print(proc.name(), proc.create_time())


if __name__ == '__main__':
	import datetime, os, psutil
	main()
