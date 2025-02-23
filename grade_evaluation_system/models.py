from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator


# Subjects
class Subject(models.Model):
    """Subjects Information"""
    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.subject_name}"

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    
# Informations of instructor
class Instructor(models.Model):
    """Instructor Information."""
    instructor_id_number = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject_handled = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string represented of the Model."""
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructors"

# Course
class Course(models.Model):
    course = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string represented of the Model."""
        return f"{self.course}"
    
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
    
# Grades
class Grade(models.Model):
    """Students grades evaluation"""
    student_number = models.CharField(max_length=10)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)])
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    mid_terms_grade = models.DecimalField(max_digits=10, decimal_places = 2, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    finals_grade = models.DecimalField(max_digits=10, decimal_places = 2, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    average = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    remarks = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_number} - {self.remarks}"
    
    class Meta:
        verbose_name = "Grade"
        verbose_name_plural = "Grades"