# Segunda ronda (11 oct 2026): rediseño de secciones pedido por Alejandro.
# Corre sobre el index.html ya transformado por build.py.
import pathlib, sys, re

ROOT = pathlib.Path(__file__).resolve().parent
P = ROOT.parent / "index.html"
s = P.read_text(encoding="utf-8")
if "ROUND2" in s:
    sys.exit("ya aplicado")

def sub_between(start, end, new):
    global s
    a = s.index(start); b = s.index(end, a)
    s = s[:a] + new + s[b:]

def rep(old, new):
    global s
    if old not in s: sys.exit(f"NO ENCONTRADO: {old[:70]!r}")
    s = s.replace(old, new, 1)

# 1 ── quitar la fecha encima de la cuenta regresiva
sub_between("  <!-- FECHA -->", "  <!-- COUNTDOWN -->", "")

# 2 ── botones de ubicación que inviten a tocarlos
rep('<button class="loc-tab" data-panel="recepcion">Recepción</button>',
    '<button class="loc-tab loc-tab--hint" data-panel="recepcion"><span>Recepción</span><i class="loc-dot"></i></button>')
rep('<button class="loc-tab" data-panel="lunes">Lunes 16</button>',
    '<button class="loc-tab loc-tab--hint" data-panel="lunes"><span>Lunes 16</span><i class="loc-dot"></i></button>')
rep('<button class="loc-tab active" data-panel="misa">Misa</button>',
    '<button class="loc-tab active" data-panel="misa"><span>Misa</span></button>')
rep('    <div class="loc-panel active" id="panel-misa">',
    '    <p class="loc-tap-hint rv"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11V5.5a1.5 1.5 0 0 1 3 0V11"/><path d="M12 10.5V9a1.5 1.5 0 0 1 3 0v2"/><path d="M15 10.5a1.5 1.5 0 0 1 3 0V15a6 6 0 0 1-6 6h-.6a6 6 0 0 1-4.9-2.6L4 14.6a1.5 1.5 0 0 1 2.4-1.8L9 15"/></svg>Toca cada pestaña para ver las 3 ubicaciones</p>\n    <div class="loc-panel active" id="panel-misa">')
rep("    tab.classList.add('active');",
    "    tab.classList.add('active');tab.classList.remove('loc-tab--hint');")

# 3 ── itinerario: medianoche de cuento
rep('<section id="itinerario" class="sec rv">\n    <p class="eyebrow">Programa del Día</p>\n    <h2 class="script-title">Itinerario</h2>\n    <p class="section-sub">Domingo 15 de noviembre</p>',
    '''<section id="itinerario" class="sec rv">
    <div class="itin-sky" aria-hidden="true"></div>
    <div class="itin-clock" aria-hidden="true">
      <svg viewBox="0 0 120 120">
        <defs><linearGradient id="slv" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8E959E"/><stop offset=".3" stop-color="#F4F6F8"/><stop offset=".55" stop-color="#B9C0C8"/><stop offset=".75" stop-color="#FFFFFF"/><stop offset="1" stop-color="#9AA1AA"/></linearGradient></defs>
        <circle cx="60" cy="60" r="54" fill="rgba(255,255,255,.04)" stroke="url(#slv)" stroke-width="2"/>
        <circle cx="60" cy="60" r="47" fill="none" stroke="url(#slv)" stroke-width=".7" opacity=".7"/>
        <g fill="#E6ECF2" font-family="Bodoni Moda,serif" font-size="10" text-anchor="middle">
          <text x="60" y="22">XII</text><text x="99" y="64">III</text><text x="60" y="105">VI</text><text x="21" y="64">IX</text>
        </g>
        <g stroke="#EEF3F8" stroke-linecap="round">
          <line class="clk-h" x1="60" y1="60" x2="60" y2="34" stroke-width="3"/>
          <line class="clk-m" x1="60" y1="60" x2="60" y2="24" stroke-width="1.8"/>
        </g>
        <circle cx="60" cy="60" r="3.5" fill="url(#slv)"/>
      </svg>
    </div>
    <p class="eyebrow">Programa del Día</p>
    <h2 class="script-title">Itinerario</h2>
    <p class="section-sub">Domingo 15 de noviembre · una noche de cuento</p>''')

