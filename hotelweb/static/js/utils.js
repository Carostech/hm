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

function updateOrder(url, data) {
    var jqxhr = $.post(url, data, function (order) {
        $(document).trigger('success', {message: "Successfully updated " + order.status})
    }, 'json');

    jqxhr.fail(function (jqXHR, status, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function addOrder(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('addOrder', {order: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully added " + result.order_status})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}


function addFood(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('addFood', {food: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully added " + result.food_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function updateFood(url, data) {
    var jqxhr = $.post(url, data, function (food) {
        $(document).trigger('success', {message: "Successfully updated " + food.food_id})
    }, 'json');

    jqxhr.fail(function (jqXHR, status, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}


function deleteFood(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('deleteFood', {food: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully deleted " + result.food_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}


function addDrink(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('addDrink', {drink: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully added " + result.drink_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function updateDrink(url, data) {
    var jqxhr = $.post(url, data, function (drink) {
        $(document).trigger('success', {message: "Successfully updated " + drink.drink_id})
    }, 'json');

    jqxhr.fail(function (jqXHR, status, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}


function deleteDrink(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('deleteDrink', {drink: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully deleted " + result.drink_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}


function addCommodity(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('addCommodity', {commodity: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully added " + result.commodity_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function updateCommodity(url, data) {
    var jqxhr = $.post(url, data, function (commodity) {
        $(document).trigger('success', {message: "Successfully updated " + commodity.commodity_id})
    }, 'json');

    jqxhr.fail(function (jqXHR, status, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}


function deleteCommodity(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('deleteCommodity', {commodity: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully deleted " + result.commodity_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}


function addSupplier(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('addSupplier', {supplier: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully added " + result.supplier_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function updateSupplier(url, data) {
    var jqxhr = $.post(url, data, function (supplier) {
        $(document).trigger('success', {message: "Successfully updated " + supplier.supplier_id})
    }, 'json');

    jqxhr.fail(function (jqXHR, status, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}


function deleteSupplier(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('deleteSupplier', {supplier: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully deleted " + result.supplier_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}


function addWorker(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('addWorker', {worker: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully added " + result.worker_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function updateWorker(url, data) {
    var jqxhr = $.post(url, data, function (worker) {
        $(document).trigger('success', {message: "Successfully updated " + worker.worker_id})
    }, 'json');

    jqxhr.fail(function (jqXHR, status, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}


function deleteWorker(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('deleteWorker', {worker: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully deleted " + result.worker_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function addLaundryTpeCost(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('addLaundryTpeCost', {laundry: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully added " + result.laundry_item_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function updateLaundryTypeCost(url, data) {
    var jqxhr = $.post(url, data, function (laundry) {
        $(document).trigger('success', {message: "Successfully updated " + laundry.laundry_item_id})
    }, 'json');

    jqxhr.fail(function (jqXHR, status, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}


function deleteLaundryTypeCost(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('deleteLaundryTypeCost', {laundry: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully deleted " + result.laundry_item_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function addFacilityTpe(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('addFacilityTpe', {facility: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully added " + result.facility_type_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function updateFacilityType(url, data) {
    var jqxhr = $.post(url, data, function (facility) {
        $(document).trigger('success', {message: "Successfully updated " + facility.facility_type_id})
    }, 'json');

    jqxhr.fail(function (jqXHR, status, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}


function deleteFacilityType(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('deleteFacilityType', {facility: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully deleted " + result.facility_type_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function addFacility(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('addFacility', {facility: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully added " + result.facility_type_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function updateFacility(url, data) {
    var jqxhr = $.post(url, data, function (facility) {
        $(document).trigger('success', {message: "Successfully updated " + facility.facility_id})
    }, 'json');

    jqxhr.fail(function (jqXHR, status, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}


function deleteFacility(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('deleteFacility', {facility: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully deleted " + result.facility_type_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}


function addRating(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('addRating', {rate: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully added " + result.rating_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function updateRating(url, data) {
    var jqxhr = $.post(url, data, function (rate) {
        $(document).trigger('success', {message: "Successfully updated " + rate.rating_id})
    }, 'json');

    jqxhr.fail(function (jqXHR, status, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}


function deleteRating(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('deleteRating', {rate: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully deleted " + result.rating_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}


function addEvent(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('addEvent', {event: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully added " + result.event_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function updateEvent(url, data) {
    var jqxhr = $.post(url, data, function (event) {
        $(document).trigger('success', {message: "Successfully updated " + event.event_id})
    }, 'json');

    jqxhr.fail(function (jqXHR, status, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}


function deleteEvent(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('deleteEvent', {event: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully deleted " + result.event_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}


function addRoomCleaning(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('addRoomCleaning', {room: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully added " + result.facility_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function updateRoomCleaning(url, data) {
    var jqxhr = $.post(url, data, function (room) {
        $(document).trigger('success', {message: "Successfully updated " + room.facility_id})
    }, 'json');

    jqxhr.fail(function (jqXHR, status, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}


function deleteRoomCleaning(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('deleteRoomCleaning', {event: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully deleted " + result.facility_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}


function addFacilityCleaning(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('addFacilityCleaning', {facility: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully added " + result.facility_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

function updateFacilityCleaning(url, data) {
    var jqxhr = $.post(url, data, function (facility) {
        $(document).trigger('success', {message: "Successfully updated " + facility.facility_id})
    }, 'json');

    jqxhr.fail(function (jqXHR, status, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}


function deleteFacilityCleaning(url, params) {
    var request = $.ajax({
        url: url,
        method: 'POST',
        data: params,
        dataType: 'json'
    });

    request.done(function (result) {
        $(document).trigger('deleteFacilityCleaning', {event: result});
        $('#stop-modal').modal('hide');
        $(document).trigger('success', {message: "Successfully deleted " + result.facility_id})
    });

    request.fail(function (jqXHR, textStatus, error) {
        $(document).trigger('error', {message: 'Failed due to: ' + status + " " + error})
    });
}

