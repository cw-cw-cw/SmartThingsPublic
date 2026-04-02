
"""
Patch the sabbatical site index.html with:
1. Correct city-specific images using source.unsplash.com keyword URLs
2. Leaflet.js interactive route maps with waypoints
3. Hyperlinks for all stores, restaurants, attractions
"""

with open('/home/user/SmartThingsPublic/sabbatical-site/index.html', 'r') as f:
    html = f.read()

# ─────────────────────────────────────────────
# 1. REPLACE IMAGES with keyword-specific URLs
# ─────────────────────────────────────────────
# Format: source.unsplash.com/featured/WxH/?keyword,keyword
def img(keywords, w=900, h=500):
    kw = ','.join(keywords.split())
    return f"https://source.unsplash.com/featured/{w}x{h}/?{kw}"

CITY_IMAGES = {
    # Option A hero
    'photo-1476514525535-07fb3b4ae5f1': img('midwest,great-lakes,road,highway', 1600, 900),
    # Minneapolis
    'photo-1478827819961-7e0c2dea2d72': img('minneapolis,minnesota,skyline,stone-arch-bridge'),
    # Stillwater MN
    'photo-1505118380757-91f5f5632de0': img('stillwater,minnesota,historic,main-street,river'),
    # Door County (Day 5 - mountain trail is WRONG)
    'photo-1441974231531-c6227db76b6e': img('door-county,wisconsin,caves,limestone,kayak'),
    # Madison WI (the Tiananmen Square lookalike)
    'photo-1547981609-4b6bfe67ca0b': img('madison,wisconsin,state-capitol,lake-mendota'),
    # Galena IL
    'photo-1486325212027-8081e485255e': img('galena,illinois,historic,main-street,victorian'),
    # Park City (Day 2)
    'photo-1542314831-068cd1dbfeeb': img('park-city,utah,main-street,mountain,boutique'),
    # Jackson Hole
    'photo-1566438480900-0609be27a4be': img('jackson-hole,wyoming,town-square,elk-antler,arches'),
    # Jackson Day 5 wildlife art
    'photo-1551362110-a073d2e1bdad': img('jackson-hole,wyoming,snake-river,wildlife,nature'),
    # Bozeman MT
    'photo-1501854140801-50d01698950b': img('bozeman,montana,main-street,bridger-mountains'),
    # Portland Day 7
    'photo-1564937028927-f7dff4ad00b5': img('portland,oregon,city,bridges,willamette-river'),
    # Portland Day 8 (GF food day)
    'photo-1539302577158-7d87aab5db82': img('portland,oregon,alberta-street,hawthorne,boutique'),
    # Option B hero (keep the mountain lake - it's correct for Tetons)
    # SLC/Park City Day 1
    # 'photo-1501854140801-50d01698950b': already replaced above for Bozeman
}

# Apply image replacements
for old_id, new_url in CITY_IMAGES.items():
    old_url = f"https://images.unsplash.com/photo-{old_id}?auto=format&fit=crop&w=900&q=80"
    old_url_1600 = f"https://images.unsplash.com/photo-{old_id}?auto=format&fit=crop&w=1600&q=80"
    html = html.replace(old_url, new_url)
    html = html.replace(old_url_1600, new_url.replace('900x500', '1600x900'))

# Fix Park City Day 1 (reuses same ID as Bozeman - need separate handling)
# The SLC/Park City day 1 photo is the same ID as the old bozeman one
# After the above replace, it now shows bozeman keywords - we want SLC/Park City
# It was already replaced above - let's update the Park City one specifically
# Day 1 is line ~943, Day 6 is line ~1043 - after replacement both show bozeman keywords
# Let's do a targeted fix for Park City Day 1 by finding the context
park_city_img = img('salt-lake-city,utah,mountains,park-city,wasatch', 900, 500)
# Find the SLC/Park City day block and fix the image
html = html.replace(
    f'<div class="city-img" style="background-image:url(\'{img("bozeman,montana,main-street,bridger-mountains")}\')"><div class="city-name-overlay">Salt Lake City / Park City, UT</div>',
    f'<div class="city-img" style="background-image:url(\'{park_city_img}\')"><div class="city-name-overlay">Salt Lake City / Park City, UT</div>'
)

# ─────────────────────────────────────────────
# 2. REPLACE MAPS with Leaflet.js route maps
# ─────────────────────────────────────────────
LEAFLET_HEAD = '''<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" crossorigin=""></script>'''

