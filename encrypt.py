print("Please only use A-Z Letters and spaces, thank you!")
string = input("Input your message here: ").lower()

string = string.replace("a", "OO")
string = string.replace("b", "OA")
string = string.replace("c", "OB")
string = string.replace("d", "OC")
string = string.replace("e", "OD")
string = string.replace("f", "OE")
string = string.replace("g", "OF")
string = string.replace("h", "OG")
string = string.replace("i", "OH")
string = string.replace("j", "OI")
string = string.replace("k", "OJ")
string = string.replace("l", "AO")
string = string.replace("m", "AA")
string = string.replace("n", "AB")
string = string.replace("o", "AC")
string = string.replace("p", "AD")
string = string.replace("q", "AE")
string = string.replace("r", "AF")
string = string.replace("s", "AG")
string = string.replace("t", "AH")
string = string.replace("u", "AI")
string = string.replace("v", "AJ")
string = string.replace("w", "BO")
string = string.replace("x", "BA")
string = string.replace("y", "BB")
string = string.replace("z", "BC")
string = string.replace(" ", "BD")

print(string)