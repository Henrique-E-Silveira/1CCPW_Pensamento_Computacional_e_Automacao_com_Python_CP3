# %% [markdown]
# ## Pensamento Computacional e Automação com Python 

# %% [markdown]
# Uma escola está testando um sistema simples de monitoramento ambiental para identificar salas com possível risco de calor excessivo.
# 
# Você recebeu uma matriz em que cada linha representa uma sala e cada coluna representa a temperatura registrada em um horário diferente do dia.

# %%
temperaturas = [
    [28, 31, 34, 33], 
    [25, 27, 29, 28], 
    [32, 35, 36, 34], 
    [24, 26, 25, 27]
]

# %%
lista_media_salas = []
lista_maior_salas = [0,0,0]

# %%
for key, sala in enumerate(temperaturas):
    media_sala = 0
    lista_maior_salas.append(0)
    tamanho = len(sala)

    for temp in sala:
        
        media_sala += temp
        
        if temp >= 33:
            lista_maior_salas[key] +=1

    media_sala = media_sala/tamanho

    lista_media_salas.append(media_sala)

# %% [markdown]
# ### Resultado

# %%
maior_risco = lista_maior_salas[0]

# %%
for key, sala in enumerate(temperaturas):
    if lista_maior_salas[key] > maior_risco:
        maior_risco = lista_maior_salas[key]
    print('NÚMERO DA SALA: ', key+1)
    print('MÉDIA DE TEMPERATURA DA SALA: ', lista_media_salas[key])
    print('QUANTIDADE DE REGISTROS CRÍTICOS DA SALA: ', lista_maior_salas[key])

print('SALA COM MAIOR RISCO: ',maior_risco)





