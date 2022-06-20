$(document).ready(function () {
    $('#24htable_id').DataTable({
        ajax: {
            method: 'GET',
            url: 'http://localhost:7000/',
            dataType: 'json',
            dataSrc: '',
        },
        columns: [
            { data: 'symbol' },
            { data: 'priceChangePercent' },
            { data: 'lastPrice' },
            { data: 'volume' },
            { data: 'weightedAvgPrice' },
        ],
        drawCallback: function () {
            $("#24htable_id td").not(":nth-child(1),:nth-child(3),:nth-child(4),:nth-child(5)").colorize()
        }
    }
    );
});