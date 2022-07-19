from django.db import models
from django.conf import settings

from django.utils import timezone

# Create your models here.

class Localite(models.Model):
    district_list=(('A','Abidjan'),('B','Bas_Sassandra'),('C','Comoe'),('D','Denguele'),('G','Goh_Djiboua'),('L','Lacs'),('La','Lagunes'),('M','Montagnes'),('SM','Sassandra_Marahoue'),('Sa','Savanes'),('Va','Vallee_du_Bandama'),('W','Woroba'),('Y','Yamoussoukro'),('Za','Zanzan'))
    district=models.CharField(max_length=100,blank=False,choices=district_list)
    list_region=(('A','Abidjan'),('AT','Agneby_tiassa'),('Ba','Bafing'),('Ba','Bagoue'),('Be','Belier'),('B','Bere'),('Bo','Bounkani'),('Ca','Cavally'),('Fo','Folon'),('Gb','Gbeke'),('Gbo','Gbokle'),('Go','Goh'),('Gu','Guemon'),('In','Indenie_djuablin'),('Ka','Kabadougou'),('Na','Nawa'),('Lo','Loh_Djiboua'),('If',' Iffou'),('Mo','Moronou'),('Nz','Nzi'),('LM','La_Me'),('To','Tonkpi'),('Hs','Haut_Sassandra'),('Mr','Marahoué'),('Po','Poro'),('Tc','Tchologo'),('Ha','Hambol'),('Go','Gontougou'),('Sp','San_pedro'),('Sc','Sud_Comoe'),('Wo','Worodougou'))
    region=models.CharField(max_length=100,blank=False,choices=list_region)
    departement=models.CharField(max_length=100,blank=False)
    sous_prefecture=models.CharField(max_length=100,blank=False)
    commune=models.CharField(max_length=100,blank=False)
    milieu_r=models.CharField(max_length=100,blank=False)
    quartier=models.CharField(max_length=100,blank=False)
    def __str__(self):
        return '{}_{}'.format(self.commune,self.quartier)

class Affecter(models.Model):
    agentr=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    localite=models.ForeignKey(Localite,on_delete=models.CASCADE)
    create=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{}_{}'.format(self.agentr,self.localite)

class Personne(models.Model):
    agentr=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    nom=models.CharField(max_length=100,blank=False)
    prenom=models.CharField(max_length=100,blank=False)
    annee_naissance=models.DateField(blank=False)
    lieu_de_naissance=models.CharField(max_length=100,blank=False,default="abidjan")
    nationalite=models.CharField(max_length=100,blank=False,default="ivoirienne")
    numero_cni=models.CharField(max_length=100,blank=False)
    sexe=(('M','Maxculin'),('F','Feminin'))
    sexes=models.CharField(max_length=1,choices=sexe)
    ethnie=models.CharField(max_length=100,blank=False)
    class Meta:
        abstract=True
    def __str__(self):
        return '{}_{}'.format(self.nom,self.prenom)



class Chef_menage(Personne):
    id=models.BigAutoField(primary_key=True)
    type_m=(('M','Monogamie'),('P','Polygamie'))
    type_mariage=models.CharField(max_length=100,blank=False,choices=type_m)
    immigre=models.BooleanField(default=False)
    def __str__(self):
        return '{}_{}'.format(self.nom,self.prenom)

class Conjoint(Personne):
    id=models.BigAutoField(primary_key=True)
    niveau_etude=models.CharField(max_length=100,blank=True,default='master')
    occupation=models.CharField(max_length=100,blank=True,default='Informaticien')
    idc=models.ForeignKey(Chef_menage,on_delete=models.CASCADE)
    def __str__(self):
        return '{}_{}'.format(self.nom,self.prenom)

