import sys, os, time
from playwright.sync_api import sync_playwright
w, nw = int(sys.argv[1]), int(sys.argv[2])
FPS=30; DUR=49.2; N=int(round(DUR*FPS))
os.makedirs("frames", exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
    pg.goto("file://"+os.path.abspath("index.html")); pg.wait_for_function("window.READY===true"); pg.wait_for_timeout(400)
    t0=time.time()
    for f in range(w, N, nw):
        pg.evaluate(f"render({f/FPS})")
        pg.screenshot(path=f"frames/{f:05d}.jpg", type="jpeg", quality=93)
    b.close()
print("worker",w,"done",round(time.time()-t0,1),"s")
