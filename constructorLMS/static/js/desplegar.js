const elements = [
    {button: 'open-close', aside: 'aside'},
    {button: 'open-closeU', aside: 'asideU'},
    {button: 'open-closeC', aside: 'asideC'}
  ];
  
  // Agregar eventos de clic a cada elemento
  elements.forEach(element => {
    const $button = document.getElementById(element.button),
          $aside = document.getElementById(element.aside);
    $button.addEventListener('click', () => {
      $aside.classList.toggle('desplegar');
    });
  });
  
  
  
  
  