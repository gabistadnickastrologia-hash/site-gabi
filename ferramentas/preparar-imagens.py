#!/usr/bin/env python3
"""
Prepara as fotos do site a partir dos originais.

Uso:
    1. salve as três fotos em  fotos-originais/  com estes nomes:
         janela.jpg   → retrato na janela, camisa branca, xícara
         varanda.jpg  → em pé na porta da varanda, calça bege
         grama.jpg    → sentada na grama lendo a carta, com os livros
    2. rode:  python3 ferramentas/preparar-imagens.py
    3. os arquivos prontos aparecem em  assets/img/

O script corta cada foto na proporção do espaço onde ela vai aparecer,
mantendo o rosto (ou o detalhe principal) dentro do quadro, redimensiona
e comprime. Os originais não são alterados.

Precisa da biblioteca Pillow:  pip install pillow
"""

import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Falta a biblioteca Pillow. Rode:  pip install pillow")

RAIZ = Path(__file__).resolve().parent.parent
ORIGINAIS = RAIZ / "fotos-originais"
DESTINO = RAIZ / "assets" / "img"

# (arquivo de saída, foto de origem, largura, altura, foco x, foco y, aproximação, qualidade)
#
# foco x / foco y  ponto da foto que precisa sobreviver ao corte, em fração
#                  da largura e da altura (0 = esquerda/topo, 1 = direita/base).
#                  É onde o corte fica centrado — normalmente, o seu rosto.
#
# aproximação      1.0 usa o máximo da foto; 0.8 usa 80% dela e chega mais
#                  perto. Serve para te tirar do centro quando o texto do
#                  site entra por cima de um dos lados.
#
# Se algum recorte ficar ruim, mexa só nesses três números.
TRABALHOS = [
    # capa: a varanda dá o respiro à esquerda para o nome no centro
    ("hero.jpg",                    "varanda.jpg", 2000, 1300, 0.72, 0.35, 1.00, 82),

    # "por que ler o seu mapa": aproxima e te joga para a esquerda,
    # porque o texto desse bloco entra pela direita
    ("porque.jpg",                  "grama.jpg",   2000, 1300, 0.66, 0.45, 0.78, 82),

    # faixa antes das leituras: os livros e a carta na grama
    ("divisor-leituras.jpg",        "grama.jpg",   2000,  900, 0.50, 0.72, 1.00, 82),

    # cards das três leituras (verticais)
    ("leitura-mapa.jpg",            "janela.jpg",  1000, 1250, 0.58, 0.35, 1.00, 84),
    ("leitura-solar.jpg",           "varanda.jpg", 1000, 1250, 0.72, 0.30, 1.00, 84),
    ("leitura-astrocartografia.jpg","grama.jpg",   1000, 1250, 0.52, 0.45, 1.00, 84),

    # miniatura de compartilhamento (WhatsApp, Instagram, Google)
    ("og.jpg",                      "janela.jpg",  1200,  630, 0.58, 0.35, 1.00, 80),
]


def recortar(img, larg, alt, fx, fy, aprox=1.0):
    """Corta na proporção pedida mantendo o ponto (fx, fy) dentro do quadro."""
    orig_l, orig_a = img.size
    alvo = larg / alt

    if orig_l / orig_a > alvo:          # original mais largo: corta as laterais
        nova_l, nova_a = int(orig_a * alvo), orig_a
    else:                                # original mais alto: corta topo e base
        nova_l, nova_a = orig_l, int(orig_l / alvo)

    if aprox < 1.0:                      # aproxima mantendo a proporção
        nova_l, nova_a = max(int(nova_l * aprox), 1), max(int(nova_a * aprox), 1)

    # centraliza no ponto focal, sem deixar a janela sair da foto
    esq = min(max(int(orig_l * fx - nova_l / 2), 0), orig_l - nova_l)
    topo = min(max(int(orig_a * fy - nova_a / 2), 0), orig_a - nova_a)

    return img.crop((esq, topo, esq + nova_l, topo + nova_a)) \
              .resize((larg, alt), Image.LANCZOS)


def main():
    if not ORIGINAIS.is_dir():
        sys.exit(f"Não achei a pasta {ORIGINAIS}")

    DESTINO.mkdir(parents=True, exist_ok=True)
    cache, feitos, faltando = {}, 0, set()

    for saida, origem, larg, alt, fx, fy, aprox, qual in TRABALHOS:
        caminho = ORIGINAIS / origem
        if not caminho.exists():
            faltando.add(origem)
            continue

        if origem not in cache:
            # exif_transpose corrige fotos que o celular salva deitadas
            cache[origem] = ImageOps.exif_transpose(Image.open(caminho)).convert("RGB")

        destino = DESTINO / saida
        recortar(cache[origem], larg, alt, fx, fy, aprox).save(
            destino, "JPEG", quality=qual, optimize=True, progressive=True)

        kb = destino.stat().st_size / 1024
        print(f"  {saida:<32} {larg}x{alt}  {kb:6.0f} KB   ← {origem}")
        feitos += 1

    print(f"\n{feitos} de {len(TRABALHOS)} imagens geradas em assets/img/")

    if faltando:
        print("\nFaltou salvar em fotos-originais/: " + ", ".join(sorted(faltando)))
        print("Os espaços sem foto continuam com o degradê de fundo — o site não quebra.")


if __name__ == "__main__":
    main()
