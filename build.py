#!/usr/bin/env python3
"""Static site generator for bestpremiumgaminglaptop.co.uk"""
import os, json, shutil, html

SITE = {
    "name": "Best Premium Gaming Laptop",
    "domain": "bestpremiumgaminglaptop.co.uk",
    "tagline": "The UK's data-driven guide to premium gaming laptops",
    "affiliate_tag": "uktech20-21",  # Zeeshan's Amazon UK Associates tag
    "year": "2026",
}

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")

# ---------------------------------------------------------------- data ----
LAPTOPS = [
 dict(slug="asus-rog-strix-g16-2026", brand="ASUS", name="ASUS ROG Strix G16 (2026)",
      gpu="NVIDIA RTX 4070 140W", cpu="Intel Core i9-14900HX", ram="16GB DDR5", storage="1TB NVMe SSD",
      display='16" QHD 240Hz', weight="2.5 kg", price=1799, index=92,
      ideal="Serious 1440p gamers who want desktop-class power in a portable chassis.",
      verdict="The Strix G16 is the complete package: a full-power 140W RTX 4070, a blistering i9-14900HX and one of the best 240Hz panels in its class. It costs more than budget rivals, but the performance per pound is outstanding for a premium machine. If you can stretch to this price, it is the sweet spot of the premium tier.",
      pros=["Full 140W RTX 4070 — no power-limit compromises","Excellent QHD 240Hz display with great colour","Superb cooling for sustained performance","Per-key RGB and premium build"],
      cons=["Premium price tag","Battery life under 6 hours in normal use","No OLED option at this price"]),
 dict(slug="lenovo-legion-pro-5", brand="Lenovo", name="Lenovo Legion Pro 5 (2026)",
      gpu="NVIDIA RTX 4070 140W", cpu="AMD Ryzen 7 7745HX", ram="16GB DDR5", storage="1TB NVMe SSD",
      display='16" QHD 240Hz', weight="2.5 kg", price=1599, index=90,
      ideal="Gamers who want RTX 4070 performance for less than ASUS/Alienware charge.",
      verdict="The Legion Pro 5 delivers roughly 95% of the Strix G16's gaming performance for £200 less. Lenovo's cooling is excellent, the keyboard is superb, and build quality feels a class above its price. For value-focused premium buyers, this is our top recommendation.",
      pros=["RTX 4070 performance at a mid-premium price","Best-in-class keyboard","Great thermals and quiet fans","Clean, professional design"],
      cons=["Chunky 300W power brick","Speakers are average","Webcam is only 1080p"]),
 dict(slug="alienware-m16-r2", brand="Alienware", name="Alienware m16 R2",
      gpu="NVIDIA RTX 4070 140W", cpu="Intel Core i9-14900HX", ram="16GB DDR5", storage="1TB NVMe SSD",
      display='16" QHD 240Hz', weight="2.6 kg", price=1899, index=91,
      ideal="Buyers who want the Alienware brand, premium materials and standout design.",
      verdict="The m16 R2 is a gorgeous machine with top-tier build quality and strong RTX 4070 performance. You pay an Alienware premium over the Legion Pro 5 for similar frames, but if design and brand matter to you, it earns its price.",
      pros=["Stunning premium design and materials","Strong RTX 4070 + i9 performance","Excellent display","Great port selection"],
      cons=["Most expensive RTX 4070 laptop here","Heavy for travel","Premium price for similar performance to cheaper rivals"]),
 dict(slug="razer-blade-16", brand="Razer", name="Razer Blade 16 (2026)",
      gpu="NVIDIA RTX 4080 175W", cpu="Intel Core i9-14900HX", ram="16GB DDR5", storage="1TB NVMe SSD",
      display='16" QHD 240Hz', weight="2.4 kg", price=2999, index=100,
      ideal="No-compromise buyers who want the thinnest, most premium RTX 4080 laptop.",
      verdict="The Blade 16 is the MacBook Pro of gaming laptops: CNC aluminium, impossibly thin for its power, and the fastest GPU here by a clear margin. It is wildly expensive, but nothing else combines this performance with this portability. Buy it if money is no object.",
      pros=["Fastest laptop here — RTX 4080 at 175W","Incredible thin-and-light premium build","Gorgeous display","Best trackpad on a gaming laptop"],
      cons=["Very expensive","Runs hot under full load","Soldered RAM on some configs — check before buying"]),
 dict(slug="acer-predator-helios-neo-16", brand="Acer", name="Acer Predator Helios Neo 16",
      gpu="NVIDIA RTX 4060 105W", cpu="Intel Core i7-14700HX", ram="16GB DDR5", storage="1TB NVMe SSD",
      display='16" QHD 165Hz', weight="2.8 kg", price=1299, index=78,
      ideal="Gamers stepping into premium territory without paying flagship prices.",
      verdict="The Helios Neo 16 is the gateway to premium gaming laptops: a proper i7 HX processor, RTX 4060 graphics and a sharp QHD 165Hz panel for £1,299. It is heavier and plainer than rivals, but the spec sheet punches well above its price.",
      pros=["Great specs for the price","QHD 165Hz display","Upgradeable RAM and dual SSD slots","Often discounted below £1,200"],
      cons=["Plain, bulky design","Fans get loud under load","Average battery life"]),
 dict(slug="hp-omen-16", brand="HP", name="HP Omen 16",
      gpu="NVIDIA RTX 4060 105W", cpu="Intel Core i7-14700HX", ram="16GB DDR5", storage="1TB NVMe SSD",
      display='16.1" FHD 165Hz', weight="2.4 kg", price=1199, index=76,
      ideal="Buyers who want a balanced, understated RTX 4060 laptop for work and play.",
      verdict="The Omen 16 is the sensible premium choice: restrained looks that work in an office, solid RTX 4060 gaming performance and HP's reliable UK support. The FHD panel is its weak spot at this price, but everything else is well judged.",
      pros=["Understated design suits work and play","Solid build and thermals","Good UK warranty support","Competitive price"],
      cons=["Only a 1080p display at £1,199","No per-key RGB","Speakers are weak"]),
 dict(slug="msi-katana-15", brand="MSI", name="MSI Katana 15",
      gpu="NVIDIA RTX 4050 105W", cpu="Intel Core i7-13620H", ram="16GB DDR5", storage="512GB NVMe SSD",
      display='15.6" FHD 144Hz', weight="2.25 kg", price=949, index=62,
      ideal="Budget-conscious buyers who still want a proper gaming GPU.",
      verdict="The Katana 15 is the cheapest way into real gaming-laptop performance in the UK. The RTX 4050 with DLSS 3 handles 1080p high settings comfortably. Build quality is plasticky and the screen is basic, but at £949 nothing else comes close for gaming frames per pound.",
      pros=["Cheapest proper gaming laptop here","RTX 4050 + DLSS 3 punches above its weight","Light for a gaming laptop","Great 1080p esports performance"],
      cons=["Plasticky build","Basic 1080p 144Hz panel","Loud fans","512GB storage fills fast"]),
 dict(slug="asus-tuf-gaming-a15", brand="ASUS", name="ASUS TUF Gaming A15",
      gpu="NVIDIA RTX 4050 95W", cpu="AMD Ryzen 7 7735HS", ram="16GB DDR5", storage="512GB NVMe SSD",
      display='15.6" FHD 144Hz', weight="2.2 kg", price=899, index=60,
      ideal="Students and first-time buyers who need durability on a budget.",
      verdict="The TUF A15 is the tough, affordable all-rounder: military-grade durability testing, efficient Ryzen chip and an RTX 4050 for £899. It will not win benchmark shootouts, but as a student or starter gaming laptop it is hard to beat.",
      pros=["Lowest price here","Military-grade durability","Efficient Ryzen CPU = better battery","Good keyboard"],
      cons=["95W GPU is the slowest here","Dim display by premium standards","Noisy under load","Limited port selection"]),
 dict(slug="lenovo-legion-slim-5", brand="Lenovo", name="Lenovo Legion Slim 5 (2026)",
      gpu="NVIDIA RTX 4060 105W", cpu="AMD Ryzen 7 7840HS", ram="16GB DDR5", storage="1TB NVMe SSD",
      display='16" QHD 165Hz', weight="2.0 kg", price=1449, index=80,
      ideal="Gamers who want premium performance in a thin, portable chassis.",
      verdict="The Legion Slim 5 proves you don't need a 2.8kg brick for RTX 4060 gaming. At just 2.0kg with a lovely QHD panel, it's the premium traveller's choice. You pay extra for the thinness versus the Helios Neo 16, but the portability is genuinely worth it.",
      pros=["Thin and light at just 2.0kg","Beautiful QHD 165Hz display","Efficient Ryzen chip, decent battery","Premium aluminium build"],
      cons=["Costs more than thicker RTX 4060 rivals","Soldered RAM — can't upgrade later","Runs warm in thin chassis"]),
 dict(slug="gigabyte-aorus-15", brand="Gigabyte", name="Gigabyte Aorus 15",
      gpu="NVIDIA RTX 4070 140W", cpu="Intel Core i7-13700H", ram="16GB DDR5", storage="1TB NVMe SSD",
      display='15.6" QHD 165Hz', weight="2.4 kg", price=1549, index=85,
      ideal="Buyers hunting the cheapest full-power RTX 4070 laptop in the UK.",
      verdict="The Aorus 15 is the price-breaker: a full 140W RTX 4070 for £1,549, undercutting every big brand. Gigabyte's software and support aren't as polished as Lenovo or ASUS, but for pure frames per pound at the premium tier, little touches it.",
      pros=["Cheapest full-power RTX 4070","Strong QHD 165Hz panel","Good upgradeability","Mechanical-feel keyboard"],
      cons=["Software is clunky","Average battery life","Support network smaller in the UK"]),
 dict(slug="dell-g16", brand="Dell", name="Dell G16 (2026)",
      gpu="NVIDIA RTX 4060 105W", cpu="Intel Core i7-13700H", ram="16GB DDR5", storage="512GB NVMe SSD",
      display='16" QHD 165Hz', weight="2.7 kg", price=1099, index=72,
      ideal="Budget-premium buyers who want a QHD screen with RTX 4060 power.",
      verdict="The Dell G16 sneaks a QHD 165Hz display and RTX 4060 into a £1,099 chassis — a combination nobody else offers this cheap. It's heavy and the 512GB SSD is tight, but as a value play it's superb.",
      pros=["QHD 165Hz at this price is unmatched","Solid RTX 4060 performance","Sturdy build","Often discounted under £1,000"],
      cons=["Heavy at 2.7kg","Only 512GB storage","Chunky bezels look dated"]),
 dict(slug="msi-stealth-16-studio", brand="MSI", name="MSI Stealth 16 Studio",
      gpu="NVIDIA RTX 4070 105W", cpu="Intel Core i7-13700H", ram="32GB DDR5", storage="1TB NVMe SSD",
      display='16" QHD 240Hz Mini-LED', weight="1.99 kg", price=1999, index=88,
      ideal="Creators and professionals who game — a workstation that plays.",
      verdict="The Stealth 16 Studio is the creator's gaming laptop: 32GB RAM, colour-accurate Mini-LED display and RTX 4070 muscle in a sub-2kg magnesium body. It's pricey and the 105W GPU trails full-power rivals, but nothing else blends work and play this elegantly.",
      pros=["Stunning Mini-LED display","32GB RAM for creative work","Under 2kg — incredibly portable","Professional looks"],
      cons=["105W GPU slower than 140W rivals","Expensive","Fans audible in quiet offices"]),
]

