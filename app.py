"""
Servidor Flask para Análisis de Sentimiento de Noticias
Utiliza FinBERT para análisis y Google Translate para traducción español-inglés
"""
 
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from deep_translator import GoogleTranslator
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicializar Flask
app = Flask(__name__)
CORS(app)  # Permitir peticiones desde el frontend

# Inicializar el traductor
translator = GoogleTranslator(source='es', target='en')

# Cargar modelo FinBERT
logger.info("Cargando modelo FinBERT...")
model_name = "ProsusAI/finbert"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()  # Modo evaluación
logger.info("Modelo FinBERT cargado exitosamente")

def translate_to_english(text):
    """
    Traduce texto de español a inglés usando Google Translate
    
    Args:
        text (str): Texto en español
        
    Returns:
        str: Texto traducido al inglés
    """
    try:
        translation = translator.translate(text)
        #logger.info(f"Traducción: {text[:50]}... -> {translation.text[:50]}...")
        return translation
    except Exception as e:
        logger.error(f"Error en traducción: {str(e)}")
        raise Exception(f"Error al traducir el texto: {str(e)}")

def analyze_sentiment(text):
    """
    Analiza el sentimiento del texto usando FinBERT
    
    Args:
        text (str): Texto en inglés para analizar
        
    Returns:
        dict: Diccionario con label, confidence y scores
    """
    try:
        # Tokenizar el texto
        inputs = tokenizer(text, return_tensors="pt", truncation=True, 
                          max_length=512, padding=True)
        
        # Hacer predicción
        with torch.no_grad():
            outputs = model(**inputs)
            predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        
        # Obtener probabilidades
        scores = predictions[0].tolist()
        
        # FinBERT retorna: [positive, negative, neutral]
        sentiment_map = {
            0: 'positive',
            1: 'negative', 
            2: 'neutral'
        }
        
        # Obtener el índice con mayor probabilidad
        predicted_class = torch.argmax(predictions).item()
        
        result = {
            'label': sentiment_map[predicted_class],
            'confidence': scores[predicted_class],
            'scores': {
                'positive': scores[0],
                'negative': scores[1],
                'neutral': scores[2]
            }
        }
        
        logger.info(f"Análisis completado: {result['label']} ({result['confidence']:.2f})")
        return result
        
    except Exception as e:
        logger.error(f"Error en análisis de sentimiento: {str(e)}")
        raise Exception(f"Error al analizar el sentimiento: {str(e)}")

@app.route('/')
def home():
    """Endpoint de bienvenida"""
    return jsonify({
        'message': 'API de Análisis de Sentimiento',
        'version': '1.0',
        'endpoints': {
            'POST /analyze': 'Analizar sentimiento de texto en español'
        }
    })

@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Endpoint principal para análisis de sentimiento
    
    Espera JSON con formato: {"text": "texto a analizar"}
    Retorna: {"label": "positive/negative/neutral", "confidence": float, "scores": {...}}
    """
    try:
        # Obtener datos del request
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({'error': 'No se proporcionó texto para analizar'}), 400
        
        spanish_text = data['text'].strip()
        
        if not spanish_text:
            return jsonify({'error': 'El texto está vacío'}), 400
        
        if len(spanish_text) > 5000:
            return jsonify({'error': 'El texto es demasiado largo (máximo 5000 caracteres)'}), 400
        
        logger.info(f"Recibida petición de análisis: {spanish_text[:100]}...")
        
        # Paso 1: Traducir de español a inglés
        english_text = translate_to_english(spanish_text)
        
        # Paso 2: Analizar sentimiento con FinBERT
        result = analyze_sentiment(english_text)
        
        # Añadir información adicional
        result['original_text'] = spanish_text[:100] + '...' if len(spanish_text) > 100 else spanish_text
        result['translated_text'] = english_text[:100] + '...' if len(english_text) > 100 else english_text
        
        return jsonify(result), 200
        
    except Exception as e:
        logger.error(f"Error en endpoint /analyze: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Endpoint para verificar el estado del servidor"""
    return jsonify({
        'status': 'healthy',
        'model': 'FinBERT',
        'translator': 'Google Translate'
    }), 200

if __name__ == '__main__':
    logger.info("Iniciando servidor Flask...")
    app.run(host='0.0.0.0', port=5000, debug=True)
