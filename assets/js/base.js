/* global jQuery */
/*
 * Copyright 2018 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

(function ($) {
  'use strict';

  // Initialize Bootstrap tooltips and popovers
  $(function () {
    $('[data-bs-toggle="tooltip"]').tooltip();
    $('[data-bs-toggle="popover"]').popover();

    $('.popover-dismiss').popover({
      trigger: 'focus',
    });
  });

  // Calculate the bottom position of an element
  function bottomPos(element) {
    return element.offset().top + element.outerHeight();
  }

  // Bootstrap Fixed Header scroll behavior
  $(function () {
    const promo = $('.js-td-cover');
    if (!promo.length) {
      return;
    }

    const promoOffset = bottomPos(promo);
    const navbar = $('.js-navbar-scroll');
    const navbarOffset = navbar.offset().top;
    const threshold = Math.ceil(navbar.outerHeight());

    if (promoOffset - navbarOffset < threshold) {
      navbar.addClass('navbar-bg-onscroll');
    }

    $(window).on('scroll', function () {
      const promoOffset = bottomPos(promo);
      const navbarOffset = navbar.offset().top;

      if (promoOffset - navbarOffset < threshold) {
        navbar.addClass('navbar-bg-onscroll');
        navbar.removeClass('navbar-bg-onscroll--fade');
      } else {
        navbar.removeClass('navbar-bg-onscroll');
        navbar.addClass('navbar-bg-onscroll--fade');
      }
    });
  });
})(jQuery);