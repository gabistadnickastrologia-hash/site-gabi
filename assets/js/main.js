/* ═══════════════════════════════════════════════════════════
   Gabi Stadnick · Astrologia — comportamentos da página
   ═══════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  /* ── menu mobile ─────────────────────────────────────── */
  var toggle = document.getElementById('navToggle');
  var menu   = document.getElementById('navMenu');

  function fecharMenu() {
    menu.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Abrir menu');
  }

  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var aberto = menu.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(aberto));
      toggle.setAttribute('aria-label', aberto ? 'Fechar menu' : 'Abrir menu');
    });

    menu.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') fecharMenu();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('is-open')) {
        fecharMenu();
        toggle.focus();
      }
    });
  }

  /* ── barra de navegação: fundo ao rolar ──────────────── */
  var nav = document.getElementById('nav');
  var ticking = false;

  function atualizarNav() {
    if (nav) nav.classList.toggle('is-stuck', window.scrollY > 80);
    ticking = false;
  }

  window.addEventListener('scroll', function () {
    if (!ticking) {
      window.requestAnimationFrame(atualizarNav);
      ticking = true;
    }
  }, { passive: true });

  atualizarNav();

  /* ── revelação dos blocos ao entrar na tela ──────────── */
  var alvos = document.querySelectorAll('.reveal');

  if (!('IntersectionObserver' in window)) {
    alvos.forEach(function (el) { el.classList.add('is-visible'); });
  } else {
    var observador = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (entrada) {
        if (entrada.isIntersecting) {
          entrada.target.classList.add('is-visible');
          observador.unobserve(entrada.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });

    alvos.forEach(function (el) { observador.observe(el); });
  }

  /* ── só uma pergunta aberta por vez no FAQ ───────────── */
  var perguntas = document.querySelectorAll('.faq__item');
  perguntas.forEach(function (item) {
    item.addEventListener('toggle', function () {
      if (!item.open) return;
      perguntas.forEach(function (outro) {
        if (outro !== item) outro.open = false;
      });
    });
  });

  /* ── logo: só troca o texto pela imagem depois que ela carregar ──
     Assim, se o arquivo do logo não existir, ninguém vê ícone
     quebrado — fica o nome composto na fonte da marca. */
  document.querySelectorAll('.marca').forEach(function (marca) {
    var img = marca.querySelector('.marca__img');
    if (!img) return;
    if (img.complete && img.naturalWidth > 0) {
      marca.classList.add('marca--ok');
    } else {
      img.addEventListener('load', function () {
        if (img.naturalWidth > 0) marca.classList.add('marca--ok');
      });
    }
  });

  /* ── ano do rodapé ───────────────────────────────────── */
  var ano = document.getElementById('ano');
  if (ano) ano.textContent = new Date().getFullYear();
})();