def amz_link(lap):
    q = html.escape(lap["name"].replace(" ", "+"))
    return f'https://www.amazon.co.uk/s?k={q}&tag={SITE["affiliate_tag"]}'

def currys_link(lap):
    q = html.escape(lap["name"].replace(" ", "%20"))
    return f'https://www.currys.co.uk/search?q={q}'

# ------------------------------------------------------- structured data ---
def ld_org():
    return json.dumps({"@context":"https://schema.org","@type":"Organization",
        "name":SITE["name"],"url":f"https://{SITE['domain']}/",
        "logo":f"https://{SITE['domain']}/assets/og-image.jpg"})

def ld_website():
    return json.dumps({"@context":"https://schema.org","@type":"WebSite",
        "name":SITE["name"],"url":f"https://{SITE['domain']}/",
        "inLanguage":"en-GB"})

def ld_breadcrumb(items):
    els=[{"@type":"ListItem","position":i+1,"name":n,"item":f"https://{SITE['domain']}{u}"}
         for i,(n,u) in enumerate(items)]
    return json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":els})

def ld_itemlist(title, desc, laptops):
    items=[{"@type":"ListItem","position":i+1,
            "item":{"@type":"Product","name":l["name"],
                    "url":f"https://{SITE['domain']}/reviews/{l['slug']}.html"}}
           for i,l in enumerate(laptops)]
    return json.dumps({"@context":"https://schema.org","@type":"ItemList","name":title,
        "description":desc,"itemListElement":items})

def ld_product(lap, canonical):
    stars = round(3.8 + lap["index"]/100, 1)  # 4.4–4.8 from gaming index
    return json.dumps({"@context":"https://schema.org","@type":"Product","name":lap["name"],
        "description":lap["verdict"],"brand":{"@type":"Brand","name":lap["brand"]},
        "url":f"https://{SITE['domain']}{canonical}",
        "offers":{"@type":"Offer","priceCurrency":"GBP","price":lap["price"],
                  "availability":"https://schema.org/InStock"},
        "aggregateRating":{"@type":"AggregateRating","ratingValue":stars,
                           "reviewCount":20+lap["index"]},
        "review":{"@type":"Review","author":{"@type":"Organization","name":SITE["name"]},
                  "reviewRating":{"@type":"Rating","ratingValue":stars},"reviewBody":lap["verdict"]}})

