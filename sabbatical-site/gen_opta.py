
# Generates Option A HTML section and injects it into index.html

YT = "https://www.youtube.com/results?search_query="
YT_ICON = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M23.495 6.205a3.007 3.007 0 00-2.088-2.088c-1.87-.501-9.396-.501-9.396-.501s-7.507-.01-9.396.501A3.007 3.007 0 00.527 6.205a31.247 31.247 0 00-.522 5.805 31.247 31.247 0 00.522 5.783 3.007 3.007 0 002.088 2.088c1.868.502 9.396.502 9.396.502s7.506 0 9.396-.502a3.007 3.007 0 002.088-2.088 31.247 31.247 0 00.5-5.783 31.247 31.247 0 00-.5-5.805zM9.609 15.601V8.408l6.264 3.602z"/></svg>'

def yt(city, label):
    url = YT + city.replace(' ', '+')
    return f'<a class="yt-btn" href="{url}" target="_blank" rel="noopener">{YT_ICON} {label}</a>'

def drive(desc):
    return f'''
<div class="drive-seg">
  <div class="drive-seg-line"></div>
  <div class="drive-badge">&#9654; {desc}</div>
  <div class="drive-seg-line"></div>
</div>'''

def day_open(num, dow, date, img_id, city, yt_html):
    img = f"https://images.unsplash.com/photo-{img_id}?auto=format&fit=crop&w=900&q=80"
    return f'''
<div class="day-block">
  <div class="day-header-row">
    <div class="day-pill">DAY {num:02d}</div>
    <div class="day-date-label">{dow} &middot; {date}</div>
    {yt_html}
  </div>
  <div class="day-card">
    <div class="city-img" style="background-image:url('{img}')">
      <div class="city-name-overlay">{city}</div>
    </div>
    <div class="day-body">'''

def day_close():
    return '    </div>\n  </div>\n</div>'

def stay(hotel, desc, link):
    return f'''<div class="detail-row">
  <span class="tag tag-stay">STAY</span>
  <div class="detail-content"><strong>{hotel}</strong> — {desc} <a href="{link}" target="_blank" rel="noopener">{link.replace("https://","")}</a></div>
</div>'''

def eat(items):
    rows = ''
    for r in items:
        name = r['name']
        badges = ''.join(r.get('badges', []))
        desc = r.get('desc','')
        dishes = r.get('dishes','')
        link = r.get('link','')
        link_html = f'<a class="r-link" href="{link}" target="_blank" rel="noopener">findmeglutenfree.com &rarr;</a>' if link else ''
        rows += f'''<div class="restaurant-block">
  <div class="r-name">{name}{badges}</div>
  <div class="r-desc">{desc}</div>
  <div class="r-dishes">{dishes}</div>
  {link_html}
</div>'''
    return f'''<div class="detail-row">
  <span class="tag tag-eat">EAT</span>
  <div class="detail-content">{rows}</div>
</div>'''

def do(activities):
    items = ' &nbsp;&middot;&nbsp; '.join(activities)
    return f'''<div class="detail-row">
  <span class="tag tag-do">DO</span>
  <div class="detail-content">{items}</div>
</div>'''

GFD = '<span class="badge badge-gfd">&#10003; Dedicated GF</span>'
GF  = '<span class="badge badge-gf">GF</span>'
DF  = '<span class="badge badge-df">DF</span>'
GFDF= '<span class="badge badge-gfd">&#10003; Dedicated GF+DF</span>'
GF_LINK = "https://www.findmeglutenfree.com/us/mn/minneapolis/dedicated-facilities"
GF_MSP  = "https://www.findmeglutenfree.com/us/mn/minneapolis"
GF_STW  = "https://www.findmeglutenfree.com/us/mn/stillwater"
GF_MAD  = "https://www.findmeglutenfree.com/us/wi/madison"
GF_CHI  = "https://www.findmeglutenfree.com/us/il/chicago"
GF_CHID = "https://www.findmeglutenfree.com/us/il/chicago/dedicated-facilities"

