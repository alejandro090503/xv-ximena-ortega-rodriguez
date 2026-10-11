# Tercera ronda (11 oct 2026): itinerario de cuento con ilustraciones reales,
# zapatilla real en el botón de música, levitación de cards, QR sin marco.
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent
P = ROOT.parent / "index.html"
s = P.read_text(encoding="utf-8")
if "ROUND3" in s:
    sys.exit("ya aplicado")

def sub_between(start, end, new):
    global s
    a = s.index(start); b = s.index(end, a)
    s = s[:a] + new + s[b:]

# ── ITINERARIO: un cuento en capítulos ──
def cap(n, img, alt, hora, titulo, desc, side):
    return f'''      <article class="cap itin-entry cap--{side}">
        <div class="cap-art itin-node"><span class="cap-halo"></span><img src="cuento/{img}.webp" alt="{alt}" decoding="async"></div>
        <div class="cap-txt">
          <span class="cap-num">Capítulo {n}</span>
          <span class="cap-hora">{hora}</span>
          <h3 class="cap-tit">{titulo}</h3>
          <p class="cap-desc">{desc}</p>
        </div>
      </article>
      <div class="cap-dust" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div>
'''
sub_between('  <section id="itinerario" class="sec rv">', '  <!-- DRESS CODE -->', '''  <section id="itinerario" class="sec rv">
    <div class="sec-fx" aria-hidden="true"></div>
    <div class="itin-sky" aria-hidden="true"></div>
    <img class="itin-castle" src="cuento/castillo.webp" alt="" aria-hidden="true">
    <p class="cap-once">Érase una vez…</p>
    <p class="eyebrow">Programa del Día</p>
    <h2 class="script-title">Itinerario</h2>
    <p class="section-sub">Domingo 15 de noviembre · una noche de cuento</p>
    <div class="cap-list" id="itinCards">
''' + cap("I", "misa", "Paloma blanca", "2:00 PM", "Misa de XV Años", "Parroquia del Señor de la Salud", "l")
    + cap("II", "carroza", "Carroza de Cenicienta", "4:00 – 4:30 PM", "Recepción", "La carroza nos lleva a Casa Génesis Events", "r")
    + cap("III", "calabaza", "Calabaza mágica", "5:30 PM", "Comida", "Un banquete digno del palacio", "l")
    + cap("IV", "vals", "Cenicienta y el príncipe bailando", "7:00 PM", "Vals", "El baile más esperado de la noche", "r").replace('cap--r"', 'cap--r cap--star"')
    + '''      <article class="cap itin-entry cap--l cap--last">
        <div class="cap-art itin-node"><span class="cap-halo"></span><img src="cuento/castillo.webp" alt="Castillo" decoding="async"></div>
        <div class="cap-txt">
          <span class="cap-num">Capítulo V</span>
          <span class="cap-hora">Toda la noche</span>
          <h3 class="cap-tit">Y muchas sorpresas más</h3>
          <p class="cap-desc">…antes de que el reloj marque las doce</p>
        </div>
      </article>
    </div>
    <div class="cap-reloj rv">
      <img src="cuento/reloj.webp" alt="Torre del reloj" decoding="async">
      <div>
        <p class="cap-reloj-t">Tu puntualidad es muy importante</p>
        <p class="cap-reloj-d">Como en el cuento, cada minuto cuenta: te pedimos llegar a tiempo para vivir juntos esta noche desde el inicio.</p>
      </div>
    </div>
  </section>

''')

# ── BOTÓN DE MÚSICA: zapatilla de cristal real ──
sub_between('<button class="music-fab" id="musicFab"', '</button>\n<audio', '''<button class="music-fab" id="musicFab" aria-label="Reproducir o pausar música">
  <span class="zap">
    <img src="zapatilla.webp" alt="" width="240" height="194">
    <span class="zap-shine"></span>
    <i class="zap-sp z1"></i><i class="zap-sp z2"></i><i class="zap-sp z3"></i>
  </span>
''')

# ── QR sin marco azul ──
s = s.replace('<div class="album-qr-wrap album-locked rv">\n      <div class="qr-corner-extra tr"></div>\n      <div class="qr-corner-extra bl"></div>',
              '<div class="album-qr-wrap album-locked rv">', 1)

CSS = (ROOT / "extra3.css").read_text(encoding="utf-8")
s = s.replace("</style>", "/* ROUND3 */\n" + CSS + "\n</style>", 1)
P.write_text(s, encoding="utf-8")
print("ok")
