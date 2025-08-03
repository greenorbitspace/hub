{{ with .Site.Params.drawio }}
{{ if .enable }}
(function () {
  'use strict';

  let shade;
  let iframe;

  const insertFrame = () => {
    shade = document.createElement('div');
    shade.classList.add('drawioframe');
    iframe = document.createElement('iframe');
    shade.appendChild(iframe);
    document.body.appendChild(shade);
  };

  const closeFrame = () => {
    if (shade) {
      document.body.removeChild(shade);
      shade = undefined;
      iframe = undefined;
    }
  };

  const imghandler = (img, imgdata) => {
    const baseUrl = {{ .drawio_server | default "https://embed.diagrams.net/" | jsonify }};
    const url = `${baseUrl}?embed=1&ui=atlas&spin=1&modified=unsavedChanges&proto=json&saveAndEdit=1&noSaveBtn=1`;

    const wrapper = document.createElement('div');
    wrapper.classList.add('drawio');
    img.parentNode.insertBefore(wrapper, img);
    wrapper.appendChild(img);

    const btn = document.createElement('button');
    btn.classList.add('drawiobtn');
    btn.innerHTML = '<i class="fas fa-edit"></i>';
    wrapper.appendChild(btn);

    btn.addEventListener('click', () => {
      if (iframe) return; // Prevent multiple iframes

      insertFrame();

      const messageHandler = (evt) => {
        const wind = iframe.contentWindow;

        if (evt.source !== wind || !evt.data) return;

        let msg;
        try {
          msg = JSON.parse(evt.data);
        } catch {
          return; // Ignore invalid JSON
        }

        switch (msg.event) {
          case 'init':
            wind.postMessage(JSON.stringify({ action: 'load', xml: imgdata }), '*');
            break;
          case 'save':
            const fmt = imgdata.startsWith('data:image/png') ? 'xmlpng' : 'xmlsvg';
            wind.postMessage(JSON.stringify({ action: 'export', format: fmt }), '*');
            break;
          case 'export':
            const filename = img.src.replace(/^.*?([^/]+)$/, '$1');
            const dl = document.createElement('a');
            dl.href = msg.data;
            dl.download = filename;
            document.body.appendChild(dl);
            dl.click();
            dl.remove();
            break;
          case 'exit':
          case 'export':
            window.removeEventListener('message', messageHandler);
            closeFrame();
            break;
        }
      };

      window.addEventListener('message', messageHandler);
      iframe.src = url;
    });
  };

  document.addEventListener('DOMContentLoaded', () => {
    // Process all png and svg images for embedded mxfile xml diagrams
    const images = Array.from(document.getElementsByTagName('img'));
    images.forEach((img) => {
      const src = img.getAttribute('src');
      if (!src || (!src.endsWith('.svg') && !src.endsWith('.png'))) {
        return;
      }

      const xhr = new XMLHttpRequest();
      xhr.responseType = 'blob';
      xhr.open('GET', src);
      xhr.onload = () => {
        const reader = new FileReader();
        reader.onload = () => {
          if (reader.result.includes('mxfile')) {
            const dataUrlReader = new FileReader();
            dataUrlReader.onload = () => {
              imghandler(img, dataUrlReader.result);
            };
            dataUrlReader.readAsDataURL(xhr.response);
          }
        };
        reader.readAsBinaryString(xhr.response);
      };
      xhr.send();
    });
  });
})();
{{ end }}
{{ end }}