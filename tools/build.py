"""Builds the Help Pc Ninja pages in Hebrew, English and Spanish from one template.

Run from the repo root:  python tools/build.py
Edit the text in LANGS below, then run it again; it rewrites the HTML pages.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://help.pcninja.pro"
ACCESS_KEY = "2fe4508c-cd5f-4f0e-9826-55a80dd93fe1"  # Web3Forms public key, sends to javier@pcninja.pro

# URL paths for each language. Hebrew keeps the original Google Sites paths.
PATHS = {
    "he": {"home": "/", "about": "/aboutMe/", "contact": "/aboutMe/contact/"},
    "en": {"home": "/en/", "about": "/en/about/", "contact": "/en/contact/"},
    "es": {"home": "/es/", "about": "/es/about/", "contact": "/es/contact/"},
}

LANGS = {
    "he": {
        "dir": "rtl", "label": "עב", "name": "עברית",
        "nav": {"home": "תמיכה מרחוק", "about": "אודות", "contact": "צור קשר"},
        "titles": {"home": "תמיכה מרחוק", "about": "אודות השירות", "contact": "צור קשר"},
        "desc": "תמיכה מרחוק במחשבים: מורידים את AnyViewer, שולחים את מספר המכשיר, ואני מתחבר לעזור.",
        "hero_h1": "תמיכה מרחוק במחשב",
        "hero_lede": "שירותי תמיכה ופתרונות מחשוב לאנשים פרטיים ולעסקים. מורידים תוכנה קטנה, ואני מתחבר אליכם ופותר את התקלה.",
        "hero_dl": "הורדת AnyViewer",
        "hero_contact": "צור קשר לפני ההורדה",
        "hero_note": "קובץ התקנה ל־Windows (64 ביט).",
        "steps_title": "איך זה עובד",
        "steps_intro": "שלושה צעדים, ואני כבר אצלכם במחשב.",
        "steps": [
            ("מורידים ומתקינים", "לוחצים על \"הורדת AnyViewer\" ומריצים את הקובץ."),
            ("פותחים את התוכנה", "בחלון התוכנה מופיע מספר המכשיר שלכם."),
            ("שולחים לי את המספר", "אני שולח בקשת התחברות, ואתם מאשרים אותה."),
        ],
        "alt_title": "אפשרויות תמיכה מרחוק נוספות",
        "alt_intro": "אם AnyViewer לא מתאים, אפשר להתחבר גם דרך אחת מהתוכנות האלה. כדאי לתאם איתי קודם.",
        "ru": ("גרסה מותאמת להורדה.", "הורדה מותאמת"),
        "pv": "תוכנת קוד פתוח.",
        "hd": "תוכנה חינמית לשליטה מרחוק.",
        "download": "הורדה", "site": "לאתר התוכנה",
        "more_title": "עוד הורדות",
        "win": ("התקנת Windows", "קבצי התקנה של Windows 11 ו־10 Pro."),
        "office": ("התקנת Office", "Smart Office Installer, הגרסה האחרונה."),
        "about_h1": "אודות השירות",
        "about_lead": "Help PC Ninja מספקת שירותי תמיכה ופתרונות מחשוב מגוונים לאנשים פרטיים ולעסקים הזקוקים למענה מקצועי, יסודי וממוקד פתרון.",
        "about_p1": "הפעילות מתקיימת בעיקר ללא מטרת רווח, לצד ניהול מעגל לקוחות אקסקלוסיבי הזוכה לליווי אישי ולשירות המותאם לצרכיו.",
        "prep_title": "כדי לטפל ביעילות, צרפו לפנייה:",
        "prep": ["תיאור ברור של הנושא", "איך הוא משפיע עליכם", "מידת הדחיפות"],
        "prep_note": "כל פנייה נבחנת ברצינות, תוך התמדה באיתור פתרון ושיקול דעת לגבי היקף הטיפול הנדרש.",
        "about_p2": "הרווח אינו מטרת הפעילות, אך במקרים מסוימים השירות כרוך בתשלום המאפשר להקצות את הזמן והמשאבים הדרושים. שאלת העלות אינה צריכה להרתיע מפנייה ראשונית.",
        "about_img_alt": "נינג'ה מתקן מחשב נייד",
        "contact_h1": "טופס בקשת שירות",
        "contact_sub": "השאירו פרטים ואחזור אליכם.",
        "tips_title": "מה לכתוב בפנייה",
        "tips_note": "שאלת העלות אינה צריכה להרתיע מפנייה ראשונית.",
        "f_name": "שם", "f_email": "מייל", "f_phone": "טלפון", "f_problem": "מה הבעיה?",
        "f_impact": "איך היא משפיעה עליך?", "f_urgency": "דחיפות",
        "f_optional": "(רשות)", "f_choose": "בחרו…",
        "urgency": ["רגיל", "דחוף", "קריטי"],
        "f_send": "שליחת הפנייה", "f_sending": "שולח…",
        "f_sent": "הפנייה נשלחה. אחזור אליכם בהקדם.",
        "f_failed": "הפנייה לא נשלחה. בדקו את החיבור לאינטרנט ונסו שוב.",
        "f_required": "שדות עם * הם חובה.",
        "f_subject": "פנייה חדשה מ-help.pcninja.pro",
        "footer": ["PcNinja - דף הבית", "התקנת Windows", "התקנת Office", "הכלים שלי ב-GitHub"],
    },
    "en": {
        "dir": "ltr", "label": "EN", "name": "English",
        "nav": {"home": "Remote support", "about": "About", "contact": "Contact"},
        "titles": {"home": "Remote support", "about": "About the service", "contact": "Contact"},
        "desc": "Remote computer support: download AnyViewer, send me your device ID, and I'll connect to help.",
        "hero_h1": "Remote computer support",
        "hero_lede": "Support and IT solutions for individuals and businesses. Download a small app, and I'll connect to your PC and fix the problem.",
        "hero_dl": "Download AnyViewer",
        "hero_contact": "Contact me first",
        "hero_note": "Installer for Windows (64-bit).",
        "steps_title": "How it works",
        "steps_intro": "Three steps, and I'm on your computer.",
        "steps": [
            ("Download and install", "Click \"Download AnyViewer\" and run the file."),
            ("Open the app", "The app window shows your device ID."),
            ("Send me the ID", "I send a connection request, and you accept it."),
        ],
        "alt_title": "Other remote support options",
        "alt_intro": "If AnyViewer doesn't suit you, we can also connect through one of these apps. Check with me first.",
        "ru": ("Custom build for download.", "Custom download"),
        "pv": "Open-source app.",
        "hd": "Free remote control app.",
        "download": "Download", "site": "Website",
        "more_title": "More downloads",
        "win": ("Windows installation", "Windows 11 and 10 Pro install images."),
        "office": ("Office installation", "Smart Office Installer, latest version."),
        "about_h1": "About the service",
        "about_lead": "Help PC Ninja provides support and IT solutions for individuals and businesses that need a professional, thorough and solution-focused answer.",
        "about_p1": "The service runs mostly on a not-for-profit basis, alongside a small circle of clients who get personal, tailored support.",
        "prep_title": "To help quickly, include in your request:",
        "prep": ["A clear description of the issue", "How it affects you", "How urgent it is"],
        "prep_note": "Every request is taken seriously, with persistence in finding a solution and judgment about the scope of work needed.",
        "about_p2": "Profit isn't the goal, but in some cases the service involves a fee that covers the time and resources it needs. Cost shouldn't stop you from getting in touch.",
        "about_img_alt": "A ninja repairing a laptop",
        "contact_h1": "Service request",
        "contact_sub": "Leave your details and I'll get back to you.",
        "tips_title": "What to include",
        "tips_note": "Cost shouldn't stop you from getting in touch.",
        "f_name": "Name", "f_email": "Email", "f_phone": "Phone", "f_problem": "What's the problem?",
        "f_impact": "How does it affect you?", "f_urgency": "Urgency",
        "f_optional": "(optional)", "f_choose": "Choose…",
        "urgency": ["Normal", "Urgent", "Critical"],
        "f_send": "Send request", "f_sending": "Sending…",
        "f_sent": "Request sent. I'll get back to you soon.",
        "f_failed": "The request wasn't sent. Check your internet connection and try again.",
        "f_required": "Fields marked * are required.",
        "f_subject": "New request from help.pcninja.pro (EN)",
        "footer": ["PcNinja home", "Windows installation", "Office installation", "My tools on GitHub"],
    },
    "es": {
        "dir": "ltr", "label": "ES", "name": "Español",
        "nav": {"home": "Soporte remoto", "about": "Acerca de", "contact": "Contacto"},
        "titles": {"home": "Soporte remoto", "about": "Acerca del servicio", "contact": "Contacto"},
        "desc": "Soporte remoto para tu computadora: descarga AnyViewer, envíame el ID de tu equipo y me conecto para ayudarte.",
        "hero_h1": "Soporte remoto para tu computadora",
        "hero_lede": "Soporte y soluciones informáticas para particulares y empresas. Descargas una pequeña aplicación, me conecto a tu equipo y resuelvo el problema.",
        "hero_dl": "Descargar AnyViewer",
        "hero_contact": "Contáctame antes",
        "hero_note": "Instalador para Windows (64 bits).",
        "steps_title": "Cómo funciona",
        "steps_intro": "Tres pasos y ya estoy en tu computadora.",
        "steps": [
            ("Descarga e instala", "Haz clic en \"Descargar AnyViewer\" y ejecuta el archivo."),
            ("Abre la aplicación", "En la ventana aparece el ID de tu equipo."),
            ("Envíame el ID", "Te envío una solicitud de conexión y tú la aceptas."),
        ],
        "alt_title": "Otras opciones de soporte remoto",
        "alt_intro": "Si AnyViewer no te sirve, también podemos conectarnos con una de estas aplicaciones. Consúltame antes.",
        "ru": ("Versión personalizada para descargar.", "Descarga personalizada"),
        "pv": "Aplicación de código abierto.",
        "hd": "Aplicación gratuita de control remoto.",
        "download": "Descargar", "site": "Sitio web",
        "more_title": "Más descargas",
        "win": ("Instalación de Windows", "Imágenes de instalación de Windows 11 y 10 Pro."),
        "office": ("Instalación de Office", "Smart Office Installer, última versión."),
        "about_h1": "Acerca del servicio",
        "about_lead": "Help PC Ninja ofrece soporte y soluciones informáticas a particulares y empresas que necesitan una respuesta profesional, minuciosa y enfocada en resolver.",
        "about_p1": "El servicio funciona principalmente sin fines de lucro, junto con un círculo reducido de clientes que reciben atención personal y adaptada.",
        "prep_title": "Para ayudarte rápido, incluye en tu solicitud:",
        "prep": ["Una descripción clara del problema", "Cómo te afecta", "Qué tan urgente es"],
        "prep_note": "Cada solicitud se toma en serio, con constancia para encontrar una solución y criterio sobre el alcance del trabajo necesario.",
        "about_p2": "El lucro no es el objetivo, pero en algunos casos el servicio tiene un costo que cubre el tiempo y los recursos necesarios. El costo no debería impedirte escribirme.",
        "about_img_alt": "Un ninja reparando una laptop",
        "contact_h1": "Solicitud de servicio",
        "contact_sub": "Deja tus datos y te respondo.",
        "tips_title": "Qué incluir",
        "tips_note": "El costo no debería impedirte escribirme.",
        "f_name": "Nombre", "f_email": "Correo", "f_phone": "Teléfono", "f_problem": "¿Cuál es el problema?",
        "f_impact": "¿Cómo te afecta?", "f_urgency": "Urgencia",
        "f_optional": "(opcional)", "f_choose": "Elige…",
        "urgency": ["Normal", "Urgente", "Crítico"],
        "f_send": "Enviar solicitud", "f_sending": "Enviando…",
        "f_sent": "Solicitud enviada. Te respondo pronto.",
        "f_failed": "La solicitud no se envió. Revisa tu conexión a internet e inténtalo de nuevo.",
        "f_required": "Los campos con * son obligatorios.",
        "f_subject": "Nueva solicitud desde help.pcninja.pro (ES)",
        "footer": ["PcNinja inicio", "Instalación de Windows", "Instalación de Office", "Mis herramientas en GitHub"],
    },
}

FOOTER_URLS = ["https://www.pcninja.pro/", "https://win11.pcninja.pro/", "https://office.pcninja.pro/", "https://github.com/JavierTorresFelendler"]


def head(lang, page, extra_og=""):
    L = LANGS[lang]
    alternates = "\n".join(
        f'  <link rel="alternate" hreflang="{k}" href="{SITE}{PATHS[k][page]}">' for k in PATHS
    )
    return f"""<!doctype html>
