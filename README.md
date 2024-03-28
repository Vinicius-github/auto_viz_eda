# EDA de forma prática

Muitas vezes gastamos um tempo fazendo as análises prévias dos dados, para identificar quantidade de dados **missing**, **valores distintos**, **categorias** dentre outras análises iniciais para entender o banco de dados.
Visto isso, criei esses três algoritmos que mostram esses resultados de maneira rápida para um primeira exploração e entendimento do conjunto de dados.
Para isto, utilizei a base de dados do [Titanic](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)

## ydata
Neste [site](https://pypi.org/project/ydata-profiling/) você pode obter mais informações sobre esta biblioteca.

Abaixo algumas imagens resultante desta biblioteca:

![image](https://github.com/Vinicius-github/auto_viz_eda/assets/146575176/acdeb159-f51f-47da-b1a7-486578c79ee0)

## sweetviz
Neste [site](https://pypi.org/project/sweetviz/) você encontrará mais informações sobre esta biblioteca.

Esta biblioteca gera uma webpage com os dados a serem analisados. Caso queira, pode colocar uma variável como **target** que os resultados serão levados em consideração tendo em vista este target.

´´´
analyze_df = sweetviz.analyze([dataset, "df"], target_feat = 'Survived')
´´´

![image](https://github.com/Vinicius-github/auto_viz_eda/assets/146575176/faf42953-49fb-42b4-839a-dda3a88de90b)

## autoviz
Neste [site](https://pypi.org/project/autoviz/) você encontrará mais informações sobre esta biblioteca.

Da mesma forma que a biblioteca anterior pode setar a variável target, a biblioteca autoviz também permite fazer este procedimento.

![image](https://github.com/Vinicius-github/auto_viz_eda/assets/146575176/90b0ec69-1d75-44bb-b297-f167eeb66dcd)

