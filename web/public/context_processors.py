def settings(request):
    """
    Put selected settings variables into the default template context
    """
    from electric.global_settings import GLOBAL_SETTINGS
    return GLOBAL_SETTINGS