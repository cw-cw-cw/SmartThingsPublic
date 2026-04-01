
YT_BASE = "https://www.youtube.com/results?search_query="
YT_ICON = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M23.495 6.205a3.007 3.007 0 00-2.088-2.088c-1.87-.501-9.396-.501-9.396-.501s-7.507-.01-9.396.501A3.007 3.007 0 00.527 6.205a31.247 31.247 0 00-.522 5.805 31.247 31.247 0 00.522 5.783 3.007 3.007 0 002.088 2.088c1.868.502 9.396.502 9.396.502s7.506 0 9.396-.502a3.007 3.007 0 002.088-2.088 31.247 31.247 0 00.5-5.783 31.247 31.247 0 00-.5-5.805zM9.609 15.601V8.408l6.264 3.602z"/></svg>'

def yt(q, label):
    return f'<a class="yt-btn" href="{YT_BASE}{q.replace(" ","+")}" target="_blank" rel="noopener">{YT_ICON} {label}</a>'

def drive(desc):
    return f'<div class="drive-seg"><div class="drive-seg-line"></div><div class="drive-badge">&#9654; {desc}</div><div class="drive-seg-line"></div></div>'

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
    link_html = f'<a href="{link}" target="_blank" rel="noopener">{link.replace("https://","")}</a>' if link else ''
    return f'<div class="detail-row"><span class="tag tag-stay">STAY</span><div class="detail-content"><strong>{hotel}</strong> — {desc} {link_html}</div></div>'

def eat(items):
    rows = ''
    for r in items:
        badges = ''.join(r.get('badges', []))
        link = r.get('link', '')
        link_html = f'<a class="r-link" href="{link}" target="_blank" rel="noopener">findmeglutenfree.com &rarr;</a>' if link else ''
        rows += f'''<div class="restaurant-block">
  <div class="r-name">{r["name"]}{badges}</div>
  <div class="r-desc">{r.get("desc","")}</div>
  <div class="r-dishes">{r.get("dishes","")}</div>
  {link_html}
</div>'''
    return f'<div class="detail-row"><span class="tag tag-eat">EAT</span><div class="detail-content">{rows}</div></div>'

def do(items):
    return f'<div class="detail-row"><span class="tag tag-do">DO</span><div class="detail-content">{"&nbsp;&middot;&nbsp;".join(items)}</div></div>'

GFD  = ['<span class="badge badge-gfd">&#10003; Dedicated GF</span>']
GFDF = ['<span class="badge badge-gfd">&#10003; Dedicated GF+DF</span>']
GF   = ['<span class="badge badge-gf">GF</span>']
DF   = ['<span class="badge badge-df">DF</span>']

SLC_D = "https://www.findmeglutenfree.com/us/ut/salt-lake-city/dedicated-facilities"
SLC   = "https://www.findmeglutenfree.com/us/ut/salt-lake-city"
BZN   = "https://www.findmeglutenfree.com/us/mt/bozeman"
PDX_D = "https://www.findmeglutenfree.com/us/or/portland/dedicated-facilities"
PDX   = "https://www.findmeglutenfree.com/us/or/portland"

