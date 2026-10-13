# Cuarta ronda (13 oct 2026): correcciones de la clienta.
# Paleta clara (azul cielo + blanco + oro), portada foto1, padres/padrinos con
# marcos de xv-zoe, cuenta regresiva sobre foto, fotos sueltas entre secciones,
# ubicaciones en lista con foto del lugar, lluvia de sobres, sin hospedaje.
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent
P = ROOT.parent / "index.html"
s = P.read_text(encoding="utf-8")
if "ROUND4" in s:
    sys.exit("ya aplicado")

def sub_between(start, end, new):
    global s
    a = s.index(start); b = s.index(end, a)
    s = s[:a] + new + s[b:]

def rep(old, new):
    global s
    if old not in s: sys.exit(f"NO ENCONTRADO: {old[:70]!r}")
    s = s.replace(old, new, 1)

def foto(n, side):
    return f'''  <div class="foto-break foto-break--{side} rv"><figure><img src="foto{n}.jpg" alt="Sara Ximena" decoding="async"></figure><i class="fb-sp"></i></div>

'''

HEART = '<div class="heart-div"><span class="hd-bar"></span><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 21s-7.5-4.9-10-9.5C.5 8.5 2 5 5.3 5c1.9 0 3.3 1.1 4.2 2.4C10.4 6.1 11.8 5 13.7 5 17 5 18.5 8.5 17 11.5 14.5 16.1 12 21 12 21z"/></svg><span class="hd-bar r"></span></div>'

# ── foto 2 entre cuenta regresiva y la frase
rep("  <!-- QUOTE -->", foto(2, "r") + "  <!-- QUOTE -->")

# ── cuenta regresiva sobre una foto de la quinceañera
rep('<section id="countdown" class="sec rv">\n    <div class="sec-fx" aria-hidden="true"></div>',
    '<section id="countdown" class="sec rv">\n    <div class="sec-fx" aria-hidden="true"></div>\n    <div class="cd-photo" aria-hidden="true"></div>')

# ── padres y padrinos (marcos florales de xv-zoe); primero mamá y madrina
sub_between("  <!-- FAMILIARES -->", "  <!-- UBICACION -->",
    foto(9, "l") + f'''  <!-- MIS PADRES -->
  <section id="padres" class="fam-sec rv">
    <div class="sec-fx" aria-hidden="true"></div>
    <div class="marco marco-a">
      <h2 class="sec-title">Mis Padres</h2>
      {HEART}
      <div class="fam-names">Marta Leticia Rodríguez Briano<span class="fam-amp">y</span>Pablo Ortega García</div>
    </div>
  </section>

''' + foto(3, "r") + f'''  <!-- MIS PADRINOS -->
  <section id="padrinos" class="fam-sec rv">
    <div class="sec-fx" aria-hidden="true"></div>
    <div class="marco marco-b">
      <h2 class="sec-title">Mis Padrinos</h2>
      {HEART}
      <div class="fam-names">Santa Teresa Rodríguez Briano<span class="fam-amp">y</span>Rafael Guevara Rodríguez</div>
    </div>
  </section>

''' + foto(12, "l"))

