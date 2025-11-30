/*!
 * Docsy-adapted version of Bootstrap's color mode toggler.
 * Original: https://github.com/twbs/examples/blob/main/color-modes/js/color-modes.js
 * Copyright 2011-2024 The Bootstrap Authors
 * Licensed under the Creative Commons Attribution 3.0 Unported License.
 */

(() => {
  'use strict';

  const themeKey = 'td-color-theme';

  const getStoredTheme = () => localStorage.getItem(themeKey);
  const setStoredTheme = theme => localStorage.setItem(themeKey, theme);

  const getPreferredTheme = () => {
    const storedTheme = getStoredTheme();
    if (storedTheme) return storedTheme;

    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  };

  const setTheme = theme => {
    const appliedTheme =
      theme === 'auto'
        ? (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')
        : theme;

    document.documentElement.setAttribute('data-bs-theme', appliedTheme);
  };

  const showActiveTheme = (theme, focus = false) => {
    const themeSwitcher = document.querySelector('#bd-theme');
    if (!themeSwitcher) return;

    const themeSwitcherText = document.querySelector('#bd-theme-text');
    const activeThemeIcon = document.querySelector('.theme-icon-active use');
    const btnToActive = document.querySelector(`[data-bs-theme-value="${theme}"]`);

    if (!btnToActive || !activeThemeIcon) return;

    const svgHref = btnToActive.querySelector('svg use').getAttribute('href');

    document.querySelectorAll('[data-bs-theme-value]').forEach(el => {
      el.classList.remove('active');
      el.setAttribute('aria-pressed', 'false');
    });

    btnToActive.classList.add('active');
    btnToActive.setAttribute('aria-pressed', 'true');
    activeThemeIcon.setAttribute('href', svgHref);

    if (themeSwitcherText) {
      const label = `${themeSwitcherText.textContent} (${btnToActive.dataset.bsThemeValue})`;
      themeSwitcher.setAttribute('aria-label', label);
    }

    if (focus) themeSwitcher.focus();
  };

  // Listen for system color scheme changes
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
    const storedTheme = getStoredTheme();
    if (storedTheme !== 'light' && storedTheme !== 'dark') {
      setTheme(getPreferredTheme());
      showActiveTheme(getPreferredTheme());
    }
  });

  // Initialize on DOM ready
  window.addEventListener('DOMContentLoaded', () => {
    const currentTheme = getPreferredTheme();
    setTheme(currentTheme);
    showActiveTheme(currentTheme);

    document.querySelectorAll('[data-bs-theme-value]').forEach(toggle => {
      toggle.addEventListener('click', () => {
        const selectedTheme = toggle.getAttribute('data-bs-theme-value');
        setStoredTheme(selectedTheme);
        setTheme(selectedTheme);
        showActiveTheme(selectedTheme, true);
      });
    });
  });
})();