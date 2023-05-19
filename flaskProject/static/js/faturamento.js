google.charts.load('current', {packages: ['corechart']});
google.charts.setOnLoadCallback(function () {
    drawCharts(allData2022, '2022'); // Dados de 2022
    drawCharts(allData2021, '2021'); // Dados de 2021
});

var allData2022 = [
    [11355189, 11718061, 62468095.57],
    [11896319, 11183848, 61055572.19],
    [13589381, 11961338, 68567964.06],
    [12237109, 12020019, 71098304.87],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
];

var allData2021 = [
    [458903, 764104, 9567205.57],
    [578244, 936292, 7885899.19],
    [894502, 842509, 5796122.06],
    [764802, 915710, 6760894.87],
    [951331, 868602, 6842430.90],
    [874921, 838912, 6750901.44],
    [945740, 876192, 6789438.77],
    [942662, 965432, 7598847.37],
    [812401, 854302, 6979081.49],
    [938402, 785302, 6587421.07],
    [1078522, 663329, 5248603.91],
    [843937, 865332, 7592743.02]
];
var allData2020 = [
    // Dados para 2020
     [458903, 764104, 9567205.57],
    [578244, 936292, 7885899.19],
    [894502, 842509, 5796122.06],
    [764802, 915710, 6760894.87],
    [951331, 868602, 6842430.90],
    [874921, 838912, 6750901.44],
    [945740, 876192, 6789438.77],
    [942662, 965432, 7598847.37],
    [812401, 854302, 6979081.49],
    [938402, 785302, 6587421.07],
    [1078522, 663329, 5248603.91],
    [843937, 865332, 7592743.02]
];

var allData2019 = [
    // Dados para 2019
     [458903, 764104, 9567205.57],
    [578244, 936292, 7885899.19],
    [894502, 842509, 5796122.06],
    [764802, 915710, 6760894.87],
    [951331, 868602, 6842430.90],
    [874921, 838912, 6750901.44],
    [945740, 876192, 6789438.77],
    [942662, 965432, 7598847.37],
    [812401, 854302, 6979081.49],
    [938402, 785302, 6587421.07],
    [1078522, 663329, 5248603.91],
    [843937, 865332, 7592743.02]
];

var allData2018 = [
    // Dados para 2018
     [458903, 764104, 9567205.57],
    [578244, 936292, 7885899.19],
    [894502, 842509, 5796122.06],
    [764802, 915710, 6760894.87],
    [951331, 868602, 6842430.90],
    [874921, 838912, 6750901.44],
    [945740, 876192, 6789438.77],
    [942662, 965432, 7598847.37],
    [812401, 854302, 6979081.49],
    [938402, 785302, 6587421.07],
    [1078522, 663329, 5248603.91],
    [843937, 865332, 7592743.02]
];

var allData2017 = [
    // Dados para 2017
     [458903, 764104, 9567205.57],
    [578244, 936292, 7885899.19],
    [894502, 842509, 5796122.06],
    [764802, 915710, 6760894.87],
    [951331, 868602, 6842430.90],
    [874921, 838912, 6750901.44],
    [945740, 876192, 6789438.77],
    [942662, 965432, 7598847.37],
    [812401, 854302, 6979081.49],
    [938402, 785302, 6587421.07],
    [1078522, 663329, 5248603.91],
    [843937, 865332, 7592743.02]
];

var allData2016 = [
    // Dados para 2016
     [458903, 764104, 9567205.57],
    [578244, 936292, 7885899.19],
    [894502, 842509, 5796122.06],
    [764802, 915710, 6760894.87],
    [951331, 868602, 6842430.90],
    [874921, 838912, 6750901.44],
    [945740, 876192, 6789438.77],
    [942662, 965432, 7598847.37],
    [812401, 854302, 6979081.49],
    [938402, 785302, 6587421.07],
    [1078522, 663329, 5248603.91],
    [843937, 865332, 7592743.02]
];




   var chartColors = [
        '#3374dc',
        '#ffbd15',
        '#067237',
    ];


function drawCharts(dataSet, idSuffix) {
    var columnTitles = [
        'FAT',
        'RENT($)',
        'RENT(%)',
    ];

    for (var i = 1; i <= columnTitles.length; i++) {
        drawIndividualChart(i, columnTitles[i - 1], dataSet, idSuffix);
    }
}

function drawIndividualChart(chartIndex, columnTitle, dataSet, idSuffix) {
    var data = google.visualization.arrayToDataTable([
        ['Month', columnTitle],
        ['Janeiro', dataSet[0][chartIndex - 1]],
        ['Fevereiro', dataSet[1][chartIndex - 1]],
        ['Março', dataSet[2][chartIndex - 1]],
        ['Abril', dataSet[3][chartIndex - 1]],
        ['Maio', dataSet[4][chartIndex - 1]],
        ['Junho', dataSet[5][chartIndex - 1]],
        ['Julho', dataSet[6][chartIndex - 1]],
        ['Agosto', dataSet[7][chartIndex - 1]],
        ['Setembro', dataSet[8][chartIndex - 1]],
        ['Outubro', dataSet[9][chartIndex - 1]],
        ['Novembro', dataSet[10][chartIndex - 1]],
        ['Dezembro', dataSet[11][chartIndex - 1]],
    ]);

    var view = new google.visualization.DataView(data);
    view.setColumns([
        0,
        1,
        {
            calc: function (dt, rowIndex) {
                return dt.getFormattedValue(rowIndex, 1);
            },
            type: 'string',
            role: 'annotation',
        },
    ]);




    var options = {
        curveType: 'function',
        colors: [chartColors[chartIndex % chartColors.length]],
        pointSize: 10,
        vAxis: {
            textPosition: 'none',
            gridlines: {
                color: 'transparent'  // adicione esta linha para remover as linhas de grade verticais
            }
        },
        hAxis: {
            textStyle: {
                color: '#FFFFFF',
                fontName: 'Arial',
                fontSize: 16,
                fontWeight: 'normal'
            },
            gridlines: {
                color: 'transparent'  // adicione esta linha para remover as linhas de grade horizontais
            }
        },
        backgroundColor: '#383838',
        legend: {position: 'none'},
    };
    var chart = new google.visualization.LineChart(
        document.getElementById('chart' + chartIndex + idSuffix)
    );
    chart.draw(view, options);
}
function createLegend(dataSet, id) {
    var legendDiv = document.getElementById(id);
    var columnTitles = [
        'FAT',
        'RENT($)',
        'RENT(%)',
    ];
     var legendHtml = '<ul style="display: flex; flex-wrap: wrap; padding: 0;">';
    for (var i = 0; i < columnTitles.length; i++) {
        legendHtml += '<li style="list-style-type: none; margin-right: 20px;"><span style="color:' + chartColors[i % chartColors.length] +
            '">&#9679;</span> ' + columnTitles[i] + '</li>';
    }
    legendHtml += '</ul>';
    legendDiv.innerHTML = legendHtml;
}

// Chamar a função quando os gráficos são desenhados
google.charts.setOnLoadCallback(function () {
    drawCharts(allData2022, '2022'); // Dados de 2022
    drawCharts(allData2021, '2021'); // Dados de 2021
    drawCharts(allData2020, '2020'); // Dados de 2020
    drawCharts(allData2019, '2019'); // Dados de 2019
    drawCharts(allData2018, '2018'); // Dados de 2018
    drawCharts(allData2017, '2017'); // Dados de 2017
    drawCharts(allData2016, '2016'); // Dados de 2016
     createLegend(allData2022, 'legend2022'); // Cria a legenda para 2022
});
