google.charts.load('current', { 'packages': ['line'] });

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


function drawCombinedChart() {
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Month');

  // Adicione colunas para cada série de dados
  var columnTitles = ['ITENSENTRADA', 'ITENSVENDIDOS', 'Faturamento', 'Rentabilidade', 'FxR', 'sku', 'SKUESTOQUE'];
  for (var i = 0; i < columnTitles.length; i++) {
    data.addColumn('number', columnTitles[i]);
  }

  // Adicione as linhas de dados
  var monthNames = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'];
  for (var i = 0; i < allData.length; i++) {
    var row = allData[i];
    data.addRow([monthNames[i], ...row]);
  }

  // Defina as cores do gráfico
  var chartColors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF', '#800000', '#008000', '#000080'];

  // Configure as opções do gráfico
  var options = {
    chart: {
      title: 'Data Visualization',
      subtitle: 'in appropriate units',
    },
    colors: chartColors,
    pointSize: 5,
    width: '100%',
    height: 500,
    curveType: 'function'
  };

  // Desenhe o gráfico
  var chart = new google.charts.Line(document.getElementById('combinedChart'));
  chart.draw(data, google.charts.Line.convertOptions(options));
}

google.charts.setOnLoadCallback(drawCombinedChart);
