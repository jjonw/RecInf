import os
import codecs

from bs4 import BeautifulSoup

def carregar_HTML(arquivo):
    """Carregar HTML e remover tags"""
    with open(arquivo, "rb") as arq:
        texto = arq.read()

    texto_bs = BeautifulSoup(texto, "html.parser")

    # Remove js scripts
    for script in texto_bs(["script", "style"]):
        script.decompose()
    
    texto = texto_bs.text
    # break into lines and remove leading and trailing space on each
    linhas = (linha.strip() for linha in texto.splitlines())
    # break multi-headlines into a line each
    pedacos = (frase.strip() for linha in linhas for frase in linha.split(" "))
    # drop blank lines
    texto = '\n'.join(pedaco for pedaco in pedacos if pedaco)

    #print(text)
    return texto.lower()


def remover_stopwords(palavras, arquivo_stopwords):
    """Remover Stopwords"""
    with codecs.open(arquivo_stopwords, "r", encoding="utf-8") as stopwords:
        sw = stopwords.read()
    
    stopwords_lista = sw.split()

    palavras_novo = [palavra for palavra in palavras 
                    if palavra not in stopwords_lista]

    return palavras_novo


def tokenize(texto, arquivo_stopwords):
    """Tokenização"""
    pontuacao = " .,-!#$%^&*();:\n\t\\\"|/?!\{\}[]<>+©"
    for i in range(0, len(texto)):
        for j in range(0, len(pontuacao)):
            if texto[i] == pontuacao[j]:
                texto = texto.replace(pontuacao[j], " ") 

    termos = remover_stopwords(texto.split(), arquivo_stopwords)

    return termos