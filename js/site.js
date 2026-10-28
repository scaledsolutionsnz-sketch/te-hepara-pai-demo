(function () {
  var doc = document.documentElement;
  doc.classList.add('js');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Mobile menu
  var btn = document.querySelector('.menu-btn');
  var menu = document.getElementById('mobile-menu');
  if (btn && menu) {
    btn.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('open')) {
        menu.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); btn.focus();
      }
    });
  }

  // Hero crossfade
  var stack = document.querySelector('.hero-media.slides');
  if (stack) {
    var imgs = stack.querySelectorAll('img');
    var cap = document.querySelector('.hero-caption');
    var i = 0;
    if (imgs.length > 1 && !reduce) {
      setInterval(function () {
        imgs[i].classList.remove('is-on');
        i = (i + 1) % imgs.length;
        imgs[i].loading = 'eager';
        imgs[i].classList.add('is-on');
        if (cap) cap.textContent = imgs[i].getAttribute('data-caption') || '';
      }, 6000);
    }
  }

  // Lightbox: photo wall buttons plus large content photos
  var lb = document.getElementById('lightbox');
  if (lb && typeof lb.showModal === 'function') {
    var lbImg = lb.querySelector('img'), lbCap = lb.querySelector('figcaption');
    var items = [];
    document.querySelectorAll('.gallery button[data-full]').forEach(function (b) {
      var im = b.querySelector('img');
      items.push({ el: b, src: b.getAttribute('data-full'), alt: im.alt });
    });
    document.querySelectorAll('.split figure img, .trio-item figure img, .leader figure img').forEach(function (im) {
      im.setAttribute('data-lightbox', '');
      im.setAttribute('tabindex', '0');
      im.setAttribute('role', 'button');
      im.setAttribute('aria-label', 'View larger: ' + im.alt);
      items.push({ el: im, src: im.getAttribute('src'), alt: im.alt });
    });
    var cur = 0, opener = null;
    function show(n) {
      cur = (n + items.length) % items.length;
      lbImg.src = items[cur].src; lbImg.alt = items[cur].alt; lbCap.textContent = items[cur].alt;
    }
    items.forEach(function (it, n) {
      it.el.addEventListener('click', function () { opener = it.el; show(n); lb.showModal(); });
      if (it.el.tagName === 'IMG') it.el.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); opener = it.el; show(n); lb.showModal(); }
      });
    });
    lb.querySelector('.lb-close').addEventListener('click', function () { lb.close(); });
    lb.querySelector('.lb-prev').addEventListener('click', function () { show(cur - 1); });
    lb.querySelector('.lb-next').addEventListener('click', function () { show(cur + 1); });
    lb.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') show(cur - 1);
      if (e.key === 'ArrowRight') show(cur + 1);
    });
    lb.addEventListener('click', function (e) { if (e.target === lb) lb.close(); });
    lb.addEventListener('close', function () { if (opener) opener.focus(); });
  }

  // Reveal on scroll
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('in'); });
  }

  // Gmail compose links (address assembled here, never in the HTML)
  document.querySelectorAll('a[data-gmail]').forEach(function (a) {
    var to = a.getAttribute('data-user') + '@' + a.getAttribute('data-domain');
    a.href = 'https://mail.google.com/mail/?view=cm&fs=1&to=' + encodeURIComponent(to) + '&su=' + (a.getAttribute('data-su') || '') + '&body=' + (a.getAttribute('data-body') || '');
    a.target = '_blank'; a.rel = 'noopener';
  });
  document.querySelectorAll('[data-email-text]').forEach(function (el) {
    el.textContent = el.getAttribute('data-user') + '@' + el.getAttribute('data-domain');
  });

  // Upcoming Sunday services (weekly, 9:30 am)
  var list = document.getElementById('upcoming-sundays');
  if (list) {
    var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    var d = new Date();
    var now = new Date();
    d.setHours(9, 30, 0, 0);
    var add = (7 - d.getDay()) % 7;
    d.setDate(d.getDate() + add);
    if (add === 0 && now.getHours() * 60 + now.getMinutes() > 10 * 60 + 30) d.setDate(d.getDate() + 7);
    var html = '';
    for (var k = 0; k < 6; k++) {
      html += '<li class="date"><div class="cal"><small>' + months[d.getMonth()] + '</small><b>' + d.getDate() + '</b></div>' +
        '<div><h3>Sunday service' + (k === 0 ? ' (this week)' : '') + '</h3><p>9:30 am, followed by morning tea. 131 Cole Street, Masterton</p></div></li>';
      d.setDate(d.getDate() + 7);
    }
    list.innerHTML = html;
  }

  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
