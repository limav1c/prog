from config import *
from modelo import *

# apagar o arquivo, se houver
if os.path.exists(arquivobd):
    os.remove(arquivobd)
    
db.create_all()

print("Tabelas criadas")