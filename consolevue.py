class ConsoleVue:
    """
    Class gérant les affichages sur la sortie standard.
    """

    def __init__(self, maximum: int):
        """
        Initialise une nouvelle instance de la classe 'ConsoleVue'. ;
        :param maximum: La larguer maximum d'une ligne. ;
        """
        self.MAXIMUM = maximum
        self.PREVIOUS_MESSAGE_LENGTH: int = 0

        self.SUCCES = "[OK]"
        self.ERREUR = "[ERREUR]"

        self.INFO: str = "   [INFO] "
        self.ACTION: str = " [ACTION] "

    def remplir_espace(self, caractere: str) -> str:
        """
        Méthode permettant de remplir l'espace restant d'une ligne avec un caractère désigné. ;
        :param caractere : Le caractère de complétion. ;
        :return : Une chaîne de caractère de la longueur de l'espace nécessaire.
        """
        maximum: int = self.MAXIMUM - self.PREVIOUS_MESSAGE_LENGTH
        index: int = 0

        resultat: str = ""

        while index < maximum:
            resultat += caractere
            index += 1

        return resultat

    def __imprimer_resultat__(self, resultat: str, message: (str | None), caractere: str):
        """
        Affiche sur la sortie standard un résultat. ;
        :param resultat: Le résultat de l'opération. ;
        :param message : Le message de du résultat si nécessaire.
        :param caractere : Le caractere de complétion.
        """
        self.PREVIOUS_MESSAGE_LENGTH = self.PREVIOUS_MESSAGE_LENGTH + len(resultat)
        a_transmettre = self.remplir_espace(caractere) + resultat + "\n"

        print(a_transmettre, end="") if message is None \
            else print(a_transmettre + message + "\n", end="")

    def __imprimer_ligne__(self, info: str, message: str, caractere: str):
        """
        Imprime sur la sortie standard une ligne complète. ;
        :param info: Le type de message. ;
        :param message : Le message à afficher. ;
        :param caractere: Le caractère de complétion. ;
        """
        self.PREVIOUS_MESSAGE_LENGTH = len(message) + len(info)
        a_transmettre = info + message + self.remplir_espace(caractere) + "\n"

        print(a_transmettre, end="")

    def titre(self, titre):
        """
        Affiche sur la sortie standard un titre. ;
        :param titre : Le titre à afficher. ;
        """
        self.PREVIOUS_MESSAGE_LENGTH = 0
        message: str = self.remplir_espace("x") + "\n"

        self.PREVIOUS_MESSAGE_LENGTH = len(titre) + 2 + (self.MAXIMUM - (len(titre)))/2
        message += "x" + self.remplir_espace(" ") + titre + self.remplir_espace(" ") + "x\n"

        self.PREVIOUS_MESSAGE_LENGTH = 0
        message += self.remplir_espace("x") + "\n"

        print(message, end="")

    def sous_titre_1(self, sous_titre):
        """
        Affiche sur la sortie standard un sous-titre (niveau 1). ;
        :param sous_titre : Le sous-titre à afficher. ;
        """
        self.PREVIOUS_MESSAGE_LENGTH = len(sous_titre) + 2 + (self.MAXIMUM - (len(sous_titre) + 2)) / 2
        message: str = "[" + self.remplir_espace("#") + " " + sous_titre + " " + self.remplir_espace("#") + "]\n"

        #self.PREVIOUS_MESSAGE_LENGTH = 0
        # message += self.remplir_espace("-") + "\n"

        print(message, end="")

    def sous_titre_2(self, sous_titre):
        """
        Affiche sur la sortie standard un titre (niveau 2). ;
        :param sous_titre : Le sous-titre à afficher. ;
        """
        self.PREVIOUS_MESSAGE_LENGTH = len(sous_titre) + (self.MAXIMUM - (len(sous_titre))) / 2
        message: str = self.remplir_espace("_") + sous_titre + self.remplir_espace("_") + "\n"

        self.PREVIOUS_MESSAGE_LENGTH = 0
        #message += self.remplir_espace("-") + "\n"

        print(message, end="")

    def info(self, message: str):
        """
        Imprime sur la sortie standard un message d'information.;
        :param message: Le message d'information.
        """
        self.__imprimer_ligne__(self.INFO, message, ".")

    def action(self, message: str):
        """
        Imprime sur la sortie standard un message d'action.;
        :param message: Le message d'action.
        """
        self.PREVIOUS_MESSAGE_LENGTH = len(message) + len(self.ACTION)
        print(self.ACTION + message, end="")

    def erreur(self, message: str, exception: (Exception | None)):
        """
        Imprime sur la sortie standard un message d'erreur.;
        :param exception: L'exception qui pourrait être à l'origine de l'erreur.
        :param message: Le message d'erreur.
        """
        self.__imprimer_resultat__(self.ERREUR, message, ".")
        if exception is not None:
            print("Et voici l'exception qui en est la cause :\n" + str(exception))

    def succes(self, message: (str | None)):
        """
        Imprime sur la sortie standard un message de succes.;
        :param message: Le message d'erreur.
        """
        self.__imprimer_resultat__(self.SUCCES, message, ".")
