from django.db import models

# Create your models here.
class Day(models.Model):
    
    prey_choices = [
        ('Done in mosque' , 'Yes in mosque' ),
        ('Done but not in mosque' , 'Yes/no mosque'),
        ('Done but not in mosque and late' , 'Yes/no mosque + late'),
        ('Done but qada\'' , 'Yes/no mosque + qada\''),
        ('Wasn\'t done' ,'NO'),
    ]
    
    quraan_choices = [
        ('Yes' , 'Yes'),
        ('No' , 'No'),
    ]
    
    date = models.DateField(auto_now=False, auto_now_add=False)
    Alfajr = models.CharField(null = True , max_length = 70 , choices = prey_choices)
    Aldohr = models.CharField(null = True , max_length = 70, choices = prey_choices)
    Al3asr = models.CharField(null = True , max_length = 70, choices = prey_choices)
    Almaghrib = models.CharField(null = True , max_length = 70, choices = prey_choices)
    Al3esha = models.CharField(null = True , max_length = 70, choices = prey_choices)
    daily_quraan = models.CharField(null = True , max_length = 70 , choices=quraan_choices)
    tasbee7 = models.CharField(null = True , max_length = 70 , choices = quraan_choices)
    the_thousand_pray = models.CharField(null = True , max_length = 70 , choices = quraan_choices)
    alsonan = models.CharField(null = True , max_length = 70 , choices = quraan_choices)
    notes = models.TextField(null=True)

    def alfajr_points(self):
        points_sum = 0
        if self.Alfajr == 'Done in mosque' :
            points_sum += 4
        elif self.Alfajr == 'Done but not in mosque' :
            points_sum += 3
        elif self.Alfajr == 'Done but not in mosque and late' :
            points_sum += 2
        elif self.Alfajr == 'Done but qada\'' :
            points_sum += 1
        elif self.Alfajr == 'Wasn\'t done' :
            points_sum += -1
        return points_sum

    def aldohr_points(self):
        points_sum = 0
        if self.Aldohr == 'Done in mosque' :
            points_sum += 4
        elif self.Aldohr == 'Done but not in mosque' :
            points_sum += 3
        elif self.Aldohr == 'Done but not in mosque and late' :
            points_sum += 2
        elif self.Aldohr == 'Done but qada\'' :
            points_sum += 1
        elif self.Aldohr == 'Wasn\'t done' :
            points_sum += -1
        return points_sum

    def al3asr_points(self):
        points_sum = 0
        if self.Al3asr == 'Done in mosque' :
            points_sum += 4
        elif self.Al3asr == 'Done but not in mosque' :
            points_sum += 3
        elif self.Al3asr == 'Done but not in mosque and late' :
            points_sum += 2
        elif self.Al3asr == 'Done but qada\'' :
            points_sum += 1
        elif self.Al3asr == 'Wasn\'t done' :
            points_sum += -1
        return points_sum

    def almaghrib_points(self):
        points_sum = 0
        if self.Almaghrib == 'Done in mosque' :
            points_sum += 4
        elif self.Almaghrib == 'Done but not in mosque' :
            points_sum += 3
        elif self.Almaghrib == 'Done but not in mosque and late' :
            points_sum += 2
        elif self.Almaghrib == 'Done but qada\'' :
            points_sum += 1
        elif self.Almaghrib == 'Wasn\'t done' :
            points_sum += -1
        return points_sum

    def al3isha_points(self):
        points_sum = 0
        if self.Al3esha == 'Done in mosque' :
            points_sum += 4
        elif self.Al3esha == 'Done but not in mosque' :
            points_sum += 3
        elif self.Al3esha == 'Done but not in mosque and late' :
            points_sum += 2
        elif self.Al3esha == 'Done but qada\'' :
            points_sum += 1
        elif self.Al3esha == 'Wasn\'t done' :
            points_sum += -1
        return points_sum
    
    def quraan_points(self):
        points_sum = 0
        if self.daily_quraan == 'Yes':
            points_sum+=1
        else:
            points_sum-=1
        return points_sum
    
    def tasbee7_points(self):
        points_sum = 0
        if self.tasbee7 == 'Yes':
            points_sum+=1
        else:
            points_sum-=1
        return points_sum
    
    def the_thousand_pray_points(self):
        points_sum = 0
        if self.the_thousand_pray == 'Yes':
            points_sum+=1
        else:
            points_sum-=1
        return points_sum
    
    def alsonan_points(self):
        points_sum = 0
        if self.alsonan == 'Yes':
            points_sum+=1
        else:
            points_sum-=1
        return points_sum
        
    def points_sum(self):
        salawat_points = self.alfajr_points()+ self.aldohr_points() + self.al3asr_points()+self.almaghrib_points()+self.al3isha_points()
        extra_points = self.alsonan_points() + self.quraan_points()+ self.the_thousand_pray_points()+self.tasbee7_points()
        return salawat_points+extra_points
    
    def __str__(self):
        return str(self.date)
    
    