<html lang="{lang}" dir="{L['dir']}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Help Pc Ninja - {L['titles'][page]}</title>
  <meta name="description" content="{L['desc']}">
  <meta property="og:title" content="Help Pc Ninja - {L['titles'][page]}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{SITE}{PATHS[lang][page]}">
  <meta property="og:image" content="{SITE}/assets/ninja.png">
  <link rel="canonical" href="{SITE}{PATHS[lang][page]}">
{alternates}
  <link rel="alternate" hreflang="x-default" href="{SITE}{PATHS['he'][page]}">
  <link rel="icon" type="image/png" href="/assets/favicon.png">
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Assistant:wght@400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/site.css">
</head>
<body>
"""


def topbar(lang, page):
    L = LANGS[lang]
    nav = "\n".join(
        f'          <li><a href="{PATHS[lang][p]}"{" aria-current=\"page\"" if p == page else ""}>{L["nav"][p]}</a></li>'
        for p in ("home", "about", "contact")
    )
    langs = "\n".join(
        f'          <li><a href="{PATHS[k][page]}" hreflang="{k}" lang="{k}" title="{LANGS[k]["name"]}"{" aria-current=\"true\"" if k == lang else ""}>{LANGS[k]["label"]}</a></li>'
        for k in ("he", "en", "es")
    )
    return f"""  <header class="topbar">
    <div class="wrap">
      <a class="brand" href="{PATHS[lang]['home']}"><img src="/assets/logo.png" alt="" width="40" height="40"><span>Help Pc Ninja</span></a>
      <div class="menus">
        <ul class="nav">
{nav}
        </ul>
        <ul class="langs" aria-label="Language">
{langs}
        </ul>
      </div>
    </div>
  </header>
