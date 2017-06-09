from urllib.request import Request, urlopen

def Title():

    print(" _________________________________________ ")
    print("|                                         |")
    print("| PeDO (Powned Daemon Oriented)           |")
    print("|_________________________________________|")
    print("\n")

def PreCheck():
    counts = open("counts.txt","r")
    owneds = counts.readlines()
    counts.close()
    for owned in owneds:
        owned = owned.strip("\n")
        ownedslist.append(owned)
    
def Check():

    print ("Analyzing your accounts...\n")
    for count in ownedslist:
        try:
            result = Request("https://haveibeenpwned.com/api/breachedaccount/"+ count, headers={'User-Agent': 'Mozilla/5.0'})
            data = urlopen(result).read()
            print (count + " pass Leaked in:")
            print (data)
            print ("\n")
        
        except:
            print (count + " You are safe for now \n")

if __name__ == "__main__":
    
    ownedslist = []

    PreCheck()
    Title()
    Check()
    input ("Chek done")

