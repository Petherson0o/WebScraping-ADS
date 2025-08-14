from db import engine
import Models.models


def create_tables() -> None:
    print('Excluindo as tabelas existentes...')
    with engine.begin() as conn:
        Models.models.Base.metadata.drop_all(conn)
        print('Criando as tabelas no banco de dados...')
        Models.models.Base.metadata.create_all(conn)
        print('Tabelas criadas com sucesso.')


if __name__ == '__main__':
    create_tables()