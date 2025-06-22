<div align="center">
  <p>
    <h1>Template Builder</h1>
      <p>
        Ferramenta para preenchimento semiautomático dos cabeçalhos da caderneta de campo compilada para a disciplina de Mapeamento Geológico do curso de graduação em Geologia da UFSC.
      </p>
      <a href="https://github.com/FrostPredator/template-builder/releases/latest"><img alt="Static Badge" src="https://img.shields.io/badge/Download%20-%20Vers%C3%A3o%20mais%20recente%20-%20%231082c3"></a>
      <img alt="Static Badge" src="https://img.shields.io/github/downloads/FrostPredator/template-builder/total">
      <br>
      <br>
      <img src="https://github.com/user-attachments/assets/a4107126-c9ca-482d-9aec-c73a10c52faa" width="700">
  </p>
</div>

## Guia de uso para Coordenadores de Disciplina

### 1. Configurando as listas de opções

Em construção...

## Guia de uso para Alunos de Mapeamento

### 1. Preenchendo a tabela
A tabela deve ser preenchida diretamente a partir dos dados da caderneta de campo. Cada linha inserida na tabela corresponde a um ponto de campo. Siga as instruções de preenchimento abaixo para cada coluna.

> [!IMPORTANT]
> **NÃO insira ou exclua colunas manualmente.**
>
> **NÃO edite os nomes das colunas.**
>
> **NÃO troque a ordem das colunas.**
>
> Você **pode** utilizar acentos, cedilhas e caracteres especiais no preenchimento dos campos.
>
> **Salve a tabela usando os formatos .xlsx ou .xlsm.**

> [!NOTE]
> Para a geração do template da caderneta, é necessário apenas o preenchimento da aba "Geral" da planilha. As abas "Litologia", "Estruturas_planares" e "Estruturas lineares" podem ser preenchidas em etapas posteriores para a geração de um arquivo de pontos para uso em SIG.

> [!TIP]
> Evite colar dados de outras tabelas e softwares. **Quando colar quaisquer dados, utilize a colagem apenas de valores**. No Microsoft Office Excel, essa opção pode ser encontrada clicando com o botão direito do mouse na célula alvo da colagem, acessando a opção "Colar Especial..." e selecionando "Valores" (símbolo de prancheta com "123"). Isso impede que a formatação de validação dos dados seja substituída ao colar.

#### Aba "Geral"

Esta planilha apresenta os dados gerais e de localização do afloramento.

> [!NOTE]
> Os campos Tipo_de_afloramento, In_situ, Grau_de_intemperismo, Unidade_geologica_1 e 2, e Unidade_litoestratigrafica_1 e 2 devem ser preenchidos **apenas** nos pontos que contêm afloramento, e deixados em branco nos pontos de controle.

| **Campo**               | **Descrição** |
|-------------------------|--------------|
| **Ponto**               | O código do ponto de campo. Ex: "PTI-2001". Preencha na ordem de numeração. **Não deixe em branco**. |
| **Faixa**               | A área/faixa do projeto a qual o ponto pertence. **Não deixe em branco**. |
| **Fase**                | A disciplina ou fase do projeto na qual o ponto foi visitado pela primeira vez. Ex: "Mapeamento Geológico I" ou "Mapeamento Geológico II". Preencha apenas de forma contínua (na ordem das fases do projeto). **Não deixe em branco**. |
| **SRC**                 | O sistema de referência das coordenadas. Ex: "WGS 84 / UTM zone 22S". **Não deixe em branco**. |
| **Easting**             | A coordenada UTM leste (*easting*) do ponto, em metros. Insira apenas números. **Não deixe em branco**. |
| **Northing**            | A coordenada UTM norte (*northing*) do ponto, em metros. Insira apenas números. **Não deixe em branco**. |
| **Altitude**            | A altitude do ponto, em metros. Insira apenas números. |
| **UF**                  | A sigla da unidade da federação na qual o ponto está inserido. Ex: "SC". |
| **Municipio**           | O município no qual o ponto está inserido. Ex: "Botuverá". |
| **Toponimia**           | A toponímia do local ou um ponto de referência próximo ao ponto. Utilize apenas referências duradouras e que possam ajudar alguém que nunca esteve no local a encontrar o ponto no futuro. |
| **Data**                | A data da primeira visita ao ponto, no formato dia/mês/ano. Ex: "01/08/1997". **Não deixe em branco**. |
| **Equipe**              | Os nomes dos integrantes da equipe que visitou o ponto, incluindo professores, separados por vírgula e espaço. Utilize apenas o último sobrenome de cada integrante, e nenhum nome do meio. Ex: "Ana Sutili, Gabriel Maccari, Vicente Wetter, Luana Florisbal". **Não deixe em branco**. |
| **Ponto_de_controle**   | Se o ponto em questão é apenas um ponto de controle, ou se possui afloramento. Preencha com "Sim" ou "Não" (sem aspas, com acento, inicial maiúscula). Se o ponto possui afloramento e foi possível determinar a litologia, preencha com "Não". **Não deixe em branco**. |
| **Numero_de_amostras**  | O número de amostras coletadas no ponto. Preencha apenas com números inteiros. Preencha com zero caso nenhuma amostra tenha sido coletada. **Não deixe em branco**. |
| **Amostra_laminada**    | Se foram confeccionadas lâminas petrográficas a partir de amostras do afloramento. Preencha com "Sim" ou "Não" (sem aspas, com acento, inicial maiúscula). |
| **Tipo_de_afloramento**            | O tipo de afloramento presente no ponto em questão. Ex: "Corte de estrada", "Barranco", "Drenagem", etc. **Não preencha nos pontos de controle**. |
| **In_situ**                        | Se as rochas descritas no ponto encontravam-se in situ ou se foram transportadas de outro local (como no caso de matacões rolados morro abaixo ou seixos em uma drenagem). Preencha com "Sim" ou "Não" (sem aspas, com acento, inicial maiúscula). **Não preencha nos pontos de controle**. |
| **Grau_de_intemperismo**           | O grau de alteração do afloramento frente às intempéries. Preencha com "Baixo", "Médio" ou "Alto" (sem aspas, com acento, inicial maiúscula). **Não preencha nos pontos de controle**. |
| **Unidade_geologica_N**            | A unidade maior na qual a litologia principal(1)/secundária(2) do ponto está contida. O preenchimento deste campo deve ser feito conforme as unidades listadas na segunda aba da planilha. Ex: "Complexo Metamórfico Brusque", "Suíte Valsungana", "Coberturas Cenozoicas", etc. Caso o ponto em questão seja um ponto de contato entre duas unidades, acrescente na aba de Listas uma unidade mista, separada por "/" (Ex: "Grupo Itararé / Grupo Itajaí"), e então preencha o ponto com a unidade adicionada. **Não preencha nos pontos de controle**. |
| **Unidade_lito_N**   | A unidade litoestratigráfica/litodêmica na qual a litologia principal(1)/secundária(2) do ponto está contida. O preenchimento deste campo deve ser feito conforme as unidades litoestratigráficas/litodêmicas listadas na aba Listas. Ex: "Formação Rio Bonito", "Granodiorito Estaleiro", etc. **Não preencha nos pontos de controle**. |

