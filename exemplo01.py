# Teste de tipagem ganso para validar dados.

from pydantic import validate_arguments


@validate_arguments
def soma(x:int, y: int):
    return x + y

