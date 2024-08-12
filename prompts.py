
gpt_chave = """Dada uma CONSULTA e uma PASSAGEM de texto, você deve fornecer uma PONTUAÇÃO 0 ou 1 com os seguintes significados:
1 = Relevante: a PASSAGEM é relevante à CONSULTA, pois responde parcial ou totalmente à CONSULTA.
0 = Irrelevante: a PASSAGEM não tem nada a ver com a CONSULTA.
Procedimento: Leia a CONSULTA. Depois leia a PASSAGEM e verifique se dentro dela existem trechos que podem responder à CONSULTA. Se existir alguma resposta à CONSULTA, mesmo que parcial, atribua PONTUAÇÃO 1. Se a PASSAGEM não tiver nenhuma relação com a CONSULTA, atribua a PONTUAÇÃO 0.
Você deve primeiramente fornecer a EXPLICAÇÃO do porquê você atribuiu a referida PONTUAÇÃO à PASSAGEM e depois adicionar a PONTUAÇÃO atribuída.
"""

gpt_llm4evalPT = """Dada uma CONSULTA e uma PASSAGEM de texto, você deve fornecer uma PONTUAÇAO em uma escala inteira de 0 a 3 com os seguintes significados:
3 = Perfeitamente relevante: a PASSAGEM responde totalmente à CONSULTA.
2 = Altamente relevante: a PASSAGEM contém alguma resposta para a CONSULTA, mas a resposta é parcial ou incompleta.
1 = Relacionado: a PASSAGEM parece relacionada à CONSULTA, mas não inclui nenhuma resposta à mesma.
0 = Irrelevante: a PASSAGEM não tem nada a ver com a CONSULTA.

Procedimento: Leia a CONSULTA. Depois leia a PASSAGEM e verifique se dentro dela existem trechos que podem responder à CONSULTA. Se existir uma resposta completa à CONSULTA atribua PONTUAÇÃO 3. Se existir uma resposta parcial atribua PONTUAÇÃO 2. Se a PASSAGEM parecer relacionada a CONSULTA, mas não contiver nenhuma resposta direta a mesma, atribua PONTUAÇÃO 1. Se a PASSAGEM não tiver nenhuma relação com a CONSULTA, atribua a PONTUAÇÃO 0.
Você deve primeiramente fornecer a EXPLICAÇÃO do porquê você atribuiu a referida PONTUAÇÃO à PASSAGEM e depois adicionar a PONTUAÇÃO atribuída conforme os exemplos a seguir.

CONSULTA: "qual o ser vivo com o maior genoma"
PASSAGEM: "Ao contrário do que se pensaria, os seres humanos não têm o maior genoma dentre os seres vivos. 
Pesquisadores apresentaram o ser vivo com o maior genoma do mundo em um estudo publicado no dia 31 de maio na revista iScience. Trata-se da planta Tmesipteris oblanceolata, que mede poucos centímetros de altura, mas contém mais de 100 metros de DNA — e possui 50 vezes mais material genético do que nós humanos."
EXPLICAÇÃO: "A passagem contém exatamente a resposta à consulta descrevendo o achado da planta Tmesipteris oblanceolata, que possui o maior genoma já encontrado."
PONTUAÇÃO: "3"

CONSULTA: "quais são os principais sintomas da diabetes tipo 2"
PASSAGEM: "A diabetes tipo 2 pode causar vários problemas de saúde, incluindo complicações cardiovasculares e neuropatia. Na grande maioria dos casos, o diabetes tipo 2 não ocasiona sintomas, mas sintomas aparecem quando o paciente está descompensado com níveis de glicose extremamente elevados no sangue." 
EXPLICAÇÃO: "Embora a passagem mencione problemas de saúde relacionados à diabetes tipo 2 e esclarece que na maioria dos casos não há sintomas, não lista explicitamente os sintomas nos casos mais graves. "
PONTUAÇÃO: "2"

CONSULTA: "como é a estrutura das áreas que compõem os jardins reais de Kew”
PASSAGEM: "Os Jardins Botânicos de Kew continuam a ser um dos centros de excelência na investigação botânica, um afamado centro de formação profissional em jardinagem e uma das principais atrações turísticas de Londres. Oferecem cursos de manejo de jardins botânicos.”
EXPLICAÇÃO: "Apesar da passagem falar sobre a importância dos Jardins Botânicos de Kew como centro de excelência, não menciona a estrutura das áreas que compõem os jardins."
PONTUAÇÃO: "1"

CONSULTA: "quais as principais causas do aquecimento global"
PASSAGEM: "Os jardins botânicos são na sua maioria geridos por universidades ou outras organizações de investigação científica, estando associados a programas de investigação em taxonomia ou outros aspectos de ciência botânica, para os quais contam com um herbário. Por princípio, o seu papel é a manutenção de coleções documentadas de plantas vivas"
EXPLICAÇÃO: "A passagem descreve questões relacionadas à gestão de jardins botânicos e não menciona nada sobre aquecimento global."
PONTUAÇÃO: "0"
"""