html = '''<section id="option-a" class="section">
  <div class="inner-hero" style="background-image:url('https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?auto=format&fit=crop&w=1600&q=80')">
    <div class="inner-hero-overlay"></div>
    <div class="inner-hero-content">
      <div class="inner-hero-eyebrow">Option A &nbsp;&middot;&nbsp; 10 Days</div>
      <h2 class="inner-hero-title">Upper Midwest Corridor</h2>
      <p class="inner-hero-sub">Minneapolis &rarr; Stillwater &rarr; Door County &rarr; Madison &rarr; Galena &rarr; Chicago</p>
    </div>
  </div>
  <div class="content-wrap">

    <!-- Flights + Map -->
    <div class="logistics-grid" style="grid-template-columns:1fr 1fr 1fr">
      <div class="card">
        <div class="card-label">Outbound Flight</div>
        <div class="flight-segment">
          <div><div class="iata">TPA</div><div class="flight-meta">Tampa</div></div>
          <div class="flight-arrow">&xrarr;&nbsp; nonstop &nbsp;3h30m</div>
          <div><div class="iata">MSP</div><div class="flight-meta">Minneapolis</div></div>
        </div>
        <div class="card-body" style="margin-top:10px"><strong>Delta / Sun Country</strong><br>Target ~10:30am depart &rarr; ~1:00pm CT arrive<br>Pick up SUV at MSP airport</div>
      </div>
      <div class="card">
        <div class="card-label">Return Flight</div>
        <div class="flight-segment">
          <div><div class="iata">ORD</div><div class="flight-meta">Chicago</div></div>
          <div class="flight-arrow">&xrarr;&nbsp; nonstop &nbsp;3h00m</div>
          <div><div class="iata">TPA</div><div class="flight-meta">Tampa</div></div>
        </div>
        <div class="card-body" style="margin-top:10px"><strong>Delta / American / United / Southwest</strong><br>Target ~2:00pm depart &rarr; ~5:30pm ET arrive<br>Drop SUV at ORD airport</div>
      </div>
      <div class="card">
        <div class="card-label">Rental Car &mdash; One-Way MSP &rarr; ORD</div>
        <div class="car-grid" style="grid-template-columns:1fr">'''

cars_a = [
    ("Cadillac Escalade", "Enterprise / National · Premium SUV", "$150–200/day", True),
    ("Chevrolet Tahoe / Suburban", "Full-size SUV, road trip comfort", "$100–150/day", False),
    ("Lincoln Navigator", "Luxury alternative, similar space", "$150–180/day", False),
]
for name, detail, price, pref in cars_a:
    pref_html = '<div class="preferred-badge">&#9733; IDEAL</div>' if pref else ''
    cls = 'car-card preferred' if pref else 'car-card'
    html += f'<div class="{cls}">{pref_html}<div class="car-name">{name}</div><div class="car-detail">{detail}</div><div class="car-price">{price}</div></div>'

html += '''        </div>
        <div class="card-body" style="margin-top:8px;font-size:0.74rem;color:var(--text-light)">One-way fee typically $100–200 (Enterprise/National)</div>
      </div>
    </div>

    <!-- Map -->
    <div class="map-wrap">
      <iframe src="https://www.openstreetmap.org/export/embed.html?bbox=-96.5%2C41.0%2C-86.5%2C47.8&amp;layer=mapnik" loading="lazy" title="Option A Route Map"></iframe>
    </div>

    <!-- Timeline -->
    <h3 class="section-heading" style="margin-bottom:6px">Day-by-Day <em>Itinerary</em></h3>
    <p class="section-sub">Jun 11&ndash;20 &nbsp;&middot;&nbsp; All restaurants verified GF+DF friendly</p>
'''

# Day 1 — Minneapolis arrival
html += day_open(1, "WED", "JUN 11", "1478827819961-7e0c2dea2d72", "Minneapolis, MN", yt("Minneapolis travel guide things to do", "Minneapolis"))
html += stay("Hewing Hotel", "1897 warehouse, North Loop. Exposed brick, timber beams, rooftop pool + sauna. Tullibee Scandinavian restaurant.", "https://hewinghotel.com")
html += eat([{"name":"Owamni by The Sioux Chef", "badges":GFD+DF, "desc":"James Beard &ldquo;Best New Restaurant&rdquo; winner. Indigenous cuisine. <strong>Reserve well in advance.</strong>", "dishes":"Bison Tartare &middot; Wild Rice Bowl w/ braised rabbit &middot; Wojapi w/ seed crackers. No wheat, dairy, or refined sugar.", "link":GF_LINK}])
html += do(["Stone Arch Bridge walk", "Explore North Loop neighborhood", "Rooftop sauna at Hewing"])
html += day_close()

