from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=150, help_text='Название организации', verbose_name='Название организации')
    delivery = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Branch(models.Model):
    address = models.CharField(max_length=100, verbose_name='Адрес', help_text='Введите адрес')
    phone = models.CharField(max_length=13, verbose_name='Телефон', help_text='Введите телефон')
    open_time = models.TimeField()
    close_time = models.TimeField()
    organization = models.ForeignKey(Organization, verbose_name='Организация', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.organization.name},{self.address}'


class Category(models.Model):
    name = models.CharField(max_length=50)


class Medicament(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название', help_text='Название препарата')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField()
    manual = models.TextField()
    manufacturer = models.CharField(max_length=100)
    purpose = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class MedicamentInBranch(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
    count = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.medicament.name
