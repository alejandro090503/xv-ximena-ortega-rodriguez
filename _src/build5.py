# Quinta ronda (13 oct 2026): menos saturación de fotos.
# 10 polaroids sueltas → 3 secciones de foto a pantalla completa (bordes
# difuminados, como el cierre) + 3 pares de polaroids. Cuenta regresiva
# justo antes de Ubicación.
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent
P = ROOT.parent / "index.html"
s = P.read_text(encoding="utf-8")
if "ROUND5" in s:
    sys.exit("ya aplicado")

def rep(old, new):
    global s
    if old not in s: sys.exit(f"NO ENCONTRADO: {old[:70]!r}")
    s = s.replace(old, new, 1)

# 1 ── quitar todas las polaroids sueltas
s, n = re.subn(r'  <div class="foto-break[^"]*"><figure><img src="foto\d+\.jpg"[^>]*></figure><i class="fb-sp"></i></div>\n\n', "", s)
print("polaroids quitadas:", n)

# 2 ── mover la cuenta regresiva arriba de Ubicación
a = s.index("  <!-- COUNTDOWN -->"); b = s.index("  <!-- QUOTE -->")
cd = s[a:b]; s = s[:a] + s[b:]
rep("  <!-- UBICACION -->", cd + "  <!-- UBICACION -->")

def full(n, pos, frase, firma=""):
    f = f'\n      <span class="fs-firma">{firma}</span>' if firma else ""
    return f'''  <section class="foto-sec rv">
    <div class="foto-sec-bg" style="background-image:url('foto{n}.jpg');background-position:{pos}"></div>
    <div class="foto-sec-veil"></div>
    <p class="fs-frase">{frase}</p>{f}
  </section>

'''

def par(a_, b_):
    return f'''  <div class="foto-par rv">
    <figure class="fp-a"><img src="foto{a_}.jpg" alt="Sara Ximena" decoding="async"></figure>
    <figure class="fp-b"><img src="foto{b_}.jpg" alt="Sara Ximena" decoding="async"></figure>
  </div>

'''

# 3 ── nueva distribución
rep("  <!-- COUNTDOWN -->", full(9, "center 25%", "Quince años de sueños,<br>una noche de magia") + "  <!-- COUNTDOWN -->")
rep("  <!-- ITINERARIO -->", par(3, 10) + "  <!-- ITINERARIO -->")
rep("  <!-- DRESS CODE -->", full(12, "center 30%", "Cada cuento comienza<br>con un sueño") + "  <!-- DRESS CODE -->")
rep("  <!-- REGALOS -->", par(13, 2) + "  <!-- REGALOS -->")
rep("  <!-- ALBUM -->", par(8, 11) + "  <!-- ALBUM -->")
rep("  <!-- RSVP · Panel de invitados (X pases) -->", full(6, "center 20%", "Y esa noche,<br>el reloj se detuvo para mí") + "  <!-- RSVP · Panel de invitados (X pases) -->")

CSS = r"""
/* ROUND5 · fotos a pantalla completa con bordes difuminados + pares de polaroids */
.foto-sec{position:relative;min-height:82vh;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;text-align:center;padding:60px 28px 120px;overflow:hidden}
.foto-sec-bg{position:absolute;inset:0;background-size:cover;background-repeat:no-repeat;
  -webkit-mask-image:linear-gradient(to bottom,transparent 0,rgba(0,0,0,.35) 60px,rgba(0,0,0,.85) 140px,#000 180px,#000 calc(100% - 180px),rgba(0,0,0,.85) calc(100% - 140px),rgba(0,0,0,.35) calc(100% - 60px),transparent 100%);
          mask-image:linear-gradient(to bottom,transparent 0,rgba(0,0,0,.35) 60px,rgba(0,0,0,.85) 140px,#000 180px,#000 calc(100% - 180px),rgba(0,0,0,.85) calc(100% - 140px),rgba(0,0,0,.35) calc(100% - 60px),transparent 100%);
  animation:fsZoom 18s ease-in-out infinite alternate}
@keyframes fsZoom{from{scale:1}to{scale:1.06}}
.foto-sec-veil{position:absolute;inset:0;pointer-events:none;background:linear-gradient(180deg,rgba(15,47,85,0) 30%,rgba(15,47,85,.42) 68%,rgba(15,47,85,.3) 86%,rgba(15,47,85,0) 100%)}
.fs-frase{position:relative;z-index:2;font-family:'Great Vibes',cursive;font-size:clamp(36px,10vw,48px);line-height:1.2;color:#fff;text-shadow:0 3px 18px rgba(0,0,0,.45);max-width:340px}
.foto-par{position:relative;display:flex;justify-content:center;align-items:flex-start;gap:4px;padding:34px 14px 40px}
.foto-par figure{margin:0;width:46%;max-width:200px;background:#fff;padding:7px 7px 26px;border-radius:3px;box-shadow:0 16px 34px rgba(42,69,96,.17),0 2px 6px rgba(42,69,96,.08);animation:levitate 6s ease-in-out infinite}
.foto-par .fp-a{rotate:-4deg}
.foto-par .fp-b{rotate:3.5deg;margin-top:34px;animation-delay:-3s}
.foto-par img{width:100%;aspect-ratio:2/3;object-fit:cover;object-position:center 25%;display:block;border-radius:2px}
.foto-par::before{content:'';position:absolute;left:50%;top:50%;width:90%;height:70%;transform:translate(-50%,-50%);background:radial-gradient(ellipse,rgba(130,201,255,.25),transparent 70%);z-index:-1;pointer-events:none}
"""
rep("</style>", "/* ROUND5 */" + CSS + "\n</style>")
P.write_text(s, encoding="utf-8")
print("ok")
