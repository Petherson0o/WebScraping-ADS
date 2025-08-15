from db import engine, Session
from Models import models

# postagem = models.Post(id=3, texto_postagem="Texto da postagem asdasd", nome_portal="Portal notícias 2 ")
comment = models.Comment(id=1, post_id = 5, comment="comentario da postagem", user="usuario")
print(comment)


session = Session()

session.add(comment)
session.commit()
session.close()