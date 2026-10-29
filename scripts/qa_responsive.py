#!/usr/bin/env python3
import asyncio,json
from pathlib import Path
from playwright.async_api import async_playwright
OUT=Path("qa-output");OUT.mkdir(exist_ok=True)
URL="http://127.0.0.1:8000/"
async def main():
 rows=[]
 async with async_playwright() as p:
  browser=await p.chromium.launch(headless=True,args=["--no-sandbox"])
  for w,h,label in [(320,740,"small"),(390,844,"phone"),(768,900,"tablet"),(1024,768,"laptop"),(1440,900,"desktop")]:
   context=await browser.new_context(viewport={"width":w,"height":h},accept_downloads=True,reduced_motion="reduce")
   page=await context.new_page();errors=[];console=[];requests=[]
   page.on("pageerror",lambda e:errors.append(str(e)))
   page.on("console",lambda m:console.append(m.text) if m.type=="error" else None)
   page.on("requestfailed",lambda request:requests.append(request.url))
   await page.goto(URL,wait_until="domcontentloaded",timeout=60000)
   try:await page.get_by_role("button",name="Add Item").wait_for(timeout=16000)
   except Exception:
    diagnostic=await page.evaluate("""() => ({root:document.querySelector('#root')?.innerHTML.slice(0,900),react:typeof window.React,babel:typeof window.Babel,idb:typeof window.idb,ready:document.readyState})""")
    await page.screenshot(path=str(OUT/"render-failure.png"))
    print(json.dumps({"errors":errors,"console":console[-15:],"requests":requests[-15:],"diagnostic":diagnostic},indent=2),flush=True)
    raise
   assert await page.locator(".pp-hero h1").is_visible(),(label,"hero")
   assert await page.locator(".pp-overview article").count()==3,(label,"summary")
   metrics=await page.evaluate("() => ({viewport:innerWidth,scrollWidth:document.documentElement.scrollWidth,hero:document.querySelector('.pp-hero').getBoundingClientRect().width})")
   assert metrics["scrollWidth"]<=w+2,(label,"overflow",metrics)
   if w<768:assert await page.locator(".pp-nav-mobile").is_visible(),(label,"bottom navigation")
   await page.get_by_role("button",name="Add Item").click()
   dialog=page.get_by_role("dialog");await dialog.wait_for(state="visible")
   await dialog.get_by_role("textbox",name="Item name").fill("Brown rice")
   await dialog.get_by_role("spinbutton",name="Quantity").fill("2")
   await dialog.get_by_role("button",name="Save Item").click()
   await page.get_by_role("cell",name="Brown rice",exact=True).wait_for(timeout=8000)
   await page.get_by_role("button",name="Edit Brown rice").click()
   await dialog.get_by_role("textbox",name="Item name").fill("Brown rice pack")
   await dialog.get_by_role("button",name="Save Item").click()
   await page.get_by_role("cell",name="Brown rice pack",exact=True).wait_for()
   await page.reload(wait_until="domcontentloaded")
   await page.get_by_role("cell",name="Brown rice pack").wait_for(timeout=25000)
   async with page.expect_download(timeout=15000) as download:
    await page.get_by_role("button",name="Download backup").click()
   file=await download.value
   assert file.suggested_filename.endswith(".json")
   if w<768:await page.locator(".pp-nav-mobile").get_by_role("button",name="Shopping list").click()
   else:await page.locator(".pp-nav-desktop").get_by_role("button",name="Shopping list").click()
   await page.locator("#pp-grocery-input").fill("Tomatoes & basil")
   await page.get_by_role("button",name="Add item").click()
   await page.get_by_text("Tomatoes & basil").wait_for()
   await page.get_by_role("checkbox",name="Mark Tomatoes & basil as purchased").check()
   await page.reload(wait_until="domcontentloaded")
   await page.get_by_role("checkbox",name="Mark Tomatoes & basil as not purchased").wait_for(timeout=25000)
   if w<768:await page.locator(".pp-nav-mobile").get_by_role("button",name="Insights").click()
   else:await page.locator(".pp-nav-desktop").get_by_role("button",name="Insights").click()
   await page.get_by_text("Totals:").wait_for()
   assert not errors,(label,"errors",errors)
   if label in ["desktop","phone","small"]:
    if w<768:await page.locator(".pp-nav-mobile").get_by_role("button",name="Inventory").click()
    else:await page.locator(".pp-nav-desktop").get_by_role("button",name="Inventory").click()
    await page.screenshot(path=str(OUT/(label+"-dashboard.png")),full_page=False)
   rows.append({"viewport":label,"width":w,"dashboard":"pass","database":"pass","shopping":"pass","navigation":"pass","errors":errors})
   await context.close()
  await browser.close()
 (OUT/"responsive-results.json").write_text(json.dumps(rows,indent=2))
 print(json.dumps(rows,indent=2))
if __name__=="__main__":asyncio.run(main())
