google.charts.load('current', {packages: ['corechart']});
google.charts.setOnLoadCallback(function () {
    drawCharts(allData, ''); // Dados de 2023
    drawCharts(allData2022, '2022'); // Dados de 2022
});

var allData = [
    [11355189, 11718061, 62468095.57, 12596033.16, 20.16, 11552, 13118, 10.58, 5.32],
    [11896319, 11183848, 61055572.19, 12859511.51, 21.06, 11353, 12949, 11.13, 5.46],
    [13589381, 11961338, 68567964.06, 14712653.97, 21.46, 11411, 13319, 11.14, 5.73],
    [12237109, 12020019, 71098304.87, 14210656.16, 19.99, 11475, 13050, 11.19, 5.91],
    [13556538, 12168837, 70810820.90, 13735203.40, 19.40, 11420, 12971, 10.92, 5.83],
    [12737822, 11947683, 69850925.44, 13815450.16, 19.78, 11385, 12828, 11.14, 5.84],
    [13870218, 12246174, 72887743.77, 14073049.80, 19.31, 11506, 13173, 10.68, 5.96],
    [13865484, 12556573, 73508469.37, 13443927.25, 18.29, 11497, 13174, 9.98, 5.86],
    [13481756, 11978051, 69041381.49, 13265398.77, 19.21, 11498, 13269, 10.89, 5.76],
    [11863401, 12196536, 71017607.07, 13489160.19, 18.99, 11467, 13209, 10.97, 5.83],
    [12996121, 11185470, 66867305.91, 12765939.66, 19.09, 9714, 12992, 11.57, 6.00],
    [13510175, 11923872, 76916857.02, 14875790.73, 19.34, 9940, 13308, 19.31, 6.45],
];

var allData2022 = [
    [458903, 764104, 9567205.57, 1245233.16, 22.16, 15840, 24128, 12.58, 6.32],
    [578244, 936292, 7885899.19, 1383722.51, 24.06, 16741, 21049, 14.13, 7.46],
    [894502, 842509, 5796122.06, 1512367.97, 23.46, 14251, 16319, 15.14, 6.73],
    [764802, 915710, 6760894.87, 1470196.16, 21.99, 13752, 16560, 16.19, 7.01],
    [951331, 868602, 6842430.90, 1435532.40, 20.40, 13658, 15871, 14.92, 6.93],
    [874921, 838912, 6750901.44, 1341376.16, 20.78, 12655, 14782, 16.14, 6.94],
    [945740, 876192, 6789438.77, 1427245.80, 21.31, 14406, 16897, 15.68, 7.06],
    [942662, 965432, 7598847.37, 1337729.25, 19.29, 14105, 17232, 14.98, 6.86],
    [812401, 854302, 6979081.49, 1305731.77, 21.21, 13219, 16698, 15.89, 6.76],
    [938402, 785302, 6587421.07, 1285501.19, 20.99, 12467, 15679, 16.97, 7.03],
    [1078522, 663329, 5248603.91, 1209289.66, 21.09, 11474, 12992, 17.57, 8.00],
    [843937, 865332, 7592743.02, 1397701.73, 21.34, 11409, 16308, 20.31, 8.45]
];

function drawCharts(dataSet, idSuffix) {
    var columnTitles = [
        'ITENSENTRADA',
        'ITENSVENDIDOS',
        'Faturamento',
        'Rentabilidade',
        'FxR',
        'sku',
        'SKUESTOQUE',
        'Margem de Lucro',
        'Preço Médio de Venda',
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

    var chartColors = [
        '#FF0000',
        '#00FF00',
        '#0000FF',
        '#a6a13a',
        '#FF00FF',
        '#00FFFF',
        '#800000',
        '#008000',
        '#000080',
    ];

   var options = {
    title: columnTitle,
    curveType: 'function',
    colors: [chartColors[chartIndex % chartColors.length]],
    pointSize: 5,
    width: '59%%', // Atualizar a largura aqui
    height: 60, // Atualizar a altura aqui
    legend: {position: 'none'},
};
    // var options = {
    //     title: columnTitle,
    //     curveType: 'function',
    //     colors: [chartColors[chartIndex % chartColors.length]],
    //     pointSize: 5,
    //     width: '15%',
    //     height: 60,
    //     legend: {position: 'none'},
    // };



    var chart = new google.visualization.LineChart(
        document.getElementById('chart' + chartIndex + idSuffix)
    );
    chart.draw(view, options);
}