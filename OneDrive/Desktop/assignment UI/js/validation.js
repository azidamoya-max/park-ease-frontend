function validateName(name) {
  return /^[A-Z][a-zA-Z\s'-]{1,}$/.test(name.trim());
}

function validatePlate(plate) {
  const clean = plate.replace(/\s/g, '');
  return /^U[A-Z0-9]{2,6}$/.test(clean);
}

function validatePhone(phone) {
  const clean = phone.replace(/\s/g, '');
  return /^(\+256|0)(7|6)\d{8}$/.test(clean);
}

function validateNIN(nin) {
  return /^[A-Z]{2}[0-9A-Z]{8,10}[A-Z]$/i.test(nin.trim());
}