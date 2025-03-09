from Personne import Personne

class Compte_bancaire():
    """
    Définition d'un compte bancaire.

    Attributs
    ---------
    - proprietaire : Personne
        Personne propriétaire du compte. Initialisé à la création de l'objet.
    - identifiant : int
        Identifiant unique du compte. Initialisé à la création de l'objet par un calcul réalisé par une méthode statique.
    - solde : float
        Solde du compte. Initialisé à la création de l'objet.
    """

    def __init__(self, proprietaire, montant_initial):
        """
        Initialisation des attributs.
        """
        self.proprietaire = proprietaire
        self.identifiant = self.determine_id(proprietaire)
        self.solde = montant_initial

    @staticmethod
    def determine_id(proprietaire):
        """
        Détermine l'identifiant du compte à partir du
        nom et du prénom du propriétaire.
        """
        identite = proprietaire.nom + proprietaire.prenom
        return len(identite) * 12345 % 10**8

    def obtenir_solde(self):
        """
        Retourne le solde du compte.
        """
        return self.solde

    def depot(self, montant):
        """
        Ajoute montant au solde
        """
        if montant > 0:
            self.solde += montant
        else:
            print("Le montant du dépôt doit être positif")

    def retrait(self, montant):
        """
        Retire le montant du solde à la condition qu'il y ait suffisamment d'argent.
        """
        if montant <= 0:
            print("Le montant du retrait doit être positif")
            return None
        if montant > self.solde:
            print("Fonds insuffisants")
            return None
        self.solde -= montant


    def infos(self):
        """
        Informations sur le compte.
        """
        chaine = " Compte numéro : {} / Solde : {}".format(self.identifiant, self.solde)
        chaine += self.proprietaire.infos()

        return chaine