# 4 ── código de vestimenta: diseño de xv-mia (Mia F. Correa) sin copos
sub_between('  <section id="dresscode" class="sec rv">', '  <!-- HOSPEDAJE -->', '''  <section id="dresscode" class="sec rv">
    <p class="eyebrow">Etiqueta</p>
    <h2 class="script-title">Código de Vestimenta</h2>
    <div class="dc-note">Formal</div>
    <p class="dc-optional">De preferencia, opcional para quien guste</p>
    <div class="dc-cards">
      <figure class="dc-card tex-card">
        <img src="./caballero.png" alt="Caballero con traje formal" loading="eager">
        <figcaption>
          <span class="dc-card-lbl">Caballeros</span>
          <span class="dc-card-sub">Traje formal</span>
        </figcaption>
      </figure>
      <figure class="dc-card tex-card">
        <img src="./dama.png" alt="Dama con vestido largo" loading="eager">
        <figcaption>
          <span class="dc-card-lbl">Damas</span>
          <span class="dc-card-sub">Vestido largo</span>
        </figcaption>
      </figure>
    </div>
    <p class="dc-reserve">Estos colores están <strong>reservados</strong> para la quinceañera</p>
    <div class="dc-crown-row">
      <span class="dc-crown" style="background-color:#82c9ff;" title="Azul cielo"></span>
      <span class="dc-crown dc-crown--silver" title="Plata"></span>
    </div>
    <p class="dc-crown-names">Azul cielo · Plata</p>
  </section>

''')

# 5 ── mesa de regalos
sub_between('  <section id="regalos">', '  <!-- ALBUM -->', '''  <section id="regalos">
    <div class="gift-glow" aria-hidden="true"></div>
    <p class="eyebrow rv">Mesa de Regalos</p>
    <h2 class="script-title rv">Un Detalle</h2>
    <div class="gift-card rv">
      <span class="gift-corner gc-tl"></span><span class="gift-corner gc-tr"></span><span class="gift-corner gc-bl"></span><span class="gift-corner gc-br"></span>
      <div class="gift-box" aria-hidden="true">
        <svg viewBox="0 0 64 64" fill="none">
          <defs><linearGradient id="gslv" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#9AA1AA"/><stop offset=".35" stop-color="#FFFFFF"/><stop offset=".6" stop-color="#B9C0C8"/><stop offset="1" stop-color="#E6ECF2"/></linearGradient></defs>
          <rect x="9" y="28" width="46" height="29" rx="2.5" stroke="url(#gslv)" stroke-width="1.8" fill="rgba(130,201,255,.10)"/>
          <rect x="6" y="20" width="52" height="9" rx="2" stroke="url(#gslv)" stroke-width="1.8" fill="rgba(130,201,255,.16)"/>
          <path d="M32 20V57" stroke="url(#gslv)" stroke-width="2.2"/>
          <path d="M32 20C25 9 15 10 17 16C18.5 20 26 20 32 20Z" stroke="url(#gslv)" stroke-width="1.8" fill="rgba(255,255,255,.08)"/>
          <path d="M32 20C39 9 49 10 47 16C45.5 20 38 20 32 20Z" stroke="url(#gslv)" stroke-width="1.8" fill="rgba(255,255,255,.08)"/>
        </svg>
        <i class="gift-spark s1"></i><i class="gift-spark s2"></i><i class="gift-spark s3"></i>
      </div>
      <p class="gift-msg">Tu presencia es mi regalo más preciado.<br>Si deseas tener un detalle conmigo,<br>con infinita gratitud lo recibiré.</p>
      <div class="gift-sep"><span></span><svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C12.9 7 17 11.1 24 12C17 12.9 12.9 17 12 24C11.1 17 7 12.9 0 12C7 11.1 11.1 7 12 0Z"/></svg><span></span></div>
      <!-- PENDIENTE: datos de mesa de regalos del cliente -->
      <p class="gift-soon">Muy pronto compartiré aquí los detalles de mi mesa de regalos</p>
    </div>
  </section>


''')