#### Aba "Litologia"

Esta planilha apresenta dados litológicos das rochas encontradas no campo. Há espaço para descrição de duas litologias, que estão separadas pela numeração ao fim dos nomes das colunas (Ex: *Classe_de_rocha_1* e *Classe_de_rocha_2*). Caso sejam litologias de unidades distintas, elas devem estar descritas na mesma ordem que as suas respectivas unidades foram listadas na aba Geral.

> [!NOTE]
> Com exceção do código do ponto, os demais campos desta planilha devem ser preenchidos **apenas** nos pontos que contêm afloramento, e deixados em branco nos pontos de controle.

| **Campo**                       | **Descrição** |
|---------------------------------|--------------|
|**Ponto** | O código do ponto de campo. Ex: "PTI-2001". Preencha na ordem de numeração, e apenas com códigos já existentes na aba Geral. **Não deixe em branco**.
| **Classe_de_rocha_N**               | A classe de rocha na qual a litologia se encaixa. Preencha com "Ígnea", "Sedimentar", "Metamórfica" ou "Sedimentar inconsolidada". |
| **Cor_N**                           | A coloração geral observada na rocha. Ex: "Marrom avermelhada". |
| **Estrutura_N**                     | A estrutura observada na rocha. Quando for observada mais de uma estrutura, preencha todas elas separadas por vírgula e espaço, ordenando da mais importante para a menos importante. Ex: "Xistosidade, Bandamento gnáissico". |
| **Textura_N**                       | A textura observada na rocha. Quando for observada mais de uma textura, preencha todas elas separadas por vírgula e espaço, ordenando da mais importante para a menos importante. Ex: "Granoblástica, Lepidoblástica". |
| **Granulacao_N**                    | A granulometria dos minerais observados na rocha. Preencha com "Muito fina", "Fina", "Média", "Grossa", "Muito grossa" ou uma variação entre estas (Ex: "Fina a grossa"). |
| **Minerais_principais_N**           | As siglas dos principais minerais identificados na assembleia mineral da rocha, em ordem da maior para a menor abundância, separados por traço. Inicie as siglas de todos os minerais com letra maiúscula. Ex: "Qz-Kfs-Pl-Bt-Zr". |
| **Classificacao_litologia_N**       | A nomenclatura completa da rocha, incluindo sua mineralogia principal, nome raiz e outros apêndices necessários. Os minerais devem estar ordenados da menor para a maior abundância (minerais mais abundantes ficam mais próximos do nome raiz) e separados por traço. Minerais essenciais para a classificação devem ser omitidos (quartzo, feldspato alcalino e plagioclásio, por exemplo, não são listados na nomenclatura de um granito). Ex: "Bt-Ms sienogranito com apatita". |
| **Observacao_N**                    | Quaisquer outras informações importantes sobre a litologia em questão, até um máximo de 254 caracteres. |

