# part. 1

urls = ["http://www.google.com/a.txt",
		"http://www.google.com.tw/a.txt",
		"http://www.google.com/download/c.jpg",
		"http://www.google.co.jp/a.txt",
		"http://www.google.com/b.txt",
		"https://facebook.com/movie/b.txt",
		"http://yahoo.com/123/000/c.jpg",
		"http://gliacloud.com/haha.png",
		]

fnames = [str.split('/')[-1] for str in urls] 	# split url with '/' and obtain the file name in the url
fnames.sort()									# sort the file names in the ascending order
files = {fname: 0 for fname in fnames}			# create a dict to calculate the number of files.

for fname in fnames:
	files[fname] += 1
	
files = [[file, files[file]] for file in sorted(files, key=files.get, reverse=True)] # sort dict in the descending order

for i in range(3):
	print(files[i][0], files[i][1])