"""


def footer(lang, script=""):
    L = LANGS[lang]
    items = "\n".join(f'        <li><a href="{u}">{t}</a></li>' for u, t in zip(FOOTER_URLS, L["footer"]))
    return f"""
  <footer class="site-footer">
    <div class="wrap">
      <span>Help Pc Ninja</span>
      <ul>
{items}
      </ul>
    </div>
  </footer>
{script}</body>
</html>
"""


def home(lang):
    L, P = LANGS[lang], PATHS[lang]
    steps = "\n".join(f"          <li><strong>{a}</strong><p>{b}</p></li>" for a, b in L["steps"])

    def row(tile, logo, name, desc, dl_href, dl_label, site_href):
        return f"""        <div class="tool-row">
          <div class="logo-tile {tile}"><img src="/assets/{logo}" alt="{name}"></div>
          <div><h3>{name}</h3><p>{desc}</p></div>
          <div class="links">
            <a class="btn btn-dark" href="{dl_href}">{dl_label}</a>
            <a class="btn btn-line" href="{site_href}">{L['site']}</a>
          </div>
        </div>"""

    rows = "\n\n".join([
        row("tile-ru", "remoteutilities.png", "RemoteUtilities", L["ru"][0], "https://ru.pcninja.pro", L["ru"][1], "https://www.remoteutilities.com/"),
        row("tile-pv", "peerviewer.png", "PeerViewer", L["pv"], "https://github.com/PeerViewer/codebase/releases/", L["download"], "https://github.com/PeerViewer"),
        row("tile-hd", "hoptodesk.jpg", "HopToDesk", L["hd"], "https://download.hoptodesk.com/HopToDesk.exe", L["download"], "https://www.hoptodesk.com/"),
    ])
    return head(lang, "home") + topbar(lang, "home") + f"""
  <main>
    <section class="hero">
      <div class="wrap">
        <div>
          <h1>{L['hero_h1']}</h1>
          <p class="lede">{L['hero_lede']}</p>
          <div class="actions">
            <a class="btn btn-primary" href="https://go.anyviewer.com/dl/AnyViewerSetup_x64.exe">{L['hero_dl']}</a>
            <a class="btn btn-ghost" href="{P['contact']}">{L['hero_contact']}</a>
          </div>
          <p class="file-note">{L['hero_note']} Powered by <a href="https://www.anyviewer.com/">AnyViewer</a>.</p>
        </div>
        <img src="/assets/ninja.png" alt="" width="512" height="512">
      </div>
    </section>

    <section>
      <div class="wrap">
        <h2 class="section-title">{L['steps_title']}</h2>
        <p class="section-intro">{L['steps_intro']}</p>
        <ol class="steps">
{steps}
        </ol>
      </div>
    </section>

    <section class="tools-alt">
      <div class="wrap">
        <h2 class="section-title">{L['alt_title']}</h2>
        <p class="section-intro">{L['alt_intro']}</p>

