# -*- coding: utf-8 -*-

from odoo import models, fields,api
from datetime import date

class Notaire(models.Model):
    _name="notaire.notaire"
    _description = "Notaire model"

    prenom= fields.Char(string="Prénom", required=True)
    nom=fields.Char(string="Nom", required=True)
    date_naissance= fields.Date(string="Date de Naissance", required=True)
    adresse_complete= fields.Char(string="Adresse", required=True)
    tel= fields.Integer(string="Numéro de téléphone")

    email = fields.Char(string="Email")

    # Calculer l'âge en fonction de la date de naissance
    @api.depends('date_naissance')
    def _compute_age(self):
        today = date.today()
        for notaire in self:
            if notaire.date_naissance:
                birth_date = fields.Date.from_string(notaire.date_naissance)
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                notaire.age = age
            else:
                notaire.age = 0

    age = fields.Integer(string="Age", compute="_compute_age",store=True)



class Client(models.Model):
    _name="notaire.client"
    nom=fields.Char(string="Nom",required=True)
    prenom=fields.Char(string="Prénom",required=True)
    date_naissance = fields.Date(string="Date de Naissance")
    lieux_naissance= fields.Char(string="Lieux de Naissance")
    sequence_acte_naissance= fields.Integer(string="La séquence d'acte de naissance")
    metier = fields.Char(string="Métier")
    adresse= fields.Char(string="Adresse")
    type_carte= fields.Char(string="type de la carte (permis, carte d'identité ...)")
    num_carte = fields.Char(string="Numéro de la carte")
    date_carte= fields.Date(string="Date de sortie de la carte")
    lieu_carte = fields.Char(string="Lieu de sortie de la carte")
    num_identite_nationale= fields.Char(string="Numéro d'identité nationale")
    nationalite= fields.Char(string="Nationalité")

    def __str__(self):
        return self.nom + " " + self.prenom

class Assurance(models.Model):
    _name="notaire.assurance"
    _description = 'Assurance de bien'

    agence = fields.Char(string="Nom d'agence", required=True)
    date_assurance= fields.Date(string="Date d'assurance")
    type_assurance= fields.Char(string="Type assurance")

    def __str__(self):
        return self.agence



class Bien(models.Model):
    _name="notaire.bien"
    _description = "Le Bien"

    type = fields.Selection([("appartement", "Appartement"),("villa", "Villa"),("terrain","Terrain")],string="Type de Bien",required=True)
    adresse= fields.Char(string="Adresse")
    superficie = fields.Integer(string="Superficie")
    assurance = fields.Many2one("notaire.assurance",string="Assurance")

    def __str__(self):
        return self.type + " en " + self.adresse


class Acte(models.Model):
    _name = "notaire.acte"
    _description = "Acte"
    categorie = fields.Selection([("location", "Location"), ("vente", "Vente"), ("donation", "Donation")],
                                 string="Categorie", required=True)
    client_rec = fields.Many2one("notaire.client",string="Client Receive")
    client_des = fields.Many2many("notaire.client",string="Client Destinataire")
    bien = fields.Many2one("notaire.bien",string="Bien")

    display_name = fields.Char(string="Nom/Prenom/adresse de client", compute="_compute_display_name", store=True)

    def _compute_display_name(self):
        for acte in self:
            if acte.client_rec:
                acte.display_name = f"{acte.client_rec.nom} {acte.client_rec.prenom} {acte.client_rec.adresse}"
            else:
                acte.display_name = "Pas de Nom"
