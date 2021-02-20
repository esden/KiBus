try:
    # Note the relative import!
    from .action_kibus import KiBus
    # Instantiate and register to Pcbnew
    KiBus().register()
except Exception as e:
    import os
    plugin_dir = os.path.dirname(os.path.realpath(__file__))
    log_file = os.path.join(plugin_dir, 'kibus_error.log')
    with open(log_file, 'w') as f:
        f.write(repr(e))
