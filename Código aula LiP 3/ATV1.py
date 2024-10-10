temperaruraF = float(input())
caracterEscala = input()

temperaruraConvertida = 0

if "c" in caracterEscala or "C" in caracterEscala:
    temperaruraConvertida = (temperaruraF - 32)/1.8
    caracterEscala = "C"

elif "k" in caracterEscala or "K" in caracterEscala:
    temperaruraConvertida = (temperaruraF - 32)*(5/9) + 273.15
    caracterEscala = "K"

print(f"{temperaruraF}F equivale a {temperaruraConvertida:.2f}{caracterEscala}")