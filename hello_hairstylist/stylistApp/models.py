# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Freelancer(models.Model):
    freelancer_id = models.AutoField(db_column='Freelancer_Id', primary_key=True)  # Field name made lowercase.
    freelancer_ful_name = models.CharField(db_column='Freelancer_Ful_Name', max_length=150)  # Field name made lowercase.
    freelancer_email = models.CharField(db_column='Freelancer_Email', max_length=100)  # Field name made lowercase.
    freelancer_password = models.CharField(db_column='Freelancer_Password', max_length=45)  # Field name made lowercase.
    freelancer_recv_updt = models.IntegerField(db_column='Freelancer_Recv_Updt')  # Field name made lowercase.
    freelancer_contact_no = models.CharField(db_column='Freelancer_Contact_No', max_length=45)  # Field name made lowercase.
    freelancer_location = models.CharField(db_column='Freelancer_Location', max_length=100)  # Field name made lowercase.
    freelancercol = models.CharField(db_column='Freelancercol', max_length=45, blank=True, null=True)  # Field name made lowercase.
    task_task = models.ForeignKey('Task', models.DO_NOTHING, db_column='Task_Task_Id')  # Field name made lowercase.
    task_job_owner_jo = models.ForeignKey('Task', models.DO_NOTHING, db_column='Task_Job_Owner_JO_Id')  # Field name made lowercase.
    freelancer_skills = models.CharField(db_column='Freelancer_Skills', max_length=200, blank=True, null=True)  # Field name made lowercase.
    freelancer_qualifications = models.CharField(db_column='Freelancer_Qualifications', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'freelancer'
        unique_together = (('freelancer_id', 'task_task', 'task_job_owner_jo'),)


class JobOwner(models.Model):
    jo_id = models.AutoField(db_column='JO_Id', primary_key=True)  # Field name made lowercase.
    jo_full_name = models.CharField(db_column='JO_Full_Name', max_length=150)  # Field name made lowercase.
    jo_email = models.CharField(db_column='JO_Email', max_length=100)  # Field name made lowercase.
    jo_password = models.CharField(db_column='JO_Password', max_length=45)  # Field name made lowercase.
    jo_salon_name = models.CharField(db_column='JO_Salon_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    jo_recv_updt = models.IntegerField(db_column='JO_Recv_Updt')  # Field name made lowercase.
    jo_contact_no_off = models.CharField(db_column='JO_Contact_No_Off', max_length=45, blank=True, null=True)  # Field name made lowercase.
    jo_contact_no_personnel = models.CharField(db_column='JO_Contact_No_Personnel', max_length=45)  # Field name made lowercase.
    jo_location = models.CharField(db_column='JO_Location', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'job_owner'


class Payment(models.Model):
    payment_id = models.AutoField(db_column='Payment_Id', primary_key=True)  # Field name made lowercase.
    payement_amount = models.DecimalField(db_column='Payement_Amount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    payment_status = models.CharField(db_column='Payment_Status', max_length=6)  # Field name made lowercase.
    payment_init_date = models.DateField(db_column='Payment_Init_Date')  # Field name made lowercase.
    payment_due_date = models.DateField(db_column='Payment_Due_Date', blank=True, null=True)  # Field name made lowercase.
    job_owner_jo = models.ForeignKey(JobOwner, models.DO_NOTHING, db_column='Job_Owner_JO_Id')  # Field name made lowercase.
    freelancer_freelancer = models.ForeignKey(Freelancer, models.DO_NOTHING, db_column='Freelancer_Freelancer_Id')  # Field name made lowercase.
    task_task = models.ForeignKey('Task', models.DO_NOTHING, db_column='Task_Task_Id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment'
        unique_together = (('payment_id', 'job_owner_jo', 'freelancer_freelancer', 'task_task'),)


class Schedule(models.Model):
    schedule_date = models.DateField(db_column='Schedule_Date', primary_key=True)  # Field name made lowercase.
    schedule_time = models.CharField(db_column='Schedule_Time', max_length=45)  # Field name made lowercase.
    schedule_desc = models.CharField(db_column='Schedule_Desc', max_length=45, blank=True, null=True)  # Field name made lowercase.
    freelancer_freelancer = models.ForeignKey(Freelancer, models.DO_NOTHING, db_column='Freelancer_Freelancer_Id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'schedule'
        unique_together = (('schedule_date', 'schedule_time', 'freelancer_freelancer'),)


class Task(models.Model):
    task_id = models.AutoField(db_column='Task_Id', primary_key=True)  # Field name made lowercase.
    task_date = models.DateField(db_column='Task_Date')  # Field name made lowercase.
    task_time = models.CharField(db_column='Task_Time', max_length=45, blank=True, null=True)  # Field name made lowercase.
    task_status = models.CharField(db_column='Task_Status', max_length=4, blank=True, null=True)  # Field name made lowercase.
    taskcol = models.CharField(db_column='Taskcol', max_length=45, blank=True, null=True)  # Field name made lowercase.
    task_rating = models.CharField(db_column='Task_Rating', max_length=1, blank=True, null=True)  # Field name made lowercase.
    task_review = models.CharField(db_column='Task_Review', max_length=500, blank=True, null=True)  # Field name made lowercase.
    job_owner_jo = models.ForeignKey(JobOwner, models.DO_NOTHING, db_column='Job_Owner_JO_Id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'task'
        unique_together = (('task_id', 'job_owner_jo'),)