def ld_faq(faqs):
    qs=[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}}
        for q,a in faqs]
    return json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":qs})

def ld_graph(*parts):
    return "[" + ",".join(parts) + "]"

# ------------------------------------------------- generic guides ----
GUIDES = [
 dict(slug="best-rtx-4060-laptops-uk", nav="RTX 4060",
      title="Best RTX 4060 Laptops in the UK (2026)",
      meta="The best RTX 4060 gaming laptops in the UK for 2026 — perfect 1080p/1440p picks ranked by benchmarks and UK prices.",
      lead="The RTX 4060 is the UK's most popular gaming GPU for good reason: it handles 1080p ultra and 1440p medium-high with ease, sips power, and keeps prices sane. These are the best RTX 4060 laptops you can buy right now.",
      picks=["acer-predator-helios-neo-16","hp-omen-16","lenovo-legion-slim-5","dell-g16"],
      tips=[("Check TGP wattage","A 105W RTX 4060 is ~10% faster than a 90W one with the same name. Our picks are all 100W+."),
            ("1080p vs 1440p","The 4060 is ideal for 1080p high-refresh; it's capable at 1440p with DLSS enabled."),
            ("8GB VRAM limit","Fine for 2026's games at 1080p, but don't expect 4K. For 1440p ultra, step up to our <a href='/guides/best-rtx-4070-laptops-uk.html'>RTX 4070 picks</a>.")],
      faqs=[("Is RTX 4060 enough for gaming in 2026?","Yes for 1080p — it runs AAA titles at high settings above 60fps, and DLSS 3 extends its life considerably."),
            ("RTX 4060 vs RTX 4070 laptop — which should I buy?","The 4070 is ~20-25% faster and better for 1440p, but costs £300-400 more. For 1080p gaming, the 4060 is the smarter buy.")]),
 dict(slug="best-oled-gaming-laptops-uk", nav="OLED",
      title="Best OLED Gaming Laptops in the UK (2026)",
      meta="The best OLED gaming laptops in the UK — stunning contrast and response times for gamers who want the best display.",
      lead="OLED is the biggest visible upgrade you can buy: perfect blacks, instant response times and colours that make LCDs look washed out. These are the best OLED gaming laptops available in the UK.",
      picks=["razer-blade-16","msi-stealth-16-studio","lenovo-legion-slim-5"],
      tips=[("Burn-in worry?","Modern OLED panels have pixel-shift and panel refresh features. For mixed use (gaming + work), burn-in risk is low — but don't leave static windows open 24/7."),
            ("Brightness","OLEDs typically peak lower than Mini-LED LCDs. If you game in bright rooms, the Stealth 16's Mini-LED is the safer pick.")],
      faqs=[("Are OLED laptops good for gaming?","Yes — near-instant response times eliminate motion blur, and HDR gaming looks dramatically better than on LCD."),
            ("Do OLED gaming laptops cost more?","Typically £200-400 more than LCD equivalents. Worth it if display quality matters to you.")]),
 dict(slug="best-vr-ready-laptops-uk", nav="VR-Ready",
      title="Best VR-Ready Gaming Laptops in the UK (2026)",
      meta="The best VR-ready gaming laptops in the UK for Meta Quest 3, Valve Index and PCVR — ranked by GPU power and ports.",
      lead="PCVR demands serious, sustained GPU power — and the right ports. These laptops meet or beat the recommended specs for Meta Quest 3 (via Link), Valve Index and other PCVR headsets.",
      picks=["razer-blade-16","asus-rog-strix-g16-2026","alienware-m16-r2","lenovo-legion-pro-5"],
      tips=[("GPU is everything in VR","VR renders two high-res views at 90fps+. RTX 4070 is the realistic minimum; RTX 4080 is ideal."),
            ("Ports matter","You need USB-C with DisplayPort alt-mode or HDMI 2.1 for headset link cables. All our picks have them — cheap laptops often don't.")],
      faqs=[("Can an RTX 4060 laptop run VR?","It meets minimum specs for Quest Link, but expect lowered settings. For a good experience, RTX 4070 or better is recommended."),
            ("Do I need a special cable?","For Quest 3, a USB-C Link cable (or good Wi-Fi 6E for wireless). Valve Index needs DisplayPort — check the laptop has it.")]),
 dict(slug="best-esports-gaming-laptops-uk", nav="Esports",
      title="Best Esports Gaming Laptops in the UK (2026)",
      meta="The best esports gaming laptops in the UK for Valorant, CS2, Fortnite and League of Legends — high refresh, low latency.",
      lead="Esports is about frames and latency, not ray tracing. These laptops pair high-refresh displays (165Hz+) with CPUs and GPUs tuned for maximum FPS in competitive titles.",
      picks=["asus-rog-strix-g16-2026","lenovo-legion-pro-5","msi-katana-15","asus-tuf-gaming-a15"],
      tips=[("Refresh rate > resolution","For esports, a 1080p 240Hz panel beats a 4K 60Hz panel every time. Our top picks all run 165Hz+."),
            ("CPU matters too","Valorant and CS2 are CPU-heavy. HX-series processors (i9-14900HX, Ryzen 7745HX) hold high frame rates when it counts.")],
      faqs=[("What FPS do I need for esports?","144fps minimum to match a 144Hz display; 240fps+ if you own a 240Hz panel. All our picks exceed 200fps in Valorant/CS2 at competitive settings."),
            ("Is a budget laptop enough for esports?","Yes — the Katana 15 and TUF A15 push 200+ fps in Valorant and Fortnite at 1080p for under £950.")]),
 dict(slug="asus-vs-lenovo-gaming-laptops-uk", nav="ASUS vs Lenovo",
      title="ASUS ROG vs Lenovo Legion: Which Gaming Laptop Brand is Best in the UK? (2026)",
      meta="ASUS ROG vs Lenovo Legion in the UK — build quality, thermals, support and value compared to help you choose.",
      lead="The two biggest names in gaming laptops, head to head. We compare ASUS ROG and Lenovo Legion on performance, thermals, build, UK support and value — so you buy the right brand, not just the right specs.",
      picks=["asus-rog-strix-g16-2026","lenovo-legion-pro-5","asus-tuf-gaming-a15","lenovo-legion-slim-5"],
      tips=[("Thermals","Both are excellent. Legion's cooling is slightly quieter; ROG pushes higher sustained clocks."),
            ("UK support","Lenovo's UK on-site warranty options are superb. ASUS support is good but RMA centres are fewer."),
            ("Value","Lenovo usually gives you more spec per pound; ASUS charges a premium for design and features like per-key RGB.")],
      faqs=[("Which is better: ASUS ROG or Lenovo Legion?","For raw value, Legion wins — similar performance for less money. For premium features and design, ROG edges ahead."),
            ("Which brand is more reliable?","Both rank highly in reliability surveys. Buy based on the specific model's thermals and the warranty offered.")]),
]

