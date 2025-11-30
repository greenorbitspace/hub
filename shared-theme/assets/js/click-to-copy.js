/* global bootstrap */

(() => {
  const codeListings = document.querySelectorAll('.highlight > pre');

  const copyCode = (codeSample) => {
    navigator.clipboard.writeText(codeSample.textContent.trim() + '\n');
  };

  codeListings.forEach((pre) => {
    const codeSample = pre.querySelector('code');
    if (!codeSample) return;

    const copyButton = document.createElement('button');
    const buttonAttributes = {
      type: 'button',
      title: 'Copy to clipboard',
      'data-bs-toggle': 'tooltip',
      'data-bs-placement': 'top',
      'data-bs-container': 'body',
    };

    Object.entries(buttonAttributes).forEach(([key, value]) => {
      copyButton.setAttribute(key, value);
    });

    copyButton.classList.add(
      'fas',
      'fa-copy',
      'btn',
      'btn-sm',
      'td-click-to-copy'
    );

    const tooltip = new bootstrap.Tooltip(copyButton);

    copyButton.addEventListener('click', () => {
      copyCode(codeSample);
      copyButton.setAttribute('data-bs-original-title', 'Copied!');
      tooltip.show();
    });

    copyButton.addEventListener('mouseout', () => {
      copyButton.setAttribute('data-bs-original-title', 'Copy to clipboard');
      tooltip.hide();
    });

    const buttonDiv = document.createElement('div');
    buttonDiv.classList.add('click-to-copy');
    buttonDiv.appendChild(copyButton);

    pre.insertBefore(buttonDiv, codeSample);
  });
})();