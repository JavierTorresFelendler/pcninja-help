// Dropdown menu + header that turns solid after scrolling past the hero
(function () {
  document.querySelectorAll('.nav .toggle').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var li = btn.closest('li');
      var open = li.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function () {
    document.querySelectorAll('.nav li.open').forEach(function (li) {
      li.classList.remove('open');
      var t = li.querySelector('.toggle');
      if (t) t.setAttribute('aria-expanded', 'false');
    });
  });

  var bar = document.querySelector('.topbar[data-transparent]');
  if (bar) {
    var update = function () {
      bar.classList.toggle('is-transparent', window.scrollY < 40);
    };
    update();
    window.addEventListener('scroll', update, { passive: true });
  }
})();