{rows}
      </div>
    </section>

    <section>
      <div class="wrap">
        <h2 class="section-title">{L['more_title']}</h2>
        <div class="more">
          <a href="https://win11.pcninja.pro/"><strong>{L['win'][0]}</strong><span>{L['win'][1]}</span><span class="host"><bdi>win11.pcninja.pro</bdi></span></a>
          <a href="https://office.pcninja.pro/"><strong>{L['office'][0]}</strong><span>{L['office'][1]}</span><span class="host"><bdi>office.pcninja.pro</bdi></span></a>
        </div>
      </div>
    </section>
  </main>
""" + footer(lang)


def about(lang):
    L, P = LANGS[lang], PATHS[lang]
    prep = "\n".join(f"              <li>{x}</li>" for x in L["prep"])
    return head(lang, "about") + topbar(lang, "about") + f"""
  <main>
    <div class="page-head"><div class="wrap"><h1>{L['about_h1']}</h1></div></div>

    <section>
      <div class="wrap about">
        <div class="about-text">
          <p class="lead">{L['about_lead']}</p>
          <p>{L['about_p1']}</p>

          <div class="prep">
            <h2>{L['prep_title']}</h2>
            <ul class="dash-list">
{prep}
            </ul>
            <p>{L['prep_note']}</p>
          </div>

          <p>{L['about_p2']}</p>
          <a class="btn btn-primary" href="{P['contact']}">{L['nav']['contact']}</a>
        </div>
        <figure><img src="/assets/ninja-laptop.jpg" alt="{L['about_img_alt']}" width="786" height="652"></figure>
      </div>
    </section>
  </main>
