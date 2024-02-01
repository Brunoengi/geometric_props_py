<h1>Propriedades Geométricas</h1>

<p>Esta documentação tem o objetivo de contextualizar com relação ao projeto  <i>geometric_props_py</i> e está disponível tanto em inglês (en) quanto português-Brasil (pt-br). Serão abordados os seguintes tópicos:</p>

<ol>
  <li>O que é / objetivo do projeto</li>
  <li>Introdução</li>
  <li>Como executar a aplicação</li>
  <li>Tecnologias Utilizadas</li>
  <li>Exemplos</li>
  <li>Licença de Uso</li>
  <li>Referências bibliográficas</li>
</ol>


<h2>1 - O que é / objetivo do projeto</h2>
<p>O projeto tem como objetivo calcular um conjunto de propriedades geométricas de figuras poligonais inseridas em um plano bidimensional. Nesse projeto, implementa-se uma classe utilizando a linguagem de programação python que abstrai a metodologia utilizada no teorema de green, que transforma integrais de superfície em integrais de linha ao longo de um contorno para assim, calcular as seguintes propriedades geométricas:</p>

Observação: As unidades disponibilizadas na tabela são válidas quando se insere as coordenadas da figura poligonal em centímetros (cm).

<table border="1">
  <thead>
  <th>Propriedades Geométricas</th>
  <th>Sigla</th>
  <th>Unidade</th>
  </thead>

  <tbody>
    <tr>
      <td>Área da seção</td>
      <td style="text-align: center;">A</td>
      <td style="text-align: center;">cm²</td>
    </tr>
    <tr>
      <td>Momento estático com relação ao eixo x</td>
      <td style="text-align: center;">S<sub>x</sub></td>
      <td style="text-align: center;">cm³</td>
    </tr>
    <tr>
      <td>Momento estático com relação ao eixo y</td>
      <td style="text-align: center;">S<sub>y</sub></td>
      <td style="text-align: center;">cm³</td>
    </tr>
    <tr>
      <td>Momento de inércia com relação ao eixo x</td>
      <td style="text-align: center;">I<sub>x</sub></td>
      <td style="text-align: center;">cm⁴</td>
    </tr>
    <tr>
      <td>Momento de inércia com relação ao eixo y</td>
      <td style="text-align: center;">I<sub>y</sub></td>
      <td style="text-align: center;">cm⁴</td>
    </tr>
    <tr>
      <td>Produto da inércia em relação aos eixos x e y</td>
      <td style="text-align: center;">I<sub>xy</sub></td>
      <td style="text-align: center;">cm⁴</td>
    </tr>
    <tr>
      <td>Centróide da seção em relação ao eixo x</td>
      <td style="text-align: center;">x<sub>g</sub></td>
      <td style="text-align: center;">cm</td>
    </tr>
    <tr>
      <td>Centróide da seção em relação ao eixo y</td>
      <td style="text-align: center;">y<sub>g</sub></td>
      <td style="text-align: center;">cm</td>
    </tr>
    <tr>
      <td>Momento de inércia baricêntrica (com relação ao centróide) no eixo x</td>
      <td style="text-align: center;">I<sub>xg</sub></td>
      <td style="text-align: center;">cm⁴</td>
    </tr>
    <tr>
      <td>Momento de inércia baricêntrica (com relação ao centróide) no eixo y</td>
      <td style="text-align: center;">I<sub>yg</sub></td>
      <td style="text-align: center;">cm⁴</td>
    </tr>
    <tr>
      <td>Distância vertical entre o centro de gravidade e o ponto mais baixo ao longo do eixo vertical</td>
      <td style="text-align: center;">Y<sub>1</sub></td>
      <td style="text-align: center;">cm</td>
    </tr>
    <tr>
      <td>Distância vertical entre o ponto mais alto ao longo do eixo vertical e o centro de gravidade</td>
      <td style="text-align: center;">Y<sub>2</sub></td>
      <td style="text-align: center;">cm</td>
    </tr>
    <tr>
      <td>Módulo resistente, calculado considerando Y<sub>1</sub></td>
      <td style="text-align: center;">W<sub>1</sub></td>
      <td style="text-align: center;">cm³</td>
    </tr>
    <tr>
      <td>Módulo resistente, calculado considerando Y<sub>2</sub></td>
      <td style="text-align: center;">W<sub>2</sub></td>
      <td style="text-align: center;">cm³</td>
    </tr>
    <tr>
      <td>Altura</td>
      <td style="text-align: center;">h</td>
      <td style="text-align: center;">cm</td>
    </tr>
  </tbody>
</table>

<br>

<p>Além disso, a aplicação permite também obter mais algumas informações relevantes, como:</p>

