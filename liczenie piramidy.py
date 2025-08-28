blocks = int(input("Enter the number of blocks: "))

warstwa=1
wysokosc=0

while blocks >=warstwa:
    blocks-=warstwa
    wysokosc+=1
    warstwa+=1
    
# Write your code here.
#	

print("The height of the pyramid:", wysokosc)