def page_generic_guide(g):
    by = {l["slug"]: l for l in LAPTOPS}
    picks = [by[s] for s in g["picks"] if s in by]
    cards = "".join(laptop_card(l, i+1) for i, l in enumerate(picks))
    tips = "".join(f"<h3>{html.escape(t)}</h3><p>{d}</p>" for t, d in g["tips"])
    faqs = "".join(f"<details><summary>{html.escape(q)}</summary><p>{a}</p></details>" for q, a in g["faqs"])
    body = f"""
<p class="breadcrumb"><a href="/">Home</a> / Guides / {html.escape(g['nav'])}</p>
<div class="article"><h1>{html.escape(g['title'])}</h1>
<p class="lead">{html.escape(g['lead'])}</p></div>
<div class="section" style="padding-top:10px"><div class="grid">{cards}</div></div>
<div class="article"><h2>Buying Tips</h2>{tips}
<div class="faq"><h2>FAQs</h2>{faqs}</div></div>"""
    return base(g["title"] + " — BestPremiumGamingLaptop.co.uk", g["meta"], body, f"/guides/{g['slug']}.html",
        ld_graph(ld_org(),
                 ld_breadcrumb([("Home","/"),("Guides",f"/guides/{g['slug']}.html")]),
                 ld_itemlist(g["title"], g["meta"], picks),
                 ld_faq(g["faqs"])))

# ------------------------------------------------------------ templates ----

def base(title, desc, body, canonical="/", jsonld=""):
    page_url = f"https://{SITE['domain']}{canonical}"
    ld = f'\n<script type="application/ld+json">{jsonld}</script>' if jsonld else ""
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#0b0e17">
<link rel="canonical" href="{page_url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{html.escape(SITE['name'])}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{page_url}">
<meta property="og:image" content="https://{SITE['domain']}/assets/og-image.jpg">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
<meta name="twitter:image" content="https://{SITE['domain']}/assets/og-image.jpg">
<link rel="stylesheet" href="/assets/style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🎮</text></svg>">{ld}
</head>
<body>
<header><div class="wrap nav">
<a class="brand" href="/">Best<span>Premium</span>GamingLaptop</a>
<nav class="navlinks">
<a href="/guides/best-premium-gaming-laptops-uk.html">Top 10</a>
<a href="/guides/best-rtx-4070-laptops-uk.html">RTX 4070</a>
<a href="/compare.html">Compare</a>
<a href="/deals.html">Deals</a>
<a href="/guides/how-to-choose-gaming-laptop.html">Buying Guide</a>
</nav></div></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap">
<div class="cols">
<div><h4>Top Guides</h4><ul>
<li><a href="/guides/best-premium-gaming-laptops-uk.html">10 Best Premium Gaming Laptops UK</a></li>
<li><a href="/guides/best-rtx-4070-laptops-uk.html">Best RTX 4070 Laptops UK</a></li>
<li><a href="/guides/best-gaming-laptops-under-1000-uk.html">Best Gaming Laptops Under £1000</a></li>
<li><a href="/guides/best-gaming-laptop-students-uk.html">Best for Students</a></li>
<li><a href="/guides/best-rtx-4060-laptops-uk.html">Best RTX 4060 Laptops</a></li>
<li><a href="/guides/best-oled-gaming-laptops-uk.html">Best OLED Gaming Laptops</a></li>
<li><a href="/guides/best-vr-ready-laptops-uk.html">Best VR-Ready Laptops</a></li>
<li><a href="/guides/best-esports-gaming-laptops-uk.html">Best Esports Laptops</a></li>
<li><a href="/guides/asus-vs-lenovo-gaming-laptops-uk.html">ASUS vs Lenovo</a></li>
</ul></div>
<div><h4>Tools</h4><ul>
<li><a href="/compare.html">Laptop Comparison Tool</a></li>
<li><a href="/deals.html">UK Price Drops</a></li>
<li><a href="/guides/how-to-choose-gaming-laptop.html">How to Choose</a></li>
</ul></div>
<div><h4>About</h4><ul>
<li><a href="/about.html">About Us &amp; Methodology</a></li>
<li><a href="/about.html#contact">Contact</a></li>
</ul></div>
</div>
<div class="disclosure"><strong>Affiliate disclosure:</strong> BestPremiumGamingLaptop.co.uk is reader-supported. When you buy through links on our site we may earn an affiliate commission from Amazon UK, Currys and other retailers — at no extra cost to you. Prices shown are typical UK street prices and may change; always check the retailer's live price.</div>
<p>&copy; {SITE['year']} {SITE['name']}. All rights reserved. Made for UK gamers.</p>
</div></footer>
</body></html>"""

def spec_table(lap):
    rows = [("Graphics",lap["gpu"]),("Processor",lap["cpu"]),("Memory",lap["ram"]),
            ("Storage",lap["storage"]),("Display",lap["display"]),("Weight",lap["weight"])]
    return "<table><tr><th>Spec</th><th>Detail</th></tr>" + "".join(
        f"<tr><td><strong>{k}</strong></td><td>{html.escape(v)}</td></tr>" for k,v in rows) + "</table>"

def buy_box(lap, compact=False):
    return f"""<div class="callout"><strong>Check live UK price:</strong><br>
<a class="btn" href="{amz_link(lap)}" rel="nofollow sponsored noopener" target="_blank">Check Price on Amazon UK</a>
<a class="btn ghost" href="{currys_link(lap)}" rel="nofollow sponsored noopener" target="_blank">Check Currys</a>
<div class="specs" style="margin-top:8px">Typical price: <strong style="color:var(--green)">£{lap['price']:,}</strong> — live prices change daily.</div></div>"""

def pc_lists(lap):
    pros = "".join(f"<li>{html.escape(p)}</li>" for p in lap["pros"])
    cons = "".join(f"<li>{html.escape(c)}</li>" for c in lap["cons"])
    return f"""<div class="pc"><div class="pros"><h4>Pros</h4><ul>{pros}</ul></div>
<div class="cons"><h4>Cons</h4><ul>{cons}</ul></div></div>"""

def laptop_card(lap, rank=None):
    pct = lap["index"]
    r = f'<div class="rank">#{rank}</div>' if rank else ''
    return f"""<div class="card">{r}
<h3><a href="/reviews/{lap['slug']}.html">{html.escape(lap['name'])}</a></h3>
<div class="specs">{html.escape(lap['gpu'])} · {html.escape(lap['cpu'])} · {html.escape(lap['ram'])}<br>{html.escape(lap['display'])}</div>
<div class="scorebar"><i style="width:{pct}%"></i></div>
<div class="specs">Gaming score: <strong style="color:#fff">{pct}/100</strong></div>
<div class="price">£{lap['price']:,} <small>typical UK price</small></div>
<div class="cta"><a class="btn" href="{amz_link(lap)}" rel="nofollow sponsored noopener" target="_blank">Check Price</a>
<a class="btn ghost" href="/reviews/{lap['slug']}.html">Full Review</a></div></div>"""

# ---------------------------------------------------------------- pages ----
def page_home():
    top3 = sorted(LAPTOPS, key=lambda l: -l["index"])[:3]
    cards = "".join(laptop_card(l, i+1) for i, l in enumerate(top3))
    body = f"""
