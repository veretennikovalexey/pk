text = 'Сусеки'

def fmt(x):
    s = str(x)
    if len(s) == 1:
        return f"{s:^3}"   # по центру
    elif len(s) == 2:
        return f"{s:>3}"   # по правому краю
    else:
        return s           # как есть (влезает ровно 3)
        
indexes_positive = "|".join(fmt(i) for i in range(len(text)))
symbols = "|".join(fmt(ch) for ch in text)
indexes_negative = "|".join(fmt(i) for i in range(-len(text), 0))

print("|" + indexes_positive + "|")
print("|" + symbols + "|")
print("|" + indexes_negative + "|")