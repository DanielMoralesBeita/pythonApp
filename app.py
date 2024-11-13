from flask import Flask,  render_template_string, request, jsonify
import requests
import logging
import pandas as pd

app = Flask(__name__)
# Configurar logging
logging.basicConfig(level=logging.INFO)
# Token y URL de la API de WhatsApp
WHATSAPP_TOKEN = 'EAAGyt5UBx9cBOxveVvJDEoMIfUss5QQSn2VMDgPaoRF6RcNBZBTOudbZA3lbs6sNqFfMumYw1FUuKSJ70sV3iQhJZAFCt7npMYdyo71ZBnFeTDIAlUqQcIZBFDc9d9GJR7fpYKxefmZC2y1085SyHcgBgAvsGg6wePyYqSwsnYDT6C1FwQ8qjmgdKnLzSjkbUGCBXYmdR50ZB6rONB6Wa8ia97JR2lH'
WHATSAPP_URL = 'https://graph.facebook.com/v21.0/391164540756694/messages'
EXCEL_FILE = 'comparativa_respuestas.xlsx'  # Reemplaza con la ruta a tu archivo Excel

VERIFY_TOKEN = 'EAAGyt5UBx9cBOxveVvJDEoMIfUss5QQSn2VMDgPaoRF6RcNBZBTOudbZA3lbs6sNqFfMumYw1FUuKSJ70sV3iQhJZAFCt7npMYdyo71ZBnFeTDIAlUqQcIZBFDc9d9GJR7fpYKxefmZC2y1085SyHcgBgAvsGg6wePyYqSwsnYDT6C1FwQ8qjmgdKnLzSjkbUGCBXYmdR50ZB6rONB6Wa8ia97JR2lH'
@app.route('/Privacidad', methods=['GET'])
def Privacidad():
    try:
        html_content = """ <!DOCTYPE html> <html lang="es"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Política de Privacidad - ADESA</title> <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"> </head> <body> <div class="container my-5"> <h1>Política de Privacidad</h1> <p>En ADESA, valoramos tu privacidad y estamos comprometidos a proteger tu información personal. Esta política de privacidad describe cómo recopilamos, utilizamos y compartimos tu información.</p> <h2>Información Recopilada</h2> <p>Recopilamos información personal como tu nombre, dirección de correo electrónico y detalles de pago para procesar tus pedidos.</p> <h2>Uso de la Información</h2> <p>Utilizamos tu información para procesar pedidos, enviar boletines informativos y mejorar nuestros servicios.</p> <h2>Compartición de Información</h2> <p>No compartimos tu información personal con terceros sin tu consentimiento, excepto cuando sea necesario para cumplir con nuestras obligaciones legales.</p> <h2>Seguridad de la Información</h2> <p>Implementamos medidas de seguridad avanzadas para proteger tu información personal contra accesos no autorizados.</p> <h2>Derechos del Usuario</h2> <p>Tienes derecho a acceder, rectificar y suprimir tu información personal en cualquier momento.</p> <h2>Actualizaciones a la Política de Privacidad</h2> <p>Esta política de privacidad puede ser actualizada. Te notificaremos de cualquier cambio significativo.</p> </div> <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script> </body> </html> """ 
        return render_template_string(html_content)
    except Exception as e:
        logging.error(f"Error en webhook: {e}")
        return "Internal Server Error", 500

@app.route('/Terminos', methods=['GET']) 
def Terminos(): 
    try: 
        html_content = """ <!DOCTYPE html> <html lang="es"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Términos de Servicio - ADESA</title> <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"> </head> <body> <div class="container my-5"> <h1>Términos de Servicio</h1> <p>Bienvenido a ADESA. Al utilizar nuestros servicios, aceptas los siguientes términos y condiciones. Por favor, léelos detenidamente.</p> <h2>1. Alcance del Servicio</h2> <p>Nuestros servicios incluyen Servicio de chat bot. Nos esforzamos por ofrecer servicios confiables y eficientes a todos nuestros clientes.</p> <h2>2. Obligaciones del Cliente</h2> <p>Como cliente de ADESA, te comprometes a proporcionar información precisa y actualizada para permitirnos ofrecer nuestros servicios de manera efectiva. También es tu responsabilidad cumplir con todas las leyes y regulaciones aplicables.</p> <h2>3. Confidencialidad</h2> <p>Respetamos tu privacidad y nos comprometemos a proteger la confidencialidad de tu información personal. No compartiremos tu información con terceros sin tu consentimiento, excepto cuando sea necesario para cumplir con nuestras obligaciones legales.</p> <h2>4. Pagos y Facturación</h2> <p>Las tarifas por nuestros servicios se detallarán en tu factura. Todos los pagos deben realizarse dentro del período especificado. Nos reservamos el derecho de suspender o cancelar servicios por falta de pago.</p> <h2>5. Resolución de Disputas</h2> <p>En caso de disputa, nos esforzaremos por resolver cualquier problema de manera amistosa. Si no es posible llegar a un acuerdo, las disputas se resolverán de acuerdo con las leyes aplicables en Costa Rica.</p> <h2>6. Modificaciones de los Términos de Servicio</h2> <p>Nos reservamos el derecho de modificar estos términos de servicio en cualquier momento. Te notificaremos de cualquier cambio significativo a través de nuestro sitio web o por correo electrónico.</p> <h2>7. Contacto</h2> <p>Si tienes alguna pregunta o inquietud sobre estos términos de servicio, no dudes en contactarnos a través de telefono a <a href="tel:+50686261018">+50686261018</a>.</p> </div> <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script> </body> </html> """ 
        return render_template_string(html_content) 
    except Exception as e: 
        logging.error(f"Error en la página de términos de servicio: {e}") 
        return "Internal Server Error", 500