html = '''<section id="option-b" class="section">
  <div class="inner-hero" style="background-image:url('https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1600&q=80')">
    <div class="inner-hero-overlay"></div>
    <div class="inner-hero-content">
      <div class="inner-hero-eyebrow">Option B &nbsp;&middot;&nbsp; 10 Days</div>
      <h2 class="inner-hero-title">Mountain West &rarr; Pacific Northwest</h2>
      <p class="inner-hero-sub">Salt Lake City &rarr; Park City &rarr; Jackson Hole &rarr; Grand Teton &rarr; Bozeman &#x2708; Portland &rarr; Seattle</p>
    </div>
  </div>
  <div class="content-wrap">

    <!-- Flights -->
    <div class="logistics-grid" style="grid-template-columns:repeat(3,1fr)">
      <div class="card">
        <div class="card-label">Outbound Flight</div>
        <div class="flight-segment">
          <div><div class="iata">TPA</div><div class="flight-meta">Tampa</div></div>
          <div class="flight-arrow">&xrarr;&nbsp;nonstop&nbsp;4h30m</div>
          <div><div class="iata">SLC</div><div class="flight-meta">Salt Lake City</div></div>
        </div>
        <div class="card-body" style="margin-top:10px"><strong>Delta / Southwest</strong><br>Target ~10:00am ET &rarr; ~12:30pm MT<br>Pick up SUV #1 at SLC airport</div>
      </div>
      <div class="card">
        <div class="card-label">Mid-Trip Hop</div>
        <div class="flight-segment">
          <div><div class="iata">BZN</div><div class="flight-meta">Bozeman</div></div>
          <div class="flight-arrow">&xrarr;&nbsp;nonstop&nbsp;1h50m</div>
          <div><div class="iata">PDX</div><div class="flight-meta">Portland</div></div>
        </div>
        <div class="card-body" style="margin-top:10px"><strong>Alaska Airlines</strong><br>~4:00pm MT &rarr; ~4:50pm PT (Day 7)<br>Drop SUV #1 at BZN. Pick up SUV #2 at PDX.</div>
      </div>
      <div class="card">
        <div class="card-label">Return Flight</div>
        <div class="flight-segment">
          <div><div class="iata">SEA</div><div class="flight-meta">Seattle</div></div>
          <div class="flight-arrow">&xrarr;&nbsp;nonstop&nbsp;5h30m</div>
          <div><div class="iata">TPA</div><div class="flight-meta">Tampa</div></div>
        </div>
        <div class="card-body" style="margin-top:10px"><strong>Alaska Airlines / Delta</strong><br>Target ~10:00am PT &rarr; ~5:30pm ET<br>Drop SUV #2 at SEA airport</div>
      </div>
    </div>

    <!-- Rental Cars -->
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:20px">
      <div class="card">
        <div class="card-label">Rental Car #1 &mdash; SLC &rarr; BZN Drop</div>
        <div class="car-grid">'''

cars_b1 = [
    ("Cadillac Escalade", "Enterprise / National · Ideal for mountain passes", "$150–200/day", True),
    ("Chevrolet Tahoe", "Full-size, widely available in SLC", "$100–150/day", False),
    ("Jeep Grand Cherokee L", "Luxury-ish, handles mountain roads well", "$120–160/day", False),
]
for name, detail, price, pref in cars_b1:
    pref_html = '<div class="preferred-badge">&#9733; IDEAL</div>' if pref else ''
    cls = 'car-card preferred' if pref else 'car-card'
    html += f'<div class="{cls}">{pref_html}<div class="car-name">{name}</div><div class="car-detail">{detail}</div><div class="car-price">{price}</div></div>'

html += '''        </div>
      </div>
      <div class="card">
        <div class="card-label">Rental Car #2 &mdash; PDX &rarr; SEA Drop (3 days)</div>
        <div class="car-grid">'''

cars_b2 = [
    ("Range Rover Sport", "Turo — if you want luxury for PNW", "$200–280/day", True),
    ("Volvo XC90", "Very PNW-appropriate, comfortable", "$150–200/day", False),
    ("Cadillac Escalade", "Consistency from Car #1", "$150–200/day", False),
]
for name, detail, price, pref in cars_b2:
    pref_html = '<div class="preferred-badge">&#9733; IDEAL</div>' if pref else ''
    cls = 'car-card preferred' if pref else 'car-card'
    html += f'<div class="{cls}">{pref_html}<div class="car-name">{name}</div><div class="car-detail">{detail}</div><div class="car-price">{price}</div></div>'

html += '''        </div>
      </div>
    </div>

    <!-- Map -->
    <div class="map-wrap">
      <iframe src="https://www.openstreetmap.org/export/embed.html?bbox=-124.5%2C40.0%2C-109.0%2C49.5&amp;layer=mapnik" loading="lazy" title="Option B Route Map"></iframe>
    </div>

    <!-- Timeline -->
    <h3 class="section-heading" style="margin-bottom:6px">Day-by-Day <em>Itinerary</em></h3>
    <p class="section-sub">Jun 11&ndash;20 &nbsp;&middot;&nbsp; GF food improves dramatically in Portland (Day 8+)</p>
'''

# Day 1
html += day_open(1,"WED","JUN 11","1501854140801-50d01698950b","Salt Lake City / Park City, UT", yt("Park City Utah travel guide Main Street","Park City"))
html += stay("Washington School House Hotel","Two MICHELIN Keys. Converted 1889 schoolhouse, only 12 rooms. Complimentary breakfast + afternoon charcuterie &amp; drinks. Pool. 5.0 service rating.","https://www.washingtonschoolhouse.com")
html += eat([
    {"name":"Good Food Gluten Free Bakery (SLC stop en route)","badges":GFD,"desc":"<strong>Stock up on bread, wraps, cinnamon rolls</strong> for mountain days when GF options are limited.","dishes":"GF bread loaves &middot; wraps &middot; cinnamon rolls &middot; cookies","link":SLC_D},
    {"name":"Zest Kitchen &amp; Bar (SLC)","badges":GFDF,"desc":"100% dedicated GF + 100% vegan = automatically DF. Everything safe by default.","dishes":"Korean BBQ Bowl &middot; Loaded Nachos w/ cashew queso &middot; Raw Cheesecake","link":SLC_D},
])
html += do(["40-min drive SLC &rarr; Park City", "Walk Park City Main Street upon arrival", "Enjoy Washington School House afternoon charcuterie &amp; drinks"])
html += day_close()

