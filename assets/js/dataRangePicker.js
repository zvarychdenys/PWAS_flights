const today = new Date();
    const picker = new Litepicker({
      element: document.getElementById('start-date'),
      elementEnd: document.getElementById('end-date'),
      singleMode: false,
      allowRepick: false,
      autoApply: false,
      minDate: today - 1,
    });