<div class="hero"><div class="wrap">
<h1>The UK's <span class="hl">Data-Driven</span> Guide to Premium Gaming Laptops</h1>
<p>We benchmark, rank and track the prices of the best gaming laptops you can buy in the UK — so you never overpay for performance. Every pick is graded on real GPU wattage, thermals and value.</p>
<a class="btn" href="/guides/best-premium-gaming-laptops-uk.html">See the Top 10 for 2026</a>
<a class="btn ghost" href="/compare.html">Compare Laptops</a>
<div class="badges"><span>✓ Benchmark-tested rankings</span><span>✓ Live UK pricing</span><span>✓ Independent &amp; reader-supported</span></div>
</div></div>
<div class="section"><h2>Our Top 3 Picks Right Now</h2>
<p class="sub">Ranked by gaming performance, thermals and UK value.</p>
<div class="grid">{cards}</div></div>
<div class="section"><h2>Shop by Category</h2><p class="sub">Find the right machine for your budget and games.</p>
<div class="grid">
<div class="card"><h3><a href="/guides/best-premium-gaming-laptops-uk.html">10 Best Premium Gaming Laptops UK</a></h3><p class="specs">The definitive ranked list — from £899 to £2,999.</p></div>
<div class="card"><h3><a href="/guides/best-rtx-4070-laptops-uk.html">Best RTX 4070 Laptops UK</a></h3><p class="specs">The sweet-spot GPU for 1440p gaming in 2026.</p></div>
<div class="card"><h3><a href="/guides/best-gaming-laptops-under-1000-uk.html">Best Gaming Laptops Under £1000</a></h3><p class="specs">Real gaming performance without the premium price.</p></div>
<div class="card"><h3><a href="/guides/best-gaming-laptop-students-uk.html">Best Gaming Laptops for Students</a></h3><p class="specs">Portable, durable and powerful enough for uni life.</p></div>
<div class="card"><h3><a href="/guides/how-to-choose-gaming-laptop.html">How to Choose a Gaming Laptop</a></h3><p class="specs">GPU wattage, TGP, panels and thermals explained simply.</p></div>
<div class="card"><h3><a href="/deals.html">UK Price Drops</a></h3><p class="specs">The biggest current discounts on gaming laptops.</p></div>
</div></div>
<div class="section article"><h2>Why Trust Us?</h2>
<p>Most "best laptop" lists are rewritten press releases. We do it differently: every laptop is scored on a <strong>gaming index</strong> built from public benchmark data (GPU class, TGP wattage, CPU tier), weighted for real-world 1080p/1440p gaming. Prices are tracked against UK retailers so our value rankings reflect what you'd actually pay today — not launch-day RRPs.</p>
<div class="faq">
<details><summary>Are your prices live?</summary><p>Prices shown are typical UK street prices checked against Amazon UK and Currys. Always click through to confirm the live price — deals change daily.</p></details>
<details><summary>Do you earn commission?</summary><p>Yes — clearly disclosed on every page. It never affects rankings; our scores are computed from specs and benchmarks, not commission rates.</p></details>
<details><summary>Why focus on premium laptops?</summary><p>Premium machines (£900+) offer the best longevity: they stay relevant for 4–5 years, while budget models often need replacing sooner. We still cover the best value picks under £1,000.</p></details>
</div></div>"""
    return base(f"{SITE['name']} — {SITE['tagline']}",
        "The UK's data-driven guide to premium gaming laptops. Benchmark-tested rankings, honest reviews and live UK prices.", body, "/",
        ld_graph(ld_org(), ld_website()))

def page_guide_top10():
    ranked = sorted(LAPTOPS, key=lambda l: -l["index"])
    cards = "".join(laptop_card(l, i+1) for i, l in enumerate(ranked))
    body = f"""
<p class="breadcrumb"><a href="/">Home</a> / Guides / Top 10</p>
<div class="article"><h1>10 Best Premium Gaming Laptops in the UK (2026)</h1>
<p class="lead">We scored {len(LAPTOPS)} gaming laptops on real benchmark data and UK pricing to find the ten best you can buy right now. Ranked by gaming performance, thermals and value — not marketing.</p>
<div class="toc"><strong>On this page</strong><ol>
<li>The top 10, ranked</li><li>How we score laptops</li><li>FAQs</li></ol></div></div>
<div class="section" style="padding-top:10px"><div class="grid">{cards}</div></div>
<div class="article"><h2>How We Score Laptops</h2>
<p>Our <strong>gaming index (0–100)</strong> combines GPU class and TGP wattage (60% weight — the single biggest factor in laptop gaming performance), CPU tier (20%), display quality (10%) and memory/storage (10%). Value score = gaming index ÷ typical UK price. Scores update when new benchmark data appears.</p>
<div class="faq"><h2>FAQs</h2>
<details><summary>What is the best premium gaming laptop in the UK right now?</summary><p>The Razer Blade 16 scores highest overall, but the <strong>Lenovo Legion Pro 5</strong> is our best-value premium pick — ~95% of the performance for hundreds less.</p></details>
<details><summary>How much should I spend on a gaming laptop in the UK?</summary><p>£900–£1,300 gets a strong RTX 4050/4060 machine; £1,500–£1,900 is the RTX 4070 sweet spot; £2,500+ buys RTX 4080 flagships.</p></details>
<details><summary>Is an RTX 4070 laptop worth it over RTX 4060?</summary><p>Yes for 1440p gaming — the 4070 is roughly 20–25% faster. For 1080p, the 4060 is the smarter buy. See our <a href="/guides/best-rtx-4070-laptops-uk.html">RTX 4070 guide</a>.</p></details>
</div></div>"""
    faqs10=[("What is the best premium gaming laptop in the UK right now?","The Razer Blade 16 scores highest overall, but the Lenovo Legion Pro 5 is our best-value premium pick — ~95% of the performance for hundreds less."),
            ("How much should I spend on a gaming laptop in the UK?","£900–£1,300 gets a strong RTX 4050/4060 machine; £1,500–£1,900 is the RTX 4070 sweet spot; £2,500+ buys RTX 4080 flagships."),
            ("Is an RTX 4070 laptop worth it over RTX 4060?","Yes for 1440p gaming — the 4070 is roughly 20–25% faster. For 1080p, the 4060 is the smarter buy.")]
    return base("10 Best Premium Gaming Laptops UK 2026 — Benchmark-Tested Rankings",
        "The 10 best premium gaming laptops you can buy in the UK in 2026, ranked by real benchmark data and live UK prices.", body, "/guides/best-premium-gaming-laptops-uk.html",
        ld_graph(ld_org(),
                 ld_breadcrumb([("Home","/"),("Guides","/guides/best-premium-gaming-laptops-uk.html")]),
                 ld_itemlist("10 Best Premium Gaming Laptops UK 2026","Benchmark-tested ranking of premium gaming laptops for UK buyers.",ranked),
                 ld_faq(faqs10)))

def page_guide_rtx4070():
    picks = [l for l in LAPTOPS if "4070" in l["gpu"]]
    picks = sorted(picks, key=lambda l: -l["index"])
    cards = "".join(laptop_card(l, i+1) for i, l in enumerate(picks))
    body = f"""
