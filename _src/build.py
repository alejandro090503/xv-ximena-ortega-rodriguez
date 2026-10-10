# Transforma el clon de boda-victor-fernanda en XV Sara Ximena Ortega Rodríguez.
# Correr una sola vez sobre el index.html original del template.
import re, pathlib, sys

P = pathlib.Path(__file__).resolve().parent.parent / "index.html"
s = P.read_text(encoding="utf-8")
if "Sara Ximena" in s:
    sys.exit("ya transformado")

def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n == 0:
        sys.exit(f"NO ENCONTRADO: {old[:80]!r}")
    s = s.replace(old, new) if count == 0 else s.replace(old, new, count)

def sub_between(start, end, new):
    """Reemplaza desde start (incluido) hasta end (excluido)."""
    global s
    a = s.index(start); b = s.index(end, a)
    s = s[:a] + new + s[b:]

URL = "https://xv-ximena-ortega-rodriguez.vercel.app"
AUDIO = "https://bsjoelxktbvlavfoozhk.supabase.co/storage/v1/object/public/fotos-clientes/audio/xv-ximena-ortega-rodriguez/cancion.mp3"
PIN = '<svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>'

# ── META ──
sub_between("<title>", '<link rel="preconnect"', f'''<title>XV Años · Sara Ximena · 15 Noviembre 2026</title>
<meta name="description" content="Mis XV Años · Sara Ximena Ortega Rodríguez · Domingo 15 de noviembre de 2026 · León, Guanajuato">
<meta property="og:type" content="website">
<meta property="og:url" content="{URL}/">
<meta property="og:title" content="Mis XV Años · Sara Ximena">
<meta property="og:description" content="Domingo 15 de noviembre de 2026 · León, Guanajuato. Me encantaría que me acompañes.">
<meta property="og:image" content="{URL}/og-image.jpg">
<meta property="og:image:secure_url" content="{URL}/og-image.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Invitación XV años Sara Ximena">
<meta property="og:locale" content="es_MX">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:url" content="{URL}/">
<meta name="twitter:title" content="Mis XV Años · Sara Ximena">
<meta name="twitter:image" content="{URL}/og-image.jpg">
''')

# ── PALETA: azul cielo #82c9ff + plata #C0C0C0 (roles del template conservados) ──
sub_between("  --bg:#F5F8FF;", "}\n*{margin:0", """  --bg:#F6FAFF;
  --surface:#E9F4FF;
  --card:#FFFFFF;
  --accent:#1E62A0;
  --accent2:#3D6690;
  --dark:#0F2F55;
  --text:#0C2340;
  --copper:#8C97A6;
  --copper-light:#D6DCE4;
  --blush:#CDE8FF;
  --plum:#0C2340;
  --sky:#82C9FF;
  --silver:linear-gradient(135deg,#8E959E 0%,#F4F6F8 28%,#B9C0C8 50%,#FFFFFF 66%,#9AA1AA 100%);
""")
# ornamentos SVG: azul medio del template → plata
s = s.replace("#5588CC", "#9AA4B2").replace("85,136,204", "154,164,178")

# ── LOADER ──
rep('<span>F</span><span>&nbsp;</span><span>&amp;</span><span>&nbsp;</span><span>V</span>',
    '<span>S</span><span>&nbsp;</span><span>·</span><span>&nbsp;</span><span>X</span>')
rep("Nos casamos · 10 Octubre 2026", "Mis XV Años · 15 Noviembre 2026")
rep('alt="Invitación de boda"', 'alt="Invitación XV años Sara Ximena"')

# ── HERO: nombres grandes + apellidos debajo ──
sub_between('<span class="hero-tag rv">', '    </div>\n    <div class="scroll-hint"', '''<span class="hero-tag rv">Mis XV Años</span>
      <span class="hero-bride rv">Sara</span>
      <span class="hero-groom rv">Ximena</span>
      <span class="hero-amp rv hero-surname">Ortega Rodríguez</span>
      <span class="hero-date rv">15 · Noviembre · 2026</span>
''')
# orden de animación: nombres → apellidos
rep("gsap.fromTo('.hero-amp',{y:18,opacity:0},{y:0,opacity:1,duration:.7,delay:.9,ease:'power2.out'});",
    "gsap.fromTo('.hero-amp',{y:18,opacity:0},{y:0,opacity:1,duration:.9,delay:1.5,ease:'power2.out'});")