#### Aba "Estruturas Planares"

Esta planilha apresenta dados de medidas de atitude de estruturas planares (Ex: Acamadamento sedimentar, foliação metamórfica, etc.), no formato sentido de mergulho/ângulo de mergulho (*dip direction*/*dip*).

Quando uma estrutura é preenchida nos espaços de estruturas planares da aba "Listas", dois campos aparecem aqui para a estrutura em questão, sendo um deles para o sentido de mergulho (*dip direction*) da estrutura e outro para o ângulo de mergulho (*dip*).

| **Campo**         | **Descrição**                                                                             |
|-------------------|-------------------------------------------------------------------------------------------|
| **Ponto**         | O ponto onde a medida foi realizada.                                                      |
| **Estrutura_std** | O sentido de mergulho medido para a estrutura. Preencha apenas com números entre 0 e 360. |
| **Estrutura_mgl** | O ângulo de mergulho medido para a estrutura. Preencha apenas com números entre 0 e 90.   |          

#### Aba "Estruturas Lineares"

Esta planilha apresenta dados de medidas de atitude de estruturas lineares (Ex: Lineação mineral, eixo de dobra, etc.), no formato ângulo de mergulho/sentido de mergulho (*dip*/*dip direction*)

| **Campo**         | **Descrição**                                                                             |
|-------------------|-------------------------------------------------------------------------------------------|
| **Ponto**         | O ponto onde a medida foi realizada.                                                      |
| **Estrutura_mgl** | O ângulo de mergulho medido para a estrutura. Preencha apenas com números entre 0 e 90.   | 
| **Estrutura_std** | O sentido de mergulho medido para a estrutura. Preencha apenas com números entre 0 e 360. |

> [!NOTE]
> Perceba que a ordem dos componentes das medidas é diferente para estruturas planares e lineares.

### 2. Gerando uma nova caderneta
- Execute o Template Builder (arquivo .exe).
- Clique no botão "Selecionar" e escolha a tabela preenchida nos passos anteriores.
A ferramenta irá analisar se os dados de cada coluna estão no formato correto e mostrará em sua interface. Colunas no formato correto terão o ícone ![ok](https://github.com/FrostPredator/template-builder/assets/114439033/86bfa387-320b-44e7-a71e-f8a474fd1ce2) ao lado enquanto colunas com problemas aparecerão com o ícone ![not_ok](https://github.com/FrostPredator/template-builder/assets/114439033/3e9c5ee1-99d1-4185-b1a9-4e4001d33f09):

<img src="https://github.com/user-attachments/assets/e08e013d-aca1-460c-9afc-d2fc378540f6" width="300">

Passar o mouse sobre o ícone revela que tipo de problema está presente na coluna. Também é possível clicar sobre os ícones vermelhos para ver detalhes sobre o problema identificado e em quais linhas, especificamente, ele ocorre:

<img src="https://github.com/user-attachments/assets/6a683beb-c0c8-4d2a-9074-c27b1694fa10" width="400">

A ferramenta apenas liberará a geração da caderneta quando todos os problemas na tabela forem resolvidos.</br>
Recomenda-se que seja utilizada apenas a tabela fornecida junto à ferramenta para o preenchimento. Utilizar tabelas em outros formatos irá impossibilitar ou limitar as funcionalidades da ferramenta.
- Com todas as colunas devidamente corrigidas, clique no botão "Gerar caderneta" para preencher o template com os dados da tabela. 
- Depois disso, em um editor de texto, basta adicionar as descrições dos afloramentos e amostras, assim como os painéis de croquis e fotos.

> [!TIP]
> Obs: Devido a diferenças de software, podem haver problemas de formatação caso a caderneta seja editada no Google Docs ou LibreOffice. Recomenda-se que seja utilizado o Microsoft Office Word ou, no caso de alternativas gratuitas, o ONLYOFFICE ou Softmaker FreeOffice. Para edição colaborativa, a versão online do Word pode ser usada gratuitamente.</sub>

### 3. Adicionando novos pontos a uma caderneta
Para adicionar novos pontos a uma caderneta gerada anteriormente (como quando é preciso adicionar pontos do Map2 à caderneta já preenchida do Map1):

- Execute o Template Builder (arquivo .exe).
- Clique no botão "Selecionar" e escolha a tabela preenchida com os novos pontos (você pode utilizar a tabela contendo todos os pontos, tanto do Map1 quanto do Map2).
- Verifique e corrija quaisquer problemas contidos nos dados da tabela e indicados na interface, conforme explicado na seção anterior.
- Desmarque a opção "Incluir folha de rosto no início da caderneta".
- Marque a opção "Continuar caderneta existente". Uma janela de seleção de arquivo surgirá, para que você selecione a caderneta (arquivo .docx) à qual deseja adicionar os novos pontos.
- Na caixa "Iniciar a partir do ponto", escolha o ponto de início dos dados novos.
- Clique em "Gerar caderneta", aguarde o processamento e escolha o local de salvamento do arquivo.

