import cv2 as cv 

def main ():
    events = [i for i in dir(cv)]
    #to print event 
    events = [i for i in dir (cv) if 'EVENT' in i]
    print (events)

main ()

