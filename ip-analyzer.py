print("===IP ADDRESS ANALYZER ===")
ip = input("Enter an IP address:")

parts = ip.split(".")

if len(parts) !=4:
    print("Invalid IP address")
else:
    valid = True
    for part in parts:
        if not part.isdigit():
            valid = False
            break
    
        number = int(part)

        if number < 0 or number > 255:
            valid = False
            break

if valid:
    print("Valid IPv4 Address")
    first = int(parts[0])
    second = int(parts[1])
    #Private or public IP
    if first == 10:
        print("Private IP Address")

    elif first == 172 and (second >= 16 and second <= 31):
        print("Type: Private IP")
        
    elif first == 192 and second == 168:
        print("Type: Private IP")
    
    else:
        print("Type: public IP")

    #class check
    if 1 <= first <= 126:
        print("Class: A")
    
    elif 128 <= first <= 191:
        print("Class: B")

    elif 192 <= first <= 223:
        print("Class: C")

    elif 224 <= first <= 239:
        print("Class: D")
    
    else:
        print("Class: E")

else:
    print("Invalid IP Address")

print("\nAnalysis complete.")
