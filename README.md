# Projet_Django_Flutter

# Mon Projet
un site internet complet avec une base de données, représentant un blog du festival afronation 2k24
## Description
Développez une interface d'application mobile avec Flutter qui doit être connectée au backend Django.
Mettre en place un système d'authentification avec JWT.
Affichage les articles (photos/vidéos AFN2k24) créés à partir de Django dans l'application mobile.
S'assurez que les modifications apportées aux articles depuis l'application mobile sont renvoyées à Django.

## Installation des packages et initialisation du projet
  I. Back end (Django & DRF)
  Installation de django-environ: pip install django-environ

ignorer les variables d'environnement avec .gitignore
    

1. Installation Django & DRF : " pip install django " ; " pip install djangorestframework "
2. Création du projet Django : " django-admin startproject BlogAFN_2k24 . "
3. Création de l'application Django : " django-admin startapp BlogAFN "
4. Première migration & syncronisation : " python manage.py migrate "
5. Création du compte administrateur : " python manage.py createsuperuser --email brunondjeff@gmail.com --username admin " ; pwd : " NNbb2001 "
6. Modifier le fichier setting.py et ajouter quelques informations: INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'BlogAFN',
    'rest_framework'
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

7.
   


## Modèle de données
Création du modèle dans BlogAFN/models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=1024)
    author = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

Creation du fichier serializer qui convertira les objets du modèle Article en format JSON pour les utiliser dans notre API. 

Modifier le fichier views.py  ViewSet Django REST Framework qui  permettra de créer une API pour afficher et éditer des Articles.

Modifier le fichier BlogAFN_2k24/urls.py afin de configurer les URL pour une l'app Django  avec une API REST pour gérer les articles, en utilisant le module d’administration de Django et le Django REST framework

Mise à jour de la BD avec le nouveau modèle de données : python manage.py makemigrations
Suivi d'une migration :  python manage.py migrate

Connexion au compte administrateur puis création d'un nouvel utilisateur

#Utilisation de JWT
Installation JWT : pip install djangorestframework_simplejwt

## Inscription d’un user 
 Creation de l'application "jwauth": python manage.py startapp jwtauth

Test de l'api d'authentification via Postman :  http://localhost:8000/api/jwtauth/register/

Documentation des API avec Swagger : pip install django-rest-swagger

## Structure du Projet
lancement du serveur : python manage.py runserver
- ...

## Contributions
Les contributions sont les bienvenues ! Suivez ces étapes :
1. Fork ce dépôt.
2. Créez une branche (`git checkout -b feature/nouvelle-fonctionnalite`).
3. Faites vos modifications.
4. Soumettez une pull request.

## Licence
Ce projet est sous licence MIT.

## Contact
Contactez-moi à contact@monprojet.com.
