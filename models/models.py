# -*- coding: utf-8 -*-

from odoo import models, fields,api
from datetime import date
class ClientNotaire(models.Model):
    _name="notaire.client"
    _description = "Client"

    nom = fields.Char("Nom",required=True)
    prenom= fields.Char("Prénom",required=True)
    lieu_de_naissance= fields.Char("Lieu de naissance",required=True)
    date_de_naissance= fields.Date("Date de naissance", required=True)
    numero_acte_naissance= fields.Integer("Numéro d'acte de naissance")
    metier= fields.Char("Metier")
    adresse= fields.Char("adresse", required=True)
    numero_carte_identite = fields.Char("Numéro de carte d'idendité")
    date_carte_identite = fields.Date("Date de sortie de la carte d'identité")
    lieu_carte_identite = fields.Char("Lieu de sortie de la carte d'identité")
    numero_identification_national= fields.Char("Numéro d'identification_national")
    natioanalite = fields.Char("Nationalité", default="جزائرية")




class Assurance(models.Model):
    _name="notaire.assurance"
    _description = 'Assurance de bien'
    nom= fields.Char("Nom de propiétaire", required=True)
    prenom = fields.Char("Prénom de propriétaire",required= True)
    sexe = fields.Selection([('homme', 'Homme'), ('femme', 'Femme')])

    agence = fields.Char(string="Nom d'agence d'assurance", required=True)
    adresse_agence = fields.Char("Adresse de l'agence")
    date_assurance= fields.Date(string="Date d'assurance")
    type_assurance= fields.Char(string="Type assurance")



class Bien(models.Model):
    _name="notaire.bien"
    _description = "Le Bien"
    assurance = fields.Many2one("notaire.assurance",string="Assurance")
    Position = fields.Char('Etage et appartement')
    adresse = fields.Char("adresse", required=True)
    pieces = fields.Char("pieces de l'appartement", required=True)
    superficie = fields.Float("superficie")

class Appartement(models.Model):
    _name="notaire.appartement"
    _description = "Appartement"

    Position = fields.Char('Etage et appartement')
    adresse = fields.Char("adresse", required=True)
    pieces = fields.Char("pieces de l'appartement", required=True)
    superficie = fields.Float("superficie")

class Villa(models.Model):
    _name="notaire.appartement"
    _description = "Appartement"

    Position = fields.Char('Etage et appartement')
    adresse = fields.Char("adresse", required=True)
    pieces = fields.Char("pieces de l'appartement", required=True)
    superficie = fields.Float("superficie")


class Acte(models.Model):
    _name = "notaire.acte"
    _description = "Acte"
    categorie = fields.Selection([("location", "Location"), ("vente", "Vente"), ("donation", "Donation"),("fredha","Fredha")],
                                 string="Categorie",readonly=True)
    bien = fields.Many2one("notaire.bien",string="Bien")
    client_rec = fields.Many2one("notaire.client",string="Client Receive")
    client_des = fields.Many2many("notaire.client",string="Client Destinataire")


class Location(models.Model):
    _inherit = "notaire.acte"
    _name="notaire.location"
    _description = "Location"

    prix_lettre= fields.Char("prix en lettres", required=True)
    prix_chiffre= fields.Char('Prix en chiffres', required=True)
    duree_lettre = fields.Char("Durée de location en lettres")
    duree_chiffre= fields.Char("Durée de location en chiffres")
    debut = fields.Date("Date de debut de location")
    fin = fields.Date('Date de fin de location')


class Vente(models.Model):
    _inherit = "notaire.acte"
    _name="notaire.vente"
    _description = "Vente"

    prix_lettre= fields.Char("prix en lettres", required=True)
    prix_chiffre= fields.Char('Prix en chiffres', required=True)
    debut = fields.Date("Date de debut de vente")



