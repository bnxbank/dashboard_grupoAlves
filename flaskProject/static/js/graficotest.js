function drawIndividualChart(chartIndex, columnTitle, idSuffix) {
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
            '#FF0000',    '#00FF00',       '#0000FF',          '#a6a13a',          '#FF00FF',          '#00FFFF',          '#800000',          '#008000',
          '#000080',
        ];

        var options = {
          title: columnTitle,
          curveType: 'function',
          colors: [chartColors[chartIndex % chartColors.length]],
          pointSize: 5,
          width: '15%',
          height: 60,
          legend: { position: 'none' },
        };

        var chart = new google.visualization.LineChart(
          document.getElementById('chart' + chartIndex + idSuffix)
        );
        chart.draw(view, options);
      }