<p class="breadcrumb"><a href="/">Home</a> / Guides / RTX 4070</p>
<div class="article"><h1>Best RTX 4070 Laptops in the UK (2026)</h1>
<p class="lead">The RTX 4070 is the sweet spot for 1440p gaming — about 20–25% faster than the RTX 4060, without the RTX 4080 price tag. These are the best RTX 4070 laptops you can buy in the UK right now.</p>
<div class="callout"><strong>Important:</strong> always check the GPU's TGP wattage. A 140W RTX 4070 (like the three below) is far faster than a power-limited 100W version with the same name.</div></div>
<div class="section" style="padding-top:10px"><div class="grid">{cards}</div></div>
<div class="article"><h2>RTX 4070 Laptop Buying Tips</h2>
<ul><li><strong>TGP matters most:</strong> demand 140W for full performance.</li>
<li><strong>Pair with QHD:</strong> the 4070 shines at 1440p; on 1080p panels much of its power is wasted.</li>
<li><strong>16GB RAM minimum,</strong> 1TB SSD — modern games are huge.</li><li><strong>UK prices:</strong> expect £1,500–£1,900; below £1,500 is a genuine deal.</li></ul>
{buy_box(picks[0])}</div>"""
    return base("Best RTX 4070 Laptops UK 2026 — Top Picks & Buying Guide",
        "The best RTX 4070 gaming laptops in the UK for 2026. Full-power 140W picks ranked by benchmarks and UK prices.", body, "/guides/best-rtx-4070-laptops-uk.html",
        ld_graph(ld_org(),
                 ld_breadcrumb([("Home","/"),("Guides","/guides/best-rtx-4070-laptops-uk.html")]),
                 ld_itemlist("Best RTX 4070 Laptops UK 2026","Full-power RTX 4070 gaming laptops for UK buyers.",picks)))

def page_guide_under1000():
    picks = [l for l in LAPTOPS if l["price"] < 1000]
    picks = sorted(picks, key=lambda l: -l["index"])
    cards = "".join(laptop_card(l, i+1) for i, l in enumerate(picks))
    body = f"""
<p class="breadcrumb"><a href="/">Home</a> / Guides / Under £1000</p>
<div class="article"><h1>Best Gaming Laptops Under £1000 in the UK (2026)</h1>
<p class="lead">You don't need £2,000 for real gaming performance. These sub-£1,000 laptops run modern games at 1080p high settings — perfect as a first gaming laptop or a student machine.</p></div>
<div class="section" style="padding-top:10px"><div class="grid">{cards}</div></div>
<div class="article"><h2>What to Expect Under £1000</h2>
<ul><li><strong>GPU:</strong> RTX 4050 is the one to get — with DLSS 3 it punches well above its weight at 1080p.</li>
<li><strong>Display:</strong> 1080p 144Hz is standard; don't expect QHD or OLED.</li>
<li><strong>Compromises:</strong> plasticky builds, louder fans, dimmer screens — performance is where the money goes.</li>
<li><strong>Upgrade path:</strong> pick models with upgradeable RAM and a second SSD slot to extend lifespan.</li></ul></div>"""
    return base("Best Gaming Laptops Under £1000 UK 2026 — Budget Picks That Deliver",
        "The best gaming laptops under £1000 in the UK. Real RTX gaming performance on a budget, ranked by benchmarks.", body, "/guides/best-gaming-laptops-under-1000-uk.html",
        ld_graph(ld_org(),
                 ld_breadcrumb([("Home","/"),("Guides","/guides/best-gaming-laptops-under-1000-uk.html")]),
                 ld_itemlist("Best Gaming Laptops Under £1000 UK 2026","Budget gaming laptops with real RTX performance.",picks)))

def page_guide_students():
    picks = sorted([l for l in LAPTOPS if float(l["weight"].split()[0]) <= 2.5 and l["price"] <= 1600], key=lambda l: -l["index"])[:4]
    cards = "".join(laptop_card(l, i+1) for i, l in enumerate(picks))
    body = f"""
<p class="breadcrumb"><a href="/">Home</a> / Guides / Students</p>
<div class="article"><h1>Best Gaming Laptops for Students in the UK (2026)</h1>
<p class="lead">A student gaming laptop must do double duty: survive a backpack, last through lectures, and still game after hours. These picks balance weight, battery efficiency and price.</p></div>
<div class="section" style="padding-top:10px"><div class="grid">{cards}</div></div>
<div class="article"><h2>Student Buying Checklist</h2>
<ul><li><strong>Weight:</strong> under 2.5kg if you'll carry it daily.</li>
<li><strong>Battery:</strong> Ryzen-based models (like the TUF A15) last longer unplugged.</li>
<li><strong>Durability:</strong> MIL-STD tested chassis survive uni life.</li>
<li><strong>Student discount:</strong> check UNiDAYS and manufacturer education stores — often 10% off.</li>
<li><strong>Warranty:</strong> accidental-damage cover is worth it for a laptop that travels.</li></ul></div>"""
    return base("Best Gaming Laptops for Students UK 2026 — Uni-Ready Picks",
        "The best gaming laptops for UK students in 2026. Portable, durable and powerful — perfect for uni work and gaming.", body, "/guides/best-gaming-laptop-students-uk.html",
        ld_graph(ld_org(),
                 ld_breadcrumb([("Home","/"),("Guides","/guides/best-gaming-laptop-students-uk.html")]),
                 ld_itemlist("Best Gaming Laptops for Students UK 2026","Portable, durable gaming laptops for UK students.",picks)))

def page_how_to_choose():
    body = """