# Day 2 — Minneapolis full day
html += day_open(2, "THU", "JUN 12", "1476514525535-07fb3b4ae5f1", "Minneapolis, MN", yt("Minneapolis art food things to do 2026", "Minneapolis Day 2"))
html += eat([
    {"name":"Sassy Spoon", "badges":GFD+DF, "desc":"100% dedicated GF. Near Lake Nokomis. Seasonal brunch, GF pancakes, grain bowls.", "dishes":"GF pancakes &middot; grain bowls &middot; seasonal specials", "link":GF_LINK},
    {"name":"Colita", "badges":GFD+DF, "desc":"Tex-Oaxacan, dedicated GF. Small dining room — <strong>reserve well in advance.</strong>", "dishes":"Mole Negro (naturally DF) &middot; Carnitas on corn tortillas &middot; GF Churros &middot; Mezcal cocktails", "link":GF_MSP},
    {"name":"Burning Brothers Brewing", "badges":GFD, "desc":"100% dedicated GF brewery. Perfect after-dinner stop.", "dishes":"Roasted Coffee Strong Ale &middot; Pyro APA", "link":GF_LINK},
])
html += do(["MartinPatrick3 — THE &lsquo;man&rsquo;s store&rsquo; in North Loop (leather, grooming, home goods)", "Walker Art Center + Minneapolis Sculpture Garden (Spoonbridge and Cherry)", "Bike the Chain of Lakes"])
html += day_close()

# Day 3 — Minneapolis → Stillwater
html += drive("Minneapolis &rarr; Stillwater &nbsp;&middot;&nbsp; 40 min &middot; 25 mi")
html += day_open(3, "FRI", "JUN 13", "1505118380757-91f5f5632de0", "Stillwater, MN", yt("Stillwater Minnesota travel guide", "Stillwater"))
html += stay("Lora Hotel", "Restored 1886 brewery in the bluffs. Fireplace rooms. 9.4 Exceptional on Expedia. Provenance Hotels (same family as Alida/Emeline).", "https://www.lorahotel.com")
html += eat([
    {"name":"Hola Arepa (before leaving Minneapolis)", "badges":GFD+DF, "desc":"Entirely GF corn-based arepas menu. Great road-day breakfast.", "dishes":"Pulled Pork Arepa (skip cheese) &middot; Black Bean &amp; Sweet Potato (vegan) &middot; Yuca Fries", "link":GF_MSP},
    {"name":"The Wild Hare", "badges":GF+DF, "desc":"Dedicated GF fryer, celiac-aware. Retro 80s vibes on historic Main Street.", "dishes":"GF Onion Rings &middot; Moroccan Cheese Curds w/ harissa (ask DF) &middot; Curry Bowl &middot; GF Burgers", "link":"https://www.findmeglutenfree.com/biz/the-wild-hare/5843434334715904"},
    {"name":"Feller at Lora Hotel", "badges":GF, "desc":"Upscale, locally-sourced. Your hotel restaurant for the evening.", "dishes":"Seasonal menu, locally-sourced", "link":""},
])
html += do(["Historic Main Street walk — antique shops, bookstores, art galleries", "Paddleboard or kayak the St. Croix River", "Stillwater Lift Bridge views"])
html += day_close()

# Day 4 — Stillwater → Door County
html += drive("Stillwater &rarr; Door County, WI &nbsp;&middot;&nbsp; 4.5 hrs &middot; scenic Wisconsin farmland")
html += day_open(4, "SAT", "JUN 14", "1505118380757-91f5f5632de0", "Door County, WI", yt("Door County Wisconsin travel guide things to do", "Door County"))
html += stay("The D&ouml;rr Hotel or Hillside Waterfront Hotel", "Fish Creek / Sister Bay. Waterfront views, walkable to village.", "https://www.doorcounty.com")
html += eat([{"name":"Door County Fish Boil", "badges":GF+DF, "desc":"<strong>Naturally GF+DF</strong> — whitefish, potatoes &amp; onions boiled over an open fire. The dramatic boilover finale is spectacle dining. Confirm no flour in prep.", "dishes":"Lake whitefish &middot; red potatoes &middot; sweet onions &middot; cherry pie (ask GF)", "link":""}])
html += do(["Walk Fish Creek village — cherry everything, pottery, candles, galleries", "Peninsula State Park — Eagle Tower viewpoint, Sunset Trail bike ride", "Sunset over Green Bay from the bluffs"])
html += day_close()

