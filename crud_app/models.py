from django.db import models
from datetime import datetime

# Create your model

class create_expense(models.Model):
    user = models.ForeignKey('authentication_app.CustomUser', on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    created_at=models.DateField(default=datetime.now)

    def __str__(self):
        return self.user.username

    #specify the db whare store this db (lable from the project.dbrouter)
    class Meta:
        app_label = 'crud_app'  # Ensure the app label matches the router's route_app_labels
