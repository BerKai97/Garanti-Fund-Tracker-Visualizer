const gridTable = document.getElementById('FundUxPortfolioDetailTable');
const csvData = [];

// Iteratin over each row in the table, skipping the table header row
for (let i = 1; i < gridTable.rows.length; i++) {
  const row = gridTable.rows[i];
  const rowData = [];

  // each cell in the row
  for (let j = 0; j < row.cells.length; j++) {
    const cell = row.cells[j];
    const cellData = cell.innerText.trim();

    rowData.push(cellData);
  }

  csvData.push(rowData);
}

// CSV content start
let csvContent = 'data:text/csv;charset=utf-8,';

//CSV header row
const headerRow = gridTable.rows[0];
for (let j = 0; j < headerRow.cells.length; j++) {
  const headerCell = headerRow.cells[j].innerText.trim();
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
const encodedUri = encodeURI(csvContent);
const link = document.createElement('a');
link.setAttribute('href', encodedUri);
link.setAttribute('download', 'grid_data.csv');
document.body.appendChild(link);

link.click();

document.body.removeChild(link);