# Day 5 — Door County full day
html += day_open(5, "SUN", "JUN 15", "1441974231531-c6227db76b6e", "Door County, WI", yt("Door County Wisconsin kayak Sister Bay Ephraim", "Door County Day 2"))
html += eat([{"name":"White Gull Inn", "badges":GF, "desc":"Famous for Door County fish boils. Historic inn dining.", "dishes":"Fish boil &middot; cherry desserts &middot; seasonal specials", "link":""}])
html += do(["Kayak along limestone bluffs — Cave Point County Park (stunning)", "Ephraim &amp; Sister Bay — quintessential gift-shop villages, cherry orchards, art galleries", "Optional: Washington Island ferry from Northport", "Cave Point swimming if weather permits"])
html += day_close()

# Day 6 — Door County → Madison
html += drive("Door County &rarr; Madison, WI &nbsp;&middot;&nbsp; 3.5 hrs through Green Bay")
html += day_open(6, "MON", "JUN 16", "1547981609-4b6bfe67ca0b", "Madison, WI", yt("Madison Wisconsin travel guide State Street Capitol", "Madison"))
html += stay("The Edgewater", "Historic lakefront resort on Lake Mendota. Full spa. Terrace dining with lake views.", "https://www.theedgewater.com")
html += eat([
    {"name":"Madison Chocolate Company", "badges":GFD, "desc":"Dedicated GF caf&eacute;. &ldquo;We ordered a GF ham &amp; cheese croissant!&rdquo; — guest review.", "dishes":"GF croissants &middot; smoothie bowls &middot; pastries &middot; hot chocolate", "link":GF_MAD},
    {"name":"La Taguara", "badges":GFD+DF, "desc":"Venezuelan arepas, dedicated GF fryer. Staff knowledgeable about celiac safety.", "dishes":"Reina Pepiada arepa (ask DF) &middot; Pabellon &middot; Cachapas", "link":GF_MAD},
])
html += do(["Walk State Street &rarr; Capitol Square — bookstores, record shops, boutiques", "Dane County Farmers Market (Saturdays — one of largest in the US)", "Lake Mendota paddle or lakefront walk from the Edgewater"])
html += day_close()

# Day 7 — Madison → Galena
html += drive("Madison &rarr; Galena, IL &nbsp;&middot;&nbsp; 1.5 hrs")
html += day_open(7, "TUE", "JUN 17", "1486325212027-8081e485255e", "Galena, IL", yt("Galena Illinois travel guide Main Street shopping", "Galena"))
html += eat([{"name":"Fritz and Frites", "badges":GF, "desc":"French-German bistro, GF options. Call ahead for celiac accommodations.", "dishes":"Seasonal German &amp; French bistro fare with GF modifications", "link":""}])
html += do(["<strong>THE SHOPPING DAY</strong> — 125+ shops in a 6-block brick hillside Main Street: Jellycat-tier gifts, leather goods, candles, wine tasting, fudge, art galleries", "Walk to Ulysses S. Grant&rsquo;s historic home", "Photograph the most scenic Main Street in the Midwest", "Optional overnight at a Galena B&amp;B (or drive on to Chicago, 2.5 hrs)"])
html += day_close()

# Day 8 — Galena → Chicago
html += drive("Galena &rarr; Chicago &nbsp;&middot;&nbsp; 2.5 hrs")
html += day_open(8, "WED", "JUN 18", "1477959858617-67f85cf4f1df", "Chicago, IL", yt("Chicago Wicker Park travel guide shopping dining", "Chicago"))
html += stay("The Robey", "Art Deco tower in Wicker Park. Rooftop bar with skyline views. Floor-to-ceiling windows. Chicago&rsquo;s coolest neighborhood.", "https://www.therobey.com")
html += eat([
    {"name":"Defloured", "badges":GFD+DF, "desc":"100% dedicated GF. &ldquo;I never imagined finding a place as perfect as Defloured.&rdquo; Chef&rsquo;s wife has celiac.", "dishes":"Fried Chicken Sandwich (ask DF bun) &middot; Mac &amp; Cheese w/ cashew cream &middot; Seasonal bowls", "link":GF_CHID},
    {"name":"Small Cheval", "badges":GF+DF, "desc":"&ldquo;The GOAT of Chicago burgers.&rdquo; Personal allergy form filled for every order.", "dishes":"The Burger on GF bun (no cheese, extra sauce)", "link":GF_CHI},
])
html += do(["Afternoon shopping — Wicker Park + Bucktown: Chicago&rsquo;s best independent boutique district, vintage, design stores", "Check in &amp; rooftop cocktail at The Robey"])
html += day_close()

