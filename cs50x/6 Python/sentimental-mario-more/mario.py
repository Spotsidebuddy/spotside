
while True:
    try:
        h = int(input("Height: "))
    except ValueError:
        continue
    if h < 1 or h > 8:
        continue
    else:
        break

for i in range(h):
    print(f'{" "*(h-i-1)}{"#"*(i+1)}  {"#"*(i+1)}')

