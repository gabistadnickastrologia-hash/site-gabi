# Gabi Stadnick · Astrologia

Site institucional de página única. HTML, CSS e JavaScript puros — sem build,
sem dependências, sem `npm install`. É só abrir o `index.html`.

A direção de arte sai do **logo e do dossiê da marca**: o azul da identidade em
três profundidades, tipografia geométrica art déco no mesmo espírito do
logotipo, e o tom de voz do dossiê — direto, prático, sem romantizar processo.
O ritmo editorial (foto sangrada alternando com blocos de texto) vem do
catálogo enviado como referência.

**Paleta** — todas as combinações do site passam de 4,5:1 de contraste.

| Token | Cor | Onde |
| --- | --- | --- |
| `--azul` | `#3B76A4` | a cor do logo, acento |
| `--azul-fundo` | `#2C5C82` | blocos de fundo cheio |
| `--azul-noite` | `#12293B` | capa, fecho e rodapé |
| `--azul-claro` | `#8FB6D2` | texto e traços sobre escuro |
| `--bruma` | `#DDE8F0` | seções claras |
| `--papel` | `#F4F8FA` | fundo da página |
| `--tinta` | `#10293A` | texto sobre claro |

> **Sobre a paleta do brandbook.** O brandbook define outra paleta — azul
> `#1E3A5F`, areia `#E7E3D4`, cinza `#B0B0B0` e dourado `#C6A76D`. O site não
> a usa: por decisão da Gabi, valem as cores do logo, e `#35729C` foi extraído
> do arquivo original, não estimado. Se um dia a paleta do brandbook tiver de
> prevalecer, corrija **só a linha `--azul`** e os tons derivados acompanham.

**Tipografia** — Poiret One nos títulos (mesma construção geométrica do
logotipo), Jost no texto corrido e Cormorant Garamond em itálico nas frases de
marca.

---

## Como ver o site

Abra o `index.html` no navegador. Se preferir um servidor local:

```bash
python3 -m http.server 8000
# depois acesse http://localhost:8000
```

---

## O que você precisa editar

Tudo o que é seu está marcado no código. Procure por estes pontos:

### 1. Telefone do WhatsApp ✔ já configurado

Está como **(47) 99643-4126** nos dois botões (o da chamada final e o
flutuante). Se um dia mudar, procure por `5547996434126` no `index.html` — o
formato é `55` + DDD + número, só dígitos.

### 2. Instagram ✔ já configurado

Está como **@gabistadnick**. Para mudar, procure por `instagram.com/gabistadnick`
no `index.html`.

### 3. Valores ✔ já configurados

| Leitura | Valor |
| --- | --- |
| Mapa Astral | R$350 |
| Revolução Solar | R$260 |
| Astrocartografia | R$260 |
| Mapa Astral + Revolução Solar | R$530 |

O combo está no bloco "As duas juntas" — procure por `combo__valor`. Se mudar
o preço, ajuste também a linha `combo__antes`, que mostra a economia.

Estão no `index.html`, um em cada card. Procure por `data-icon="valor"`:

```html
<li data-icon="valor"><strong>R$350</strong></li>
```

Se quiser mostrar parcelamento, é só escrever na mesma linha:

```html
<li data-icon="valor"><strong>R$350 à vista</strong> ou 3x R$120</li>
```

### 3b. O logo ✔ já configurado

Está em `assets/img/logo.png`, com fundo transparente.

Os dois arquivos enviados (`GS_bluelogo_whitecolorbackground` e
`GS_whitelogo_bluecolorbackground`) tinham **fundo opaco**, apesar de serem
PNG — sobre a foto escura da capa apareceria um retângulo. Extraí a
transparência da versão azul calculando o alfa a partir do canal vermelho,
que é o de maior variação entre o azul do logo e o branco do fundo; assim as
curvas finas mantêm o antisserrilhado.

Basta esse arquivo: sobre fundo escuro o CSS converte o azul para branco. Se
um dia trocar o logo, mantenha o nome `logo.png` e o fundo transparente.

Esses arquivos também deram o **azul exato da marca**: `#35729C`.

### 3c. Astroviagem ✔ já configurado

O ebook está no site com o texto oficial, a capa e o botão apontando para a
Eduzz (`https://chk.eduzz.com/7WXQ3KKG9A`). Procure por `id="astroviagem"`.

A capa (`assets/img/astroviagem.jpg`) foi extraída do anúncio de feed: o
script isola o livro, corta acima da caixa de texto branca e recompõe sobre
o mesmo azul do anúncio, em retrato 3:4. Assim a peça de venda com data e
botão "comprar agora" não vai para o site — num site a data vence e passa a
depor contra a venda.

### 3d. O que ainda é suposição minha

Estes pontos eu preenchi para o layout funcionar. Confira antes de publicar,
porque são compromissos com quem contrata:

