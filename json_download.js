
const tableElement = document.getElementById('FundUxPortfolioDetailTable');
const jsonData = [];

// Iterat over each row in the table, skipping the table header row
for (let i = 1; i < tableElement.rows.length; i++) {
  const row = tableElement.rows[i];
  const rowData = {};

  // Iterate over each cell in the row
  for (let j = 0; j < row.cells.length; j++) {
    const headerCell = tableElement.rows[0].cells[j].innerText.trim();
    const cell = row.cells[j];
    const cellData = cell.innerText.trim();

    // Add the cell data to the row data object
    rowData[headerCell] = cellData;
  }

  // Push the row data to the JSON data array
  jsonData.push(rowData);
}

// Convert the JSON data to a string
const jsonString = JSON.stringify(jsonData, null, 2);

// Create a Blob object
const blob = new Blob([jsonString], { type: 'application/json' });

// Create a download link
const link = document.createElement('a');
link.setAttribute('href', URL.createObjectURL(blob));

// file name dd-mm-yyyy.json
const today = new Date();
const fileName = `${today.getDate()}-${today.getMonth() + 1}-${today.getFullYear()}.json`;

link.setAttribute('download', fileName);
document.body.appendChild(link);

// Click the download link to trigger the download
link.click();

// Remove the download link from the document
document.body.removeChild(link);