# Insert Leaflet into <head> before </style>
html = html.replace('</style>', '</style>\n' + LEAFLET_HEAD, 1)

# Add Leaflet map styles
MAP_CSS = '''
.lmap { width:100%; height:280px; border-radius:var(--radius); border:1px solid var(--border); margin-bottom:36px; }
.lmap-wrap .leaflet-tile { filter: saturate(0) contrast(1.1) brightness(1.05); }
'''
html = html.replace('/* ── RESPONSIVE ── */', MAP_CSS + '\n/* ── RESPONSIVE ── */')

# Option A map (OSM embed → Leaflet)
MAP_A_OLD = '''<div class="map-wrap">
      <iframe src="https://www.openstreetmap.org/export/embed.html?bbox=-96.5%2C41.0%2C-86.5%2C47.8&amp;layer=mapnik" loading="lazy" title="Option A Route Map"></iframe>
    </div>'''

MAP_A_NEW = '''<div id="map-a" class="lmap lmap-wrap"></div>
    <script>
    (function(){
      var map = L.map('map-a', {scrollWheelZoom:false}).setView([43.5, -91.5], 6);
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
        attribution:'&copy; OpenStreetMap contributors', maxZoom:18
      }).addTo(map);
      var stops = [
        [44.9778,-93.2650,'Minneapolis, MN'],
        [44.9214,-92.8081,'Stillwater, MN'],
        [44.8669,-87.3292,'Door County, WI'],
        [43.0731,-89.4012,'Madison, WI'],
        [42.4174,-90.4321,'Galena, IL'],
        [41.8781,-87.6298,'Chicago, IL']
      ];
      var icon = L.divIcon({className:'',html:'<div style="width:10px;height:10px;border-radius:50%;background:#b5714a;border:2px solid #fff;box-shadow:0 1px 4px rgba(0,0,0,.4)"></div>',iconSize:[10,10],iconAnchor:[5,5]});
      stops.forEach(function(s){
        L.marker([s[0],s[1]],{icon:icon}).addTo(map).bindPopup('<b>'+s[2]+'</b>');
      });
      L.polyline(stops.map(function(s){return[s[0],s[1]];}),{color:'#b5714a',weight:2.5,opacity:0.8,dashArray:'6,4'}).addTo(map);
    })();
    </script>'''

html = html.replace(MAP_A_OLD, MAP_A_NEW)

# Option B map
MAP_B_OLD = '''<div class="map-wrap">
      <iframe src="https://www.openstreetmap.org/export/embed.html?bbox=-124.5%2C40.0%2C-109.0%2C49.5&amp;layer=mapnik" loading="lazy" title="Option B Route Map"></iframe>
    </div>'''

MAP_B_NEW = '''<div id="map-b" class="lmap lmap-wrap"></div>
    <script>
    (function(){
      var map = L.map('map-b', {scrollWheelZoom:false}).setView([44.5,-114], 5);
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
        attribution:'&copy; OpenStreetMap contributors', maxZoom:18
      }).addTo(map);
      var stops = [
        [40.7608,-111.8910,'Salt Lake City, UT'],
        [40.6461,-111.4980,'Park City, UT'],
        [43.4799,-110.7624,'Jackson Hole, WY'],
        [43.7904,-110.6818,'Grand Teton NP'],
        [45.6770,-111.0429,'Bozeman, MT'],
        [45.5231,-122.6765,'Portland, OR'],
        [47.6062,-122.3321,'Seattle, WA']
      ];
      var icon = L.divIcon({className:'',html:'<div style="width:10px;height:10px;border-radius:50%;background:#b5714a;border:2px solid #fff;box-shadow:0 1px 4px rgba(0,0,0,.4)"></div>',iconSize:[10,10],iconAnchor:[5,5]});
      stops.forEach(function(s){
        L.marker([s[0],s[1]],{icon:icon}).addTo(map).bindPopup('<b>'+s[2]+'</b>');
      });
      L.polyline(stops.map(function(s){return[s[0],s[1]];}),{color:'#b5714a',weight:2.5,opacity:0.8,dashArray:'6,4'}).addTo(map);
      // Flight leg BZN->PDX shown as dashed different color
      var flight = [[45.6770,-111.0429],[45.5231,-122.6765]];
      L.polyline(flight,{color:'#5a7a58',weight:2,opacity:0.7,dashArray:'3,6'}).addTo(map).bindPopup('✈ BZN → PDX (Alaska Airlines)');
    })();
    </script>'''

