class DescripcionNoEmbebida(Exception):
    """
    Cuando la descripcion de la oferta de trabajo no esta embebida en la pagina
    de resultados, y abre otra pestaña. Caso particular de Indeed.com. Suele ser
    provocada porque nos ha detectado como bot.
    """