#!/usr/bin/env bash
# Monta a pasta que vai ao ar, em _site/
#
# Só o que o navegador precisa é publicado. As fotos originais (24 MB) e as
# ferramentas ficam no repositório, mas fora do site — não faz sentido servir
# arquivos de 3 MB que ninguém pede.
set -euo pipefail

rm -rf _site
mkdir -p _site

cp index.html _site/
cp -r assets _site/

# arquivos que não são do site, caso algum dia entrem em assets/
find _site -name '.DS_Store' -delete

echo "publicado em _site/:"
du -sh _site
find _site -type f | wc -l | xargs echo "arquivos:"
