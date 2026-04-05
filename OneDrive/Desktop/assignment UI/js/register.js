document.addEventListener('DOMContentLoaded', function() {

  const vehicleType = document.getElementById('vehicle-type');
if (vehicleType) {
vehicleType.addEventListener('change', function() {
const ninSection = document.getElementById('nin-section');
if (ninSection) {
if (this.value === 'Boda-boda') {
ninSection.style.display = 'block';
} else {
ninSection.style.display = 'none';
}
}
});
}

  document.getElementById('registration-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const name = document.getElementById('driver-name').value;
    const plate = document.getElementById('plate').value;
    const phone = document.getElementById('phone').value;

    if (!validateName(name)) {
      alert('Name must start with a capital letter and have no numbers');
      return;
    }

    if (!validatePlate(plate)) {
      alert('Plate must start with U and be max 8 characters');
      return;
    }

    if (!validatePhone(phone)) {
      alert('Enter a valid Ugandan phone number');
      return;
    }

    alert('Vehicle registered successfully!');
  });

});