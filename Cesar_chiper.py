#Date:24/2/2024
#Author:Ammar Sayed Mansour Mohamed
#id:20230561
print("Welcome")
while True:
 message=str(input("enter a message : "))
 result = ""
 alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
 for char in message:
      if char =="z":
        next_char="a"
      elif char=="Z":
        next_char="A"
      else:
        if char in alpha:
            next_char = alpha[alpha.index(char)+1]
        else:
            next_char = char
      result += next_char
 print(result)