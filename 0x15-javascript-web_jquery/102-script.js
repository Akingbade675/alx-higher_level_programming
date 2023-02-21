$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $.get('https://hellosalut.stefanbohacek.dev/',
      { lang: $('#language_code').val() },
      function (data) {
        $('DIV#hello').html(data.hello);
      }
    );
  });
});
