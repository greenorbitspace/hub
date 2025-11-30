{{ with .Site.Params.plantuml }}
{{ if .enable }}
{{ if .svg }}
// https://unpkg.com/external-svg-loader@1.3.4/svg-loader.min.js
(function() {
  // ... (external-svg-loader code as is) ...
})();
{{ end }}

(function($) {
  'use strict';

  // Encode input string to PlantUML compressed base64 format
  function encode64(data) {
    let r = '';
    for (let i = 0; i < data.length; i += 3) {
      if (i + 2 === data.length) {
        r += append3bytes(data.charCodeAt(i), data.charCodeAt(i + 1), 0);
      } else if (i + 1 === data.length) {
        r += append3bytes(data.charCodeAt(i), 0, 0);
      } else {
        r += append3bytes(data.charCodeAt(i), data.charCodeAt(i + 1), data.charCodeAt(i + 2));
      }
    }
    return r;
  }

  function append3bytes(b1, b2, b3) {
    const c1 = b1 >> 2;
    const c2 = ((b1 & 0x3) << 4) | (b2 >> 4);
    const c3 = ((b2 & 0xF) << 2) | (b3 >> 6);
    const c4 = b3 & 0x3F;
    let r = '';
    r += encode6bit(c1 & 0x3F);
    r += encode6bit(c2 & 0x3F);
    r += encode6bit(c3 & 0x3F);
    r += encode6bit(c4 & 0x3F);
    return r;
  }

  function encode6bit(b) {
    if (b < 10) return String.fromCharCode(48 + b);
    b -= 10;
    if (b < 26) return String.fromCharCode(65 + b);
    b -= 26;
    if (b < 26) return String.fromCharCode(97 + b);
    b -= 26;
    if (b === 0) return '-';
    if (b === 1) return '_';
    return '?';
  }

  $('.language-plantuml').parent().replaceWith(function() {
    // Get PlantUML source text and UTF-8 encode it
    const source = unescape(encodeURIComponent($(this).text()));

    {{ if .svg }}
    // Insert SVG element with PlantUML server URL and encoded diagram
    return $('<svg data-src="{{ .svg_image_url | default "//www.plantuml.com/plantuml/svg/" }}' + encode64(deflate(source, 9)) + '">');
    {{ else }}
    // Insert IMG element with PlantUML server URL and encoded diagram
    return $('<img src="{{ .svg_image_url | default "//www.plantuml.com/plantuml/svg/" }}' + encode64(deflate(source, 9)) + '">');
    {{ end }}
  });
})(jQuery);
{{ end }}
{{ end }}