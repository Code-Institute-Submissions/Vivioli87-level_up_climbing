var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'), { container: 'body' })
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl)
    })
    var popover = new bootstrap.Popover(document.querySelector('.popover-dismiss'), {
        trigger: 'focus'
    })