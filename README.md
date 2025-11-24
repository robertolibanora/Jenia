# 🎨 Jenia - Landing Page

Landing page moderna per la digitalizzazione degli ordini ceramici, sviluppata con FastAPI e design pixel-perfect con effetti glassmorphism, gradienti e animazioni.

## 📋 Indice

- [Caratteristiche](#caratteristiche)
- [Requisiti](#requisiti)
- [Installazione](#installazione)
- [Avvio del Server](#avvio-del-server)
- [Struttura del Progetto](#struttura-del-progetto)
- [Configurazione](#configurazione)
- [Sviluppo](#sviluppo)
- [Note Importanti](#note-importanti)
- [Troubleshooting](#troubleshooting)

## ✨ Caratteristiche

- **Design Moderno**: Gradienti violetto-arancione, effetti glassmorphism e glow
- **Hero Section**: Lettera "J" 3D con animazioni e light streaks
- **Sezioni Complete**: 
  - Ordini Ceramici (3 card con numerazione)
  - Metodo Jenia (layout 2 colonne)
  - Statistiche (4 card con metriche)
  - Trust Logos
  - Form CTA
  - Footer completo
- **Responsive Design**: Mobile-first con breakpoint ottimizzati
- **Animazioni**: Effetti hover, scroll animations, floating elements
- **Typography**: Font Inter con pesi precisi e spacing ottimizzato

## 🔧 Requisiti

- Python 3.11 o superiore
- pip (gestore pacchetti Python)
- Browser moderno (Chrome, Firefox, Safari, Edge)

## 📦 Installazione

### 1. Clona o scarica il progetto

```bash
cd /path/to/Jenia
```

### 2. Crea un ambiente virtuale (consigliato)

```bash
python3 -m venv venv
```

### 3. Attiva l'ambiente virtuale

**Su macOS/Linux:**
```bash
source venv/bin/activate
```

**Su Windows:**
```bash
venv\Scripts\activate
```

### 4. Installa le dipendenze

```bash
pip install -r requirements.txt
```

Le dipendenze installate saranno:
- `fastapi` - Framework web moderno
- `uvicorn` - Server ASGI per FastAPI
- `jinja2` - Motore template (incluso con FastAPI)

## 🚀 Avvio del Server

### Metodo 1: Esecuzione diretta

```bash
python3 main.py
```

### Metodo 2: Con variabili d'ambiente

```bash
# Porta personalizzata
PORT=3000 python3 main.py

# IP e porta personalizzati
HOST=127.0.0.1 PORT=3000 python3 main.py
```

### Metodo 3: Con uvicorn direttamente

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Il flag `--reload` abilita il reload automatico durante lo sviluppo.

### Output atteso

Quando avvii il server, vedrai un output simile a:

```
============================================================
🚀 Server Avviato
============================================================

📍 Porta:        8000
🌐 IP Locale:    172.26.16.29
🔗 Localhost:    http://localhost:8000
🌍 IP Locale:    http://172.26.16.29:8000
============================================================
```

### Accesso all'applicazione

Apri il browser e vai a:
- **Localhost**: `http://localhost:8000`
- **IP Locale**: `http://[IP_LOCALE]:8000` (per accesso da altri dispositivi sulla stessa rete)

## 📁 Struttura del Progetto

```
Jenia/
│
├── main.py                 # File principale FastAPI
├── requirements.txt        # Dipendenze Python
├── README.md              # Questo file
│
├── templates/             # Template HTML
│   └── index.html         # Pagina principale
│
├── static/                # File statici
│   ├── css/
│   │   └── style.css      # Stili CSS completi
│   ├── js/
│   │   └── app.js         # JavaScript per interazioni
│   ├── img/               # Immagini (da aggiungere)
│   │   ├── hero-illustration.png
│   │   ├── logo-client-1.png
│   │   └── ...
│   └── icons/             # Icone SVG (da aggiungere)
│       ├── icon-upload.svg
│       ├── icon-process.svg
│       ├── icon-deliver.svg
│       └── ...
│
└── venv/                  # Ambiente virtuale (non committare)
```

## ⚙️ Configurazione

### Variabili d'Ambiente

Puoi configurare il server usando variabili d'ambiente:

- `PORT`: Porta del server (default: `8000`)
- `HOST`: Indirizzo IP (default: `0.0.0.0` - accetta connessioni da tutte le interfacce)

### Esempio con .env (opzionale)

Crea un file `.env` nella root del progetto:

```env
PORT=8000
HOST=0.0.0.0
```

Poi installa `python-dotenv` e modifica `main.py` per caricarlo:

```bash
pip install python-dotenv
```

## 🛠️ Sviluppo

### Aggiungere Immagini

1. **Immagini Hero/Illustrazioni**: Aggiungi in `/static/img/`
   - `hero-illustration.png` - Illustrazione principale hero
   - `logo-client-*.png` - Loghi clienti (5 immagini)

2. **Icone SVG**: Aggiungi in `/static/icons/`
   - `icon-upload.svg` - Icona upload
   - `icon-process.svg` - Icona elaborazione
   - `icon-deliver.svg` - Icona consegna
   - `icon-ai.svg` - Icona AI
   - `icon-precision.svg` - Icona precisione
   - `icon-integration.svg` - Icona integrazione
   - `icon-security.svg` - Icona sicurezza
   - `icon-chart.svg` - Icona grafico
   - `icon-target.svg` - Icona target
   - `icon-speed.svg` - Icona velocità
   - `icon-clock.svg` - Icona orologio
   - `icon-twitter.svg` - Icona Twitter
   - `icon-instagram.svg` - Icona Instagram
   - `icon-linkedin.svg` - Icona LinkedIn
   - `logo.svg` - Logo principale (opzionale)

### Modificare Stili

Il file `/static/css/style.css` è organizzato in sezioni:
- Reset & Base Styles
- Navbar
- Hero Section
- Ordini Ceramici Section
- Metodo Jenia Section
- Statistiche Section
- Trust Logos Section
- CTA Section
- Footer
- Responsive Design

### Modificare Contenuti

Modifica direttamente `/templates/index.html` per cambiare testi, sezioni o struttura.

### Collegare il Form

Per collegare il form CTA al backend, modifica `/static/js/app.js` nella funzione di submit:

```javascript
contactForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const formData = new FormData(contactForm);
    
    try {
        const response = await fetch('/api/contact', {
            method: 'POST',
            body: formData
        });
        
        const result = await response.json();
        // Gestisci la risposta
    } catch (error) {
        console.error('Errore:', error);
    }
});
```

Poi aggiungi l'endpoint in `main.py`:

```python
@app.post("/api/contact")
async def contact(request: Request):
    form = await request.form()
    # Processa i dati del form
    return {"status": "success"}
```

## 📝 Note Importanti

### Placeholder Immagini

Tutte le immagini sono referenziate ma devono essere aggiunte manualmente nelle directory appropriate. Se un'immagine non viene trovata, il browser mostrerà un'icona di errore.

### Font

Il progetto usa **Inter** da Google Fonts, caricato automaticamente nel `<head>` dell'HTML. Assicurati di avere una connessione internet per il caricamento del font.

### Browser Support

- ✅ Chrome/Edge (ultime 2 versioni)
- ✅ Firefox (ultime 2 versioni)
- ✅ Safari (ultime 2 versioni)
- ⚠️ IE11: Non supportato (usa browser moderni)

### Performance

- Le animazioni CSS sono ottimizzate per performance
- Usa `transform` e `opacity` per animazioni fluide
- Le immagini dovrebbero essere ottimizzate (WebP, compressione)

## 🔍 Troubleshooting

### Errore: "TemplateNotFound: 'index.html'"

**Problema**: FastAPI non trova il template.

**Soluzione**: 
- Verifica che la directory `templates/` esista nella root del progetto
- Verifica che `index.html` sia dentro `templates/`
- Controlla che il percorso in `main.py` sia corretto: `Jinja2Templates(directory="templates")`

### Errore: "StaticFiles not found"

**Problema**: I file CSS/JS non vengono caricati.

**Soluzione**:
- Verifica che la directory `static/` esista
- Controlla i percorsi nel CSS/JS nell'HTML (devono iniziare con `/static/`)
- Verifica che `app.mount("/static", StaticFiles(directory="static"))` sia presente in `main.py`

### Porta già in uso

**Problema**: `Address already in use`

**Soluzione**:
```bash
# Usa una porta diversa
PORT=3000 python3 main.py

# Oppure trova e termina il processo sulla porta 8000
lsof -ti:8000 | xargs kill -9  # macOS/Linux
```

### Immagini non visualizzate

**Problema**: Le immagini non appaiono.

**Soluzione**:
- Verifica che i file esistano nelle directory corrette
- Controlla i nomi dei file (case-sensitive su Linux/macOS)
- Apri la console del browser (F12) per vedere errori 404
- Usa placeholder temporanei se le immagini non sono disponibili

### Gradienti/Effetti non visibili

**Problema**: I gradienti o gli effetti glassmorphism non funzionano.

**Soluzione**:
- Verifica che il browser supporti `backdrop-filter` (Chrome 76+, Safari 9+)
- Controlla che il CSS sia caricato correttamente
- Verifica che non ci siano errori nella console del browser

### Menu mobile non funziona

**Problema**: Il toggle del menu mobile non risponde.

**Soluzione**:
- Verifica che `/static/js/app.js` sia caricato nell'HTML
- Controlla la console del browser per errori JavaScript
- Assicurati che il file JS sia nella posizione corretta

## 📞 Supporto

Per problemi o domande:
1. Controlla la sezione Troubleshooting
2. Verifica i log del server nel terminale
3. Controlla la console del browser (F12) per errori JavaScript/CSS

## 📄 Licenza

Questo progetto è privato e proprietario.

---

**Sviluppato con ❤️ per Jenia**

