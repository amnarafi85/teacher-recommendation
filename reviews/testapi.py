import requests

url = "http://127.0.0.1:8080/api/reviews/"
data = {
    "teacher_name": "Dr. Atif Alvi",
    "student_id": "123456",
    "subject": "Data Structures",
    "grade_received": "A",
    "teacher_behavior": 5,  # Required (1-5)
    "grading_criteria": 4,  # Required (1-5)
    "teaching_quality": 5,  # Required (1-5)
    "review_text": "Great teacher, explains concepts well!"  # Required
}

response = requests.post(url, json=data)

print("Response Status Code:", response.status_code)
print("Response JSON:", response.json())

