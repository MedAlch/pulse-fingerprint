import requests
import sys
import re

generic_error_message = "Unknown error, please report the issue to my GitHub for assistance."

def check_args():
    if (len(sys.argv) > 2): 
        print("Too much arguments. This script only takes an adress of the form http(s)://domain.xx")
        sys.exit(-1)
    
    if (sys.argv[1] == "-h"): 
        print("Usage : " + sys.argv[0] + " http(s)://domain.xx")
        sys.exit(-2)

    try:
        a = requests.head(sys.argv[1]).status_code
    except:
        print("Unable to reach " + sys.argv[1] + " : check for typos or website availability.")
        sys.exit(-3)

def retrieve_last_patch_date(url):
    try:
        page_content = requests.get(url).text
        try:
            find_date_by_commentary(page_content)
        except:
            print("No date found in commentary, switching to HTML detection")
        try:
            find_date_by_div(page_content)
        except:
            print("No date found by HTML detection")
    except:
        print(generic_error_message)
        sys.exit(-5)

def find_date_by_commentary(text):
    x = re.search("(?<=Copyright \(c\))(.*)(?=by)", text)
    print("The following date was disclosed from a Copyright commentary :" + x.group())    

def find_date_by_div(text):
    x = re.search("(?<=Copyright &copy;)(.*)(?=Pulse Secure)", text)
    print("The following date was disclosed from HTML parts :" + x.group())

def main():
    
    check_args()
    url = sys.argv[1] + "/dana-na/"  

    try:
        if (requests.head(url).status_code == 404): 
            print("This website does not appear running any Pulse instance. If you believe this is a mistake, please open an issue on my Github.")
            sys.exit(-4)
        elif (requests.head(url).status_code == 400):
            print()
            print("Pulse instance found ! Retrieving date of last patch...")
            print()
            print("-------------------------------------------------------")
            retrieve_last_patch_date(url)
    except:
        print(generic_error_message)
                
    print("-------------------------------------------------------")
    print()
    print("Correlate your findings with the dates available on\nhttps://support.pulsesecure.net/ to identify the exact version.")
    sys.exit(0)

if __name__ == "__main__":
    main()
