import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

def authenticate():
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )

    name, authentication_status, username = authenticator.login('Login', 'main')
    return [authentication_status, authenticator]