import json
import sqlite3
import sqlalchemy

    
class BuscaPalavrasChave:
    def __init__(self, texto):
        self.texto = texto.lower()  # Convertendo o texto para minúsculas para busca case-insensitive

    def buscar_palavra(self, palavra):
        palavra = palavra.lower()
        return palavra in self.texto

    def buscar_palavras(self, palavras):
        palavras = [palavra.lower() for palavra in palavras]
        resultados = {}
        for palavra in palavras:
            resultados[palavra] = palavra in self.texto
        return resultados

#transformar a variavel 'texto' pra buscar do bd
texto = "Quero saber de estagio e quando tem"
busca = BuscaPalavrasChave(texto)

palavra_chave = "estagios"
existe_palavra = busca.buscar_palavra(palavra_chave)
print(f"A palavra '{palavra_chave}' existe no texto: {existe_palavra}")

palavras_chave_lista = ["estagio", "bolsa", "bolsas"]
resultados_busca = busca.buscar_palavras(palavras_chave_lista)
for palavra, existe in resultados_busca.items():
    print(f"A palavra '{palavra}' existe no texto: {existe}")