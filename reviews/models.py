from django.db import models

class Review(models.Model):
    teacher_name = models.CharField(max_length=255)
    student_id = models.CharField(max_length=50)
    subject = models.CharField(max_length=255)
    grade_received = models.CharField(max_length=5, blank=True, null=True)
    teacher_behavior = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    grading_criteria = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    teaching_quality = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review_text = models.TextField()
    approved = models.BooleanField(default=False)  # ✅ Only approved reviews are shown

    def __str__(self):
        return f"{self.teacher_name} - {self.student_id}"

