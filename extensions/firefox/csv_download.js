var gridTable = document.getElementById('FundUxPortfolioDetailTable');
var csvData = [];

// Iteratin over each row in the table, skipping the table header row
for (let i = 1; i < gridTable.rows.length; i++) {
  var row = gridTable.rows[i];
  var rowData = [];

  // each cell in the row
  for (let j = 0; j < row.cells.length; j++) {
    var cell = row.cells[j];
    var cellData = cell.innerText.trim();

    rowData.push(cellData);
  }

  csvData.push(rowData);
}

// CSV content start
var csvContent = 'data:text/csv;charset=utf-8,';

//CSV header row
var headerRow = gridTable.rows[0];
for (let j = 0; j < headerRow.cells.length; j++) {
  var headerCell = headerRow.cells[j].innerText.trim();
  csvContent += `"${headerCell}",`;
}
csvContent += '\n';

// Add the CSV data rows
csvData.forEach(row => {
  row.forEach(cell => {
    csvContent += `"${cell}",`;
  });
  csvContent += '\n';
});

// Download
var encodedUri = encodeURI(csvContent);
var link = document.createElement('a');
link.setAttribute('href', encodedUri);

// file name dd-mm-yyyy.json
var today = new Date();
var fileName = `${today.getDate()}-${today.getMonth() + 1}-${today.getFullYear()}.csv`;

link.setAttribute('download', fileName);
document.body.appendChild(link);

link.click();

document.body.removeChild(link);