# Day 2
html += day_open(2,"THU","JUN 12","1542314831-068cd1dbfeeb","Park City, UT", yt("Park City Utah Main Street shopping galleries","Park City Day 2"))
html += stay("Washington School House Hotel","Enjoy complimentary breakfast.","https://www.washingtonschoolhouse.com")
html += eat([
    {"name":"Sugarhouse BBQ","badges":GFD+DF,"desc":"Owner has celiac. All sauces GF. GF cornbread.","dishes":"Smoked Brisket (naturally DF) &middot; GF Cornbread &middot; Pulled Pork Plate","link":SLC},
    {"name":"Park City Main Street restaurants","badges":GF,"desc":"Handle, Riverhorse, or similar. Call ahead for celiac accommodations.","dishes":"Upscale seasonal menus with GF modifications","link":""},
])
html += do(["All-day <strong>Park City Main Street</strong> — galleries, western wear, high-end outdoor gear, jewelry, boutiques", "Olympic Park tour (US Olympic ski jump facilities)", "Hotel afternoon charcuterie &amp; drinks"])
html += day_close()

# Day 3
html += drive("Park City &rarr; Jackson Hole &nbsp;&middot;&nbsp; 5.5 hrs BIG DRIVE DAY &middot; stunning scenery")
html += day_open(3,"FRI","JUN 13","1566438480900-0609be27a4be","Jackson Hole, WY", yt("Jackson Hole Wyoming travel guide things to do","Jackson Hole"))
html += stay("Hotel Jackson","4.8&#9733; TripAdvisor, 9.8 Expedia. First LEED-built hotel in Jackson. Gas fireplaces, Nespresso, BVLGARI amenities, private hot tub time slots.","https://hoteljackson.com")
html += eat([{"name":"Jackson restaurants","badges":GF,"desc":"Glean (locally-sourced, GF-friendly) or The Kitchen — call ahead for celiac. Pack GF road snacks from Good Food Bakery.","dishes":"Bear Lake stop en route (turquoise water) &middot; Star Valley ranchland views","link":""}])
html += do(["Stop at turquoise <strong>Bear Lake</strong> en route", "Walk <strong>Jackson Town Square</strong> — elk antler arches, western galleries, guns, leather, Yeti, cowboy boots, taxidermy art", "THIS IS &lsquo;MAN&rsquo;S STORE&rsquo; HEAVEN"])
html += day_close()

# Day 4
html += day_open(4,"SAT","JUN 14","1464822759023-fed622ff2c3b","Grand Teton National Park", yt("Grand Teton National Park travel guide Jenny Lake","Grand Teton"))
html += eat([{"name":"Pack GF snacks from Good Food Bakery stockpile","badges":GFD,"desc":"<strong>Limited food options in the park</strong> — very important to pack snacks. Jackson restaurants for dinner upon return.","dishes":"Your stockpile + Jackson dinner","link":""}])
html += do(["<strong>THIS IS THE VISUAL PEAK OF THE ENTIRE TRIP</strong>", "Jenny Lake — boat shuttle + hike to Hidden Falls", "Signal Mountain summit drive — panoramic Teton panorama", "Teton Park Road + Moose-Wilson Road for wildlife", "June = wildflower season against snow-capped peaks. Moose + elk everywhere."])
html += day_close()

# Day 5
html += day_open(5,"SUN","JUN 15","1551362110-a073d2e1bdad","Jackson Hole, WY", yt("Jackson Hole Wyoming Snake River float wildlife art","Jackson Day 2"))
html += eat([{"name":"Jackson restaurants","badges":GF,"desc":"Day two in Jackson — more time to explore. Check in with hotel concierge for current GF recommendations.","dishes":"Local seasonal options","link":""}])
html += do(["<strong>National Museum of Wildlife Art</strong> — stunning building carved into a cliff, world-class collection", "Scenic float trip on the Snake River — calm, wildlife-focused, ~3 hrs", "Deeper exploration of Jackson&rsquo;s 30+ galleries and boutique shops"])
html += day_close()

