from django.contrib.auth.models import User
from django.db import models
from patients.models import Patient
from testtype.models import TestType
import datetime


# Create your models here.
class SampleData(models.Model):
    class Meta:
        db_table = "sample_data"

    AUTOSCOPE = 'autoscope'
    ACEIT = 'ace_it'
    mode_selection = ((AUTOSCOPE, 'autoscope'), (ACEIT, 'ace_it'))

    image_name = models.CharField(max_length=255)
    result_length = models.IntegerField()
    result = models.CharField(max_length=50)
    test_type = models.ForeignKey(TestType, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    mode = models.CharField(choices=mode_selection, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s  %s" % (self.image_name, self.patient_id.patient_full_name)

    def testdetail(self):
        date_time_obj = datetime.datetime.strptime(str(self.created_at).split('+')[0], '%Y-%m-%d %H:%M:%S.%f')
        date = date_time_obj.date()
        time = datetime.datetime.strptime(str(date_time_obj.time()).split('.')[0][0:5], "%H:%M")
        time = time.strftime("%I:%M %p")
        return {
            'Date_of_test_done': date,
            'Time_of_test_done': time,
            'result': self.result,
            'mode': self.mode
        }

    def calage(self, date):
        today = date.today()
        age = today.year - date.year - ((today.month, today.day) <
                                        (date.month, date.day))
        return age

    def record(self):
        return {
            'patient_id': self.patient_id.id,
            'patient_name': self.patient_id.patient_full_name,
            'patient_age': self.calage(self.patient_id.patient_dob),
            'patient_location': self.patient_id.patient_location,
            'patient_gender': self.patient_id.patient_gender,
        }
