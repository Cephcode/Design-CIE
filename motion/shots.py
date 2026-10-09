import sys, json
from playwright.sync_api import sync_playwright
times=[float(x) for x in sys.argv[1].split(",")]; out=sys.argv[2]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
    pg.goto("file://"+__import__("os").path.abspath("index.html")); pg.wait_for_function("window.READY===true"); pg.wait_for_timeout(300)
    errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)))
    for i,t in enumerate(times):
        pg.evaluate(f"render({t})")
        pg.screenshot(path=f"{out}_{i:02d}.jpg",type="jpeg",quality=70)
    print("errors",errs)
    b.close()
