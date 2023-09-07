from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

# Configuración de la clave secreta
app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = '12345678910DEV'  # Cambia esto a una clave segura y secreta

# Configuración de Flask-Mail (Reemplaza estos valores con los de tu servidor de correo)
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'tu_correo@example.com'
app.config['MAIL_PASSWORD'] = 'tu_contraseña'

# Configuración adicional para el envío de correos
app.config['MAIL_DEFAULT_SENDER'] = 'tu_correo@example.com'
app.config['MAIL_MAX_EMAILS'] = None  # Cambia según tus necesidades
app.config['MAIL_SUPPRESS_SEND'] = False  # Configuración para activar el envío de correos en desarrollo
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el formulario de contacto
@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        # Aquí puedes procesar los datos del formulario, enviar correos, etc.
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']
        
        # Por ejemplo, podrías imprimir los datos para verificar
        print(f'Nombre: {nombre}')
        print(f'Correo: {correo}')
        print(f'Mensaje: {mensaje}')
        
        # Enviar correo electrónico
        try:
            msg = Message('Nuevo mensaje de contacto', sender='tu_correo@example.com', recipients=['tu_correo@example.com'])
            msg.body = f'Nombre: {nombre}\nCorreo: {correo}\nMensaje: {mensaje}'
            mail.send(msg)
            flash('Mensaje enviado con éxito', 'success')
        except Exception as e:
            flash('Hubo un error al enviar el mensaje. Inténtalo de nuevo más tarde.', 'error')
            print(f'Error al enviar correo electrónico: {str(e)}')
        
        # Redirige a una página de confirmación (confirmation.html)
        return render_template('confirmation.html', nombre=nombre)

# Esta es una ruta de ejemplo para la página de confirmación
@app.route('/confirmation/<nombre>')
def confirmation(nombre):
    return render_template('confirmation.html', nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)
