var next_page
var previous_page

function get_table() {
    let param = 'api/get_table?'
    param += 'filter_column=' + document.getElementById("filter_column").value + '&'
    param += 'filter_condition=' + document.getElementById("filter_condition").value + '&'
    param += 'value=' + document.getElementById("value").value + '&'
    param += 'sort_column=' + document.getElementById("sort_column").value + '&'
    param += 'sort_condition=' + document.getElementById("sort_condition").value
    send_request(param)
}


function send_request(param) {
    $.ajax({
        method: 'GET',
        url: param,
        success: function (result) {
            update_table(result);
        },
    });
}


function update_table(data) {
    let row;
    let all_rows = '';

    Object.keys(data['results']).forEach(key => {
        elem = data['results'][key];
        row = '<tr><td>' + elem['title'] + '</td>' + '<td>' + elem['amount'] + '</td>' + '<td>' + elem['distance'] + '</td>' + '<td>' + elem['date'] + '</td>' + '</tr>';
        all_rows = all_rows + row;
    });

    next_page = data['links']['next'];
    previous_page = data['links']['previous'];

    $('#myTable tbody').html(all_rows);
}


window.onload = function () {
    send_request('api/get_table?');

    next_page_button.onclick = function () {
        send_request(next_page);
    };
    previous_page_button.onclick = function () {
        send_request(previous_page);
    };
};
