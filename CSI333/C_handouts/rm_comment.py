
def edit(ok):
        
        final = open(ok,"w+")
        flash = final.read().splitlines()
        for i in flash:
            i  = i.split("/*")
            print(i)
            print(i[1])
            if i.find("*/") != -1:
                i = i.split(',')
                print(type(i[1]))
                print("\n")
	for j in flash:
		final.write(j)
		final.flush()
		final.write("\n")
                final.flush() 	         
        final.close()
        return 
def main():

     
        gisher = ""    
	gisher = input("edit which file")
 	edit(gisher)
                                        
           



main()