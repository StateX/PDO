from urllib.request import Request, urlopen

def Title():

    print(" _________________________________________ ")
    print("|                                         |")
    print("| PeDO (Powned Daemon Oriented)           |")
    print("|_________________________________________|")
    print("")
    
def Check(count):
    try:
        result = Request("https://haveibeenpwned.com/api/breachedaccount/"+ count, headers={'User-Agent': 'Mozilla/5.0'})
        data = urlopen(result).read()
        print ("pass Leaked:")
        print (data)
        
    except:
        print ("You are safe for now")

if __name__ == "__main__":

    while True:
        Title()
        owned = input("Are you powned?> ")
        if owned == "exit":
            break
        else: 
            Check(owned)
        
