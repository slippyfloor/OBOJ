result = []

y = input("Input your encrypted string here: ").upper()

z = ["".join((v, g)) for v,g in zip(y[:-1:2], y[1::2])]

x = "/".join(z)

x = x.replace("OO", "a")
x = x.replace("OA", "b")
x = x.replace("OB", "c")
x = x.replace("OC", "d")
x = x.replace("OD", "e")
x = x.replace("OE", "f")
x = x.replace("OF", "g")
x = x.replace("OG", "h")
x = x.replace("OH", "i")
x = x.replace("OI", "j")
x = x.replace("OJ", "k")
x = x.replace("AO", "l")
x = x.replace("AA", "m")
x = x.replace("AB", "n")
x = x.replace("AC", "o")
x = x.replace("AD", "p")
x = x.replace("AE", "q")
x = x.replace("AF", "r")
x = x.replace("AG", "s")
x = x.replace("AH", "t")
x = x.replace("AI", "u")
x = x.replace("AJ", "v")
x = x.replace("BO", "w")
x = x.replace("BA", "x")
x = x.replace("BB", "y")
x = x.replace("BC", "z")
x = x.replace("BD", " ")

x = x.replace("/", "")

print(x)