class Recenser(models.Model):
    parent=models.ForeignKey(Chef_menage,on_delete=models.CASCADE)
    list_religion=(('C','Catholique'),('M','Méthodique'),('E','Evangélique'),('Ce','Céleste'),('H','Harriste'),('Au','AutreRC'),('Mu','Mulsuman'),('An','Animiste'),('Au','AutreR'),('S','Sans_Religion'))
    religion=models.CharField(max_length=100,blank=False,choices=list_religion)
    list_handicap=(('S','Sans_Handicap'),('Nv','Non_voyant'),('So','Sourd'),('Mu','Muet'),('Be','Begue'),('Al','Albinos'),('Hms','Handicap_membre_superieurs'),('Hmi','Handicap_membre_inferieurs'),('Hp','Handicap_physiques'),('Au','Autre_handicap'))
    handicap=models.CharField(max_length=100,blank=False,choices=list_handicap)
    list1=(('Vm','Vie_Ménage'),('Hm','Hors_Ménage'),('D','Décédé'),('N','RAS'))
    survie_de_mere=models.CharField(max_length=100,blank=False,choices=list1)
    survie_de_pere=models.CharField(max_length=100,blank=False,choices=list1 )
    alphabetisation=models.BooleanField(default=False)
    niveau_instruction=models.CharField(max_length=100,blank=False)
    status_occupation=models.CharField(max_length=100,blank=False)
    occupation_actuelle=models.CharField(max_length=100,blank=False)
    situation_occupation=models.CharField(max_length=100,blank=False)
    branche_activite=models.CharField(max_length=100,blank=False)
    situation_matrimoniale=models.CharField(max_length=100,blank=False)
    nombre_enfant=models.IntegerField(default=0)
    nombre_enfant_v=models.IntegerField(default=0)
    class Meta:
        ordering=['parent']
    def __str__(self):
        return '{}'.format(self.parent)

class Migrant(models.Model):
    parentm=models.ForeignKey(Chef_menage,on_delete=models.CASCADE)
    deplace=models.BooleanField()
    annee_deplace=models.DateField(blank=False)
    lieu_residence_a=models.CharField(max_length=100,blank=False)
    intention_ret=models.BooleanField()
    class Meta:
        ordering=['parentm']
    def __str__(self):
        return '{}'.format(self.parent)
        
class Enfant(Personne):
    parentf=models.ForeignKey(Chef_menage,on_delete=models.CASCADE)
    ecolier=models.CharField(max_length=100,blank=True,default='oui')
    id1=models.BigAutoField(primary_key=True)

class Commodite(models.Model):
    parentc=models.ForeignKey(Chef_menage,on_delete=models.CASCADE)
    nombre_piece=models.CharField(max_length=100,blank=False)
    nombre_piece_dormir=models.CharField(max_length=100,blank=False)
    nature_mur=models.CharField(max_length=100,blank=False)
    nature_toit=models.CharField(max_length=100,blank=False)
    nature_sol=models.CharField(max_length=100,blank=False)
    lieu_aisance=models.CharField(max_length=100,blank=False)
    alimentation_eau=models.CharField(max_length=100,blank=False)
    temps_acces_eau=models.CharField(max_length=100,blank=False)
    eclairage=models.CharField(max_length=100,blank=False)
    cuisson=models.CharField(max_length=100,blank=False)
    evacuation_ordure=models.CharField(max_length=100,blank=False)
    evacuation_eau=models.CharField(max_length=100,blank=False)
    loyer=models.CharField(max_length=100,blank=False)
    class Meta:
        ordering=['parentc']

class Equipement(models.Model):
    parente=models.ForeignKey(Chef_menage,on_delete=models.CASCADE)
    moyen_deplacement=models.CharField(max_length=100,blank=False)
    equipement_electr=models.CharField(max_length=100,blank=False)
    equipement_audio=models.CharField(max_length=100,blank=False)
    statut_occupation=models.CharField(max_length=100,blank=False)
    class Meta:
        ordering=['parente']

class Deces(models.Model):
    parentd=models.ForeignKey(Chef_menage,on_delete=models.CASCADE)
    sexed=(('M','Maxculin'),('F','Feminin'))
    sexesd=models.CharField(max_length=1,choices=sexed)
    age_deces=models.PositiveBigIntegerField()
    nom_decede=models.CharField(max_length=100,blank=False)
    prenom_decede=models.CharField(max_length=100,blank=False)
    annee_deces=models.DateField(blank=False)
    class Meta:
        ordering=['parentd']
    def __str__(self):
        return '{}_{}'.format(self.nom_decede,self.prenom_decede)

class Emigration(models.Model):
    parentd=models.ForeignKey(Chef_menage,on_delete=models.CASCADE)
    sexed=(('M','Maxculin'),('F','Feminin'))
    sexesd=models.CharField(max_length=1,choices=sexed)
    date_depart=models.DateField(null=True)
    motif=models.CharField(max_length=100,blank=False)
    age_depart=models.PositiveBigIntegerField()
    
    class Meta:
        ordering=['parentd']
    def __str__(self):
        return '{}_{}'.format(self.nom_decede,self.prenom_decede)