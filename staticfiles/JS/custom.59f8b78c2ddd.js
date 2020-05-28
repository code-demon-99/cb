function arrayToTable(tableData) {
    var table = $('<table></table>');
    $(tableData).each(function (i, rowData) {
        var row = $('<tr></tr>');
        $(rowData).each(function (j, cellData) {
            row.append($('<td>' + cellData + '</td>'));
        });
        table.append(row);
    });
    return table;
}

$.ajax({
    type: "GET",
    url: "{% static 'CSV/res1.csv' %}",
    success: function (data) {
        let oarr = []
        for (i = 1; i < Papa.parse(data).data.length; i++) {
            oarr.push(Papa.parse(data).data[i][4])
        }
        let uniquestates = [];
        $.each(oarr, function (i, el) {
            if ($.inArray(el, uniquestates) === -1) uniquestates.push(el);
        });

        $.each(uniquestates, function (i, p) {
            $('#selectstate').append($('<option></option>').val(p).html(p));
        });

    }
});


$('#gettable1').click(
    function () {
        $.ajax({
            type: "GET",
            url: "{% static 'CSV/res1.csv' %}",
            success: function (data) {
                let newdata = Papa.parse(data).data
                let selectedstate = $('#selectstate').val()
                $('.table1').empty()
                let tabledata = []
                for (i = 0; i < newdata.length; i++) {
                    if (i == 0) {
                        tabledata.push([newdata[i][1], newdata[i][2], newdata[i][3]])

                    }
                    else {
                        if (newdata[i][4] == selectedstate) {
                            tabledata.push([newdata[i][1], newdata[i][2], newdata[i][3]])

                        }
                    }

                }
                $('.table1').append(arrayToTable(tabledata));

            }
        });
    })
