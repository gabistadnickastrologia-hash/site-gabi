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
tons de areia com arte vetorial. Para colocar as suas, basta salvar os arquivos
em `assets/img/` com os nomes abaixo — eles entram sozinhos, sem mexer no
código.

| Arquivo | Onde aparece | Formato ideal |
| --- | --- | --- |
| `hero.jpg` | capa, tela cheia | horizontal, 2000×1300 |
| `porque.jpg` | bloco "Por que ler o seu mapa?" | horizontal, 2000×1300 |
| `divisor-leituras.jpg` | faixa antes dos pacotes | horizontal, 2000×900 |
| `leitura-mapa.jpg` | card Mapa Astral | vertical, 1000×1250 |
| `leitura-solar.jpg` | card Revolução Solar | vertical, 1000×1250 |
| `leitura-astrocartografia.jpg` | card Astrocartografia | vertical, 1000×1250 |
| `og.jpg` | miniatura ao compartilhar o link | 1200×630 |

Dicas:

- Nas fotos de capa e dos blocos largos há texto claro por cima, então
  funcionam melhor imagens de **tom médio a escuro**. O site já aplica um véu
  escuro por cima para garantir a leitura.
- As artes do seu Instagram entram bem nos três cards verticais.
- Comprima antes de subir (TinyPNG, Squoosh) — imagem pesada derruba a
  velocidade do site.

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
index.html              página inteira, com comentários marcando cada seção
assets/css/style.css    design system completo (paleta, tipos, componentes)
assets/js/main.js       menu, revelação ao rolar, FAQ
assets/img/             artes vetoriais + onde vão as suas fotos
```

## Detalhes técnicos

- Responsivo de 320px até telas grandes.
- Acessibilidade: navegação por teclado, foco visível, link de pular conteúdo,
  `aria-expanded` no menu e respeito a `prefers-reduced-motion`.
- Tipografia via Google Fonts: Oswald (títulos), Poppins (texto) e
  Caveat (manuscrito).