# ── ubicaciones en lista, con foto de cada lugar
def lugar(img, etiqueta, nombre, calle, resto, hora, hora_lbl, link, nota=""):
    return f'''    <div class="lugar-card rv">
      <div class="lugar-photo"><img src="{img}" alt="{nombre}" decoding="async"></div>
      <div class="lugar-lt">{etiqueta}</div>
      <div class="lugar-name">{nombre}</div>
      <p class="lugar-addr"><strong>{calle}</strong><br>{resto}</p>
      <div class="lugar-time"><span>{hora_lbl}</span><strong>{hora}</strong></div>{nota}
      <a class="lugar-btn" href="{link}" target="_blank" rel="noopener">
        <svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
        Cómo llegar
      </a>
    </div>
'''
a = s.index('    <div class="loc-tabs rv" id="locTabs">'); b = s.index('    <div class="cal-section rv">', a)
s = s[:a] + lugar("lugar-misa.jpg", "Misa", "Parroquia del Señor de la Salud", "Jardín Allende 124", "Col. Obregón, 37320 León, Gto.",
                  "2:00 PM", "Misa de acción de gracias", "https://maps.app.goo.gl/PDMoNkv4uzwb6ck28") \
    + lugar("lugar-salon.jpg", "Recepción", "Casa Génesis Events", "Calle San Carlos Borrovec 145", "Fracc. Jesús María, 37299 León, Gto.",
            "4:00 PM", "Recepción", "https://maps.app.goo.gl/5iEMjSiSQtNXvskCA") \
    + lugar("lugar-terraza.jpg", "Lunes 16 de Noviembre", "Terraza Anahí", "Calle Becerro #100", "Dentro de Quinta Barajas, C.P. 37207 León, Gto.",
            "12:00 PM", "Al día siguiente", "https://www.google.com/maps/search/?api=1&query=Quinta+Barajas+Calle+Becerro+100+37207+Le%C3%B3n+Guanajuato",
            '\n      <p class="lugar-nota">Al día siguiente seguimos celebrando y esperamos contar con tu presencia.</p>') + s[b:]

# ── fotos entre ubicación/itinerario/vestimenta
rep("  <!-- ITINERARIO -->", foto(10, "r") + "  <!-- ITINERARIO -->")
rep("  <!-- DRESS CODE -->", foto(7, "l") + "  <!-- DRESS CODE -->")

# ── sin hospedaje y sin carrusel: las fotos ya van sueltas por la invitación
sub_between("  <!-- HOSPEDAJE -->", "  <!-- REGALOS -->", foto(13, "r"))
rep("  /* ── GALERÍA: FOTOS QUE CAEN ── */\n  (function(){", "  /* ── GALERÍA: FOTOS QUE CAEN ── */\n  (function(){\n    if(!document.getElementById('dropStage'))return;")

# ── mesa de regalos → lluvia de sobres (de xv-zoe), regalo físico o sobre
sub_between('  <section id="regalos">', "  <!-- ALBUM -->", '''  <section id="sgifts" class="rv" style="text-align:center">
    <div class="sec-fx" aria-hidden="true"></div>
    <div class="env-rain" id="envRain" aria-hidden="true"></div>
    <div class="env-stage">
      <p class="eyebrow">Con Cariño</p>
      <h2 class="sec-title">Mesa de Regalos</h2>
      ''' + HEART + '''
      <button class="env-interactive" id="envGift" type="button" aria-label="Sobre — toca para abrir" aria-expanded="false">
        <div class="env-body" id="envGiftBody">
          <svg class="env-svg" viewBox="0 0 260 200" preserveAspectRatio="none" aria-hidden="true">
            <defs><linearGradient id="envPaper" x1="0" y1="1" x2="1" y2="0"><stop offset="0%" stop-color="#F2F8FF"/><stop offset="100%" stop-color="#ffffff"/></linearGradient></defs>
            <rect x="18" y="52" width="224" height="132" rx="8" fill="url(#envPaper)" stroke="rgba(185,143,60,.6)" stroke-width="1.4"/>
            <path d="M18 184 L130 110 L242 184" stroke="rgba(185,143,60,.4)" stroke-width="1" fill="none"/>
          </svg>
          <div class="env-flap-wrap" aria-hidden="true">
            <svg viewBox="0 0 224 86" preserveAspectRatio="none" style="width:100%;height:100%;display:block">
              <defs><linearGradient id="envFlap" x1="0" y1="1" x2="1" y2="0"><stop offset="0%" stop-color="#E8F2FE"/><stop offset="100%" stop-color="#ffffff"/></linearGradient></defs>
              <path d="M0 0 L112 86 L224 0 Z" fill="url(#envFlap)" stroke="rgba(185,143,60,.6)" stroke-width="1.5" stroke-linejoin="round"/>
            </svg>
          </div>
          <svg class="env-seal" viewBox="0 0 60 60" aria-hidden="true">
            <circle cx="30" cy="30" r="28" fill="#9CC8EE"/>
            <circle cx="30" cy="30" r="28" fill="none" stroke="#6E9CC6" stroke-width="2" opacity=".6"/>
            <circle cx="30" cy="30" r="21.5" fill="none" stroke="#C9A04E" stroke-width="1.3"/>
            <text x="30" y="38" text-anchor="middle" font-family="'Great Vibes', cursive" font-size="24" fill="#FFFFFF">SX</text>
          </svg>
        </div>
        <div class="env-open-content" aria-live="polite">
          <svg class="env-mailbox-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="8" width="18" height="13" rx="1.5"/><path d="M3 12h18"/><path d="M12 8v13"/><path d="M12 8C10 4 6.5 4.5 7 6.5 7.4 8 10 8 12 8z"/><path d="M12 8c2-4 5.5-3.5 5-1.5C16.6 8 14 8 12 8z"/></svg>
          <p class="env-title">Tu presencia es mi mayor regalo</p>
          <p class="env-desc">pero si deseas tener un detalle conmigo, puede ser un regalo físico o en efectivo mediante lluvia de sobres.</p>
        </div>
      </button>
      <p class="env-tap-hint" id="envGiftHint">Toca para abrir</p>
    </div>
  </section>

''' + foto(8, "l"))

