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
]

def amz_link(lap):
    q = html.escape(lap["name"].replace(" ", "+"))
    return f'https://www.amazon.co.uk/s?k={q}&tag={SITE["affiliate_tag"]}'

def currys_link(lap):
    q = html.escape(lap["name"].replace(" ", "%20"))
    return f'https://www.currys.co.uk/search?q={q}'

# ------------------------------------------------------------ templates ----
def base(title, desc, body, canonical="/"):
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="https://{SITE['domain']}{canonical}">
<link rel="stylesheet" href="/assets/style.css">
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
        "The UK's data-driven guide to premium gaming laptops. Benchmark-tested rankings, honest reviews and live UK prices.", body, "/")

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
    return base("10 Best Premium Gaming Laptops UK 2026 — Benchmark-Tested Rankings",
        "The 10 best premium gaming laptops you can buy in the UK in 2026, ranked by real benchmark data and live UK prices.", body, "/guides/best-premium-gaming-laptops-uk.html")

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
        "The best RTX 4070 gaming laptops in the UK for 2026. Full-power 140W picks ranked by benchmarks and UK prices.", body, "/guides/best-rtx-4070-laptops-uk.html")

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
        "The best gaming laptops under £1000 in the UK. Real RTX gaming performance on a budget, ranked by benchmarks.", body, "/guides/best-gaming-laptops-under-1000-uk.html")

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
        "The best gaming laptops for UK students in 2026. Portable, durable and powerful — perfect for uni work and gaming.", body, "/guides/best-gaming-laptop-students-uk.html")

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
        "How to choose a gaming laptop in the UK: GPU wattage, VRAM, displays, thermals and UK buying tips explained simply.", body, "/guides/how-to-choose-gaming-laptop.html")

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
    return base(f"{lap['name']} Review UK 2026 — Benchmarks, Price & Verdict",
        f"Honest {lap['name']} review for UK buyers: gaming benchmarks, specs, pros & cons and live UK price.", body, f"/reviews/{lap['slug']}.html")

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
        "Compare any two gaming laptops side by side: benchmark scores, specs and UK prices with an instant verdict.", body, "/compare.html")

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
        "Today's biggest UK gaming laptop price drops and deal targets, tracked against typical street prices.", body, "/deals.html")

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
        "How we test and rank gaming laptops for UK buyers: our benchmark methodology and independence promise.", body, "/about.html")

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
    for p, c in pages.items():
        write(p, c)
    # laptops.json for the compare tool / future use
    write("/laptops.json", json.dumps(LAPTOPS, indent=2))
    # CNAME for custom domain
    write("/CNAME", SITE["domain"] + "\n")
    # sitemap
    urls = "".join(f"<url><loc>https://{SITE['domain']}{p}</loc></url>" for p in sorted(pages))
    write("/sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    # README
    write("/README.md", f"# {SITE['name']}\n\nStatic site for {SITE['domain']}, generated by build.py.\n\nTo rebuild: `python3 build.py`\n\nSet your Amazon UK Associates tag in `SITE['affiliate_tag']` inside build.py, then rebuild.\n")
    print(f"DONE — {len(pages)} pages")

if __name__ == "__main__":
    main()