rep("gsap.fromTo('.hero-date',{y:18,opacity:0},{y:0,opacity:1,duration:.8,delay:1.5,ease:'power2.out'});",
    "gsap.fromTo('.hero-date',{y:18,opacity:0},{y:0,opacity:1,duration:.8,delay:1.9,ease:'power2.out'});")

# ── FECHA ──
rep('<span class="fecha-num">10</span>', '<span class="fecha-num">15</span>')
rep('<span class="fecha-num">OCT</span>', '<span class="fecha-num">NOV</span>')

# ── COUNTDOWN ── (León: CST, sin horario de verano)
rep("new Date('2026-10-10T13:00:00-05:00')", "new Date('2026-11-15T14:00:00-06:00')")
rep('<p class="section-sub">El momento más esperado</p>', '<p class="section-sub">Para que el reloj marque la medianoche más mágica</p>')

# ── PALABRAS PARA LOS INVITADOS ──
sub_between('<span class="quote-mark rv">"</span>', '    <div class="quote-bar rv"></div>', '''<span class="quote-mark rv">"</span>
    <p class="quote-txt rv">
      Hay noches que parecen escritas en un cuento.<br>
      Quince años después, con un vestido soñado y el corazón lleno de gratitud,
      quiero vivir la mía rodeada de las personas que más quiero.<br>
      Tu presencia será la magia que haga inolvidable esta noche.
    </p>
    <span class="quote-sig rv">Sara Ximena</span>
''')

# ── PADRES Y PADRINOS ──
sub_between('<section id="familiares" class="rv">', '  <!-- UBICACION -->', '''<section id="familiares" class="rv">
    <p class="eyebrow">Con la bendición de Dios y de</p>
    <h2 class="script-title">Mi Familia</h2>
    <p class="section-sub">Quienes me han acompañado en cada paso</p>
    <div class="fam-grid">
      <div class="fam-card rv">
        <span class="fam-side">Mis Padres</span>
        <span class="fam-name">Pablo Ortega García</span>
        <div class="fam-and"><div class="fam-and-line"></div><span class="fam-and-txt">&amp;</span><div class="fam-and-line"></div></div>
        <span class="fam-name">Marta Leticia Rodríguez Briano</span>
      </div>
      <div class="fam-card rv">
        <span class="fam-side">Mis Padrinos</span>
        <span class="fam-name">Santa Teresa Rodríguez Briano</span>
        <div class="fam-and"><div class="fam-and-line"></div><span class="fam-and-txt">&amp;</span><div class="fam-and-line"></div></div>
        <span class="fam-name">Rafael Guevara Rodríguez</span>
      </div>
    </div>
  </section>

''')

# ── UBICACIONES (Misa / Recepción / Lunes 16) ──
def loc(panel, active, venue, badge_svg, badge, street, rest, hora, hora_txt, q, link, extra=""):
    return f'''    <div class="loc-panel{' active' if active else ''}" id="panel-{panel}">
      <div class="loc-card rv">
        <div class="loc-venue-name">{venue}</div>
        <div class="loc-badge">{badge_svg}{badge}</div>
        <div class="loc-info-row">
          <svg class="loc-info-icon" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
          <div class="loc-info-text"><strong>{street}</strong>{rest}</div>
        </div>
        <div class="loc-info-row">
          <svg class="loc-info-icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          <div class="loc-info-text"><strong>{hora}</strong> {hora_txt}</div>
        </div>{extra}
        <div class="map-container">
          <iframe title="{venue}" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade"
            src="https://maps.google.com/maps?q={q}&output=embed&z=16"></iframe>
        </div>
        <a href="{link}" target="_blank" rel="noopener" class="btn-directions">
          {PIN}
          Cómo llegar
        </a>
      </div>
    </div>
'''
HEART = '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>'
HOUSE = '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>'
STAR = '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>'
LUNES_NOTE = '''
        <div class="loc-info-row">
          <svg class="loc-info-icon" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
          <div class="loc-info-text"><strong>Lunes 16 de noviembre</strong>Al día siguiente seguimos celebrando y esperamos contar con tu presencia.</div>
        </div>'''