<table border="1">
  <thead>
  <th>Informação</th>
  <th>Sigla</th>
  <th>Unidade</th>
  </thead>

  <tbody>
    <tr>
      <td>Coordenada máxima com relação ao eixo x</td>
      <td>x<sub>max</sub></td>
      <td style="text-align: center;">cm</td>
    </tr>
    <tr>
      <td>Coordenada mínima com relação ao eixo x</td>
      <td>x<sub>min</sub></td>
      <td style="text-align: center;">cm</td>
    </tr>
    <tr>
      <td>Coordenada máxima com relação ao eixo y</td>
      <td>y<sub>max</sub></td>
      <td style="text-align: center;">cm</td>
    </tr>
    <tr>
      <td>Coordenada mínima com relação ao eixo y</td>
      <td>y<sub>min</sub></td>
      <td style="text-align: center;">cm</td>
    </tr>
  </tbody>
</table>

<h2>2 - Introdução</h2>

<p>A aplicação permite que se trabalhe com figuras vazadas, mas deve-se atentar aos seguintes cuidados, a inserção de uma seção se da a medida que os vértices são inseridos no sentido anti-horário, enquanto a remoção de uma seção se da a medida que seus vértices são inseridos no sentido horário.</p>

<p>No exemplo introdutório a seguir, deseja-se calcular as propriedades de uma figura com 4 vértices, essa figura não apresenta seção vazada (sua seção é maciça). Deve-se tomar cuidado com a ordem de inserção dos vértices. O primeiro ponto é marcado com o número 1, o segundo com o número 2 e assim por diante. Nota-se que é necessário reinserir o ponto inicial, de tal forma que a coordenadas do eixo x e y do primeiro ponto e do último ponto são as mesmas. Na imagem a seguir, é apresentado na esquerda uma imagem que indica a ordem correta de inserção dos pontos, já na direita temos um exemplo de um erro comum que é utilizar o sentido errado na inserção dos pontos.</p>

<img src='./images/correctMeaning.png' width=500>

<br>
<p>A seguir será apresentada uma figura em que sua seção é vazada, nesse caso, a ordem dos pontos será:</p>

<img src='./images/hollowSection.png' width=500>


<h2>3 - Como executar a aplicação</h2>

<p>O primeiro passo para executar a aplicação é realizar a importação da classe contida no arquivo <i>geometricProps.py</i>. Caso o projeto esteja na mesma pasta que o arquivo da classe, deve-se inserir:</p>

<code>from geometricProps import GeometricProps</code>

<p>A próxima etapa é criar uma instância da classe, nesse caso, é esperado no argumento umas lista de dicionário, cada dicionário deve contar a propriedade x, que faz referência a coordenada no eixo x, e deve conter também a propriedade y, que faz referência a coordenada no eixo y. Cada vértice da figura está estritamente relacionado a uma posição da lista, em que dentro está contido um dicionário que necessita possição do vértice em relação ao eixo x e em relação ao eixo y. Ao instanciar a classe, a seguinte estrutura deve ser fornecida:</p>

No caso a seguir queremos representar uma figura retangular com base de 20cm e altura de 60cm, em que a quina inferior esquerda está situada nas coordenadas (0,0). A tabela e a figura a seguir, representam a situação em questão:

  <table border="1">
    <thead>
    <th>Ponto</th>
    <th>Coordenada no eixo x (cm)</th>
    <th>Coordenada no eixo y (cm)</th>
    </thead>
    <tbody>
      <tr>
        <td style="text-align: center;">1</td>
        <td style="text-align: center;">0</td>
        <td style="text-align: center;">0</td>
      </tr>
      <tr>
        <td style="text-align: center;">2</td>
        <td style="text-align: center;">20</td>
        <td style="text-align: center;">0</td>
      </tr>
      <tr>
        <td style="text-align: center;">3</td>
        <td style="text-align: center;">20</td>
        <td style="text-align: center;">60</td>
      </tr>
      <tr>
        <td style="text-align: center;">4</td>
        <td style="text-align: center;">0</td>
        <td style="text-align: center;">60</td>
      </tr>
      <tr>
        <td style="text-align: center;">5</td>
        <td style="text-align: center;">0</td>
        <td style="text-align: center;">0</td>
      </tr>
    </tbody>
  </table>

<br>

<p>A imagem ilustrativa que representa a situação descrita na tabela é apresentada a seguir:</p>

  <img src='./images/01_retangular.png' height=300>


<br>

<code>retangulo = GeometricProps(
  <br>
    [<br>
        {'x':0, 'y':0}, ##Ponto 1<br>
        {'x':20, 'y':0}, ##Ponto 2<br>
        {'x':20, 'y':60}, ##Ponto 3<br>
        {'x':0, 'y':60}, ##Ponto 4<br>
        {'x':0, 'y':0}, ##Ponto 5<br>
    ])
</code>
  


