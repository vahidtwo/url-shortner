from settings.phases.default import *  # NoQA: F401

PHASE = config("PHASE", "local")

if PHASE == "local":
    from settings.phases.local import *  # NoQA: F401
elif PHASE == "staging":
    from settings.phases.staging import *  # NoQA: F401
elif PHASE == "production":
    from settings.phases.production import *  # NoQA: F401
else:
    raise Exception("PHASE environment variable is not set properly.")
