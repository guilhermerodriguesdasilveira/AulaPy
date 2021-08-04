import pandas as pd
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data' 

nome_var = ['comprimento_sepala', 'largura_sepala', 'comprimento_petala', 'largura_petala', 'especie']
iris = pd.read_csv(url, header=None, names=nome_var)

amostraVersicolor = (iris[iris['especie']=='Iris-versicolor'].sample(n=10, random_state=1))
amostraSetosa = (iris[iris['especie']=='Iris-setosa'].sample(n=10, random_state=1))
amostraVirginica = (iris[iris['especie']=='Iris-virginica'].sample(n=10, random_state=1))

conjuntoteste = pd.concat([amostraVersicolor,amostraSetosa,amostraVirginica])
conjuntotreinamento = iris.drop(conjuntoteste.index)
classesVerdadeiras = conjuntoteste['especie'].tolist()

# O seu código entra aqui
# Devemos obter um vetor de resposta chamado respostaArvore


respostaArvore=conjuntoteste['especie'].values
#aqui meu comentario


errosArvore = 0

for i in range(len(conjuntoteste.index)):
  if classesVerdadeiras[i]!=respostaArvore[i]:
    errosArvore += 1

taxaErrosArvore = errosArvore/len(conjuntoteste.index)

## Verificando o desempenho do classificador
print('Árvores de Decisão: Taxa de erro: ' + '%.2f' %(taxaErrosArvore*100)+'% ou Acurácia de: ' + '%.2f' %((1-taxaErrosArvore)*100)+'%')






from sklearn.neighbors import KNeighborsClassifier
## Criando uma instância do classificador com k = 5
knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')

## Calculando as distâncias
knn.fit(conjuntotreinamento.drop(columns=['especie']), conjuntotreinamento['especie'])
respostaknnscikit = knn.predict(conjuntoteste.drop(columns=['especie'])).tolist()

## Calculando o desempenho
errosscikit = 0

for i in range(len(conjuntoteste.index)):
  if classesVerdadeiras[i]!=respostaknnscikit[i]:
    errosscikit += 1

taxaErroscikit = errosscikit/len(conjuntoteste.index)

## Verificando o desempenho do classificador
print('Exemplo Sklearn: Taxa de erro: ' + '%.2f' %(taxaErroscikit*100)+'% ou Acurácia de: ' + '%.2f' %((1-taxaErroscikit)*100)+'%')



