import gradio as gr
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Cargar modelo FinBERT
print("Cargando modelo FinBERT...")
model_name = "ProsusAI/finbert"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
print("✅ Modelo cargado")

# Intentar cargar traductor, con fallback
try:
    from deep_translator import GoogleTranslator
    translator = GoogleTranslator(source='es', target='en')
    print("✅ Traductor cargado")
    USE_TRANSLATOR = True
except Exception as e:
    print(f"⚠️ No se pudo cargar traductor: {e}")
    print("Se procesará texto directamente en inglés")
    USE_TRANSLATOR = False

def analyze_sentiment(text):
    try:
        if not text or len(text.strip()) == 0:
            return {
                "Error": "Por favor ingresa un texto para analizar"
            }
        
        print(f"Analizando: {text[:50]}...")
        
        # Traducir si está disponible
        if USE_TRANSLATOR:
            try:
                english_text = translator.translate(text)
                print(f"Traducido: {english_text[:50]}...")
            except Exception as e:
                print(f"Error en traducción: {e}")
                english_text = text
        else:
            english_text = text
        
        # Tokenizar y analizar
        inputs = tokenizer(english_text, return_tensors="pt", truncation=True,
                          max_length=512, padding=True)
        
        with torch.no_grad():
            outputs = model(**inputs)
            predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        
        scores = predictions[0].tolist()
        sentiment_map = {0: 'Positivo ✅', 1: 'Negativo ❌', 2: 'Neutral 😐'}
        predicted_class = torch.argmax(predictions).item()
        
        result = {
            "🎯 Sentimiento Detectado": sentiment_map[predicted_class],
            "📊 Confianza": f"{scores[predicted_class]*100:.1f}%",
            "✅ Score Positivo": f"{scores[0]*100:.1f}%",
            "❌ Score Negativo": f"{scores[1]*100:.1f}%",
            "😐 Score Neutral": f"{scores[2]*100:.1f}%",
            "🌍 Texto Traducido": english_text[:200] + "..." if len(english_text) > 200 else english_text
        }
        
        print(f"✅ Resultado: {sentiment_map[predicted_class]}")
        return result
        
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return {
            "Error": f"Error al procesar: {str(e)}"
        }

examples = [
    "Las exportaciones peruanas crecieron un 15% este trimestre.",
    "La inflación sigue aumentando y preocupa a los inversionistas.",
    "El banco central decidió mantener las tasas sin cambios."
]

# Interfaz con Blocks (más robusto)
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 📰 Analizador de Sentimiento de Noticias
    Analiza si una noticia en español tiene un sentimiento **positivo**, **negativo** o **neutral**.
    """)
    
    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(
                lines=5,
                placeholder="Escribe o pega aquí tu noticia en español...",
                label="📰 Texto de la Noticia"
            )
            submit_btn = gr.Button("Analizar", variant="primary")
        with gr.Column():
            output = gr.JSON(label="📈 Resultados del Análisis")
    
    submit_btn.click(
        fn=analyze_sentiment,
        inputs=text_input,
        outputs=output,
        api_name="predict"   # 🔥 esto es lo que faltaba
    )

    
    gr.Examples(
        examples=examples,
        inputs=text_input
    )
    
    gr.Markdown("""
    ### 🔧 Tecnología
    - **Modelo:** FinBERT (ProsusAI)
    - **Traducción:** Google Translate API (opcional)
    - **Framework:** Transformers + PyTorch
    """)

if __name__ == "__main__":
    print("🚀 Iniciando aplicación...")
    demo.launch(ssr_mode=False)  # Desactivar SSR