- **Duração de cada consulta** (1h30 no mapa natal, 1h nas outras);
- **Formas de pagamento** citadas nas perguntas frequentes (Pix e cartão,
  remarcação com 24h de aviso);
- **Condição especial** para quem fecha mais de uma leitura — está no site
  sem percentual, só como convite para conversar.

### 4. Textos

Os textos de "Quem é a gabi", "Por que ler o seu mapa", os passos e as
perguntas frequentes foram escritos por mim no tom da referência. Leia com
calma e ajuste para a sua voz — principalmente a seção **Quem é a gabi**, que
é onde o site fala de você.

---

## Como me entregar as imagens

O Google Drive está bloqueado pela política de rede da sessão em que eu
trabalho — não consigo abrir nenhum link `drive.google.com`. O caminho que
funciona é pelo próprio repositório, e dá para fazer tudo pelo navegador,
sem instalar nada:

1. Baixe as imagens do seu Drive para o computador.
2. Abra o repositório no GitHub e entre na pasta `fotos-originais/`.
3. Clique em **Add file → Upload files** e arraste tudo.
4. Escreva qualquer mensagem e clique em **Commit changes**.

Pode subir com os nomes que vierem do Drive — depois disso eu enxergo os
arquivos, escolho os melhores enquadramentos, gero as versões otimizadas e
coloco cada uma no lugar certo do site.

As duas que eu mais preciso: o **logo** e a **capa do Astroviagem**.

---

## Imagens

O site funciona **sem nenhuma foto**: onde falta imagem, aparecem degradês em
tons de areia com arte vetorial. Para colocar as suas, há dois caminhos.

### Caminho fácil: o script faz os recortes

1. Salve as fotos originais, **sem cortar**, em `fotos-originais/`:

   | Nome do arquivo | Qual foto |
   | --- | --- |
   | `lua.jpg` | praia à noite, a lua sobre a água, você de costas |
   | `duna-ampla.jpg` | duna aberta, montanhas ao fundo, você pequena à direita |
   | `duna-camisa.jpg` | duna, camisa branca aberta, mãos nos bolsos |
   | `duna-olhar.jpg` | duna, olhando por cima do ombro |
   | `sorriso.jpg` | retrato próximo, camisa branca, sorrindo para a câmera |
   | `escritorio.jpg` | sentada na poltrona com o notebook e os livros de astrologia |

2. Rode, na pasta do projeto:

   ```bash
   pip install pillow
   python3 ferramentas/preparar-imagens.py
   ```

O script gera os oito recortes em `assets/img/`, cada um na proporção do
espaço onde vai aparecer, já comprimido. Ele mantém o rosto dentro do quadro
e não altera os originais.

**Por que cada foto foi para cada lugar** — os espaços largos (capa, bloco do
padrão, faixa) só funcionam com fotos de bastante cenário: um retrato vertical
cortado em faixa horizontal perde quase tudo. Por isso a lua e a duna ampla
foram para os blocos largos, e os retratos foram para os cards verticais.

- **capa** → a lua sobre a água. Escura e celeste, e você aparece pequena, então
  o nome em branco fica legível sem disputar com o seu rosto.
- **"Você não está perdida"** → duna ampla, você à direita. O texto desse bloco
  entra pela esquerda; vocês não se cruzam.
- **faixa antes das leituras** → só o reflexo da lua, sem ninguém. É um respiro.
- **Quem é a Gabi** → o retrato olhando para a câmera, que é a seção que fala
  de você.
- **card Mapa Astral** → você com o notebook e os livros: mostra a leitura
  acontecendo.
- **card Revolução Solar** → duna ao entardecer, postura firme.
- **card Astrocartografia** → horizonte e distância, porque o assunto é lugar.

Se algum recorte ficar ruim, abra `ferramentas/preparar-imagens.py` e mexa nos
três números da linha: **foco x**, **foco y** e **aproximação**. Cada linha tem
um comentário dizendo para que serve aquela imagem.

### Caminho manual: salvar já cortado

Se preferir cortar por conta, salve direto em `assets/img/` com estes nomes:

| Arquivo | Onde aparece | Formato |
| --- | --- | --- |
| `hero.jpg` | capa, tela cheia | 2000×1300 |
| `padrao.jpg` | bloco "Você não está perdida" | 2000×1300 |
| `sobre.jpg` | retrato em "Quem é a Gabi" | 1000×1250 |
| `divisor-leituras.jpg` | faixa antes das leituras | 2000×900 |
| `logo.svg` | menu, capa e fecho | vetor, na cor azul |
| `astroviagem.jpg` | capa do ebook | retrato, 1000×1330 |
| `leitura-mapa.jpg` | card Mapa Astral | 1000×1250 |
| `leitura-solar.jpg` | card Revolução Solar | 1000×1250 |
| `leitura-astrocartografia.jpg` | card Astrocartografia | 1000×1250 |
| `og.jpg` | miniatura ao compartilhar o link | 1200×630 |

