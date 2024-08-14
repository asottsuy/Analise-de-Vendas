#importando a bibliotecas
import os #lê os arquivos
import pandas as pd #cria as tabelas
import plotly.express as px #faz os graficos

lista_arquivo = os.listdir("C:/Users/asota/OneDrive/Área de Trabalho/Projeto Prático/Vendas") #percorrendo o arquivo de vendas

#print(lista_arquivo)

tabela_total = pd.DataFrame() #criando uma biblioteca vazia em formato de tabela(coluna e linhas)

for arquivo in lista_arquivo: #looping para percorrer nos arquivos
    if "Vendas" in arquivo: #caso tenha a palavara "Vendas" irá passar do if
        tabela = pd.read_csv(f"C:/Users/asota/OneDrive/Área de Trabalho/Projeto Prático/Vendas/{arquivo}") # o metodo pd.read_csv está lendo o arquivo csv e atribuindo para a tabela
        tabela_total = pd.concat([tabela_total, tabela], ignore_index=True) #o metodo concat funciona como um append mais funcional, ele combina dois DataFrames em um único.
print(tabela_total)

#agrupar os produtos, aprecendo um item por vez.
#agrupando pela quantidade vendida em ordem crescente
tabela_produtos = tabela_total.groupby('Produto').sum()#agrupamento por grupo e somando-os
tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by="Quantidade Vendida", ascending=False) #filtra as colunas desejadas // Ordena a coluna em ordem crescente
print(tabela_produtos)

#calculando o produto que mais faturou
#criando coluna
tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]
tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by="Faturamento", ascending=False)
print(tabela_faturamento)

#tabela lojas que mais faturou
tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']].sort_values(by="Faturamento", ascending=False)
print(tabela_lojas)

#Quando o groupby() é chamado, ele por padrao torna o primeiro argumento como o índice da tabela, por isso a primeira coluna fica diferente
#Portanto, quando for atribuir o valor de "x" no plotly(biblioteca de graficos), é preciso escrever a tabela.index 

#criando gráficos visuais
grafico = px.bar(tabela_lojas, x=tabela_lojas.index ,y="Faturamento") #px.bar() = grafico de barras
grafico.show()

