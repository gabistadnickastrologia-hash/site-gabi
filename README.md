# Gabi Stadnick · Astrologia

Site institucional de página única. HTML, CSS e JavaScript puros — sem build,
sem dependências, sem `npm install`. É só abrir o `index.html`.

A direção de arte segue o catálogo da niná.r enviado como referência: paleta de
areia, caramelo e creme; títulos condensados em caixa-alta; manuscrito como
acento; fotografia sangrada de ponta a ponta.

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

Estão no `index.html`, um em cada card. Procure por `data-icon="valor"`:

```html
<li data-icon="valor"><strong>R$350</strong></li>
```

Se quiser mostrar parcelamento, é só escrever na mesma linha:

```html
<li data-icon="valor"><strong>R$350 à vista</strong> ou 3x R$120</li>
```

### 3b. O que ainda é suposição minha

Estes pontos eu preenchi para o layout funcionar. Confira antes de publicar,
porque são compromissos com quem contrata:

- **Duração de cada leitura** (1h30 no mapa natal, 1h nas outras);
- **O que é entregue** (PDF, gravação, 7 dias de dúvidas abertas);
- **Prazos de entrega** (gravação em 24h, material em 5 dias úteis);
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

## Imagens

O site funciona **sem nenhuma foto**: onde falta imagem, aparecem degradês em
tons de areia com arte vetorial. Para colocar as suas, há dois caminhos.

### Caminho fácil: o script faz os recortes

1. Salve as três fotos originais, **sem cortar**, em `fotos-originais/`:

   | Nome do arquivo | Qual foto |
   | --- | --- |
   | `janela.jpg` | retrato na janela, camisa branca, segurando a xícara |
   | `varanda.jpg` | em pé na porta da varanda, calça bege, de perfil |
   | `grama.jpg` | sentada na grama lendo a carta, com os livros ao lado |

2. Rode, na pasta do projeto:

   ```bash
   pip install pillow
   python3 ferramentas/preparar-imagens.py
   ```

O script gera os sete recortes em `assets/img/`, cada um na proporção do
espaço onde vai aparecer, já comprimido. Ele mantém o rosto dentro do quadro
e não altera os originais.

Se algum recorte ficar ruim, abra `ferramentas/preparar-imagens.py` e mexa nos
três números da linha correspondente: **foco x**, **foco y** e **aproximação**.
Cada linha tem um comentário dizendo para que serve aquela imagem.

### Caminho manual: salvar já cortado

Se preferir cortar por conta, salve direto em `assets/img/` com estes nomes:

| Arquivo | Onde aparece | Formato |
| --- | --- | --- |
| `hero.jpg` | capa, tela cheia | 2000×1300 |
| `porque.jpg` | bloco "Por que ler o seu mapa?" | 2000×1300 |
| `divisor-leituras.jpg` | faixa antes das leituras | 2000×900 |
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

| Arquivo | Uso |
| --- | --- |
| `marca.svg` | símbolo lua/sol do menu e favicon |
| `estrela.svg` | estrela no meio do nome, na capa |
| `constelacao.svg` | constelação de marca d'água nos fundos |

---

## Como publicar

Qualquer hospedagem de site estático serve. As duas mais simples:

**GitHub Pages** — em *Settings → Pages*, escolha a branch e a pasta raiz
(`/`). O site vai ao ar em poucos minutos.

**Netlify** — arraste a pasta inteira para app.netlify.com/drop. Dá para
conectar um domínio próprio depois.

---

## Estrutura

```
index.html                        página inteira, comentada seção a seção
assets/css/style.css              design system (paleta, tipos, componentes)
assets/css/fonts.css              fontes auto-hospedadas
assets/js/main.js                 menu, revelação ao rolar, FAQ
assets/img/                       artes vetoriais + onde vão as suas fotos
assets/fonts/                     Oswald, Poppins e Caveat
fotos-originais/                  suas fotos sem cortar (não vão para o site)
ferramentas/preparar-imagens.py   gera os recortes a partir dos originais
```

## Detalhes técnicos

- Responsivo de 320px até telas grandes.
- Acessibilidade: navegação por teclado, foco visível, link de pular conteúdo,
  `aria-expanded` no menu e respeito a `prefers-reduced-motion`.
- Tipografia via Google Fonts: Oswald (títulos), Poppins (texto) e
  Caveat (manuscrito).
