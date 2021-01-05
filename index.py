import entry as et

# Gets the functions starting with 'app_'
apps = [app for app in dir(et) if 'APP_' in app ]

for app in apps:
	ap = getattr(et,  app)
	ap()

