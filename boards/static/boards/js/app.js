function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

var csrftoken = Cookies.get('csrftoken');

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$('#boards-search').popover({
    html: true,
    content: $('#boards-search .list'),
    placement: 'bottom',
    trigger: 'manual',
    container: '#boards-search',
    template: `
        <div class="popover popover-search-boards w-100" role="tooltip">
            <h3 class="popover-header"></h3>
            <div class="popover-body"></div>
        </div>`
})

$('#boards-search > .search').blur((e) => {
    $('#boards-search').popover('hide')
    $(e.target).val('')
})

const boardsList = new List('boards-search', {
    valueNames: ['title', 'owner'],
    item: "<li><span class='title'></span><span class='owner'></span></li>",
});

const noItemsFound = $('<li class="list-group-item"><h5 class="mb-0 text-center">No boards found</h5></li>');

boardsList.on('updated', function (list) {
     if (list.matchingItems.length == 0 || $('#boards-search > .search').val() === '') {
        while (list.list.firstChild) {
            list.list.removeChild(list.list.firstChild);
        }
        $(list.list).append(noItemsFound);
    } else {
        noItemsFound.detach();
    }

    $('#boards-search').popover('show')
});