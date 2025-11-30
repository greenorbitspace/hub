{{ with .Site.Params.markmap }}
{{ if .enable }}

(function($) {
  'use strict';

  let needMarkmap = false;

  // Replace parent of elements with class 'language-markmap' with a div.markmap containing the source text
  $('.language-markmap').parent().replaceWith(function() {
    needMarkmap = true;
    return $('<div class="markmap">').text($(this).text());
  });

  // Render all markmaps if any were detected
  if (needMarkmap && window.markmap && window.markmap.autoLoader) {
    window.markmap.autoLoader.renderAll();
  }
})(jQuery);

{{ end }}
{{ end }}