$('document').ready(function () {
  $('INPUT#btn_translate').click(function () {
    translate();
  });

  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) {
      translate();
    }
  });
});

function translate () {
  $.get('https://hellosalut.stefanbohacek.dev/',
    { lang: $('#language_code').val() },
    function (data) {
      $('DIV#hello').html(data.hello);
    }
  );
}
