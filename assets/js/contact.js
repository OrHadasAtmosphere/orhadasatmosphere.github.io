// Decode only after a visitor asks to reveal the contact address.
// This discourages basic address scraping; it is not a security boundary.
(() => {
  const encoded = [38, 33, 121, 113, 120, 124, 9, 57, 59, 32, 39, 42, 44, 61, 38, 39, 103, 44, 45, 60];
  document.querySelectorAll('[data-contact]').forEach((button) => {
    button.addEventListener('click', () => {
      const address = String.fromCharCode(...encoded.map((value) => value ^ 73));
      const text = document.createElement('span');
      text.className = 'email-address';
      text.tabIndex = -1;
      text.textContent = address.replace('@', ' [at] ').replaceAll('.', ' [dot] ');
      button.replaceWith(text);
      text.focus();
    }, { once: true });
  });
})();
