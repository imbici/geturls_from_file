#-*- coding: utf-8 -*-
import re,sys,urllib2,urllib,os

#url = ''
#urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url)
def report(blocknr, blocksize, size):
	current = blocknr*blocksize
	sys.stdout.write("\r{0:.2f}%".format(100.0*current/size))

def downloadFile(url):
	print "\n",url
	#fname = url.split('/')[-1]
	#fname = url.split('?')[0]
	fname = os.path.basename(url)
	fname = fname.split('?')[0]
	fname = urllib.unquote(urllib.unquote(fname))
	fname = "./downlaod/"+fname
	print fname 
	urllib.urlretrieve(url, fname, report)

def main():
	argvfile = sys.argv[1]
	argvfile_output = argvfile+"_url_list.txt"
	readFile = open(argvfile)
	writeFile = open(argvfile_output, 'w+')
	os.makedirs('./downlaod')
	while True:
		line = readFile.readline()
		if not line: break
		#print(line)
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
		print urls
		url_str = str(urls).replace("'","").replace("[","").replace("]","\n")
		if url_str != "\n" :
			writeFile.write(url_str)
			downloadFile(url_str)			
	writeFile.close()
	readFile.close()


if __name__ == "__main__":
	main()