$(function () {
    $('[data-toggle="popover"]').popover({
        container: 'body'
    })
    $('.popover-dismiss').popover({
        trigger: 'focus'
      })
  })