""" + footer(lang)


def contact(lang):
    L = LANGS[lang]
    tips = "\n".join(f"            <li>{x}</li>" for x in L["prep"])
    urg = "\n".join(f'                <option value="{u}">{u}</option>' for u in L["urgency"])
    req = '<span class="req" aria-hidden="true">*</span>'
    opt = f'<span class="opt">{L["f_optional"]}</span>'
    return head(lang, "contact") + topbar(lang, "contact") + f"""
  <main>
    <div class="page-head"><div class="wrap"><h1>{L['contact_h1']}</h1><p>{L['contact_sub']}</p></div></div>

    <section>
      <div class="wrap contact">
        <aside class="tips">
          <h2>{L['tips_title']}</h2>
          <ul class="dash-list">
{tips}
          </ul>
          <p>{L['tips_note']}</p>
        </aside>

        <form id="request-form" class="form-card" action="https://api.web3forms.com/submit" method="POST"
              data-send="{L['f_send']}" data-sending="{L['f_sending']}" data-sent="{L['f_sent']}" data-failed="{L['f_failed']}">
          <input type="hidden" name="access_key" value="{ACCESS_KEY}">
          <input type="hidden" name="subject" value="{L['f_subject']}">
          <input type="hidden" name="from_name" value="Help Pc Ninja">
          <input type="hidden" name="language" value="{L['name']}">
          <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">

          <div class="field-row">
            <div class="field">
              <label for="f-name">{L['f_name']} {req}</label>
              <input id="f-name" name="name" type="text" required autocomplete="name" maxlength="100">
            </div>
            <div class="field">
              <label for="f-phone">{L['f_phone']} {opt}</label>
              <input id="f-phone" name="phone" type="tel" autocomplete="tel" maxlength="30">
            </div>
          </div>
          <div class="field-row">
            <div class="field">
              <label for="f-email">{L['f_email']} {req}</label>
              <input id="f-email" name="email" type="email" required autocomplete="email" maxlength="120">
            </div>
            <div class="field">
              <label for="f-urgency">{L['f_urgency']} {req}</label>
              <select id="f-urgency" name="urgency" required>
                <option value="">{L['f_choose']}</option>
{urg}
              </select>
            </div>
          </div>
          <div class="field">
            <label for="f-problem">{L['f_problem']} {req}</label>
            <textarea id="f-problem" name="problem" required maxlength="4000"></textarea>
          </div>
          <div class="field">
            <label for="f-impact">{L['f_impact']} {opt}</label>
            <textarea id="f-impact" name="impact" maxlength="2000" style="min-height:90px"></textarea>
          </div>

          <p id="form-status" class="form-status" role="status" hidden></p>
          <div class="form-foot">
            <button class="btn btn-primary" type="submit">{L['f_send']}</button>
            <small>{L['f_required']}</small>
          </div>
        </form>
      </div>
    </section>
  </main>
""" + footer(lang, '  <script src="/assets/form.js"></script>\n')


def main():
    for lang in LANGS:
        for page, fn in (("home", home), ("about", about), ("contact", contact)):
            path = os.path.join(ROOT, PATHS[lang][page].strip("/"), "index.html")
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(fn(lang))
            print("wrote", os.path.relpath(path, ROOT))


if __name__ == "__main__":
    main()
