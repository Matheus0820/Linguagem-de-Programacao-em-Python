segIn = int(input())
dias = 0
horas = 0
min = 0
seg = 0 

dias = segIn//86400
horas = (segIn%86400)//3600
min = ((segIn%86400)%3600)//60
seg = ((segIn%86400)%3600)%60

print(f"{segIn} segundos = {dias} dias, {horas} horas, {min} minutos e {seg} segundos.")


# 1d = (1d*24)h = (1d*24h*60)min = (1d*24h*60min*60)seg