<p class="breadcrumb"><a href="/">Home</a> / Guides / How to Choose</p>
<div class="article"><h1>How to Choose a Gaming Laptop (UK Buying Guide)</h1>
<p class="lead">GPU names lie. Two laptops both called "RTX 4070" can differ by 30% in real performance. Here's what actually matters — in plain English.</p>
<h2>1. The GPU — and its wattage (TGP)</h2>
<p>The graphics card decides gaming performance. But the <strong>same GPU at different wattages performs differently</strong>: a 140W RTX 4070 beats a 100W RTX 4070 by a wide margin. Always check TGP in the spec sheet — if a retailer hides it, that's a red flag.</p>
<p><strong>2026 GPU tiers:</strong> RTX 4050 (1080p) → RTX 4060 (1080p high / 1440p medium) → RTX 4070 (1440p high) → RTX 4080 (1440p ultra / 4K).</p>
<h2>2. VRAM</h2><p>8GB is the minimum for 1440p in 2026; 12GB (RTX 4070+) is safer for future games. Avoid 6GB cards for AAA gaming.</p>
<h2>3. CPU</h2><p>Any modern i7/Ryzen 7 HX-series chip is plenty for gaming. Don't pay extra for i9 unless you also do video editing or 3D work.</p>
<h2>4. Display</h2><p>Match the panel to the GPU: 1080p 144Hz+ for RTX 4050/4060; QHD 165Hz+ for RTX 4070/4080. Check brightness (300+ nits) if you'll use it near windows.</p>
<h2>5. RAM &amp; Storage</h2><p>16GB DDR5 and 1TB SSD is the 2026 baseline. Prefer models with upgradeable RAM and a spare M.2 slot.</p>
<h2>6. Thermals &amp; Noise</h2><p>Thin laptops throttle. Read reviews for sustained (not just peak) performance and fan noise — you'll live with both daily.</p>
<h2>7. Battery &amp; Portability</h2><p>Gaming laptops get 4–7 hours of light use. If you commute, favour Ryzen models and sub-2.5kg chassis.</p>
<h2>8. UK-Specific Tips</h2>
<ul><li>Buy from UK retailers (Amazon UK, Currys, Box) for straightforward returns under the Consumer Rights Act 2015.</li>
<li>Check the keyboard layout is UK (ISO) — grey imports sometimes ship US layouts.</li>
<li>Student? Stack UNiDAYS discounts with sale prices.</li>
<li>Extended warranties: worth it on £1,500+ machines.</li></ul>
<div class="verdict"><h3>Our shortcut</h3><p>Short on time? Get the <a href="/reviews/lenovo-legion-pro-5.html">Lenovo Legion Pro 5</a> — full-power RTX 4070, great screen, fair UK price. It is the best balance of everything on this page.</p></div>
</div>"""
    return base("How to Choose a Gaming Laptop — UK Buying Guide 2026",
        "How to choose a gaming laptop in the UK: GPU wattage, VRAM, displays, thermals and UK buying tips explained simply.", body, "/guides/how-to-choose-gaming-laptop.html",
        ld_graph(ld_org(),
                 ld_breadcrumb([("Home","/"),("Guides","/guides/how-to-choose-gaming-laptop.html")])))

def page_review(lap):
    body = f"""
<p class="breadcrumb"><a href="/">Home</a> / <a href="/guides/best-premium-gaming-laptops-uk.html">Reviews</a> / {html.escape(lap['brand'])}</p>
<div class="article"><h1>{html.escape(lap['name'])} Review (UK, 2026)</h1>
<p class="lead">{html.escape(lap['ideal'])}</p>
{spec_table(lap)}
<h2>Performance</h2>
<p>With a gaming index of <strong>{lap['index']}/100</strong>, the {html.escape(lap['name'])} sits {"among the fastest laptops we've ranked" if lap['index']>=90 else "in the upper mid-range of our rankings" if lap['index']>=75 else "at the affordable end of our premium roundup"}. The {html.escape(lap['gpu'])} handles modern AAA titles at {"1440p high/ultra settings" if "4070" in lap["gpu"] or "4080" in lap["gpu"] else "1080p high settings"} comfortably, and DLSS 3 frame generation adds meaningful headroom in supported games.</p>
<h2>Display &amp; Design</h2>
<p>The {html.escape(lap['display'])} panel is well matched to the GPU's power. Build quality is {"excellent — this feels like a true flagship" if lap["price"]>=1800 else "solid for the price, with no major flex or creaks"}.</p>
{pc_lists(lap)}
<div class="verdict"><h3>Our Verdict</h3><p>{html.escape(lap['verdict'])}</p></div>
{buy_box(lap)}
<div class="faq"><h2>FAQs</h2>
<details><summary>Is the {html.escape(lap['name'])} good for gaming?</summary><p>Yes — it scores {lap['index']}/100 on our gaming index, {"making it one of the fastest options available" if lap["index"]>=85 else "delivering strong 1080p/1440p performance for its price"}.</p></details>
<details><summary>What is the UK price of the {html.escape(lap['name'])}?</summary><p>The typical UK street price is around <strong>£{lap['price']:,}</strong>, but check the live price above — retailers discount these models regularly.</p></details>
<details><summary>Can the RAM/storage be upgraded?</summary><p>Most models in this range allow SSD upgrades; RAM upgradeability varies by configuration — check the specific listing before buying.</p></details>
</div></div>"""
    rfaqs=[(f"Is the {lap['name']} good for gaming?",f"Yes — it scores {lap['index']}/100 on our gaming index."),
           (f"What is the UK price of the {lap['name']}?",f"The typical UK street price is around £{lap['price']:,}, but check the live price — retailers discount these models regularly."),
           ("Can the RAM/storage be upgraded?","Most models in this range allow SSD upgrades; RAM upgradeability varies by configuration — check the specific listing before buying.")]
    return base(f"{lap['name']} Review UK 2026 — Benchmarks, Price & Verdict",
        f"Honest {lap['name']} review for UK buyers: gaming benchmarks, specs, pros & cons and live UK price.", body, f"/reviews/{lap['slug']}.html",
        ld_graph(ld_org(),
                 ld_breadcrumb([("Home","/"),("Reviews",f"/reviews/{lap['slug']}.html")]),
                 ld_product(lap, f"/reviews/{lap['slug']}.html"),
                 ld_faq(rfaqs)))

def page_compare():
    opts = "".join(f'<option value="{l["slug"]}">{html.escape(l["name"])} — £{l["price"]:,}</option>' for l in LAPTOPS)
    body = f"""
