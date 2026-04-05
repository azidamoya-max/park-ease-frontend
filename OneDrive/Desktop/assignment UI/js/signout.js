const MOCK_VEHICLES = [
  {
    plate: 'UAX 123A',
    driverName: 'John Baptist Ssemuwemba',
    vehicleType: 'Truck',
    arrivalTime: new Date(Date.now() - 4 * 60 * 60 * 1000)
  },
  {
    plate: 'UBD 456K',
    driverName: 'Amina Nakayima',
    vehicleType: 'Personal Car',
    arrivalTime: new Date(Date.now() - 2 * 60 * 60 * 1000)
  }
];

function searchVehicle() {
  const query = document.getElementById('search-input').value.trim().toLowerCase();
  const found = MOCK_VEHICLES.find(function(v) {
    return v.plate.toLowerCase().replace(/\s/g, '').includes(query.replace(/\s/g, ''));
  });

  if (!found) {
    alert('No vehicle found. Try a different plate number.');
    return;
  }

  const now = new Date();
  const durationMs = now - found.arrivalTime;
  const durationHrs = durationMs / (1000 * 60 * 60);
  const fee = durationHrs < 3 ? 2000 : 5000;

  document.getElementById('detail-driver').textContent = found.driverName;
  document.getElementById('detail-type').textContent = found.vehicleType;
  document.getElementById('fee-amount').textContent = 'UGX ' + fee.toLocaleString();
}