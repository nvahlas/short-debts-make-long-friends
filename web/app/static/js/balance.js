var eventId,participantId;

function euros(amount) {
    return new Number(Math.round(amount*100)/100);
}

function addExpense(event) {
    $('#balance').fadeOut();
    $('#expense').fadeIn();
    
    $.ajax({
        url: '/rest/event/'+eventId+'/expense_types',
        type: 'GET',
        contentType: 'application/json',
        dataType: 'json',
        success: function(data) {
            $('#expense_type option').remove();
            $(data).each(function(idx, item) {
                $('#expense_type').append(
                    $('<option/>', {'value': item.id}).text(item.name)
                )
            });
            
        }
    })
    
    $.ajax({
        url: '/rest/event/'+eventId+'/participants',
        type: 'GET',
        contentType: 'application/json',
        dataType: 'json',
        success: function(data) {
            $('#expense_detail ul li').remove();
            $(data).each(function(idx, item) {
                $('#expense_detail ul').append(
                    $('<li/>', {'id': item.id})
                        .html('<input type="checkbox" id="'+item.id+'" checked="checked" />' + item.first_name + ' ' + item.last_name)
                )
            });
            
        }
    })
}

function sendExpense(event) {
    var participants = new Array();
    $('#expense_detail ul li input').each(function(idx, checkbox) {
        if ( $(checkbox).is(':checked') )
            participants.push({'id': $(checkbox).attr('id') });
    });
    
    $.ajax({
        url: '/rest/add_expense',
        type: 'POST',
        contentType: 'application/json',
        dataType: 'json',
        data: $.toJSON({
            'expense_type': {'id': $('#expense_type').val()},
            'event':        {'id': eventId},
            'amount':       euros($('#expense_amount').val()),
            'payer':        {'id': participantId},
            'participants': participants
        }),
        success: function() {
            back();
        }
    })
}

function back(event) {
    $('#balance').fadeIn();
    $('#expense').fadeOut();
}

function load() {
    $.ajax({
        url: '/rest/calculator',
        type: 'GET',
        contentType: 'application/json',
        dataType: 'json',
        success: function(data) {
            eventId = data.event.id;
            $('#title').text(data.event.name);
            $('#amount').html(data.amount + ' &euro;');
            $('#tendancy-img').attr( 'src', data.participantAmount >= 0?'/static/img/sun.png':'/static/img/cloud.png' );
            $('#participantAmount').html(data.participant.group.name + '<br/>' + euros(data.participantAmount) + ' &euro;');
        }
    })
    
    setTimeout(load, 2000);
}

function render() {
    $('#addExpense').button().click(addExpense);
    $('#back').button().click(back);
    $('#sendExpense').button().click(sendExpense);
}
