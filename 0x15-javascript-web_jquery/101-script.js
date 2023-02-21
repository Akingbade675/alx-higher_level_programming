$('document').ready(function () {
  $('#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });

  $('#remove_item').click(function () {
    $('li:last-type-of').remove();
  });

  $('#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
