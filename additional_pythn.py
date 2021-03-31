newfile = open("Newfile.txt", "w+")
string = "we are going to talking about a form of data persistance."
#    i.e. we want to open, read and writes files in python without even  importing anything.
# for read only('r')
# for write only ('w')
# for read and write('r+')
# for write and read('w+')
# for write only('w')
# for append only('a')
# for append and read('a+')
newfile.write(string)
