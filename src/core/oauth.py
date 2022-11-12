from authlib.integrations.starlette_client import OAuth

oauth=OAuth()
google = oauth.register(
    name='google',
    client_id="1037947577335-sn9hvv8siecs8jdpdopljlptfjk7d9tu.apps.googleusercontent.com",
    client_secret="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",
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid profile email'
    }
)