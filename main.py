#read it
#Brayden Woodard
#12/20

#Opening and closing the file
##file = open("file location","permission")
#C:\Users\brayden.woodard\Desktop\read_write\assets\saved_data\readme.txt
print("opening file")

file = open("assets/saved_data/gamelist.txt","w")
games = ["wow","wow","wow","wow","wow","wow","wow","wow","wow","wow"]
for i in range (len(games)):
    file.write(str(i+1) + " " + str(games[i]) + "\n")
file.close()

file = open("assets/saved_data/gamelist.txt","r")
text = file.readline()
if "wow" in text:
    print("pass")
else:
    print("big f not a real gamer")
print(text) 
##text = file.readline()
##print(text)
##
##file.seek(0)
##print(text)
##text = file.readline()
##print(text)
##
##while text:
##    text = file.read(1)
##    print(text, end = " ")
file.close()