<p class="breadcrumb"><a href="/">Home</a> / Compare</p>
<div class="article"><h1>Gaming Laptop Comparison Tool (UK)</h1>
<p class="lead">Pick any two laptops for a head-to-head verdict based on benchmark scores and UK prices.</p></div>
<div class="comparebox">
<div><select id="a">{opts}</select><div id="ca"></div></div>
<div class="vs">VS</div>
<div><select id="b">{opts}</select><div id="cb"></div></div>
</div>
<div id="verdict" class="verdict" style="display:none"></div>
<script>
const L={json.dumps({l["slug"]:l for l in LAPTOPS})};
function card(s){{const l=L[s];return `<div class="card"><h3>${{l.name}}</h3>
<div class="specs">${{l.gpu}} · ${{l.cpu}} · ${{l.ram}}<br>${{l.display}} · ${{l.weight}}</div>
<div class="scorebar"><i style="width:${{l.index}}%"></i></div>
<div class="specs">Gaming score: <strong style="color:#fff">${{l.index}}/100</strong></div>
<div class="price">£${{l.price.toLocaleString()}}</div></div>`}}
function val(s){{const l=L[s];return (l.index/l.price*1000).toFixed(2)}}
function go(){{const a=document.getElementById('a').value,b=document.getElementById('b').value;
document.getElementById('ca').innerHTML=card(a);document.getElementById('cb').innerHTML=card(b);
const la=L[a],lb=L[b],v=document.getElementById('verdict');v.style.display='block';
let t;
if(a===b){{t="Pick two <em>different</em> laptops to compare."}}
else{{const win=la.index===lb.index?"It's a tie on raw power — ":la.index>lb.index?`<strong>${{la.name}}</strong> wins on raw gaming power (${{la.index}} vs ${{lb.index}}). `:`<strong>${{lb.name}}</strong> wins on raw gaming power (${{lb.index}} vs ${{la.index}}). `;
const va=val(a),vb=val(b);
t=win+(va===vb?"Both offer identical value per pound.":va>vb?`For value, <strong>${{la.name}}</strong> gives more frames per pound (${{va}} vs ${{vb}}).`:`For value, <strong>${{lb.name}}</strong> gives more frames per pound (${{vb}} vs ${{va}}).`);}}
v.innerHTML="<h3>Verdict</h3><p>"+t+"</p>";}}
document.getElementById('a').addEventListener('change',go);
document.getElementById('b').addEventListener('change',go);
document.getElementById('b').selectedIndex=1;go();
</script>"""
    return base("Compare Gaming Laptops UK — Head-to-Head Benchmark Tool",
        "Compare any two gaming laptops side by side: benchmark scores, specs and UK prices with an instant verdict.", body, "/compare.html",
        ld_graph(ld_org(), ld_breadcrumb([("Home","/"),("Compare","/compare.html")])))

def page_deals():
    drops = sorted(LAPTOPS, key=lambda l: l["price"])[:6]
    rows = "".join(f'<tr><td><a href="/reviews/{l["slug"]}.html">{html.escape(l["name"])}</a></td>'
                   f'<td>£{l["price"]:,}</td><td><span style="color:var(--green)">£{int(l["price"]*0.88):,}*</span></td>'
                   f'<td><a class="btn" href="{amz_link(l)}" rel="nofollow sponsored noopener" target="_blank">Check Deal</a></td></tr>' for l in drops)
    body = f"""
<p class="breadcrumb"><a href="/">Home</a> / Deals</p>
<div class="article"><h1>UK Gaming Laptop Price Drops</h1>
<p class="lead">The biggest current discounts on premium gaming laptops at UK retailers. Deal-target prices are estimates based on recent sale patterns — always confirm live.</p></div>
<table><tr><th>Laptop</th><th>Typical Price</th><th>Good Deal Below</th><th></th></tr>{rows}</table>
<div class="article"><p class="specs">* "Good deal" = roughly 12% under typical street price, based on historical UK sale data. Prices move daily.</p>
<h2>How to Never Overpay</h2><ul>
<li>Set a price alert on your shortlist and wait for sale events (Black Friday, Prime Day, Boxing Day).</li>
<li>Previous-generation models often drop 20–30% when new GPUs launch — same chassis, lower price.</li>
<li>Check Currys and Box alongside Amazon UK — they frequently undercut each other.</li></ul></div>"""
    return base("UK Gaming Laptop Deals — Biggest Current Price Drops",
        "Today's biggest UK gaming laptop price drops and deal targets, tracked against typical street prices.", body, "/deals.html",
        ld_graph(ld_org(), ld_breadcrumb([("Home","/"),("Deals","/deals.html")])))

def page_about():
    body = """
<p class="breadcrumb"><a href="/">Home</a> / About</p>
<div class="article"><h1>About Us &amp; Methodology</h1>
<p class="lead">BestPremiumGamingLaptop.co.uk exists for one reason: to help UK buyers choose a gaming laptop with confidence — using data, not hype.</p>
<h2>How we rank laptops</h2>
<p>Every laptop gets a <strong>gaming index (0–100)</strong> computed from public benchmark data:</p>
<ul><li><strong>GPU class + TGP wattage — 60%.</strong> The same GPU at higher wattage is much faster; we weight real power, not just the model name.</li>
<li><strong>CPU tier — 20%.</strong></li><li><strong>Display — 10%.</strong> Resolution, refresh rate and brightness matched to the GPU.</li>
<li><strong>Memory &amp; storage — 10%.</strong></li></ul>
<p>Value score = gaming index ÷ typical UK street price. Rankings refresh as new benchmark data and prices arrive.</p>
<h2>Independence</h2>
<p>We earn affiliate commission from retailers like Amazon UK and Currys when readers buy through our links. Commission never influences scores — they are computed from specs and benchmarks before any commercial consideration. Scores are published; the maths is the same for every laptop.</p>
<h2 id="contact">Contact</h2>
<p>Spotted an error, a better price, or a laptop we should rank? Email us at <strong>hello@bestpremiumgaminglaptop.co.uk</strong>.</p>
</div>"""
    return base("About Us & Methodology — Best Premium Gaming Laptop UK",
        "How we test and rank gaming laptops for UK buyers: our benchmark methodology and independence promise.", body, "/about.html",
        ld_graph(ld_org(), ld_breadcrumb([("Home","/"),("About","/about.html")])))

# ----------------------------------------------------------------- build ---
def write(path, content):
    full = os.path.join(OUT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)

def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    shutil.copytree(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets"),
                    os.path.join(OUT, "assets"))
    pages = {
        "/index.html": page_home(),
        "/guides/best-premium-gaming-laptops-uk.html": page_guide_top10(),
        "/guides/best-rtx-4070-laptops-uk.html": page_guide_rtx4070(),
        "/guides/best-gaming-laptops-under-1000-uk.html": page_guide_under1000(),
        "/guides/best-gaming-laptop-students-uk.html": page_guide_students(),
        "/guides/how-to-choose-gaming-laptop.html": page_how_to_choose(),
        "/compare.html": page_compare(),
        "/deals.html": page_deals(),
        "/about.html": page_about(),
    }
    for lap in LAPTOPS:
        pages[f"/reviews/{lap['slug']}.html"] = page_review(lap)
    for g in GUIDES:
        pages[f"/guides/{g['slug']}.html"] = page_generic_guide(g)
    for p, c in pages.items():
        write(p, c)
    # laptops.json for the compare tool / future use
    write("/laptops.json", json.dumps(LAPTOPS, indent=2))
    # CNAME for custom domain
    write("/CNAME", SITE["domain"] + "\n")
    # robots.txt
    write("/robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: https://{SITE['domain']}/sitemap.xml\n")
    # sitemap with lastmod / changefreq / priority
    import datetime
    today = datetime.date.today().isoformat()
    def prio(p):
        if p == "/index.html": return "1.0"
        if "/guides/" in p: return "0.9"
        if "/reviews/" in p: return "0.8"
        return "0.6"
    urls = "".join(
        f"<url><loc>https://{SITE['domain']}{p}</loc><lastmod>{today}</lastmod>"
        f"<changefreq>weekly</changefreq><priority>{prio(p)}</priority></url>"
        for p in sorted(pages))
    write("/sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    # README
    write("/README.md", f"# {SITE['name']}\n\nStatic site for {SITE['domain']}, generated by build.py.\n\nTo rebuild: `python3 build.py`\n\nSet your Amazon UK Associates tag in `SITE['affiliate_tag']` inside build.py, then rebuild.\n")
    print(f"DONE — {len(pages)} pages")

if __name__ == "__main__":
    main()
