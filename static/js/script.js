// Tema dark/light
const toggle = document.querySelector('.theme-toggle');
const html = document.documentElement;

toggle.addEventListener('click', () => {
  if (html.getAttribute('data-theme') === 'dark') {
    html.setAttribute('data-theme', 'light');
    toggle.innerHTML = '<i class="fas fa-sun"></i>';
  } else {
    html.setAttribute('data-theme', 'dark');
    toggle.innerHTML = '<i class="fas fa-moon"></i>';
  }
  localStorage.setItem('theme', html.getAttribute('data-theme'));
});

// Carregar tema salvo
const savedTheme = localStorage.getItem('theme') || 'dark';
html.setAttribute('data-theme', savedTheme);
toggle.innerHTML = savedTheme === 'dark' 
  ? '<i class="fas fa-moon"></i>' 
  : '<i class="fas fa-sun"></i>';