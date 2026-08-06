#!/usr/bin/env bash
# Monta a pasta que vai ao ar, em docs/
#
# Só o que o navegador precisa é publicado. As fotos originais (24 MB) e as
# ferramentas ficam no repositório, mas fora do site — não faz sentido servir
# arquivos de 3 MB que ninguém pede.
#
# A pasta se chama docs/ porque é uma das duas que o GitHub Pages aceita
# servir direto de um branch, sem precisar de GitHub Actions. Ela é
# versionada: o que está no repositório é exatamente o que está no ar.
set -euo pipefail

cd "$(dirname "$0")/.."

rm -rf docs
mkdir -p docs

cp index.html docs/
cp -r assets docs/

# Sem este arquivo o GitHub Pages passa tudo pelo Jekyll, que ignora
# pastas e arquivos começados por "_" e pode engolir parte dos assets.
touch docs/.nojekyll

# arquivos que não são do site, caso algum dia entrem em assets/
find docs -name '.DS_Store' -delete

echo "publicado em docs/:"
du -sh docs
find docs -type f | wc -l | xargs echo "arquivos:"
