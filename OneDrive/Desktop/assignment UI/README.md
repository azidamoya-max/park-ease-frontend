# ParkEase Frontend

## Project Description
ParkEase is a parking management web application built for the Refactory CSE programme.

## Pages
- index.html — Login page
- dashboard.html — Attendant dashboard
- register.html — Vehicle registration
- signout.html — Vehicle sign-out and receipting
- reports.html — Admin revenue reports

## How to Run
1. Clone the repo
2. Open index.html in your browser
3. Login with: admin / admin123

## Author
Azida — Refactory CSE 2026
## Project Description
ParkEase is a parking management system frontend built with HTML, CSS and JavaScript.

## Features Implemented
- [x] Login page with role-based redirect
- [x] Attendant Dashboard
- [x] Vehicle Registration with form validation
- [x] Sign-out page with fee calculation
- [x] Admin Reports page with table filtering

## Validation Rules Applied
- Driver name must start with capital letter, no numbers
- Number plate must start with U, max 8 characters
- Phone number must be valid Ugandan format (+256 or 07xx)
- NIN required for Boda-boda only

## Known Issues / Assumptions
- Mock data used for vehicle records (no backend)
- Fee calculation based on hardcoded rates