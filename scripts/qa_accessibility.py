import asyncio,json
from pathlib import Path
from playwright.async_api import async_playwright
async def main():
 failures=[];results=[]
 async with async_playwright() as p:
  browser=await p.chromium.launch(headless=True,args=["--no-sandbox"])
  for w,h in [(390,844),(1440,900)]:
   context=await browser.new_context(viewport={"width":w,"height":h})
   page=await context.new_page()
   await page.goto("http://127.0.0.1:8000/",wait_until="domcontentloaded")
   await page.get_by_role("button",name="Add Item").wait_for(timeout=30000)
   for tab in ["inventory","recipes","shopping-list","analytics"]:
    if w<768:await page.locator(".pp-nav-mobile button").filter(has_text={"inventory":"Inventory","recipes":"Recipes","shopping-list":"Shopping list","analytics":"Insights"}[tab]).click()
    else:await page.locator(".pp-nav-desktop button").filter(has_text={"inventory":"Inventory","recipes":"Recipes","shopping-list":"Shopping list","analytics":"Insights"}[tab]).click()
    await page.wait_for_timeout(250)
    await page.add_script_tag(path="node_modules/axe-core/axe.min.js")
    found=await page.evaluate("""async()=>{const data=await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa','wcag22aa']}});return data.violations.map(v=>({id:v.id,impact:v.impact,targets:v.nodes.slice(0,4).map(n=>n.target.join(' '))}));}""")
    results.append({"width":w,"tab":tab,"violations":found})
    failures.extend([{"width":w,"tab":tab,**v} for v in found if v["impact"] in ("serious","critical")])
   await context.close()
  await browser.close()
 Path("qa-output/axe-results.json").write_text(json.dumps(results,indent=2))
 print(json.dumps({"criticalOrSerious":failures,"results":results},indent=2))
 if failures:raise RuntimeError("Accessibility regression")
if __name__=="__main__":asyncio.run(main())
