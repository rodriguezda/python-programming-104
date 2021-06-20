import csv

employees = [
  {
    "first_name": "Bill",
    "last_name": "Lumbergh",
    "job_title": "Vice President",
    "hire_date": 1985,
    "performance_review": "excellent"
  }, {
    "first_name": "Michael",
    "last_name": "Bolton",
    "job_title": "Programmer",
    "hire_date": 1995,
    "performance_review": "poor"
  }, {
    "first_name": "Peter",
    "last_name": "Gibbons",
    "job_title": "Programmer",
    "hire_date": 1989,
    "performance_review": "poor"
  }, {
    "first_name": "Samir",
    "last_name": "Nagheenanajar",
    "job_title": "Programmer",
    "hire_date": 1974,
    "performance_review": "fair"
  }, {
    "first_name": "Milton",
    "last_name": "Waddams",
    "job_title": "Collator",
    "hire_date": 1974,
    "performance_review": "does he even work here?"
  }, {
    "first_name": "Bob",
    "last_name": "Porter",
    "job_title": "Consultant",
    "hire_date": 1999,
    "performance_review": "excellent"
  }, {
    "first_name": "Bob",
    "last_name": "Slydell",
    "job_title": "Consultant",
    "hire_date": 1999,
    "performance_review": "excellent"
  }
]

# Open/create a file called "tps_report.csv." The "w" means write mode.
with open("tps_report.csv", "w", newline="") as csvfile:

  # Define the header row (the top row).
  fieldnames = ["first_name", "last_name", "job_title", "hire_date", "performance_review"]

  # Open the `DictWriter` and provide the expected fieldnames.
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

  # Write out the header (this only needs to be done once!).
  writer.writeheader()

  # Loop through each employee.
  for person in employees:

    # Write out the employee's data to your report.
    writer.writerow(person)