sub_between('<section id="ubicacion">', '    <div class="cal-section rv">', '''<section id="ubicacion">
    <p class="eyebrow rv">Dónde Celebramos</p>
    <h2 class="script-title rv">Ubicación</h2>
    <p class="section-sub rv">León, Guanajuato</p>
    <div class="loc-tabs rv" id="locTabs">
      <button class="loc-tab active" data-panel="misa">Misa</button>
      <button class="loc-tab" data-panel="recepcion">Recepción</button>
      <button class="loc-tab" data-panel="lunes">Lunes 16</button>
    </div>
''' + loc("misa", True, "Parroquia del Señor de la Salud", HEART, "Misa de XV Años",
          "Jardín Allende 124", "Col. Obregón<br>37320 León, Gto.", "2:00 PM", "Misa de acción de gracias",
          "Parroquia+del+Se%C3%B1or+de+la+Salud+Jard%C3%ADn+Allende+124+Obregon+Le%C3%B3n+Gto",
          "https://maps.app.goo.gl/PDMoNkv4uzwb6ck28")
  + loc("recepcion", False, "Casa Génesis Events", HOUSE, "Recepción",
        "Calle San Carlos Borrovec 145", "Fracc. Jesús María<br>37299 León, Gto.", "4:00 PM", "Recepción de 4:00 a 4:30 PM",
        "Casa+G%C3%A9nesis+events+San+Carlos+Borrovec+145+Le%C3%B3n+Gto",
        "https://maps.app.goo.gl/5iEMjSiSQtNXvskCA")
  + loc("lunes", False, "Terraza Anahí", STAR, "Lunes 16 de Noviembre",
        "Calle Becerro #100", "Dentro de Quinta Barajas<br>C.P. 37207 León, Gto.", "Lunes 16", "Horario por confirmar",
        "Quinta+Barajas+Calle+Becerro+100+37207+Le%C3%B3n+Gto",
        "https://www.google.com/maps/search/?api=1&query=Quinta+Barajas+Calle+Becerro+100+37207+Le%C3%B3n+Guanajuato",
        LUNES_NOTE))
s = re.sub(r'href="https://calendar\.google\.com[^"]*"',
    'href="https://calendar.google.com/calendar/render?action=TEMPLATE&text=XV+A%C3%B1os+Sara+Ximena&dates=20261115T200000Z/20261116T060000Z&details=Misa+2%3A00+PM+Parroquia+del+Se%C3%B1or+de+la+Salud+%7C+Recepci%C3%B3n+4%3A00+PM+Casa+G%C3%A9nesis+Events&location=Le%C3%B3n%2C+Guanajuato"', s, count=1)

# ── ITINERARIO ──
def item(icon, hora, titulo, desc, last=False):
    line = "" if last else '\n          <div class="itin-line"></div>'
    return f'''      <div class="itin-card itin-entry">
        <div class="itin-card-left">
          <div class="itin-node"><svg viewBox="0 0 24 24">{icon}</svg></div>{line}
        </div>
        <div class="itin-body">
          <div class="itin-time">{hora}</div>
          <div class="itin-title">{titulo}</div>
          <div class="itin-desc">{desc}</div>
        </div>
      </div>
'''
I_CROSS = '<path d="M12 2v20M7 7h10"/>'
I_DOOR = '<path d="M3 21h18M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16"/><circle cx="15" cy="12" r="1"/>'
I_CUP = '<path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/>'
# zapatilla de cristal (toque Cenicienta)
I_SHOE = '<path d="M3 17c0-2 1.5-3 3.5-3.2 2.6-.3 4.3-1.6 5.7-3.6L14 8l1.2 2.6c.5 1.1 1.7 1.9 3 1.9H20a1 1 0 0 1 1 1V17z"/><path d="M19 17v4"/><path d="M3 17h18"/>'
I_STAR = '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>'
sub_between('<section id="itinerario" class="sec rv">', '  <!-- DRESS CODE -->', '''<section id="itinerario" class="sec rv">
    <p class="eyebrow">Programa del Día</p>
    <h2 class="script-title">Itinerario</h2>
    <p class="section-sub">Domingo 15 de noviembre</p>
    <div class="itin-cards" id="itinCards">
''' + item(I_CROSS, "2:00 PM", "Misa de XV Años", "Parroquia del Señor de la Salud")
  + item(I_DOOR, "4:00 – 4:30 PM", "Recepción", "Casa Génesis Events")
  + item(I_CUP, "5:30 PM", "Comida", "Casa Génesis Events")
  + item(I_SHOE, "7:00 PM", "Vals", "El momento más especial de la noche")
  + item(I_STAR, "Toda la noche", "Y muchas sorpresas más", "…antes de que el reloj marque las doce", last=True) + '''    </div>
    <div class="punctual rv">
      <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="13" r="8"/><polyline points="12 9 12 13 14.5 14.5"/><path d="M9 2h6M12 2v3"/></svg>
      <p><strong>Tu puntualidad es muy importante.</strong>Te pedimos llegar a tiempo para que vivamos juntos cada momento desde el inicio.</p>
    </div>
  </section>

''')