@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chatbot Web</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { font-family: 'Open Sans', sans-serif; background-color: #f7f7f7; }
            .container { max-width: 600px; margin-top: 50px; }
            .chatbox { max-height: 400px; overflow-y: scroll; }
            .input-group { margin-top: 10px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Chatbot Web</h2>
            <div class="card">
                <div class="card-body chatbox" id="chatbox">
                    <!-- Chat messages will appear here -->
                </div>
            </div>
            <div class="input-group">
                <input type="text" class="form-control" id="userMessage" placeholder="Escribe un mensaje...">
                <button class="btn btn-primary" id="sendButton">Enviar</button>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
        <script>
            document.getElementById('sendButton').addEventListener('click', function() {
                let userMessage = document.getElementById('userMessage').value;
                if (userMessage.trim()) {
                    let chatbox = document.getElementById('chatbox');
                    chatbox.innerHTML += '<div><strong>Tú:</strong> ' + userMessage + '</div>';
                    document.getElementById('userMessage').value = '';

                    fetch('/chat', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({message: userMessage})
                    })
                    .then(response => response.json())
                    .then(data => {
                        chatbox.innerHTML += '<div><strong>Chatbot:</strong> ' + data.response + '</div>';
                        chatbox.scrollTop = chatbox.scrollHeight;
                    });
                }
            });
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    try:
        if request.method == 'GET':
            if request.args.get('hub.verify_token') == VERIFY_TOKEN:
                logging.info("Verificación exitosa")
                return request.args.get('hub.challenge')
            else:
                logging.error("Token de verificación incorrecto")
                return 'Token de verificación incorrecto', 403
        elif request.method == 'POST':
            data = request.get_json()
            logging.info(f"Datos recibidos: {data}")
            if data:
                for entry in data.get('entry', []):
                    for message in entry.get('changes', []):
                        if message['field'] == 'messages':
                            for msg_data in message['value']['messages']:
                                handle_message(msg_data)
            return "ok", 200
    except Exception as e:
        logging.error(f"Error en webhook: {e}")
        return "Internal Server Error", 500

def handle_message(msg_data):
    try:
        from_number = msg_data['from']
        msg_text = msg_data['text']['body'].strip().lower()
        user_name = msg_data.get('contacts', [{}])[0].get('profile', {}).get('name', 'Usuario')
        logging.info(f"Mensaje recibido de {from_number} ({user_name}): {msg_text}")

        response_text = handle_option(msg_text)
        send_message(from_number, response_text)
    except Exception as e:
        logging.error(f"Error manejando el mensaje: {e}")

def handle_option(option):
    try:
        df = pd.read_excel(EXCEL_FILE)
        response = df.loc[df['Option'].str.lower() == option, 'Response'].values
        if response:
            return response[0]
        else:
            return "Opción no reconocida. Por favor, intenta con otro comando."
    except Exception as e:
        logging.error(f"Error leyendo el archivo Excel: {e}")
        return "Error al procesar tu solicitud. Por favor, intenta de nuevo más tarde."

def send_message(to_number, message):
    try:
        headers = {
            'Authorization': f'Bearer {WHATSAPP_TOKEN}',
            'Content-Type': 'application/json'
        }
        data = {
  
            'messaging_product': 'whatsapp',
"recipient_type": "individual",
            'to': to_number,
            'text': {'body': message}
        }
        response = requests.post(WHATSAPP_URL, json=data, headers=headers)
        logging.info(f"Respuesta de la API de WhatsApp: {response.json()}")
        return response.json()
    except Exception as e:
        logging.error(f"Error enviando el mensaje: {e}")


