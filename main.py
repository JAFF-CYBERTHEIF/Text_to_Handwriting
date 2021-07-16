import pywhatkit
try:
    
    get=str(input("enter string to convert"))
    pywhatkit.text_to_handwriting(get,rgb=(0,0,255))
    print("done!!!")
    print("check the folder")

except:
    print("unexpected error")
