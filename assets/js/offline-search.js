/* global jQuery, lunr, bootstrap */

(function ($) {
  'use strict';

  $(document).ready(function () {
    const $searchInput = $('.td-search input');

    //
    // Register handler
    //
    $searchInput.on('change', (event) => {
      render($(event.target));

      // Hide keyboard on mobile browser
      $searchInput.blur();
    });

    // Prevent reloading page by enter key on sidebar search.
    $searchInput.closest('form').on('submit', () => false);

    //
    // Lunr
    //
    let idx = null; // Lunr index
    const resultDetails = new Map(); // Will hold the data for the search results (titles and summaries)

    // Load the search index JSON data created by Hugo
    $.ajax($searchInput.data('offline-search-index-json-src')).then((data) => {
      idx = lunr(function () {
        this.ref('ref');

        // Specify searchable fields with boosts
        this.field('title', { boost: 5 });
        this.field('categories', { boost: 3 });
        this.field('tags', { boost: 3 });
        this.field('description', { boost: 2 });
        this.field('body');

        data.forEach((doc) => {
          this.add(doc);

          resultDetails.set(doc.ref, {
            title: doc.title,
            excerpt: doc.excerpt,
          });
        });
      });

      // Trigger initial search if input has value
      $searchInput.trigger('change');
    });

    const render = ($targetSearchInput) => {
      //
      // Dispose existing popover
      //
      const popover = bootstrap.Popover.getInstance($targetSearchInput[0]);
      if (popover) {
        popover.dispose();
      }

      //
      // Search
      //
      if (!idx) return;

      const searchQuery = $targetSearchInput.val();
      if (!searchQuery) return;

      const results = idx
        .query((q) => {
          const tokens = lunr.tokenizer(searchQuery.toLowerCase());
          tokens.forEach((token) => {
            const queryString = token.toString();
            q.term(queryString, { boost: 100 });
            q.term(queryString, {
              wildcard: lunr.Query.wildcard.LEADING | lunr.Query.wildcard.TRAILING,
              boost: 10,
            });
            q.term(queryString, { editDistance: 2 });
          });
        })
        .slice(0, $targetSearchInput.data('offline-search-max-results'));

      //
      // Build result HTML
      //
      const $html = $('<div>');

      $html.append(
        $('<div>')
          .css({ display: 'flex', justifyContent: 'space-between', marginBottom: '1em' })
          .append($('<span>').text('Search results').css({ fontWeight: 'bold' }))
          .append($('<span>').addClass('td-offline-search-results__close-button'))
      );

      const maxHeight = `calc(100vh - ${
        $targetSearchInput.offset().top - $(window).scrollTop() + 180
      }px)`;

      const $searchResultBody = $('<div>').css({ maxHeight, overflowY: 'auto' });
      $html.append($searchResultBody);

      if (results.length === 0) {
        $searchResultBody.append(
          $('<p>').text(`No results found for query "${searchQuery}"`)
        );
      } else {
        results.forEach((r) => {
          const doc = resultDetails.get(r.ref);
          const href = $searchInput.data('offline-search-base-href') + r.ref.replace(/^\//, '');

          const $entry = $('<div>').addClass('mt-4');
          $entry.append(
            $('<small>').addClass('d-block text-body-secondary').text(r.ref)
          );
          $entry.append(
            $('<a>')
              .addClass('d-block')
              .css({ fontSize: '1.2rem' })
              .attr('href', href)
              .text(doc.title)
          );
          $entry.append($('<p>').text(doc.excerpt));

          $searchResultBody.append($entry);
        });
      }

      $targetSearchInput.one('shown.bs.popover', () => {
        $('.td-offline-search-results__close-button').on('click', () => {
          $targetSearchInput.val('');
          $targetSearchInput.trigger('change');
        });
      });

      const newPopover = new bootstrap.Popover($targetSearchInput, {
        content: $html[0],
        html: true,
        customClass: 'td-offline-search-results',
        placement: 'bottom',
      });
      newPopover.show();
    };
  });
})(jQuery);