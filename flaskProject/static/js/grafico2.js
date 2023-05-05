google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
  var data = google.visualization.arrayToDataTable([
    ['Month', 'Vendas'],
    ['Janeiro', 11355189],
    ['Fevereiro', 11896319],
    ['Março', 13589381],
    ['Abril', 12237109],
    ['Maio', 13556538],
    ['Junho', 12737822],
    ['Julho', 13870218],
    ['Agosto', 13865484],
    ['Setembro', 13481756],
    ['Outubro', 11863401],
    ['Novembro', 12996121],
    ['Dezembro', 13510175]
  ]);


  var options = {
    title: 'Desempenho da Empresa',
    curveType: 'function',
    legend: { position: 'bottom' }
  };

   var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

  chart.draw(data, options);
}