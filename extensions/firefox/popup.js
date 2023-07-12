console.warn("popup.js started");
document.getElementById("downloadJson").addEventListener('click', () => {

    browser.tabs.executeScript({ file: 'json_download.js' })

});

document.getElementById("downloadCsv").addEventListener('click', () => {

    browser.tabs.executeScript({ file: 'csv_download.js' })

});