sabia_chave = """Dada uma CONSULTA e uma PASSAGEM de texto, você deve fornecer uma PONTUAÇÃO 0 ou 1 com os seguintes significados:
1 = Relevante: a PASSAGEM é relevante à CONSULTA, pois responde parcial ou totalmente à CONSULTA.
0 = Irrelevante: a PASSAGEM não tem nada a ver com a CONSULTA.
Procedimento: Leia a CONSULTA. Depois leia a PASSAGEM e verifique se dentro dela existem trechos que podem responder à CONSULTA. Se existir alguma resposta à CONSULTA, mesmo que parcial, atribua PONTUAÇÃO 1. Se a PASSAGEM não tiver nenhuma relação com a CONSULTA, atribua a PONTUAÇÃO 0.
Você deve primeiramente fornecer a PONTUAÇÃO e depois adicionar a EXPLICAÇÃO do porquê você atribuiu a referida PONTUAÇÃO à PASSAGEM, conforme os exemplos a seguir.

CONSULTA: "qual o ser vivo com o maior genoma"
PASSAGEM: "Ao contrário do que se pensaria, os seres humanos não têm o maior genoma dentre os seres vivos. Pesquisadores apresentaram o ser vivo com o maior genoma do mundo em um estudo publicado no dia 31 de maio na revista iScience. Trata-se da planta Tmesipteris oblanceolata, que mede poucos centímetros de altura, mas contém mais de 100 metros de DNA — e possui 50 vezes mais material genético do que nós humanos."
PONTUAÇÃO: "1"
EXPLICAÇÃO: "A passagem contém exatamente a resposta à consulta descrevendo o achado da planta Tmesipteris oblanceolata, que possui o maior genoma já encontrado."

CONSULTA: "como é a estrutura física das áreas que compõem os jardins reais de Kew”
PASSAGEM: "Os Jardins Botânicos de Kew continuam a ser um dos centros de excelência na investigação botânica, um afamado centro de formação profissional em jardinagem e uma das principais atrações turísticas de Londres. Oferecem cursos de manejo de jardins botânicos.”
PONTUAÇÃO: "0"
EXPLICAÇÃO: "Apesar da passagem ser sobre os Jardins Botânicos de Kew, não menciona nada da estrutura física das áreas que compõem os jardins."
"""


sabia_llm4evalPT = """Dada uma CONSULTA e uma PASSAGEM de texto, você deve fornecer uma PONTUAÇÃO em uma escala inteira de 0 a 3 com os seguintes significados:
3 = Perfeitamente relevante: a PASSAGEM responde totalmente à CONSULTA.
2 = Altamente relevante: a PASSAGEM contém alguma resposta para a CONSULTA, mas a resposta é parcial ou incompleta.
1 = Relacionado: a PASSAGEM parece relacionada à CONSULTA, mas não inclui nenhuma resposta à mesma.
0 = Irrelevante: a PASSAGEM não tem nada a ver com a CONSULTA.

Procedimento: Leia a CONSULTA. Depois leia a PASSAGEM e verifique se dentro dela existem trechos que podem responder à CONSULTA. Se existir uma resposta completa à CONSULTA atribua PONTUAÇÃO 3. Se existir uma resposta parcial atribua PONTUAÇÃO 2. Se a PASSAGEM parecer relacionada a CONSULTA, mas não contiver nenhuma resposta direta a mesma, atribua PONTUAÇÃO 1. Se a PASSAGEM não tiver nenhuma relação com a CONSULTA, atribua a PONTUAÇÃO 0.
Você deve primeiramente fornecer a PONTUAÇÃO e depois adicionar a EXPLICAÇÃO do porquê você atribuiu a referida PONTUAÇÃO à PASSAGEM. A seguir alguns exemplos.

CONSULTA: "qual o ser vivo com o maior genoma"
PASSAGEM: "Ao contrário do que se pensaria, os seres humanos não têm o maior genoma dentre os seres vivos. Pesquisadores apresentaram o ser vivo com o maior genoma do mundo em um estudo publicado no dia 31 de maio na revista iScience. Trata-se da planta Tmesipteris oblanceolata, que mede poucos centímetros de altura, mas contém mais de 100 metros de DNA — e possui 50 vezes mais material genético do que nós humanos."
PONTUAÇÃO: "3"
EXPLICAÇÃO: "A passagem contém exatamente a resposta à consulta descrevendo o achado da planta Tmesipteris oblanceolata, que possui o maior genoma já encontrado."

CONSULTA: "quais são os principais sintomas da diabetes tipo 2"
PASSAGEM: "A diabetes tipo 2 pode causar vários problemas de saúde, incluindo complicações cardiovasculares e neuropatia. Na grande maioria dos casos, o diabetes tipo 2 não ocasiona sintomas, mas sintomas aparecem quando o paciente está descompensado com níveis de glicose extremamente elevados no sangue."
PONTUAÇÃO: "2"
EXPLICAÇÃO: "Embora a passagem mencione problemas de saúde relacionados à diabetes tipo 2 e esclarece que na maioria dos casos não há sintomas, não lista explicitamente os sintomas nos casos mais graves. "

CONSULTA: "como é a estrutura das áreas que compõem os jardins reais de Kew”
PASSAGEM: "Os Jardins Botânicos de Kew continuam a ser um dos centros de excelência na investigação botânica, um afamado centro de formação profissional em jardinagem e uma das principais atrações turísticas de Londres. Oferecem cursos de manejo de jardins botânicos.”
PONTUAÇÃO: "1"
EXPLICAÇÃO: "Apesar da passagem falar sobre a importância dos Jardins Botânicos de Kew como centro de excelência, não menciona a estrutura das áreas que compõem os jardins."

CONSULTA: "quais as principais causas do aquecimento global"
PASSAGEM: "Os jardins botânicos são na sua maioria geridos por universidades ou outras organizações de investigação científica, estando associados a programas de investigação em taxonomia ou outros aspectos de ciência botânica, para os quais contam com um herbário. Por princípio, o seu papel é a manutenção de coleções documentadas de plantas vivas"
PONTUAÇÃO: "0"
EXPLICAÇÃO: "A passagem descreve questões relacionadas à gestão de jardins botânicos e não menciona nada sobre aquecimento global."
"""


