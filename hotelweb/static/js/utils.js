
function updateBooking(url, data) {
    var jqxhr = $.post(url, data, function (booking) {
        $(document).trigger('success', {message: "Successfully updated " + booking.confirmation_number})
    }, 'json');

    jqxhr.fail(function (jqXHR, status, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function add_booking(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('addStop', {booking: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully added " + result.confirmation_number})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function delete_booking(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('addStop', {booking: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully added " + result.confirmation_number})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}