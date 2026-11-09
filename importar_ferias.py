#!/usr/bin/env python3
"""Importa registros ODEPA publicados por geoidegeoidal; requiere conexión en compilación."""
import csv, io, json, re, unicodedata, urllib.request
from pathlib import Path
URL='https://raw.githubusercontent.com/geoidegeoidal/ferias-chile/master/data/ferias_libres_unicas.csv'
COMUNAS='Cerrillos Cerro Navia Conchalí El Bosque Estación Central Huechuraba Independencia La Cisterna La Florida La Granja La Pintana La Reina Las Condes Lo Barnechea Lo Espejo Lo Prado Macul Maipú Ñuñoa Pedro Aguirre Cerda Peñalolén Providencia Pudahuel Quilicura Quinta Normal Recoleta Renca San Joaquín San Miguel San Ramón Santiago Vitacura'.split('|')
COMUNAS=['Cerrillos','Cerro Navia','Conchalí','El Bosque','Estación Central','Huechuraba','Independencia','La Cisterna','La Florida','La Granja','La Pintana','La Reina','Las Condes','Lo Barnechea','Lo Espejo','Lo Prado','Macul','Maipú','Ñuñoa','Pedro Aguirre Cerda','Peñalolén','Providencia','Pudahuel','Quilicura','Quinta Normal','Recoleta','Renca','San Joaquín','San Miguel','San Ramón','Santiago','Vitacura','Puente Alto','San Bernardo','Padre Hurtado','Peñaflor','Talagante','Colina','Lampa','Buin','Calera de Tango','Pirque']
def norm(s):
 s=unicodedata.normalize('NFD',s.casefold());return re.sub(r'[^a-z0-9]+',' ',''.join(c for c in s if unicodedata.category(c)!='Mn')).strip()
lookup={norm(c):c for c in COMUNAS}
with urllib.request.urlopen(URL,timeout=45) as r: raw=r.read().decode('utf-8-sig')
rows=list(csv.DictReader(io.StringIO(raw)))
ferias=[];seen=set()
for r in rows:
 comuna=lookup.get(norm(r.get('comuna','')))
 if not comuna:continue
 if 'metropolitana' not in norm(r.get('region','')):continue
 nombre=r.get('nombre_feria','').strip() or 'Feria sin nombre'
 ubicacion=(r.get('calle_principal') or r.get('direccion') or nombre).strip()
 inicio=(r.get('calle_inicio') or '').strip()
 fin=(r.get('calle_termino') or '').strip()
 key=(norm(comuna),norm(nombre),norm(ubicacion),norm(inicio),norm(fin))
 if key in seen:continue
 seen.add(key)
 dias=(r.get('dias') or '').strip()
 horario=(r.get('horario') or '').strip()
 lat=r.get('latitud','').strip();lon=r.get('longitud','').strip()
 ferias.append(dict(id=f'odepa-{len(ferias)+1:04d}',comuna=comuna,nombre=nombre,ubicacion=ubicacion,calleInicio=inicio or 'No informado',calleFin=fin or 'No informado',dias=[dias or 'No informado'],horario=horario or 'No informado',latitud=float(lat) if lat else None,longitud=float(lon) if lon else None,fuente='ODEPA (datos publicados por geoidegeoidal)',urlFuente=URL))
if len(ferias)<100:raise SystemExit(f'Catálogo inesperadamente pequeño: {len(ferias)}; no se reemplaza la base')
out=Path('app/src/main/assets/ferias.json');out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(ferias,ensure_ascii=False,indent=1),encoding='utf-8')
print(f'Importadas {len(ferias)} ferias en {len(set(f["comuna"] for f in ferias))} comunas; archivo {out}')
