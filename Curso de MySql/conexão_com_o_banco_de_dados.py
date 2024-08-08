class Conexão:
    def __init__(self):
        self.__dado = None

        with open('conexão_mysqlbd.txt', 'r', encoding='utf-8') as arquivo:
            self.__dado = arquivo.readlines()

        for p, c in enumerate(self.__dado):
            if '\n' in c:
                self.__dado[p] = c.replace('\n', '')
                
        for p, c in enumerate(self.__dado):
            if 'host' in c:
                self.__dado[p] = c.replace('host= ', '')
            if 'user' in c:
                self.__dado[p] = c.replace('user= ', '')
            if 'password' in c:
                self.__dado[p] = c.replace('password= ', '')

    def get_dado(self):
        return self.__dado