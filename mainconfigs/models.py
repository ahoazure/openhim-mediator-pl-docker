from django.db import models

"""
Model for making is earsier to change the base URls for openIMIS.
openHIM and the mediators.

The the upstream server urls for openHIM, openIMIS and mediators 
For more information on this file, contact the Python developers
Stephen Mburu:ahoazure@gmail.com & Peter Kaniu:peterkaniu254@gmail.com

"""

# This model is used to facilitate changing URLs on admin
class configs(models.Model):
    # Server and authetication variables for connecting to openIMIS server
    openimis_url = models.CharField(max_length=200,verbose_name='OpenIMIS URL') #base url
    openimis_port = models.IntegerField(verbose_name='Port') #port
    openimis_user = models.CharField(max_length=200, verbose_name='User') #auth user
    openimis_passkey = models.CharField(max_length=200,verbose_name='Password') #auth pass


    # Server and authetication variables for connecting to MIFOS X server
    mifos_url = models.CharField(max_length=200,verbose_name='MiFOS URL') #base url
    mifos_port = models.IntegerField(verbose_name='Port') #port
    mifos_user = models.CharField(max_length=200, verbose_name='User') #auth user
    mifos_tenant = models.CharField(max_length=200,verbose_name='Tenant') #auth tenant
    mifos_passkey = models.CharField(max_length=200,verbose_name='Password') #auth pass

    # Server and authetication variables for connecting to openHIM server
    openhim_url = models.CharField(max_length=200,verbose_name='OpenHIM URL') #base url
    openhim_port = models.IntegerField(verbose_name='API Port')
    openhim_user = models.CharField(max_length=200,verbose_name='Client Name') #auth user
    openhim_passkey = models.CharField(max_length=200,verbose_name='Password') #auth pass


    # Base and port variables for connecting to python mediator to register with openHIM
    mediator_url = models.CharField(max_length=200,verbose_name='Mediator URL')
    mediator_port = models.IntegerField(verbose_name='Mediator Port')

    class Meta:
        managed = True
        db_table = 'mediator_configs'
        verbose_name = 'Configuration'
        verbose_name_plural = 'Configurations'
        

    def __str__(self):
        return self.openimis_url

    # Override Save method to store only one instance
    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)