# ── DRESS CODE ──
rep('<h2 class="script-title">Semi Formal</h2>', '<h2 class="script-title">Formal · Elegante</h2>')
rep('<p class="section-sub" style="margin-bottom:8px">¡Nos encantaría verte en otros colores!</p>',
    '<p class="section-sub" style="margin-bottom:8px">De preferencia formal, opcional para quien guste</p>')
rep('<p class="dc-avoid" style="margin-bottom:28px">Por favor evita vestir de azul cielo, azul rey o blanco —<br>esos colores son exclusivos de Victor &amp; Fernanda.</p>',
    '''<p class="dc-avoid" style="margin-bottom:22px">Los colores <strong>azul cielo</strong> y <strong>plata</strong><br>están reservados para la quinceañera.</p>
    <div class="dc-swatches rv">
      <span class="dc-sw" style="background:#000000" title="Negro"></span>
      <span class="dc-sw" style="background:#1c4995" title="Azul rey"></span>
      <span class="dc-sw" style="background:#6da36a" title="Verde salvia"></span>
      <span class="dc-sw" style="background:#ff8eb6" title="Rosa"></span>
      <span class="dc-sw" style="background:#d4b7f8" title="Lila"></span>
      <span class="dc-sw" style="background:#b02f39" title="Rojo"></span>
      <span class="dc-sw" style="background:#1e974a" title="Verde esmeralda"></span>
    </div>
    <p class="dc-sw-cap rv">Colores sugeridos</p>''')

# ── HOSPEDAJE: el cliente no dio hoteles reales ("Hotel 1") ──
sub_between('    <div class="hotel-grid">', '  <!-- GALERÍA -->', '''    <!-- PENDIENTE: hoteles del cliente (el formulario solo dijo "Hotel 1") -->
    <p class="hotel-pending rv">Muy pronto compartiremos aquí opciones de hospedaje cercanas.</p>
  </section>

''')

# ── GALERÍA: carrusel con las 13 fotos ──
fotos = "\n".join(
    f'      <div class="drop-photo" id="dropP{i}">\n        <img src="foto{i}.jpg" alt="Sara Ximena" {"loading=\"eager\"" if i < 4 else "decoding=\"async\""}>\n      </div>'
    for i in [9, 3, 6, 7, 5, 1, 4, 13, 2, 8, 10, 11, 12])
sub_between('    <div class="drop-stage" id="dropStage">', '  <!-- REGALOS -->', f'''    <div class="drop-stage" id="dropStage">
{fotos}
    </div>
    <div class="drop-dots" id="dropDots"></div>
    <span class="drop-hint rv" id="dropHint">Desliza para ver más</span>
  </section>

''')
rep('<p class="eyebrow rv">Nosotros</p>', '<p class="eyebrow rv">Galería</p>')
rep('<h2 class="script-title rv">Nuestra Historia</h2>', '<h2 class="script-title rv">Mis XV Años</h2>', 1)
rep('<p class="section-sub rv">Momentos que nos trajeron hasta aquí</p>', '<p class="section-sub rv">Un instante de mi cuento</p>')
# JS: la galería del template estaba fija a 5 fotos
sub_between("    const finalRotations=[-4,2,-3,3,-2,4];", "    ScrollTrigger.create({", '''    const finalRotations=[-3,2,-2,3,-2,2];
    const photos=[...document.querySelectorAll('#dropStage .drop-photo')].map((el,i)=>({el,rot:finalRotations[i%6]}));
    const stage=document.getElementById('dropStage'),dots=document.getElementById('dropDots');
    photos.forEach((p,i)=>{const d=document.createElement('button');d.type='button';d.setAttribute('aria-label','Foto '+(i+1));d.addEventListener('click',()=>stage.scrollTo({left:p.el.offsetLeft-(stage.clientWidth-p.el.clientWidth)/2,behavior:'smooth'}));dots.appendChild(d);});
    function syncDots(){const c=stage.scrollLeft+stage.clientWidth/2;let best=0,bd=1e9;photos.forEach((p,i)=>{const m=p.el.offsetLeft+p.el.clientWidth/2,dd=Math.abs(m-c);if(dd<bd){bd=dd;best=i;}});[...dots.children].forEach((d,i)=>d.classList.toggle('on',i===best));}
    stage.addEventListener('scroll',syncDots,{passive:true});syncDots();

''')