# 6 ── álbum: QR difuminado, se habilita el día del evento
sub_between('    <!-- PENDIENTE: link del álbum compartido (QR + botón) -->', "    <p style=\"font-family:'Cormorant Garamond'", '''    <!-- PENDIENTE: link real del álbum; al tenerlo, quitar .album-locked y poner el QR/botón -->
    <div class="album-qr-wrap album-locked rv">
      <div class="qr-corner-extra tr"></div>
      <div class="qr-corner-extra bl"></div>
      <div class="qr-deco-line"><span>Escanea para subir</span></div>
      <div class="qr-blur-box">
        <img src="https://api.qrserver.com/v1/create-qr-code/?size=190x190&color=0F2F55&bgcolor=FFFFFF&data=https%3A%2F%2Fxv-ximena-ortega-rodriguez.vercel.app" alt="" aria-hidden="true">
        <div class="qr-lock">
          <svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>
        </div>
      </div>
      <div class="qr-deco-line"><span>Álbum compartido</span></div>
      <span class="qr-label">Sara Ximena · 15 · XI · MMXXVI</span>
    </div>
    <p class="album-soon rv"><strong>Se habilitará el día del evento</strong>El 15 de noviembre podrás escanear el código y subir tus fotos y videos.</p>
''')

# 7 ── RSVP diseño boda-jennifer (+ mismo JS del panel)
sub_between("  <!-- RSVP · Panel de invitados (X pases) -->", "  <!-- FOOTER -->",
            (ROOT / "rsvp.html").read_text(encoding="utf-8") + "\n")

# 8 ── cierre + footer al estilo XV (xv-mia / xv pasadas)
sub_between("  <!-- FOOTER -->", "</div>\n\n<button class=\"music-fab\"", '''  <!-- CIERRE -->
  <section class="closing">
    <div class="closing-bg"></div>
    <div class="closing-veil"></div>
    <p class="closing-text rv">Dicen que la magia dura hasta la medianoche;<br>la mía durará para siempre si la vivo a tu lado.</p>
    <p class="closing-carino rv">Con cariño,</p>
    <div class="closing-sign rv">Sara Ximena</div>
  </section>

  <!-- FOOTER -->
  <footer id="footer">
    <div class="ft-tiara rv" aria-hidden="true">
      <svg viewBox="0 0 160 70" fill="none">
        <defs><linearGradient id="fslv" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8E959E"/><stop offset=".3" stop-color="#F4F6F8"/><stop offset=".5" stop-color="#B9C0C8"/><stop offset=".7" stop-color="#FFFFFF"/><stop offset="1" stop-color="#9AA1AA"/></linearGradient></defs>
        <path d="M14 58 Q80 40 146 58" stroke="url(#fslv)" stroke-width="1.6"/>
        <path d="M22 54 L34 30 L48 47 L62 20 L80 44 L98 20 L112 47 L126 30 L138 54" stroke="url(#fslv)" stroke-width="1.4" stroke-linejoin="round"/>
        <circle cx="80" cy="12" r="5" stroke="url(#fslv)" stroke-width="1.4"/><circle cx="62" cy="16" r="2.6" fill="url(#fslv)"/><circle cx="98" cy="16" r="2.6" fill="url(#fslv)"/>
        <circle cx="34" cy="26" r="2" fill="url(#fslv)"/><circle cx="126" cy="26" r="2" fill="url(#fslv)"/>
        <path d="M80 44 L80 54" stroke="url(#fslv)" stroke-width="1"/>
      </svg>
    </div>
    <div class="ft-eyebrow rv">Mis XV Años</div>
    <div class="footer-names rv">Sara Ximena</div>
    <div class="ft-surname rv">Ortega Rodríguez</div>
    <div class="footer-date rv">15 · Noviembre · MMXXVI</div>
    <div class="ft-line rv"><span></span><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C12.9 7 17 11.1 24 12C17 12.9 12.9 17 12 24C11.1 17 7 12.9 0 12C7 11.1 11.1 7 12 0Z"/></svg><span></span></div>
    <p class="ft-thanks rv">Gracias por ser parte de mi cuento</p>
    <a href="https://www.instagram.com/elysium.invitaciones" target="_blank" rel="noopener" class="footer-credit">Diseño por <span>@elysium.invitaciones</span></a>
  </footer>

''')
# el crédito del álbum ya vive en el footer
s = re.sub(r"\n    <p style=\"font-family:'Cormorant Garamond',serif;font-style:italic;font-size:11px;letter-spacing:2px;color:var\(--copper\);text-align:center;margin-top:18px;opacity:\.6\">@elysium\.invitaciones</p>", "", s, count=1)

