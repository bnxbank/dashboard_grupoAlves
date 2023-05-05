google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawCharts);

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

function drawCharts() {
  var columnTitles = [
    'ITENSENTRADA', 'ITENSVENDIDOS', 'Faturamento', 'Rentabilidade', 'FxR', 'sku', 'SKUESTOQUE', 'Margem de Lucro', 'Preço Médio de Venda',
  ];

  for (var i = 1; i <= columnTitles.length; i++) {
    drawIndividualChart(i, columnTitles[i - 1]);
  }
}

function drawIndividualChart(chartIndex, columnTitle) {
  var data = google.visualization.arrayToDataTable([
    ['Month', columnTitle],
    ['Janeiro', allData[0][chartIndex - 1]],
    ['Fevereiro', allData[1][chartIndex - 1]],
    ['Março', allData[2][chartIndex - 1]],
    ['Abril', allData[3][chartIndex - 1]],
    ['Maio', allData[4][chartIndex - 1]],
    ['Junho', allData[5][chartIndex - 1]],
    ['Julho', allData[6][chartIndex - 1]],
    ['Agosto', allData[7][chartIndex - 1]],
    ['Setembro', allData[8][chartIndex - 1]],
    ['Outubro', allData[9][chartIndex - 1]],
    ['Novembro', allData[10][chartIndex - 1]],
    ['Dezembro', allData[11][chartIndex - 1]],
  ]);

  var view = new google.visualization.DataView(data);
  view.setColumns([0, 1, {
    calc: function (dt, rowIndex) {
      return dt.getFormattedValue(rowIndex, 1);
    },
    type: 'string',
    role: 'annotation'
  }]);

  var chartColors = ['#FF0000', '#00FF00', '#0000FF',
    '#a6a13a', '#FF00FF', '#00FFFF', '#800000',
    '#008000', '#000080'];

 var options = {
  title: columnTitle,
  curveType: 'function',
  colors: [chartColors[chartIndex % chartColors.length]],
  pointSize: 5,
  width: '15%', // Diminua o valor para deixar os gráficos mais estreitos
  height: 60, // Aumente o valor para deixar os gráficos mais compridos
  legend: { position: 'none' }
};

  var chart = new google.visualization.LineChart(document.getElementById('chart' + chartIndex));
  chart.draw(view, options);
}