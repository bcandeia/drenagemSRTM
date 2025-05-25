# drenagemSRTM

O ArcPy Package, é um pacote com funções Python próprias para análises de dados geográficos, conversão de dados, gerenciamento de dados e automação de mapas o qual pode ser acessado por scripts stand-alone.
Dentre as diversas funções presentes no ArcPy Package é possível combinar algumas para extrair redes de drenagens de imagens SRTM. Cada função possui uma finalidade específica:
- Fill (Preenchimento): preenche pequenas imperfeições nos dados;
- Flow direction (Direção de fluxo): define as direções de escoamento da água na bacia hidrográfica;
- Flow accumulation (fluxo acumulado): determina a matriz com acumulação de fluxos que evidencia o grau de confluência do escoamento;
- Con (avaliação condicional): que limita da hidrografia as drenagens de maior acumulação de água;
- Stream to feature (conversão de formato): transforma a rede de canais que está na forma de imagem em vetor.

Através deste processo o software ArcGIS não chega a ser executado pelo sistema, sendo necessário apenas a inserção das variáveis no código – conforme a área de estudo – e a execução do mesmo pelo prompt do Python ou IDLE para que os produtos sejam gerados.
 
A princípio o código importa o pacote ArcPy, desta forma pode-se usar as extensões e ferramentas oferecidas pelo ArcGIS. Em seguida, a extensão Spatial Analyst também é importada.
O próximo passo é a configuração da pasta onde serão armazenados os arquivos de saída e os arquivos de entrada – drenagem –, atribuída a variável wksp, e a declaração das variáveis a serem utilizadas no decorrer do código, através da concatenação da variável wksp e o nome do arquivo referente a variável. 
Após as configurações iniciais no código, são utilizadas as ferramentas padrões da toolbox Hydrology: fill, flow direction, flow accumulation, con – o qual teve sua expressão lógica Value > 150, no estudo em questão –, e stream do feature.

Referência:
CANDEIA, Bruna Araujo; SILVA, Nathália de Oliveira; VALDEVINO, Diego da Silva. Extração de redes de drenagem a partir de imagens SRTM com código stand-alone através do ArcPy Package. In: SIMPÓSIO BRASILEIRO DE SENSORIAMENTO REMOTO, 20., 2023, Florianópolis. Anais [...]. São José dos Campos: INPE, 2023. Disponível em:https://proceedings.science/sbsr-2023/papers/extracao-de-redes-de-drenagem-a-partir-de-imagens-srtm-com-codigo-stand-alone-at?lang=en. Acesso em: 25 maio 2025. proceesings.science.
