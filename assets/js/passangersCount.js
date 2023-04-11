var dropdownItems = document.querySelectorAll('.dropdown-item');
    var dropdownButton = document.querySelector('#dropdownMenuButton h6');

    dropdownItems.forEach(function(item) {
      item.addEventListener('click', function() {
        var value = item.getAttribute('data-value');
        dropdownButton.textContent =  'Passengers: ' + value;
        dropdownItems.forEach(function(item) {
          item.classList.remove('active');
        });
        item.classList.add('active');
      });
    });