# 9 ── botón de música: zapatilla de cristal
sub_between('<button class="music-fab" id="musicFab" aria-label="Música">', '</button>\n<audio', '''<button class="music-fab" id="musicFab" aria-label="Reproducir o pausar música">
  <svg class="slipper" viewBox="0 0 120 84" aria-hidden="true">
    <defs>
      <linearGradient id="glassA" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".95"/><stop offset=".35" stop-color="#CDEBFF" stop-opacity=".75"/><stop offset=".7" stop-color="#82C9FF" stop-opacity=".7"/><stop offset="1" stop-color="#E9F6FF" stop-opacity=".9"/></linearGradient>
      <linearGradient id="glassE" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8E959E"/><stop offset=".3" stop-color="#FFFFFF"/><stop offset=".55" stop-color="#B9C0C8"/><stop offset=".8" stop-color="#FFFFFF"/><stop offset="1" stop-color="#9AA1AA"/></linearGradient>
      <linearGradient id="glassS" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".95"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
      <clipPath id="slipClip"><path d="M8 62C8 54 15 50 26 49C40 47.5 50 42 58 32C63 25.5 67 18 70 12C72 9 76 8.5 79 11C86 18 92 28 101 36C106 40.5 111 45 112 52C113 58 110 62 104 62Z"/></clipPath>
    </defs>
    <path class="slip-heel" d="M100 60L103 80L109 80L108 58Z" fill="url(#glassA)" stroke="url(#glassE)" stroke-width="1.6" stroke-linejoin="round"/>
    <path class="slip-body" d="M8 62C8 54 15 50 26 49C40 47.5 50 42 58 32C63 25.5 67 18 70 12C72 9 76 8.5 79 11C86 18 92 28 101 36C106 40.5 111 45 112 52C113 58 110 62 104 62Z" fill="url(#glassA)" stroke="url(#glassE)" stroke-width="2" stroke-linejoin="round"/>
    <path d="M30 52C44 50 56 44 64 33C68 27 71 21 74 16C80 24 86 33 94 40C82 41 70 46 58 52Z" fill="rgba(255,255,255,.35)"/>
    <path d="M12 62L104 62" stroke="url(#glassE)" stroke-width="2.4" stroke-linecap="round"/>
    <path d="M18 56C30 54 44 52 54 44" stroke="#fff" stroke-width="1.6" stroke-linecap="round" opacity=".85" fill="none"/>
    <g clip-path="url(#slipClip)"><rect class="slip-shine" x="-40" y="0" width="24" height="84" fill="url(#glassS)" transform="skewX(-20)"/></g>
    <g class="slip-sparks" fill="#fff">
      <path d="M86 6C86.5 9.5 88.5 11.5 92 12C88.5 12.5 86.5 14.5 86 18C85.5 14.5 83.5 12.5 80 12C83.5 11.5 85.5 9.5 86 6Z"/>
      <path d="M20 34C20.4 36.6 21.4 37.6 24 38C21.4 38.4 20.4 39.4 20 42C19.6 39.4 18.6 38.4 16 38C18.6 37.6 19.6 36.6 20 34Z"/>
      <path d="M108 22C108.3 24 109 24.7 111 25C109 25.3 108.3 26 108 28C107.7 26 107 25.3 105 25C107 24.7 107.7 24 108 22Z"/>
    </g>
  </svg>
''')

# 10 ── fundido uniforme entre secciones: capa de fondo con máscara de largo fijo
for sec in ["countdown", "quote", "familiares", "ubicacion", "itinerario", "dresscode", "hospedaje", "galeria", "regalos", "album", "rsvp"]:
    s = re.sub(rf'(<section id="{sec}"[^>]*>)', r'\1\n    <div class="sec-fx" aria-hidden="true"></div>', s, count=1)
s = s.replace('<footer id="footer">', '<footer id="footer">\n    <div class="sec-fx" aria-hidden="true"></div>', 1)
s = s.replace('<section class="closing">', '<section class="closing">\n    <div class="sec-fx" aria-hidden="true"></div>', 1)

# JS de regalos apuntaba a .gift-option (ya no existe) → .gift-card, ok si no hay matches
CSS = (ROOT / "extra2.css").read_text(encoding="utf-8")
rep("</style>", "/* ROUND2 */\n" + CSS + "\n</style>")
P.write_text(s, encoding="utf-8")
print("ok", len(s))
