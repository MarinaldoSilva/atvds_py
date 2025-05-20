import pandas as pd

alunos = pd.DataFrame({
    "Nome": ["Mario", "Luigi", "Peach", "Toad", "Yoshi", "Bowser", "Wario", "Donkey Kong", "Daisy", "Rosalina"],
    "Idade": [25, 30, 28, 22, 26, 35, 32, 40, 29, 31],
})

ordenacao_nome = alunos.sort_values(by="Nome")
print(ordenacao_nome)
print("")
ordenacao_idade = alunos.sort_values(by="Idade", ascending=True)
print(ordenacao_idade)
print("")
print(alunos.sort_values(by=["Nome", "Idade"], ascending=[True, True]))
print("fim")
