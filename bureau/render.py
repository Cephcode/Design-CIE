"""Rendu de la vidéo du bureau du CIE.

Usage (depuis le dossier bureau/) :
    python3 render.py                  # rendu complet -> sortie/
    python3 render.py --apercu 12,30   # quelques images de contrôle -> sortie/apercu_*.jpg

Il faut : Python 3, playwright (pip install playwright ; python -m playwright install chromium) et ffmpeg.
"""
import argparse, functools, http.server, json, os, shutil, socketserver, subprocess, sys, threading, time
from multiprocessing import Process

ICI = os.path.dirname(os.path.abspath(__file__))
FPS = 30
PORT = 8765


def serveur():
    class Silencieux(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass
    handler = functools.partial(Silencieux, directory=ICI)
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def ouvrir(p):
    b = p.chromium.launch()
    page = b.new_page(viewport={"width": 1080, "height": 1920})
    erreurs = []
    page.on("pageerror", lambda e: erreurs.append(str(e)))
    page.goto(f"http://127.0.0.1:{PORT}/index.html?render")
    try:
        page.wait_for_function("window.READY === true", timeout=60000)
    except Exception:
        sys.exit("La page ne démarre pas. Erreurs : " + " | ".join(erreurs) + "\nVérifie contenu.json (virgules, guillemets).")
    return b, page


def travailleur(w, nw, n, dossier):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b, page = ouvrir(p)
        clip = {"x": 0, "y": 0, "width": 1080, "height": 1920}
        for f in range(w, n, nw):
            page.evaluate(f"render({f / FPS})")
            page.screenshot(path=os.path.join(dossier, f"{f:05d}.jpg"), type="jpeg", quality=93, clip=clip)
        b.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apercu", help="instants en secondes, séparés par des virgules")
    ap.add_argument("--encoder-seulement", action="store_true", help="réutilise sortie/images déjà rendues")
    ap.add_argument("--travailleurs", type=int, default=max(1, min(4, os.cpu_count() or 1)))
    args = ap.parse_args()
    from playwright.sync_api import sync_playwright

    httpd = serveur()
    sortie = os.path.join(ICI, "sortie")
    os.makedirs(sortie, exist_ok=True)
    with sync_playwright() as p:
        b, page = ouvrir(p)
        dur = page.evaluate("window.DUR")
        musique = page.evaluate("window.MUSIQUE")
        if args.apercu:
            for i, t in enumerate(args.apercu.split(",")):
                page.evaluate(f"render({float(t)})")
                page.locator("#stage").screenshot(path=os.path.join(sortie, f"apercu_{i:02d}.jpg"), type="jpeg", quality=80)
            print("Aperçus écrits dans", sortie)
            b.close()
            return
        b.close()

    n = int(round(dur * FPS))
    images = os.path.join(sortie, "images")
    if not args.encoder_seulement:
        shutil.rmtree(images, ignore_errors=True)
        os.makedirs(images)
        print(f"Durée {dur:.1f} s, {n} images, {args.travailleurs} travailleurs", flush=True)
        t0 = time.time()
        procs = [Process(target=travailleur, args=(w, args.travailleurs, n, images)) for w in range(args.travailleurs)]
        for pr in procs: pr.start()
        for pr in procs: pr.join()
        print(f"Images faites en {time.time() - t0:.0f} s", flush=True)
    httpd.shutdown()

    fichier = os.path.join(ICI, musique.get("fichier") or "musique.mp3")
    debut = float(musique.get("debut_secondes") or 0)
    son = []
    if os.path.exists(fichier):
        son = ["-ss", str(debut), "-t", f"{dur:.2f}", "-i", fichier]
        filtre = ["-af", f"afade=t=in:st=0:d=0.05,afade=t=out:st={max(0, dur - 2.2):.2f}:d=2.2", "-c:a", "aac", "-b:a", "160k"]
    else:
        print("ATTENTION : pas de musique trouvée (" + fichier + "), la vidéo sera muette.")
        filtre = []
    base = ["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", os.path.join(images, "%05d.jpg")] + son
    hd = os.path.join(sortie, "bureau-cie.mp4")
    wa = os.path.join(sortie, "bureau-cie-whatsapp.mp4")
    subprocess.run(base + ["-c:v", "libx264", "-preset", "medium", "-crf", "21", "-maxrate", "6M", "-bufsize", "10M", "-pix_fmt", "yuv420p"] + filtre + ["-shortest", "-movflags", "+faststart", hd], check=True)
    subprocess.run(base + ["-vf", "scale=720:1280:flags=lanczos", "-c:v", "libx264", "-preset", "medium", "-b:v", "1100k", "-maxrate", "1500k", "-bufsize", "4000k", "-pix_fmt", "yuv420p"] + (filtre[:-2] + ["-b:a", "128k"] if filtre else []) + ["-shortest", "-movflags", "+faststart", wa], check=True)
    shutil.rmtree(images, ignore_errors=True)
    for f in (hd, wa):
        print(f"{f} : {os.path.getsize(f) / 1e6:.1f} Mo")


if __name__ == "__main__":
    main()
