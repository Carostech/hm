function updateBooking(url, data) {
    var jqxhr = $.post(url, data, function (booking) {
        $(document).trigger('success', {message: "Successfully updated " + booking.confirmation_number})
    }, 'json');

    jqxhr.fail(function (jqXHR, status, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function addBooking(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('addBooking', {booking: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully added " + result.confirmation_number})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function deleteBooking(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('deleteBooking', {booking: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully deleted " + result.confirmation_number})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function trackingCheckIn(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('trackingCheckIn', {booking: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully saved check in"})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function trackingCheckOut(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('trackingCheckIn', {booking: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully checked out"})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}