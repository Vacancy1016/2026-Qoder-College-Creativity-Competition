from pathlib import Path
import base64
r=Path(__file__).resolve().parent
faces=[]
for family,name,weight,stretch in [('Archivo','Archivo','100 900','62% 125%'),('Playfair','Playfair','300 900','87.5% 112.5%'),('Yellowtail','Yellowtail','400','normal'),('Titan One','TitanOne','400','normal')]:
 b=(r/'vendor'/f'{name}.woff2').read_bytes()
 fmt='woff2' if b[:4]==b'wOF2' else 'truetype'
 faces.append(f"@font-face{{font-family:'{family}';src:url(data:font/{fmt};base64,{base64.b64encode(b).decode()}) format('{fmt}');font-weight:{weight};font-stretch:{stretch};font-display:swap}}")
libs='\n'.join((r/'vendor'/f'{name}.js').read_text(encoding='utf8') for name in ['gsap','ScrollTrigger','SplitText','DrawSVGPlugin','InertiaPlugin','lenis'])
html=(r/'src/index.html').read_text(encoding='utf8').replace('/*__FONTS__*/','\n'.join(faces)).replace('/*__CSS__*/',(r/'src/style.css').read_text(encoding='utf8')).replace('/*__LIBRARIES__*/',libs.replace('</script','<\\/script')).replace('/*__JS__*/',(r/'src/app.js').read_text(encoding='utf8'))
(r/'index.html').write_text(html,encoding='utf8')
print('Built standalone index.html:',len(html.encode()),'bytes')

