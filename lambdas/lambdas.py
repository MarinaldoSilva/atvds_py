numeros = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

dobro = list(map(lambda x: x * 2, numeros))
mod = list(filter(lambda x: x % 2 == 0, numeros))

alunos = [("Ana", 18), ("Bruno", 22), ("Carla", 20), ("Daniel", 19), ("Eduardo", 21), ("Fernanda", 23), ("Gustavo", 24), ("Heloisa", 25), ("Igor", 26), ("Juliana", 27), ("Karina", 28), ("Lucas", 29), ("Mariana", 30), ("Nicolas", 31), ("Olivia", 32), ("Paulo", 33), ("Quiteria", 34), ("Rafael", 35), ("Sofia", 36), ("Tiago", 37), ("Ursula", 38), ("Vinicius", 39), ("Wesley", 40), ("Xuxa", 41), ("Yasmin", 42), ("Zoe", 43), ("Aline", 44), ("Brenda", 45), ("Carlos", 46), ("Diana", 47), ("Eliane", 48), ("Fabio", 49), ("Gabriela", 50), ("Henrique", 51), ("Isadora", 52), ("Joao", 53), ("Karla", 54), ("Luan", 55), ("Marcio", 56), ("Natasha", 57), ("Otavio", 58), ("Patricia", 59), ("Quiteria", 60), ("Ricardo", 61), ("Simone", 62), ("Tatiane", 63), ("Ulisses", 64), ("Vera", 65)] 

sorteds = sorted(alunos, key = lambda x : x[0])
print(mod)
print("")
print(dobro)
print("")
print(f"{sorteds}\n")
print("")