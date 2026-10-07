(() => {
  'use strict';

  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];

  // n8n webhook that receives every site form submission.
  const WEBHOOK_URL = 'https://api.fitnessgrizzly.com/n8n/webhook/a498528e-b6fe-4c06-8503-92600152738d';

  // Header behavior
  const header = $('.site-header');
  const body = document.body;
  const updateHeader = () => {
    if (!header) return;
    header.classList.toggle('is-scrolled', window.scrollY > 24);
  };
  updateHeader();
  window.addEventListener('scroll', updateHeader, { passive: true });

  const mobileToggle = $('.mobile-toggle');
  if (mobileToggle) {
    mobileToggle.addEventListener('click', () => {
      const open = body.classList.toggle('nav-open');
      mobileToggle.setAttribute('aria-expanded', String(open));
    });
    $$('.mobile-panel a').forEach(link => link.addEventListener('click', () => {
      body.classList.remove('nav-open');
      mobileToggle.setAttribute('aria-expanded', 'false');
    }));
  }

  // Mark active primary nav item based on current path.
  // Matches on path segments so it works both from a server and from file://.
  const path = location.pathname.replace(/index\.html$/, '');
  const inSection = seg => path.includes(`/${seg}/`);
  $$('.nav-link[data-nav]').forEach(link => {
    const key = link.dataset.nav;
    const active = key === 'services'
      ? inSection('services') || inSection('residential-repair') || inSection('equipment-health-check')
      : key === 'used' ? inSection('used-equipment')
      : key === 'projects' ? inSection('projects')
      : key === 'about' ? inSection('about')
      : key === 'contact' ? inSection('contact')
      : key === 'sell' ? inSection('sell-equipment')
      : false;
    link.classList.toggle('is-active', active);
  });

  // Intersection reveals
  const revealItems = $$('.reveal');
  if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealItems.forEach(el => io.observe(el));
  } else {
    revealItems.forEach(el => el.classList.add('is-visible'));
  }

  // Homepage lifecycle utility
  const hero = $('.home-hero');
  const lifecycleButtons = $$('.lifecycle-stage');
  const heroImage = $('#heroLifecycleImage');
  const lifecycleMessage = $('#lifecycleMessage');
  const lifecycleCta = $('#lifecycleCta');
  if (hero && heroImage && lifecycleButtons.length) {
    const preload = [...new Set(lifecycleButtons.map(btn => btn.dataset.image))];
    preload.forEach(src => { const img = new Image(); img.src = src; });

    const activateStage = btn => {
      lifecycleButtons.forEach(b => {
        const active = b === btn;
        b.classList.toggle('is-active', active);
        b.setAttribute('aria-selected', String(active));
      });
      hero.classList.add('is-changing');
      const next = btn.dataset.image;
      const swap = () => {
        heroImage.src = next;
        heroImage.removeAttribute('srcset');
        heroImage.removeAttribute('sizes');
        heroImage.alt = btn.dataset.alt || '';
        if (lifecycleMessage) lifecycleMessage.textContent = btn.dataset.message || '';
        if (lifecycleCta) {
          lifecycleCta.textContent = btn.dataset.cta || 'Explore service';
          if (btn.dataset.url) lifecycleCta.href = btn.dataset.url;
        }
        requestAnimationFrame(() => setTimeout(() => hero.classList.remove('is-changing'), 80));
      };
      setTimeout(swap, 130);
    };

    lifecycleButtons.forEach(btn => {
      btn.addEventListener('click', () => activateStage(btn));
      btn.addEventListener('keydown', e => {
        if (!['ArrowRight', 'ArrowLeft'].includes(e.key)) return;
        e.preventDefault();
        const idx = lifecycleButtons.indexOf(btn);
        const nextIdx = e.key === 'ArrowRight'
          ? (idx + 1) % lifecycleButtons.length
          : (idx - 1 + lifecycleButtons.length) % lifecycleButtons.length;
        lifecycleButtons[nextIdx].focus();
        activateStage(lifecycleButtons[nextIdx]);
      });
    });
  }

  // One machine / full facility visual focus
  const scaleVisual = $('.scale-visual');
  const scaleButtons = $$('.scale-switch button');
  if (scaleVisual && scaleButtons.length) {
    scaleButtons.forEach(btn => btn.addEventListener('click', () => {
      scaleButtons.forEach(b => b.classList.toggle('is-active', b === btn));
      scaleVisual.dataset.focus = btn.dataset.focus;
    }));
  }

  // Needs router
  const routerRows = $$('.router-row');
  const routerText = $('#routerText');
  const routerCta = $('#routerCta');
  if (routerRows.length && routerText && routerCta) {
    routerRows.forEach(row => row.addEventListener('click', () => {
      routerRows.forEach(r => r.classList.toggle('is-active', r === row));
      routerText.textContent = row.dataset.result || '';
      routerCta.textContent = row.dataset.cta || 'Continue';
      if (row.dataset.url) routerCta.href = row.dataset.url;
    }));
  }

  // Project filters
  const filterTabs = $$('.filter-tab');
  const projectItems = $$('.masonry-item[data-category]');
  if (filterTabs.length && projectItems.length) {
    filterTabs.forEach(tab => tab.addEventListener('click', () => {
      filterTabs.forEach(t => t.classList.toggle('is-active', t === tab));
      const filter = tab.dataset.filter;
      projectItems.forEach(item => {
        const categories = (item.dataset.category || '').split(' ');
        item.hidden = filter !== 'all' && !categories.includes(filter);
      });
    }));
  }

  // Quote wizard.
  const quoteForm = $('#quoteWizard');
  if (quoteForm) {
    const steps = $$('.quote-step', quoteForm);
    const bar = $('.quote-progress__bar');
    const label = $('#quoteProgressLabel');
    let current = 0;

    const show = idx => {
      current = Math.max(0, Math.min(idx, steps.length - 1));
      steps.forEach((s, i) => s.classList.toggle('is-active', i === current));
      if (bar) bar.style.width = `${((current + 1) / steps.length) * 100}%`;
      if (label) label.textContent = `Step ${current + 1} of ${steps.length}`;
      const active = steps[current];
      active.querySelector('[data-prev]')?.toggleAttribute('hidden', current === 0);
      active.querySelector('input, select, textarea, button')?.focus({ preventScroll: true });
    };

    $$('.option-button', quoteForm).forEach(button => button.addEventListener('click', () => {
      $$('.option-button', button.closest('.quote-step')).forEach(b => b.classList.remove('is-selected'));
      button.classList.add('is-selected');
      const hidden = $('input[type="hidden"][name="request_type"]', quoteForm);
      if (hidden) hidden.value = button.dataset.value || button.textContent.trim();
    }));

    quoteForm.addEventListener('click', e => {
      const next = e.target.closest('[data-next]');
      const prev = e.target.closest('[data-prev]');
      if (next) { e.preventDefault(); show(current + 1); }
      if (prev) { e.preventDefault(); show(current - 1); }
    });

    quoteForm.addEventListener('submit', e => submitToWebhook(e, quoteForm, 'request-quote'));
    show(0);
  }

  // Lead forms (contact, residential repair, sell equipment) post to the same webhook.
  $$('form[data-front-end-only]').forEach(form => {
    const formName = location.pathname.split('/').filter(p => p && p !== 'index.html').pop() || 'home';
    form.addEventListener('submit', e => submitToWebhook(e, form, formName));
  });

  // Form submission. Sends JSON, or multipart when the form has files attached (sell-equipment photos).
  function submitToWebhook(e, form, formName) {
    e.preventDefault();
    const status = $('.integration-hook', form);
    const submitBtn = $('button[type="submit"]', form);
    const setStatus = msg => {
      if (!status) return;
      status.textContent = msg;
      status.style.display = 'block';
    };

    const data = new FormData(form);
    data.append('form_name', formName);
    data.append('page_url', location.href);
    data.append('submitted_at', new Date().toISOString());

    const hasFiles = $$('input[type="file"]', form).some(input => input.files.length);
    const payload = {};
    if (!hasFiles) {
      for (const [key, value] of data.entries()) {
        if (value instanceof File) continue;
        payload[key] = value;
      }
    }

    if (submitBtn) submitBtn.disabled = true;
    setStatus('Sending…');

    fetch(WEBHOOK_URL, {
      method: 'POST',
      headers: hasFiles ? undefined : { 'Content-Type': 'application/json' },
      body: hasFiles ? data : JSON.stringify(payload)
    })
      .then(res => {
        if (!res.ok) throw new Error(`Webhook responded ${res.status}`);
        form.reset();
        $$('.option-button.is-selected', form).forEach(b => b.classList.remove('is-selected'));
        setStatus('Thanks — your request was sent. Priority Fitness will be in touch soon.');
      })
      .catch(err => {
        console.error('Form submission failed:', err);
        setStatus('Something went wrong sending your request. Please call 920-765-3644 or try again.');
      })
      .finally(() => {
        if (submitBtn) submitBtn.disabled = false;
      });
  }
})();