html = html.replace(MAP_B_OLD, MAP_B_NEW)

# ─────────────────────────────────────────────
# 3. ADD HYPERLINKS for stores & attractions
# ─────────────────────────────────────────────

# Option A hyperlinks
LINKS_A = [
    # Minneapolis
    ('Owamni by The Sioux Chef', 'https://owamni.com'),
    ('Sassy Spoon', 'https://www.sassyspoon.com'),
    ('Burning Brothers Brewing', 'https://www.burnbrosbrew.com'),
    ('Colita', 'https://colitampls.com'),
    ('MartinPatrick3', 'https://martinpatrick3.com'),
    ('Walker Art Center', 'https://walkerart.org'),
    ('Hola Arepa', 'https://www.holaarepa.com'),
    # Door County
    ('Peninsula State Park', 'https://dnr.wisconsin.gov/topic/parks/peninsulasp'),
    ('White Gull Inn', 'https://whitegullinn.com'),
    # Madison
    ('Madison Chocolate Company', 'https://www.madisonchocolatecompany.com'),
    # Galena
    ('Ulysses S. Grant', 'https://www.granthome.com'),
    # Chicago
    ('Defloured', 'https://www.deflouredchicago.com'),
    ('Small Cheval', 'https://www.smallcheval.com'),
    ('Wheat\'s End Cafe', 'https://www.wheatsendcafe.com'),
    ('Chicago Architecture Center', 'https://www.architecture.org/tours/detail/chicago-river-cruise'),
    ('Art Institute of Chicago', 'https://www.artic.edu'),
]

# Option B hyperlinks
LINKS_B = [
    ('Good Food Gluten Free Bakery', 'https://www.goodfoodglutenfree.com'),
    ('Zest Kitchen &amp; Bar', 'https://www.zestslc.com'),
    ('Olympic Park', 'https://www.usopm.org'),
    ('National Museum of Wildlife Art', 'https://www.wildlifeart.org'),
    ('Montana Ale Works', 'https://montanaaleworks.com'),
    ('New Cascadia Traditional', 'https://www.newcascadiatraditional.com'),
    ('Kann', 'https://www.kannrestaurant.com'),
    ('Petunia\'s Pies &amp; Pastries', 'https://www.petuniasbakeshop.com'),
    ('Petunia\'s Pies', 'https://www.petuniasbakeshop.com'),
    ('Ground Breaker Brewing', 'https://groundbreakerbrewing.com'),
    ('Powell\'s Books', 'https://www.powells.com'),
    ('Eem', 'https://www.eempdx.com'),
    ('Gluten Free Gem', 'https://www.glutenfreegem.com'),
    ('Schilling Cider House', 'https://www.schillingcider.com'),
    ('Pike Place Market', 'https://pikeplacemarket.org'),
    ('Snake River', 'https://barker-ewing.com'),
    ('Jenny Lake', 'https://www.jennylakeboating.com'),
    ('Grand Teton National Park', 'https://www.nps.gov/grte/'),
    ('Farmacy', 'https://www.farmacybozeman.com'),
]

def add_link(text, name, url):
    """Wrap bare 'name' text in a link if not already linked."""
    linked = f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'
    # Only replace if not already inside an href
    import re
    # Don't re-link already linked text
    pattern = f'(?<!href="{url}">)(?<!">){re.escape(name)}(?!</a>)'
    # Simple approach: replace first unlinked occurrence
    if f'href="{url}"' not in text:
        text = text.replace(name, linked, 1)
    return text

for name, url in LINKS_A + LINKS_B:
    linked = f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'
    # Replace only if this exact text isn't already linked
    if f'href="{url}">{name}' not in html:
        html = html.replace(name, linked, 1)

# ─────────────────────────────────────────────
# Write updated file
# ─────────────────────────────────────────────
with open('/home/user/SmartThingsPublic/sabbatical-site/index.html', 'w') as f:
    f.write(html)

lines = len(html.splitlines())
import re
map_count = len(re.findall(r'L\.map\(', html))
link_count = len(re.findall(r'<a href="https?://', html))
print(f"Done. Lines: {lines}, Leaflet maps: {map_count}, Hyperlinks: {link_count}")