# Day 6
html += drive("Jackson Hole &rarr; Bozeman, MT &nbsp;&middot;&nbsp; 5.5 hrs BIG DRIVE DAY #2")
html += day_open(6,"MON","JUN 16","1501854140801-50d01698950b","Bozeman, MT", yt("Bozeman Montana travel guide Main Street","Bozeman"))
html += stay("The Lark Bozeman","Boutique, design-forward hotel. Walkable to Downtown Main Street.","https://www.thelarkhotels.com/bozeman")
html += eat([
    {"name":"Farmacy","badges":GFD+DF,"desc":"Dedicated GF fryer. &ldquo;The go-to for Bozeman-based celiacs.&rdquo;","dishes":"Japan Chicken and Fries &middot; Fondue (ask DF)","link":BZN},
    {"name":"Montana Ale Works","badges":GF,"desc":"Bozeman institution in a railroad car building. Dedicated GF fryer, full GF menu.","dishes":"GF pub menu &middot; local Montana beers","link":BZN},
])
html += do(["Walk <strong>Downtown Bozeman Main Street</strong>", "Schnee&rsquo;s — legendary outdoor/western gear store since 1946", "Heyday — curated gifts and home goods", "Evening galleries and restaurants on Main Street"])
html += day_close()

# Day 7
html += day_open(7,"TUE","JUN 17","1564937028927-f7dff4ad00b5","Portland, OR", yt("Portland Oregon travel guide food things to do","Portland"))
html += stay("Hotel Lucia or Woodlark Hotel","Both boutique, downtown Portland. Hotel Lucia: Provenance Hotels (same family as Lora in Stillwater!). David Bowie photography collection. Woodlark: Two merged historic buildings, Bullard restaurant.","https://www.hotelluciaportland.com")
html += eat([
    {"name":"Breakfast in Bozeman — Jam!","badges":GF,"desc":"Famous Bozeman breakfast spot. GF pancakes available.","dishes":"GF pancakes &middot; eggs &middot; breakfast classics","link":BZN},
    {"name":"Portland dinner on arrival","badges":GFD,"desc":"Portland is ranked <strong>#10 GF city in the world</strong> with 50 dedicated GF places. Your first taste of GF paradise.","dishes":"Walk to any nearby Portland GF spot","link":PDX_D},
])
html += do(["Morning: Final Bozeman stroll + breakfast", "Drop Car #1 at BZN airport", "&#9992; BZN &rarr; PDX nonstop, Alaska Airlines, ~4:00pm MT &rarr; 4:50pm PT", "Pick up Car #2 at PDX", "Evening: Hotel Lucia / Woodlark check-in, Portland neighborhood walk"])
html += day_close()

# Day 8
html += day_open(8,"WED","JUN 18","1539302577158-7d87aab5db82","Portland, OR — GF Food Day", yt("Portland Oregon gluten free restaurants best food","Portland GF"))
html += eat([
    {"name":"New Cascadia Traditional","badges":GFD,"desc":"Dedicated GF bakery. GF challah, baguettes, maple bars, donut holes. &ldquo;You&rsquo;ll question if it&rsquo;s GF.&rdquo; Lines on weekends — arrive early.","dishes":"GF challah &middot; baguettes &middot; maple bars &middot; chocolate-filled donut holes","link":PDX_D},
    {"name":"Kann","badges":GFDF,"desc":"Top Chef winner Gregory Gourdet&rsquo;s restaurant. <strong>Dedicated GF AND DF.</strong> Haitian wood-fire cuisine. Named best new restaurant in America by Esquire.","dishes":"Wood-fired whole fish &middot; rotisserie chicken &middot; Haitian-spiced vegetables &middot; rum cocktails","link":PDX},
    {"name":"Petunia&rsquo;s Pies &amp; Pastries","badges":GFDF,"desc":"Dedicated GF + vegan. Afternoon treat between shopping.","dishes":"Bumbleberry peach pie &middot; hazelnut coconut streusel","link":PDX_D},
    {"name":"Ground Breaker Brewing","badges":GFD,"desc":"Dedicated GF brewery + gastropub. Brewed with GF oats and chestnuts. Full GF food menu.","dishes":"Seasonal GF beers &middot; full gastropub menu","link":PDX_D},
])
html += do(["Shopping: <strong>Alberta Street</strong> &amp; <strong>Hawthorne Boulevard</strong> — Portland&rsquo;s best independent boutique districts", "<strong>Powell&rsquo;s Books</strong> — covers an entire city block, largest independent bookstore in the world", "Powell&rsquo;s alone is worth the trip to Portland"])
html += day_close()

