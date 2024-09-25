#Write a program that asks the user to enter parcel dimensions and computes nd prints the volume, followed by the postage cost.
#Lwazi Somtsewu

# 15 August 2024
l =float(input("Enter the length:\n"))
         

w =float(input("Enter the width:\n"))
h =float(input("Enter the height:\n"))
if 0<l and 0<w and 0<h:
    v = l*w*h 

    if 0<v<18:
        print(f"The volume is {v:.2f}.")
        print("Shipping cost is 14.65.")
    elif 18<=v<140:
        print(f"The volume is {v:.2f}.")
        print("Shipping cost is 5.95.") 
    elif 140<=v<440:
        print(f"The volume is {v:.2f}.")
        print("Shipping cost is 12.00.")  
    elif 440<=v<2648:
        print(f"The volume is {v:.2f}.")
        print("Shipping cost is 14.65.")    
    
    else :
        print(f"The volume is {v:.2f}.")
        print("Shipping cost is not available.")
        print("Package too large.")
        
else:
    print("Dimensions must be greater than zero.")

    