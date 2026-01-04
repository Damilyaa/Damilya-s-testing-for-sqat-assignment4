# Assignment 4 – Advanced Selenium WebDriver Practice

This project is created for Assignment 4 and demonstrates using **Selenium WebDriver with the Page Object Model (POM)**.  
The tests automate a simple flight booking flow using a public demo website.

Website used for testing:  
https://blazedemo.com

---

## Project Structure

```
assignment4/
│
├── pages/
│   ├── base_page.py
│   ├── search_flights_page.py
│   ├── reserve_page.py
│   └── purchase_page.py
│
├── tests/
│   ├── test_positive.py
│   └── test_negative.py
│
├── driver_setup.py
├── requirements.txt
└── README.md
```

- **pages/** – Page Object classes with locators and action methods only  
- **tests/** – Test cases with assertions  
- **driver_setup.py** – WebDriver initialization  
- **requirements.txt** – Python packages for the project  

---

## Technologies Used

- Python 3  
- Selenium WebDriver  
- Pytest  
- Chrome browser  

---

## Setup Instructions

### 1. Clone or download the project

Navigate to the project folder:
```bash
cd Damilya-s-testing-for-sqat-assignment4
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

```bash
source venv/bin/activate
```


### 4. Install dependencies
```bash
pip install -r requirements.txt
```

---

## Running the Tests

**Run all tests**
```bash
pytest
```

**Run a specific test**

Positive test only:
```bash
pytest tests/test_positive.py
```

Negative test only:
```bash
pytest tests/test_negative.py
```

---

## Test Scenarios

### Positive Test

- Search for a flight
- Select a flight
- Enter passenger name
- Complete booking
- Verify confirmation message

### Negative Test

- Try to complete booking without entering the required name
- Verify that a browser validation error message is