# Day 9
html += drive("Portland &rarr; Seattle &nbsp;&middot;&nbsp; 3 hrs · I-5 North, straightforward")
html += day_open(9,"THU","JUN 19","1502175353174-a7a70e73b362","Seattle, WA", yt("Seattle Washington travel guide Capitol Hill Pike Place","Seattle"))
html += stay("The State Hotel or Thompson Seattle","Both boutique, downtown. Thompson has rooftop bar with Space Needle views.","https://www.thompsonhotels.com/hotels/seattle")
html += eat([
    {"name":"Gluten Free Gem (before leaving Portland)","badges":GFD,"desc":"Dedicated GF bakery since 2006. Final Portland GF stop before the drive.","dishes":"GF pastries &middot; breads &middot; morning treats","link":PDX_D},
    {"name":"Seattle GF options","badges":GF,"desc":"Schilling Cider House (dedicated GF cider bar, Capitol Hill), various GF-friendly restaurants throughout.","dishes":"Capitol Hill dining scene &middot; Pike Place Market GF finds","link":""},
])
html += do(["Walk <strong>Pike Place Market</strong> — iconic, GF finds, flower market, fish toss", "<strong>Capitol Hill</strong> — Seattle&rsquo;s best shopping, cocktail bars, indie restaurants", "Rooftop bar with Space Needle &amp; mountain views", "Evening stroll along the waterfront"])
html += day_close()

# Day 10
html += day_open(10,"FRI","JUN 20","1533591380893-1a0fbff9e01e","Fly Home: SEA &rarr; TPA", yt("Seattle airport SEA tips","Departure Day"))
html += '''<div class="detail-row">
  <span class="tag tag-fly">FLY</span>
  <div class="detail-content">
    <strong>SEA &rarr; TPA nonstop</strong><br>
    Target ~10:00am PT departure &rarr; ~5:30pm ET arrival &nbsp;&middot;&nbsp; ~5.5 hrs<br>
    Alaska Airlines / Delta<br>
    <span style="color:var(--text-light);font-size:0.76rem">Drop Car #2 at SEA airport. Allow 90 min before flight.</span>
  </div>
</div>'''
html += day_close()

html += '''
    <div class="divider"></div>
    <h3 class="section-heading">June <em>Weather</em></h3>
    <p class="section-sub">Mostly excellent — Portland carries a &ldquo;Juneuary&rdquo; grey risk.</p>
    <div class="weather-grid">
      <div class="weather-card"><div class="weather-city">Salt Lake City / Park City</div><div class="weather-temp">70&ndash;88&deg;F</div><div class="weather-desc">Dry, sunny, perfect. Park City 8–10°F cooler than SLC.</div><div class="weather-grade">Grade: A</div></div>
      <div class="weather-card"><div class="weather-city">Jackson Hole</div><div class="weather-temp">70&ndash;75&deg;F</div><div class="weather-desc">Gorgeous. Wildflower season. Perfect hiking weather.</div><div class="weather-grade">Grade: A</div></div>
      <div class="weather-card"><div class="weather-city">Bozeman, MT</div><div class="weather-temp">75&ndash;82&deg;F</div><div class="weather-desc">Dry and comfortable. Montana at its finest.</div><div class="weather-grade">Grade: A</div></div>
      <div class="weather-card"><div class="weather-city">Portland</div><div class="weather-temp">72&ndash;78&deg;F</div><div class="weather-desc">&ldquo;Juneuary&rdquo; — ~25% daily rain chance. Improving late June. Pack a light layer.</div><div class="weather-grade">Grade: B+</div></div>
      <div class="weather-card"><div class="weather-city">Seattle</div><div class="weather-temp">68&ndash;72&deg;F</div><div class="weather-desc">Similar to Portland, slightly cooler. Often clears by afternoon.</div><div class="weather-grade">Grade: B+</div></div>
    </div>
  </div>
</section>
'''

with open('/home/user/SmartThingsPublic/sabbatical-site/index.html', 'r') as f:
    content = f.read()

placeholder = '<section id="option-b" class="section"><div style="padding:120px 24px;text-align:center;color:#aaa;font-family:var(--serif);font-size:1.5rem">Loading Option B\u2026</div></section>'
content = content.replace(placeholder, html)

with open('/home/user/SmartThingsPublic/sabbatical-site/index.html', 'w') as f:
    f.write(content)

print(f"Done. Total lines: {len(content.splitlines())}")
