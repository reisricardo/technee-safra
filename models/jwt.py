from flask_jwt_extended import JWTManager

def configure_jwt(app):
    jwt = JWTManager(app)

    #Disparado quando um Token com formato válido expirou
    @jwt.expired_token_loader
    def my_expired_token_callback():
        return redirect(SITE_URL + LOGIN_URL, code = 302)