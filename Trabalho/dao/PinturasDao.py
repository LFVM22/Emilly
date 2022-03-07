from model.Pinturas import Pinturas


class PinturasDao:
    def __init__(self, connection):
        self.connection = connection

    def listarPinturas(self) -> list:
        c = self.connection.cursor()
        sql = 'SELECT * FROM pinturas ORDER BY idcodigo'
        c.execute(sql)
        recset = c.fetchall()
        c.close()

        lista = []
        for item in recset:
            pintura=Pinturas()
            pintura.idcodigo = item[0]
            pintura.nomedaobra = item[1]
            pintura.preco = item[2]
            pintura.artista = item[3]

            lista.append(pintura)

        return lista

    def selecionarPinturas(self, idcodigo) -> Pinturas:
        c = self.connection.cursor()
        c.execute("""SELECT * FROM pinturas WHERE idcodigo = {}""".format(idcodigo))
        recset = c.fetchone()
        c.close()

        print(recset)

        pintura = Pinturas()
        pintura.idcodigo = recset[0]
        pintura.nomedaobra = recset[1]
        pintura.preco = recset[2]
        pintura.artista = recset[3]

        return pintura

    def inserirPinturas(self, pintura: Pinturas) -> Pinturas:
        c = self.connection.cursor()

        c.execute("""
            insert into pinturas(idcodigo, nomedaobra, preco, artista)
            values('{}', '{}', '{}', '{}') RETURNING idcodigo
        """.format(pintura.idcodigo, pintura.nomedaobra, pintura.preco, pintura.artista))

        self.connection.commit()

    def alterarPinturas(self, pintura: Pinturas) -> Pinturas:
        c = self.connection.cursor()
        c.execute("""
            update pinturas
            SET nomedaobra = '{}', preco = '{}', artista = '{}'
            WHERE idcodigo = '{}';
        """.format(pintura.nomedaobra, pintura.preco, pintura.artista, pintura.idcodigo))

        self.connection.commit()

    def excluirPinturas(self, pintura: Pinturas) -> Pinturas:
        c = self.connection.cursor()
        c.execute("""
            delete from pinturas
            where idcodigo = '{}'
        """.format(pintura.idcodigo))
        self.connection.commit()
