const ARRIVALS = [
  { time: '10:45 AM', plate: 'UBD 123X', type: 'Sedan', status: 'Parked' },
  { time: '10:32 AM', plate: 'UAU 890L', type: 'SUV', status: 'Signed Out' },
  { time: '10:15 AM', plate: 'UBK 442A', type: 'Motorcycle', status: 'Parked' },
  { time: '09:58 AM', plate: 'UBA 551G', type: 'Van', status: 'Parked' },
  { time: '09:40 AM', plate: 'UBH 200W', type: 'Sedan', status: 'Signed Out' }
];

function renderTable(rows) {
  const tbody = document.getElementById('arrivals-tbody');
  tbody.innerHTML = '';
  rows.forEach(function(row) {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${row.time}</td>
      <td>${row.plate}</td>
      <td>${row.type}</td>
      <td>${row.status}</td>
    `;
    tbody.appendChild(tr);
  });
}

document.addEventListener('DOMContentLoaded', function() {
  renderTable(ARRIVALS);
});