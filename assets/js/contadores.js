/* ===========================================================================
   CONTADORES — Ágape
   ===========================================================================
   Anima os números da seção "em operação" de 0 até o valor final quando eles
   entram na tela.

   POR QUE ISSO NÃO FERE A REGRA DO PROJETO
   ----------------------------------------
   O CLAUDE.md pede HTML/CSS puro e proíbe funcionalidade que só exista via
   script. Este arquivo é enfeite, não funcionalidade: o valor final já está
   escrito no HTML. Sem JavaScript, com o script bloqueado ou com
   prefers-reduced-motion, o número simplesmente aparece pronto — nada se
   perde. O script só troca o valor por 0 no instante em que vai animá-lo.

   NO ELEMENTOR: widget "Contador" (Counter), que é gratuito e faz exatamente
   isto. Um widget por número, com "Número inicial" 0 e o final no lugar.
   ======================================================================== */
(function () {
  'use strict';

  var alvos = document.querySelectorAll('[data-conta]');
  if (!alvos.length) return;

  var semMovimento = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (semMovimento || !('IntersectionObserver' in window)) return;  // deixa estático

  var DURACAO = 1600;

  function animar(el) {
    var fim = parseInt(el.getAttribute('data-conta'), 10);
    var pre = el.getAttribute('data-prefixo') || '';
    var suf = el.getAttribute('data-sufixo') || '';
    if (isNaN(fim)) return;

    var inicio = null;
    function passo(agora) {
      if (inicio === null) inicio = agora;
      var k = Math.min(1, (agora - inicio) / DURACAO);
      // easeOutExpo: arranca rápido e assenta devagar no número final
      var suave = k === 1 ? 1 : 1 - Math.pow(2, -10 * k);
      el.textContent = pre + Math.round(fim * suave) + suf;
      if (k < 1) requestAnimationFrame(passo);
    }
    requestAnimationFrame(passo);
  }

  var obs = new IntersectionObserver(function (entradas) {
    entradas.forEach(function (e) {
      if (!e.isIntersecting) return;
      animar(e.target);
      obs.unobserve(e.target);     // anima uma vez só
    });
  }, { threshold: 0.6 });

  Array.prototype.forEach.call(alvos, function (el) { obs.observe(el); });
})();