rep("  <!-- RSVP · Panel de invitados (X pases) -->", foto(6, "r") + "  <!-- RSVP · Panel de invitados (X pases) -->")
rep("  <!-- CIERRE -->", foto(11, "l") + "  <!-- CIERRE -->")

# ── footer: tiara en oro (antes plata sobre azul marino)
s = s.replace('<linearGradient id="fslv" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8E959E"/><stop offset=".3" stop-color="#F4F6F8"/><stop offset=".5" stop-color="#B9C0C8"/><stop offset=".7" stop-color="#FFFFFF"/><stop offset="1" stop-color="#9AA1AA"/></linearGradient>',
              '<linearGradient id="fslv" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8A6A28"/><stop offset=".3" stop-color="#E8D5A3"/><stop offset=".5" stop-color="#B98F3C"/><stop offset=".7" stop-color="#F3E3B8"/><stop offset="1" stop-color="#8A6A28"/></linearGradient>', 1)

# ── JS: marcos que aparecen + lluvia de sobres
JS = """
<script>
/* ROUND4 · marcos florales y lluvia de sobres (de xv-zoe) */
function initMarcos(){
  var ms=[].slice.call(document.querySelectorAll('.marco'));
  if(!ms.length) return;
  function mira(){var h=window.innerHeight;ms.forEach(function(m){var r=m.getBoundingClientRect();if(r.top<h*.92&&r.bottom>0)m.classList.add('is-in');});}
  window.addEventListener('scroll',mira,{passive:true});window.addEventListener('resize',mira);mira();
}
""" + (ROOT / "zoe_env.js").read_text(encoding="utf-8") + """
(function(){
  var started=false;
  function go(){if(started)return;started=true;initMarcos();initEnvRain();}
  /* la invitación se muestra al terminar el sobre; arrancar cuando .wrap ya es visible */
  var t=setInterval(function(){var w=document.querySelector('.wrap');if(w&&getComputedStyle(w).visibility==='visible'){clearInterval(t);go();}},300);
})();
</script>
"""
rep("</body>", JS + "</body>")

CSS = (ROOT / "zoe_env.css").read_text(encoding="utf-8") + "\n" + (ROOT / "extra4.css").read_text(encoding="utf-8")
rep("</style>", "/* ROUND4 */\n" + CSS + "\n</style>")
P.write_text(s, encoding="utf-8")
print("ok")
