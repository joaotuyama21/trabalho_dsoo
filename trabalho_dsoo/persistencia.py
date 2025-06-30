import pickle
import os

def salvar(objeto, nome_arquivo):
    with open(nome_arquivo, 'wb') as f:
        pickle.dump(objeto, f)

def carregar(nome_arquivo):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'rb') as f:
            return pickle.load(f)
    return []
