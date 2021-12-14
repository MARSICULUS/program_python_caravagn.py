nums = [i for i in range(1, 1001)]
string = 'Practice Problem to Drill List Comprhendions in your Heads.'

a = [i for i in nums if i % 8 == 0]
b = [i for i in nums if '6' in str(i)]
c = sum([1 for char in string if char == ' '])
parole = string.split(' ')#non serve dichiararla in realtà
d = [parola for parola in parole if len(parola) < 5]
e = {i:len(i) for i in parole}

gg = {n:n % 2 == 0 for n in nums}

print(a)
print(b)
print(c)
print(d)
print(e)
#dizionario con la chiave il numero e se è divisibile per 47
#print(gg)