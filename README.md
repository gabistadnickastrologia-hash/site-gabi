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

### 1. Telefone do WhatsApp

Aparece **duas vezes** no `index.html` (no botão da chamada final e no botão
flutuante). Procure por `5500000000000` e troque pelo seu número, no formato
`55` + DDD + número, só dígitos:

```
https://wa.me/5541999998888?text=Oi%20Gabi!...
```

### 2. Instagram

Procure por `instagram.com/gabistadnickastrologia` e ajuste se o @ for outro.

### 3. Valores

**Os preços que estão no site são exemplos** — coloquei valores plausíveis só
para o layout não ficar vazio. Procure por `R$` no `index.html`: são 7
ocorrências (4 leituras + 3 previsões). O formato segue o da referência:

```html
<li data-icon="◈"><strong>R$447 à vista</strong> ou 6x R$82</li>
```

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
| `leitura-sinastria.jpg` | card Sinastria | vertical, 1000×1250 |
| `leitura-bebe.jpg` | card Mapa do Bebê | vertical, 1000×1250 |
| `transitos.jpg` | bloco "Previsões" | horizontal, 2000×1300 |
| `og.jpg` | miniatura ao compartilhar o link | 1200×630 |

Dicas:

- Nas fotos de capa e dos blocos largos há texto claro por cima, então
  funcionam melhor imagens de **tom médio a escuro**. O site já aplica um véu
  escuro por cima para garantir a leitura.
- As artes do seu Instagram entram bem nos quatro cards verticais.
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