# ── REGALOS ──
rep('<p class="gift-msg rv">Tu presencia es nuestro regalo más preciado.<br>Si deseas celebrarnos con un obsequio,<br>con infinita gratitud lo recibimos.</p>',
    '<p class="gift-msg rv">Tu presencia es mi regalo más preciado.<br>Si deseas tener un detalle conmigo,<br>con infinita gratitud lo recibiré.</p>\n    <!-- PENDIENTE: mesa de regalos del cliente -->')

# ── ÁLBUM: el link de Drive era de la boda original ──
sub_between('    <div style="display:flex;justify-content:center">\n      <div class="album-qr-wrap rv">', '    <p style="font-family:\'Cormorant Garamond\'', '''    <!-- PENDIENTE: link del álbum compartido (QR + botón) -->
    <p class="hotel-pending rv">El enlace del álbum compartido estará disponible muy pronto.</p>
''')
rep("Sé parte de nuestra historia. Comparte tus fotos y videos de este día tan especial — queremos verlo a través de tus ojos.",
    "Sé parte de mi cuento. Comparte tus fotos y videos de esta noche tan especial — quiero verla a través de tus ojos.")

# ── RSVP (panel de invitados, X pases) ──
RSVP = open(pathlib.Path(__file__).parent / "rsvp.html", encoding="utf-8").read()
rep("  <!-- FOOTER -->", RSVP + "\n  <!-- FOOTER -->")

# ── FOOTER ──
rep('<div class="footer-names rv">Victor &amp; Fernanda</div>', '<div class="footer-names rv">Sara Ximena</div>')
rep('<div class="footer-date rv">10 · Octubre · MMXXVI</div>', '<div class="footer-date rv">15 · Noviembre · MMXXVI</div>')

# ── AUDIO: Supabase, preload none ──
rep('<audio id="bgAudio" loop preload="auto"><source src="audio.mp3" type="audio/mpeg"></audio>',
    f'<audio id="bgAudio" src="{AUDIO}" preload="none" loop></audio>')

# ── PARTÍCULAS: polvo de hada plateado/celeste (en lugar de pétalos) ──
rep("const colors=['#8CB8F0','#C5DAF8','#5588CC','#8CB8F0','#5588CC','#C5DAF8'];".replace("#5588CC", "#9AA4B2"),
    "const colors=['#FFFFFF','#82C9FF','#C0C0C0','#E6ECF2','#A9D8FF','#D6DCE4'];")
rep('''p.innerHTML=`<svg viewBox="0 0 16 22" width="${s}" height="${s*1.4}" fill="${colors[i%colors.length]}" opacity="${(.07+Math.random()*.13).toFixed(2)}"><path d="M8 21C4 16 1 10 3 4C5-1 11 2 12 7C15 13 11 19 8 21Z"/></svg>`;''',
    '''p.innerHTML=`<svg viewBox="0 0 20 20" width="${s}" height="${s}" fill="${colors[i%colors.length]}" opacity="${(.35+Math.random()*.4).toFixed(2)}" style="filter:drop-shadow(0 0 3px rgba(130,201,255,.6))"><path d="M10 0C10.8 6 14 9.2 20 10C14 10.8 10.8 14 10 20C9.2 14 6 10.8 0 10C6 9.2 9.2 6 10 0Z"/></svg>`;''')

# ── CSS extra ──
CSS = open(pathlib.Path(__file__).parent / "extra.css", encoding="utf-8").read()
rep("</style>", CSS + "\n</style>")

P.write_text(s, encoding="utf-8")
print("ok", len(s))
