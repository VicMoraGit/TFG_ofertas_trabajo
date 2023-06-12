class SalarioDemasiadoBajo(Exception):
    """
    Si el salario es demasiado bajo, es muy probable que el bot haya detectado un numero erroneo como salario. Como minimo, debe estar por encima del SMI 2023 (15.120€)
    """
