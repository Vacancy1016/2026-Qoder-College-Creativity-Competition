import urllib.request, pathlib, re, json, time
root=pathlib.Path(__file__).resolve().parent
fonts={
 'Archivo':'https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900',
 'Playfair':'https://fonts.googleapis.com/css2?family=Playfair:opsz,wdth,wght@5..1200,87.5..112.5,300..900',
 'Yellowtail':'https://fonts.googleapis.com/css2?family=Yellowtail',
 'Titan One':'https://fonts.googleapis.com/css2?family=Titan+One'
}
def get(url):
 for attempt in range(3):
  try:
   req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'})
   return urllib.request.urlopen(req,timeout=30).read()
  except Exception:
   if attempt==2: raise
   time.sleep(1)
for name,url in fonts.items():
 out=root/'vendor'/(name.replace(' ','')+'.woff2')
 if not out.exists() or out.read_bytes()[:4]!=b'wOF2':
  css=get(url).decode(); urls=re.findall(r'url\((https[^)]+)\)',css)
  out.write_bytes(get(urls[-1]))
 print(name,out.stat().st_size)
for name,url in [
 ('gsap','https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js'),
 ('ScrollTrigger','https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js'),
 ('SplitText','https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/SplitText.min.js'),
 ('DrawSVGPlugin','https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/DrawSVGPlugin.min.js'),
 ('InertiaPlugin','https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/InertiaPlugin.min.js'),
 ('lenis','https://cdn.jsdelivr.net/npm/lenis@1.3.17/dist/lenis.min.js')]:
 out=root/'vendor'/(name+'.js')
 if not out.exists(): out.write_bytes(get(url))
 print(name,out.stat().st_size)
