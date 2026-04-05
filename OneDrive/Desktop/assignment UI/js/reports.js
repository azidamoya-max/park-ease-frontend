const TRANSACTIONS = [
  { receipt: '#PE-98231', plate: 'KAA 123X', inTime: '08:15 AM', outTime: '05:30 PM', duration: '9h 15m', fee: 'UGX 45,000' },
  { receipt: '#PE-98232', plate: 'KCB 776L', inTime: '09:00 AM', outTime: '11:30 AM', duration: '2h 30m', fee: 'UGX 5,000' },
  { receipt: '#PE-98233', plate: 'KDD 001A', inTime: '07:45 AM', outTime: '06:15 PM', duration: '10h 30m', fee: 'UGX 50,000' },
  { receipt: '#PE-98234', plate: 'KBA 999Z', inTime: '11:20 AM', outTime: '02:45 PM', duration: '3h 25m', fee: 'UGX 8,000' },
  { receipt: '#PE-98235', plate: 'KBX 442W', inTime: '06:00 AM', outTime: '08:00 PM', duration: '14h 00m', fee: 'UGX 70,000' }
];

let currentPage = 1;
const rowsPerPage = 5;

function renderReports(data) {
  const tbody = document.getElementById('reports-tbody');
  tbody.innerHTML = '';
  const start = (currentPage - 1) * rowsPerPage;
  const pageData = data.slice(start, start + rowsPerPage);
  pageData.forEach(function(row) {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${row.receipt}</td>
      <td>${row.plate}</td>
      <td>${row.inTime}</td>
      <td>${row.outTime}</td>
      <td>${row.duration}</td>
      <td>${row.fee}</td>
    `;
    tbody.appendChild(tr);
  });
}

document.addEventListener('DOMContentLoaded', function() {
  renderReports(TRANSACTIONS);

  document.getElementById('table-filter').addEventListener('input', function() {
    const query = this.value.toLowerCase();
    const filtered = TRANSACTIONS.filter(function(row) {
      return row.plate.toLowerCase().includes(query) ||
             row.receipt.toLowerCase().includes(query);
    });
    currentPage = 1;
    renderReports(filtered);
  });
});