Dicas:

- Na capa e nos blocos largos há texto claro por cima, então funcionam melhor
  imagens de **tom médio a escuro**. O site já aplica um véu escuro para
  garantir a leitura.
- Nos blocos largos, o texto entra por um dos lados — deixe o rosto do lado
  oposto. Na capa é o centro que fica livre; no "Por que ler o seu mapa?", o
  texto vem pela direita.
- Comprima antes de subir (TinyPNG, Squoosh) — imagem pesada derruba a
  velocidade do site.

### Onde os caminhos ficam no código

Todos no fim de `assets/css/style.css`, na seção **23. AS SUAS FOTOS**. Não
precisa mexer se você usar os nomes acima.

Um detalhe que custou caro descobrir: `url()` dentro de variável CSS é sempre
resolvido a partir do arquivo `.css`, nunca do HTML. Por isso os caminhos das
fotos moram no CSS e começam com `../img/`. Se algum dia você mover as fotos
para outra pasta, é lá que se ajusta.

### Arte vetorial já incluída

Enquanto não há fotografia, cada espaço mostra um desenho tirado do
instrumento da profissão — não é preenchimento, é a página se sustentando
sozinha. Quando a foto entrar, ela vem por cima e a arte desaparece junto
com o degradê.

| Arquivo | Uso |
| --- | --- |
| `roda-astral.svg` | roda do mapa: capa (girando devagar), bloco do padrão e card do Mapa Astral |
| `arte-solar.svg` | anel do ano solar, no card da Revolução Solar |
| `arte-astro.svg` | globo com meridianos e linhas planetárias: card da Astrocartografia e capa do Astroviagem |
| `arte-faixa.svg` | régua de graus, na faixa antes das leituras |
| `constelacao.svg` | constelação: marca d'água dos fundos e retrato de "Quem é a Gabi" |
| `marca.svg` | símbolo lua/sol usado como favicon |

Todos são gerados por script, com geometria calculada — não são traços
desenhados a olho. A roda tem os doze signos, a régua de graus de cinco em
cinco, as cúspides das casas e as linhas de aspecto entre os planetas.

---

## Como publicar

O site está pronto para o **Netlify**, que é grátis e dá um endereço curto —
coisa que importa, porque esse link vai para a bio do Instagram.

1. Entre em [netlify.com](https://app.netlify.com) e escolha **Sign up with
   GitHub** (não precisa criar senha nova).
2. **Add new site → Import an existing project → GitHub** e escolha o
   repositório `site-gabi`.
3. As configurações já vêm preenchidas pelo `netlify.toml` — é só confirmar e
   clicar em **Deploy**.
4. Em **Site configuration → Change site name**, troque o nome sorteado por
   `gabistadnick`. O endereço vira `gabistadnick.netlify.app`.

A partir daí, toda vez que algo mudar no repositório o site atualiza sozinho
em cerca de um minuto.

**O que vai ao ar** — o `netlify.toml` roda `ferramentas/publicar.sh`, que
copia só `index.html` e `assets/` para uma pasta `_site/`. As fotos originais
(24 MB) e as ferramentas ficam no repositório mas fora do site publicado.

**Alternativa: GitHub Pages.** Em *Settings → Pages*, escolha a branch e a
pasta raiz. Não precisa de conta nova, mas o endereço fica
`gabistadnickastrologia-hash.github.io/site-gabi`, e ele publica a pasta
inteira — inclusive as fotos originais.

**Domínio próprio.** Se um dia quiser `gabistadnick.com.br`, registre no
[registro.br](https://registro.br) (cerca de R$40 por ano) e aponte para o
Netlify em *Domain management → Add a domain*. O certificado de segurança sai
automaticamente.

## Estrutura

```
index.html                        página inteira, comentada seção a seção
netlify.toml                      configuração da publicação
assets/css/style.css              design system (paleta, tipos, componentes)
assets/css/fonts.css              fontes auto-hospedadas
assets/js/main.js                 menu, revelação ao rolar, FAQ, logo
assets/img/                       fotos tratadas, logo e arte vetorial
assets/fonts/                     Poiret One, Jost e Cormorant Garamond
fotos-originais/                  suas fotos sem cortar (não vão para o site)
ferramentas/preparar-imagens.py   gera os recortes a partir dos originais
ferramentas/publicar.sh           monta a pasta que vai ao ar
```

## Detalhes técnicos

- Responsivo de 320px até telas grandes.
- Acessibilidade: navegação por teclado, foco visível, link de pular conteúdo,
  `aria-expanded` no menu e respeito a `prefers-reduced-motion`.
- Tipografia auto-hospedada: Poiret One (títulos), Jost (texto) e
  Cormorant Garamond (frases de marca). Nenhuma requisição externa.