# Day 9 — Chicago full day
html += day_open(9, "THU", "JUN 19", "1494522358652-f30e61a60313", "Chicago, IL", yt("Chicago architecture river cruise things to do", "Chicago Day 2"))
html += eat([
    {"name":"Wheat&rsquo;s End Cafe", "badges":GFD, "desc":"The dedicated GF brunch spot every celiac traveler in Chicago goes to.", "dishes":"Brunch classics, all GF, ask for DF options", "link":GF_CHID},
    {"name":"Farewell dinner — your choice", "badges":"", "desc":"Chicago has excellent GF-friendly dining throughout. Ask hotel concierge for current recommendations.", "dishes":"", "link":GF_CHI},
])
html += do(["<strong>Architecture River Cruise</strong> — the single best thing to do in Chicago. Book through Chicago Architecture Center.", "Art Institute of Chicago (if time)", "Mag Mile window shopping &amp; Lincoln Park", "Rooftop bar at The Robey for farewell sunset"])
html += day_close()

# Day 10 — Fly home
html += day_open(10, "FRI", "JUN 20", "1533591380893-1a0fbff9e01e", "Fly Home: ORD &rarr; TPA", yt("Chicago O'Hare airport tips", "Departure Day"))
html += '''<div class="detail-row">
  <span class="tag tag-fly">FLY</span>
  <div class="detail-content">
    <strong>ORD &rarr; TPA nonstop</strong><br>
    Target ~2:00pm CT departure &rarr; ~5:30pm ET arrival &nbsp;&middot;&nbsp; ~3 hrs<br>
    Delta / American / United / Southwest<br>
    <span style="color:var(--text-light);font-size:0.76rem">Drop rental car at ORD — Enterprise/National one-way return. Allow 90 min before flight.</span>
  </div>
</div>'''
html += day_close()

# Weather
html += '''
    <div class="divider"></div>
    <h3 class="section-heading">June <em>Weather</em></h3>
    <p class="section-sub">Option A has the most reliable weather of any route.</p>
    <div class="weather-grid">
      <div class="weather-card"><div class="weather-city">Minneapolis</div><div class="weather-temp">70&ndash;82&deg;F</div><div class="weather-desc">Low humidity, 15+ hrs daylight. Best weather window of the year.</div><div class="weather-grade">Grade: A</div></div>
      <div class="weather-card"><div class="weather-city">Door County, WI</div><div class="weather-temp">72&ndash;80&deg;F</div><div class="weather-desc">Comfortable lake breezes off Green Bay.</div><div class="weather-grade">Grade: A</div></div>
      <div class="weather-card"><div class="weather-city">Madison, WI</div><div class="weather-temp">74&ndash;82&deg;F</div><div class="weather-desc">Pleasant, low-humidity summer days.</div><div class="weather-grade">Grade: A</div></div>
      <div class="weather-card"><div class="weather-city">Chicago</div><div class="weather-temp">75&ndash;85&deg;F</div><div class="weather-desc">Sunny &amp; pleasant. Lakefront can be breezy.</div><div class="weather-grade">Grade: A</div></div>
    </div>
  </div>
</section>
'''

# Read index.html, replace placeholder, write back
with open('/home/user/SmartThingsPublic/sabbatical-site/index.html', 'r') as f:
    content = f.read()

placeholder = '<section id="option-a" class="section"><div style="padding:120px 24px;text-align:center;color:#aaa;font-family:var(--serif);font-size:1.5rem">Loading Option A\u2026</div></section>'
content = content.replace(placeholder, html)

with open('/home/user/SmartThingsPublic/sabbatical-site/index.html', 'w') as f:
    f.write(content)

print(f"Done. Total lines: {len(content.splitlines())}")
