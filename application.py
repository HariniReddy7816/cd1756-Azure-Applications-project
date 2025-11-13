"""
Entry point for Azure App Service to load the FlaskWebProject application.
"""

from FlaskWebProject import app

# Gunicorn will load `app` from this module.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555)

