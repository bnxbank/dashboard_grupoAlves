google.charts.load('current', { 'packages': ['line'] });
google.charts.setOnLoadCallback(drawCharts);

var allData = [  [11355189, 11718061, 62468095.57, 12596033.16, 20.16, 11552, 13118],
  [11896319, 11183848, 61055572.19, 12859511.51, 21.06, 11353, 12949],
  [13589381, 11961338, 68567964.06, 14712653.97, 21.46, 11411, 13319],
  [12237109, 12020019, 71098304.87, 14210656.16, 19.99, 11475, 13050],
  [13556538, 12168837, 70810820.90, 13735203.40, 19.40, 11420, 12971],
  [12737822, 11947683, 69850925.44, 13815450.16, 19.78, 11385, 12828],
  [13870218, 12246174, 72887743.77, 14073049.80, 19.31, 11506, 13173],
  [13865484, 12556573, 73508469.37, 13443927.25, 18.29, 11497, 13174],
  [13481756, 11978051, 69041381.49, 13265398.77, 19.21, 11498, 13269],
  [11863401, 12196536, 71017607.07, 13489160.19, 18.99, 11467, 13209],
  [12996121, 11185470, 66867305.91, 12765939.66, 19.09, 9714, 12992],
  [13510175, 11923872, 76916857.02, 14875790.73, 19.34, 9940, 13308]
];

function drawCharts() {
  var columnTitles = [    'ITENSENTRADA',    'ITENSVENDIDOS',    'Faturamento',    'Rentabilidade',
      'FxR',    'sku',    'SKUESTOQUE',  ];

  for (var i = 1; i <= columnTitles.length; i++) {
    drawIndividualChart(i, columnTitles[i - 1]);
  }
}

function drawIndividualChart(chartIndex, columnTitle) {
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Month');
  data.addColumn('number', columnTitle);

  data.addRows([    ['Janeiro', allData[0][chartIndex - 1]],
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

       var chartColors = ['#FF0000', '#00FF00', '#0000FF',
           '#FFFF00', '#FF00FF', '#00FFFF', '#800000', '#008000',
           '#000080'];

       var options = {
         chart: {
           title: columnTitle + ' - Data Visualization',
           subtitle: 'in appropriate units',
         },
         colors: [chartColors[chartIndex % chartColors.length]],
         pointSize: 5,
         width: '20%',
         height: 200,
       };

       var chart = new google.charts.Line(
         document.getElementById('chart' + chartIndex)
       );

       chart.draw(data, google.charts.Line.convertOptions(options));
     }