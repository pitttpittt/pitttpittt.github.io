import json,os
SITE="https://pitttpittt.github.io"
CODEUR="https://www.codeur.com/-ppit"
NAV=[("index.html","Accueil"),("realisations.html","Réalisations"),("montage-video.html","Montage vidéo"),("restaurant.html","Restaurant"),("artisan.html","Artisan"),("boutique.html","E-commerce"),("blog.html","Blog"),("application.html","Appli web"),("sites-wordpress.html","Sites WordPress")]
BANNER='<div class="demo-banner" role="note">Démo interactive — projet d’exemple. Données fictives : rien n’est envoyé ni payé.</div>'
def page(fn,title,desc,body,scripts=(),extra_head=""):
    nav="".join(f'<a href="{h}"{" class=on" if h==fn else ""}>{t}</a>' for h,t in NAV)
    sc="".join(f'<script src="{s}" defer></script>' for s in scripts)
    url=SITE+"/"+("" if fn=="index.html" else fn)
    html=f'''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/assets/img/og.jpg"><meta property="og:locale" content="fr_FR"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b1020"><link rel="icon" type="image/png" href="assets/img/ppit-logo.png"><link rel="apple-touch-icon" href="assets/img/ppit-logo.png">
<link rel="stylesheet" href="assets/css/style.css">{extra_head}
</head><body>
<header class="top"><div class="wrap"><a class="logo" href="index.html"><img src="assets/img/ppit-logo.png" alt="PPIT" width="40" height="40"><span>PPIT</span></a>
<button class="burger" aria-label="Menu" aria-expanded="false">☰</button><nav class="nav" aria-label="Navigation principale">{nav}<a class="btn sm" href="{CODEUR}" target="_blank" rel="noopener">Me contacter via Codeur</a></nav></div></header>
<main>{body}</main>
<footer class="foot"><div class="wrap"><div><strong style="color:#fff">PPIT</strong> — montage vidéo, design graphique et sites WordPress, 100 % à distance.<br>Les démos de ce site sont des projets d’exemple, conçus pour montrer mon savoir-faire.</div>
<div><a href="{CODEUR}" target="_blank" rel="noopener">Me contacter via Codeur</a> · <a href="mentions-legales.html">Mentions légales</a><br>© <span id="year">2026</span></div></div></footer>
<script src="assets/js/common.js" defer></script>{sc}
</body></html>'''
    open(fn,"w").write(html)

def cta(t="Un projet en tête ?",s="Décrivez votre besoin sur Codeur : je réponds rapidement avec une proposition claire, un prix fixe et un délai."):
    return f'<section><div class="wrap"><div class="cta-band"><h2>{t}</h2><p>{s}</p><a class="btn light" href="{CODEUR}" target="_blank" rel="noopener">Me contacter via Codeur</a></div></div></section>'

# ---------- VIDEO DEMO
VIDEO_SRC="assets/video/top5-trampoline.mp4"
VIDEO_POSTER="assets/img/top5-trampoline.jpg"
VIDEO_CREDIT='<p class="credit">Musique : « Funky Chunk » – Kevin MacLeod (incompetech.com), licence <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener">CC BY 4.0</a>.</p>'
VIDEO_DESC='Montage rythmé, calé sur la musique : transitions (glitch, whip pan, zoom punch), ralentis avec arrêt sur image, rangs animés, légendes façon TikTok et sound design. Réalisé à partir de 5 rushs de téléphone fournis par le client, au format vertical 9:16.'
VIDEO_BANNER='<div class="demo-banner" role="note">Démo — projet d’exemple.</div>'
def video_player():
    return f'''<div class="video-frame">
<video class="video-vert" controls playsinline preload="metadata" poster="{VIDEO_POSTER}" width="720" height="1280">
<source src="{VIDEO_SRC}" type="video/mp4">
Désolé, votre navigateur ne peut pas lire cette vidéo.
</video>
{VIDEO_CREDIT}
</div>'''


# ---------- HOME
demos=[("restaurant.html","restaurant-plat.jpg","Restaurant","Carte filtrable et réservation en ligne avec confirmation."),
("artisan.html","artisan-cuisine.jpg","Artisan","Calculateur de devis en direct et galerie de réalisations."),
("boutique.html","immobilier-cles.jpg","E-commerce","Catalogue, panier persistant, code promo et tunnel de commande."),
("blog.html","consultant-hero.jpg","Blog","Articles en Markdown, recherche et filtres par thème."),
("application.html","consultant-tableau-de-bord.jpg","Application web","Caisse + stock : CRUD, tickets, tableau de bord et graphiques.")]
cards="".join(f'<a class="card link" href="{h}"><img class="cover" src="assets/img/{i}" alt="Démo interactive {t} — projet d’exemple" loading="lazy" width="960" height="600"><span class="tag">Projet d’exemple</span><h3>{t}</h3><p class="muted">{d}</p><span style="margin-top:auto;font-weight:600">Tester la démo →</span></a>' for h,i,t,d in demos)
services=[("🎬","Montage vidéo","Montages courts et longs (TikTok, Shorts, films, extraits) : rythme, transitions, légendes et sound design. <a href=\"montage-video.html\">Voir un exemple →</a>"),
("✨","Motion design","Habillages, titres animés et transitions pour vos vidéos, présentations et réseaux sociaux."),
("🎨","Flyers et logos","Identités visuelles, logos, flyers, cartes et déclinaisons print ou web, prêts à imprimer ou à publier."),
("🌐","Sites WordPress","Site vitrine clair, rapide et facile à modifier : pages, formulaire, SEO de base, mentions légales."),
("📘","Mise en page KDP","Couvertures et intérieurs de livres prêts pour Amazon KDP, avec une mise en page soignée."),
("🤖","Automatisation IA","Relier vos outils (formulaires, tableurs, emails, CRM) et automatiser les tâches répétitives.")]
sv="".join(f'<div class="card"><div class="ico">{i}</div><h3>{t}</h3><p class="muted">{d}</p></div>' for i,t,d in services)
home=f'''<section class="hero"><div class="wrap"><span class="pill">Freelance · 100 % à distance · France</span>
<h1>Montage vidéo, design graphique<br>et sites WordPress.</h1>
<p class="lead">PPIT réalise des montages vidéo, du motion design, des flyers et des logos, des sites WordPress, de la mise en page KDP et de l’automatisation IA. Prix fixes annoncés à l’avance, livraisons par étapes et suivi par écrit.</p>
<div class="ctas"><a class="btn" href="{CODEUR}" target="_blank" rel="noopener">Me contacter via Codeur</a><a class="btn ghost" href="#demos">Voir les démos</a></div></div></section>
<section><div class="wrap"><div class="sec-head"><h2>Ce que je fais</h2><p class="muted">Des projets livrés étape par étape, testables avant validation.</p></div><div class="grid g3">{sv}</div></div></section>
<section class="dark" id="demos"><div class="wrap"><div class="sec-head"><h2>Démos fonctionnelles par domaine</h2><p class="muted">Ce ne sont pas des maquettes : chaque démo fonctionne vraiment dans votre navigateur (formulaires, panier, calculs, graphiques). Ce sont des <strong>projets d’exemple</strong>, avec des données fictives.</p></div><div class="grid g3" style="color:var(--ink)">{cards}</div></div></section>
<section id="montage-video"><div class="wrap"><div class="video-demo"><div>
<span class="tag">Démo — projet d’exemple</span>
<h2>Montage vidéo court — Top 5 TikTok / Shorts</h2>
<p>{VIDEO_DESC}</p>
<p><a class="btn" href="montage-video.html">Ouvrir la page de la vidéo</a></p>
</div>
{video_player()}
</div></div></section>
<section><div class="wrap split"><div><h2>Une réalisation concrète : l’audit du site de L’Accord Parfait</h2><p>J’ai réalisé l’audit du site de <strong>L’Accord Parfait</strong> : performance, SEO, sécurité, accessibilité et conversion, mesurés avec Lighthouse et une analyse page par page.</p>
<p>Résultat : un score de synthèse de <strong>51/100</strong>, une page d’accueil de 11,4 Mo sur mobile et un plan d’actions en 5 priorités.</p><p><a class="btn" href="realisations.html">Voir l’audit</a> <a class="btn ghost" href="assets/docs/audit-laccord-parfait.pdf" download style="color:var(--acc)">Télécharger le PDF</a></p></div>
<div class="shot"><img src="assets/img/audit-page-01.jpg" alt="Première page du rapport d’audit" loading="lazy" data-zoom></div></div></section>
<section style="background:#fff"><div class="wrap"><div class="sec-head"><h2>Ma façon de travailler</h2></div><div class="grid g4">
<div><h3>1. Devis clair</h3><p class="muted">Prix fixe, périmètre écrit, délai annoncé. Pas de surprise.</p></div>
<div><h3>2. Livraison par étapes</h3><p class="muted">Vous testez sur une version de démonstration avant de valider.</p></div>
<div><h3>3. Paiement à la validation</h3><p class="muted">Chaque étape est réglée quand elle est livrée et validée.</p></div>
<div><h3>4. Tout à distance</h3><p class="muted">Échanges écrits, suivi régulier, où que vous soyez.</p></div></div></div></section>
{cta()}'''
JSONLD='<script type="application/ld+json">{"@context":"https://schema.org","@type":"ProfessionalService","name":"PPIT","url":"'+SITE+'/","description":"Montage vidéo, motion design, flyers et logos, sites WordPress, mise en page KDP et automatisation IA.","areaServed":"FR","sameAs":["'+CODEUR+'"]}</script>'
page("index.html","PPIT — Montage vidéo, design graphique et sites WordPress","Montage vidéo, motion design, flyers et logos, sites WordPress, mise en page KDP et automatisation IA. Réalisations et démos, 100 % à distance.",home,extra_head=JSONLD)

# ---------- RESTAURANT
rest=f'''<section class="hero sub" style="background:linear-gradient(rgba(11,16,32,.65),rgba(11,16,32,.8)),url(assets/img/restaurant-hero.jpg) center/cover"><div class="wrap">{BANNER}
<h1>Le Bistrot des Halles</h1><p class="lead">Démo de site restaurant : carte filtrable et réservation en ligne qui fonctionne vraiment (validation, confirmation, liste des réservations enregistrée dans votre navigateur).</p>
<div class="ctas"><a class="btn" href="#carte">Voir la carte</a><a class="btn ghost" href="#reserver">Réserver une table</a></div></div></section>
<section id="carte"><div class="wrap"><div class="sec-head"><h2>La carte</h2><p class="muted">Filtrez par catégorie, régime ou mot-clé.</p></div>
<div class="card" style="margin-bottom:20px"><div class="row" style="align-items:end"><div><label for="q">Rechercher un plat</label><input id="q" type="search" placeholder="ex. fromage, chocolat…"></div>
<div><label>Régime</label><label style="font-weight:400;display:inline-flex;gap:6px;margin-right:12px"><input type="checkbox" id="veg" style="width:auto"> Végétarien</label><label style="font-weight:400;display:inline-flex;gap:6px"><input type="checkbox" id="gf" style="width:auto"> Sans gluten</label></div></div>
<div id="cats" style="margin-top:12px"></div></div>
<div id="menu" class="grid g3"></div><p id="menu-empty" class="empty" hidden>Aucun plat ne correspond à ces filtres.</p></div></section>
<section style="background:#fff" id="reserver"><div class="wrap split"><div><h2>Réserver une table</h2><p class="muted">Ouvert du mardi au dimanche, 12h–14h et 19h–22h. Fermé le lundi. Groupes jusqu’à 12 personnes.</p>
<form id="resa" class="card" novalidate>
<div class="row"><div class="field"><label for="r-nom">Nom</label><input id="r-nom" autocomplete="name"><div class="err"></div></div><div class="field"><label for="r-mail">E-mail</label><input id="r-mail" type="email" autocomplete="email"><div class="err"></div></div></div>
<div class="row"><div class="field"><label for="r-date">Date</label><input id="r-date" type="date"><div class="err"></div></div><div class="field"><label for="r-heure">Heure</label><select id="r-heure"></select><div class="err"></div></div><div class="field"><label for="r-pers">Personnes</label><input id="r-pers" type="number" min="1" max="12" value="2"><div class="err"></div></div></div>
<div class="field"><label for="r-note">Remarque (allergies, occasion…)</label><textarea id="r-note" rows="2"></textarea></div>
<button class="btn" type="submit">Confirmer la réservation</button><div id="resa-msg" aria-live="polite"></div></form></div>
<div><h3>Mes réservations <span class="muted small">(enregistrées dans ce navigateur)</span></h3><div id="list" class="card"></div>
<div class="gallery" style="margin-top:20px"><img src="assets/img/restaurant-terrasse.jpg" alt="Terrasse" loading="lazy"><img src="assets/img/restaurant-chef.jpg" alt="En cuisine" loading="lazy"><img src="assets/img/restaurant-bar.jpg" alt="Le bar" loading="lazy"></div></div></div></section>
{cta("Vous voulez ce type de site pour votre restaurant ?","Carte modifiable, réservation, avis, horaires et fiche Google bien renseignée : je l’adapte à votre établissement.")}'''
page("restaurant.html","Démo site restaurant — carte filtrable et réservation en ligne | PPIT","Démo interactive (projet d’exemple) de site restaurant : carte filtrable par catégorie et régime, formulaire de réservation fonctionnel avec validation et confirmation.",rest,["assets/js/restaurant.js"])

# ---------- ARTISAN
art=f'''<section class="hero sub" style="background:linear-gradient(rgba(11,16,32,.6),rgba(11,16,32,.85)),url(assets/img/artisan-hero.jpg) center/cover"><div class="wrap">{BANNER}
<h1>Atelier Bois & Sens — menuiserie sur mesure</h1><p class="lead">Démo de site artisan : services, estimation de devis qui se met à jour en direct, et galerie de réalisations.</p><div class="ctas"><a class="btn" href="#devis">Estimer mon projet</a></div></div></section>
<section><div class="wrap"><div class="sec-head"><h2>Nos services</h2></div><div class="grid g4" id="svc"></div></div></section>
<section style="background:#fff" id="devis"><div class="wrap split"><form id="calc" class="card" novalidate><h2>Estimation de devis</h2>
<div class="field"><label for="c-type">Type de travaux</label><select id="c-type"></select></div>
<div class="row"><div class="field"><label for="c-qte" id="c-unit">Quantité</label><input id="c-qte" type="number" min="1" value="3" step="0.5"></div><div class="field"><label for="c-fin">Finition</label><select id="c-fin"><option value="1">Standard</option><option value="1.25">Premium (essences nobles)</option><option value="1.55">Haut de gamme (sur mesure intégral)</option></select></div></div>
<div class="field"><label>Options</label><div id="c-opts"></div></div>
<div class="row"><div class="field"><label for="c-km">Distance de l’atelier (km)</label><input id="c-km" type="range" min="0" max="80" value="15"><div class="small muted"><span id="c-kmv">15</span> km</div></div><div class="field"><label for="c-urg">Délai</label><select id="c-urg"><option value="1">Normal (6–8 semaines)</option><option value="1.12">Rapide (3–4 semaines, +12 %)</option></select></div></div>
<hr style="border:0;border-top:1px solid var(--line);margin:16px 0"><h3>Recevoir le devis détaillé</h3>
<div class="row"><div class="field"><label for="c-nom">Nom</label><input id="c-nom"><div class="err"></div></div><div class="field"><label for="c-mail">E-mail</label><input id="c-mail" type="email"><div class="err"></div></div></div>
<button class="btn" type="submit">Demander mon devis</button><div id="c-msg" aria-live="polite"></div></form>
<div class="card" style="position:sticky;top:84px"><p class="muted small" style="margin:0">Estimation indicative</p><div class="kpi" id="c-total" aria-live="polite">—</div><p class="muted small" id="c-range"></p><table class="tbl" id="c-detail"></table></div></div></section>
<section><div class="wrap"><div class="sec-head"><h2>Réalisations (photos d’illustration)</h2></div><div class="gallery">
<img src="assets/img/artisan-cuisine.jpg" alt="Cuisine sur mesure"><img src="assets/img/artisan-escalier.jpg" alt="Escalier bois"><img src="assets/img/artisan-terrasse.jpg" alt="Terrasse bois"><img src="assets/img/artisan-bibliotheque.jpg" alt="Bibliothèque intégrée"><img src="assets/img/artisan-atelier.jpg" alt="L’atelier"></div></div></section>
{cta("Un site qui transforme les visiteurs en demandes de devis","Calculateur adapté à vos tarifs, galerie, avis clients et formulaire : vos prospects arrivent avec un budget déjà en tête.")}'''
page("artisan.html","Démo site artisan — calculateur de devis en direct | PPIT","Démo interactive (projet d’exemple) de site artisan : services, estimation de devis en temps réel, galerie de réalisations.",art,["assets/js/artisan.js"])

# ---------- BOUTIQUE
shop=f'''<section class="hero sub"><div class="wrap">{BANNER}<h1>Maison Comptoir — épicerie fine en ligne</h1><p class="lead">Démo e-commerce : catalogue filtrable, panier persistant (quantités, total, livraison, code promo <code style="background:rgba(255,255,255,.15);padding:1px 6px;border-radius:5px">DEMO10</code>) et étape de commande. Aucun paiement réel.</p></div></section>
<section><div class="wrap split" style="grid-template-columns:1.6fr 1fr"><div><div class="card" style="margin-bottom:18px;display:flex;gap:12px;flex-wrap:wrap;align-items:end"><div style="flex:1;min-width:180px"><label for="s-q">Rechercher</label><input id="s-q" type="search" placeholder="Produit…"></div><div><label for="s-sort">Trier</label><select id="s-sort"><option value="pop">Popularité</option><option value="asc">Prix croissant</option><option value="desc">Prix décroissant</option></select></div><div id="s-cats" style="width:100%"></div></div>
<div id="products" class="grid g3"></div></div>
<aside><div class="card" style="position:sticky;top:84px" id="cart-box"><h2 style="font-size:1.3rem">🛒 Panier <span id="cart-count" class="tag">0</span></h2><div id="cart"></div></div></aside></div></section>
<section style="background:#fff" id="checkout" hidden><div class="wrap" style="max-width:760px"><h2>Commande (étape de démonstration)</h2><div class="demo-banner">Paiement désactivé : cette étape simule une commande. Aucune carte n’est demandée, rien n’est débité ni envoyé.</div>
<form id="co" class="card" novalidate><div class="row"><div class="field"><label for="co-nom">Nom complet</label><input id="co-nom" autocomplete="name"><div class="err"></div></div><div class="field"><label for="co-mail">E-mail</label><input id="co-mail" type="email"><div class="err"></div></div></div>
<div class="field"><label for="co-adr">Adresse</label><input id="co-adr" autocomplete="street-address"><div class="err"></div></div>
<div class="row"><div class="field"><label for="co-cp">Code postal</label><input id="co-cp" inputmode="numeric" maxlength="5"><div class="err"></div></div><div class="field"><label for="co-ville">Ville</label><input id="co-ville"><div class="err"></div></div><div class="field"><label for="co-liv">Livraison</label><select id="co-liv"><option value="colissimo">Colissimo (48 h)</option><option value="relais">Point relais</option></select></div></div>
<p id="co-sum" class="muted"></p><button class="btn" type="submit">Valider la commande de démonstration</button></form><div id="co-msg" aria-live="polite"></div></div></section>
{cta("Une boutique en ligne qui vend vraiment","WooCommerce ou Shopify, paiement sécurisé (Stripe, PayPal), livraison, emails automatiques et suivi des commandes.")}'''
page("boutique.html","Démo e-commerce — catalogue, panier et commande | PPIT","Démo interactive (projet d’exemple) de boutique en ligne : catalogue filtrable, panier persistant avec quantités et code promo, étape de commande simulée sans paiement.",shop,["assets/js/boutique.js"])

# ---------- BLOG
blog=f'''<section class="hero sub"><div class="wrap">{BANNER}<h1 id="b-title">Le blog</h1><p class="lead" id="b-lead">Démo de blog piloté par un fichier JSON et des articles en Markdown : recherche, filtres par thème et pages d’articles.</p></div></section>
<section><div class="wrap"><div id="b-list"><div class="card" style="margin-bottom:20px"><label for="b-q">Rechercher un article</label><input id="b-q" type="search" placeholder="ex. WordPress, vitesse…"><div id="b-tags" style="margin-top:12px"></div></div><div id="b-posts" class="grid g3"></div><p id="b-empty" class="empty" hidden>Aucun article trouvé.</p></div>
<article id="b-article" class="card prose" hidden style="margin:0 auto"></article></div></section>
{cta()}'''
page("blog.html","Démo blog — articles Markdown, recherche et thèmes | PPIT","Démo interactive (projet d’exemple) de blog : liste d’articles, recherche, filtres par thème et pages d’articles générées depuis du Markdown.",blog,["assets/js/blog.js"])

# ---------- APP
app=f'''<section class="hero sub"><div class="wrap">{BANNER}<h1>CaissePro — caisse & stock</h1><p class="lead">Démo d’application web : encaissement, gestion des produits (ajout, modification, suppression), stock mis à jour à chaque vente, tableau de bord avec graphiques et export CSV. Les données restent dans votre navigateur.</p></div></section>
<section><div class="wrap">
<div class="grid g4" style="margin-bottom:22px"><div class="card"><div class="muted small">Chiffre d’affaires</div><div class="kpi" id="k-ca">0 €</div></div><div class="card"><div class="muted small">Tickets</div><div class="kpi" id="k-n">0</div></div><div class="card"><div class="muted small">Panier moyen</div><div class="kpi" id="k-avg">0 €</div></div><div class="card"><div class="muted small">Produits en alerte stock</div><div class="kpi" id="k-low">0</div></div></div>
<div class="split" style="grid-template-columns:1.4fr 1fr"><div class="card"><h2 style="font-size:1.3rem">Encaisser</h2><div id="pos" class="grid" style="grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:10px"></div></div>
<div class="card"><h2 style="font-size:1.3rem">Ticket en cours</h2><div id="ticket"></div><div class="row" style="margin-top:10px"><div><label for="pay">Paiement</label><select id="pay"><option>Carte</option><option>Espèces</option><option>Chèque</option></select></div></div><div style="display:flex;gap:8px;margin-top:12px;flex-wrap:wrap"><button class="btn" id="checkout-btn">Encaisser</button><button class="btn ghost" id="clear-btn" style="color:var(--muted)">Vider</button></div></div></div>
<div class="grid g2" style="margin-top:22px"><div class="card"><h3>Ventes par jour (7 derniers jours)</h3><div class="chart-box"><canvas id="ch-days" aria-label="Graphique des ventes par jour"></canvas></div></div><div class="card"><h3>Répartition par catégorie</h3><div class="chart-box"><canvas id="ch-cats" aria-label="Graphique par catégorie"></canvas></div></div></div>
<div class="card" style="margin-top:22px"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px"><h2 style="font-size:1.3rem;margin:0">Produits</h2><div style="display:flex;gap:8px;flex-wrap:wrap"><button class="btn sm" id="add-btn">+ Ajouter</button><button class="btn sm ghost" id="csv-btn" style="color:var(--acc)">Exporter les ventes (CSV)</button><button class="btn sm ghost" id="reset-btn" style="color:var(--bad)">Réinitialiser la démo</button></div></div>
<form id="pform" hidden class="row" style="margin-top:14px;align-items:end" novalidate><input type="hidden" id="p-id"><div><label for="p-name">Nom</label><input id="p-name" required></div><div><label for="p-cat">Catégorie</label><input id="p-cat" list="catlist" required><datalist id="catlist"></datalist></div><div><label for="p-price">Prix (€)</label><input id="p-price" type="number" step="0.01" min="0" required></div><div><label for="p-stock">Stock</label><input id="p-stock" type="number" min="0" step="1" required></div><div style="display:flex;gap:6px"><button class="btn sm" type="submit">Enregistrer</button><button class="btn sm ghost" type="button" id="p-cancel" style="color:var(--muted)">Annuler</button></div></form>
<div style="overflow:auto;margin-top:12px"><table class="tbl" id="ptable"></table></div></div>
<div class="card" style="margin-top:22px"><h2 style="font-size:1.3rem">Derniers tickets</h2><div style="overflow:auto"><table class="tbl" id="sales"></table></div></div>
</div></section>
{cta("Besoin d’une application métier ?","Caisse, réservation, gestion de stock, espace client, back-office : développée en Laravel ou React, livrée par étapes testables.")}'''
page("application.html","Démo application web — caisse, stock et tableau de bord | PPIT","Démo interactive (projet d’exemple) d’application web : caisse enregistreuse, gestion des produits (CRUD), stock, tableau de bord et graphiques Chart.js, export CSV.",app,["https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js","assets/js/app.js"])

# ---------- REALISATIONS
scores=[("Performance",36,"Lighthouse mobile (bureau : 70)"),("SEO on-page",48,"Lighthouse SEO technique : 92"),("SEO local",62,"Fiche Google active, site peu armé"),("Accessibilité",72,"Lighthouse : 89, zoom bloqué"),("Sécurité",58,"HTTPS oui, en-têtes absents"),("Mobile / UX",50,"Responsive, mais zoom et poids"),("Contenu",42,"Pages vides ou datées"),("Conversion",40,"Formulaire présent, peu actionnable")]
def col(v): return "var(--bad)" if v<50 else ("var(--warn)" if v<70 else "var(--ok)")
sc="".join(f'<div class="card score"><span class="muted small">{n}</span><b>{v}<small class="muted" style="font-size:.9rem">/100</small></b><div class="bar"><i style="width:{v}%;background:{col(v)}"></i></div><span class="small muted">{d}</span></div>' for n,v,d in scores)
flaws=[("c","Page d’accueil trop lourde","11,4 Mo et 185 requêtes sur mobile ; la vidéo YouTube du diaporama pèse à elle seule plus de 7 Mo. LCP 6,2 s.","Remplacer la vidéo par une image compressée, alléger les scripts : objectif < 2 Mo."),
("c","Contact peu actionnable","Téléphone et e-mail non cliquables, pas de carte ni d’itinéraire, bandeau Meta qui recouvre le formulaire.","Liens tel:/mailto:, carte, horaires complets, bandeau de consentement repositionné."),
("i","SEO incomplet","Aucune meta description sur les 9 pages auditées, pas de données structurées Restaurant / LocalBusiness, pas d’Open Graph.","Meta description unique par page, H1 sur l’accueil, schema.org LocalBusiness, sitemap déclaré dans robots.txt."),
("i","Contenu daté","Page « Épicerie fine » vide, agenda figé sur un événement de janvier 2024, dimanche absent des horaires.","Remplir et mettre à jour les pages, relire les textes."),
("i","Conformité et sécurité","Consentement limité au Pixel Meta (pas Analytics, YouTube, reCAPTCHA), en-têtes de sécurité absents.","Consentement global, page confidentialité, en-têtes HTTP de sécurité.")]
fl="".join(f'<tr><td><span class="sev {s}">{"Critique" if s=="c" else "Important"}</span></td><td><strong>{t}</strong><br><span class="muted small">{d}</span></td><td class="small">{r}</td></tr>' for s,t,d,r in flaws)
rea=f'''<section class="hero sub"><div class="wrap"><span class="pill">Réalisations réelles</span><h1>Réalisations</h1><p class="lead">Des travaux réels, présentés avec des chiffres mesurés. Aucun résultat n’est inventé.</p></div></section>
<section><div class="wrap"><div class="split"><div><span class="tag">Audit de site web</span> <span class="tag">13 novembre 2026</span><h2>Audit du site de L’Accord Parfait</h2>
<p>J’ai réalisé l’audit du site de <strong>L’Accord Parfait</strong> (<a href="https://www.laccordparfait53.fr/" target="_blank" rel="noopener">voir le site</a>) : 8 pages + 1 article, en-têtes HTTP, certificat, sitemaps, formulaire, mesures Lighthouse mobile et bureau.</p>
<p>Score de synthèse : <strong style="font-size:1.4rem">51/100</strong> (moyenne pondérée, mobile prioritaire).</p>
<p><a class="btn" href="assets/docs/audit-laccord-parfait.pdf" download>Télécharger le rapport PDF (10 pages)</a></p>
<p class="small muted">Version publique du rapport : les informations internes (comptes, coordonnées) ont été retirées.</p></div>
<div class="grid" style="grid-template-columns:1fr 1fr;gap:12px"><img src="assets/img/audit-page-01.jpg" alt="Rapport d’audit, page 1" data-zoom style="border-radius:8px;border:1px solid var(--line);cursor:zoom-in"><img src="assets/img/audit-page-02.jpg" alt="Rapport d’audit, page 2" data-zoom style="border-radius:8px;border:1px solid var(--line);cursor:zoom-in"></div></div>
<h3 style="margin-top:40px">Scores mesurés (avant correction)</h3><div class="grid g4">{sc}</div>
<h3 style="margin-top:40px">Principaux défauts trouvés et corrections recommandées</h3><div class="card" style="overflow:auto"><table class="tbl"><thead><tr><th>Gravité</th><th>Constat mesuré</th><th>Correction recommandée</th></tr></thead><tbody>{fl}</tbody></table></div>
<div class="grid g2" style="margin-top:30px"><div class="card"><h3>Avant</h3><div class="shot"><img src="assets/img/audit-accueil-desktop.jpg" alt="Page d’accueil du site avant correction" loading="lazy" data-zoom></div><p class="small muted">Accueil, capture du 13 novembre 2026.</p></div>
<div class="card" style="display:flex;flex-direction:column;justify-content:center;text-align:center;background:#f8fafc"><h3>Après correction</h3><p class="kpi" style="color:var(--warn)">En cours</p><p class="muted">Les corrections sont en préparation. Les nouveaux scores seront publiés ici une fois mesurés, pas avant.</p></div></div>
</div></section>
<section style="background:#fff"><div class="wrap"><div class="sec-head"><h2>Kit vitrine WordPress maison</h2><p class="muted">Un thème WordPress léger (100 % Gutenberg, sans extension payante) avec 6 modèles prêts à personnaliser : artisan, restaurant, consultant, coiffure, santé, immobilier. Il me permet de livrer un site vitrine de 5 à 7 pages rapidement. Les entreprises affichées sont fictives.</p></div><a class="btn" href="sites-wordpress.html">Voir les modèles</a></div></section>
{cta("Vous voulez le même audit pour votre site ?","Rapport PDF chiffré, défauts classés par gravité et plan d’actions concret.")}'''
page("realisations.html","Réalisations — audit de site L’Accord Parfait et kit WordPress | PPIT","Réalisations de PPIT : audit du site de L’Accord Parfait (performance, SEO, sécurité, conversion) avec rapport PDF, kit vitrine WordPress.",rea)

# ---------- WP gallery
vs=[("restaurant","Restaurant","accueil","carte"),("artisan","Artisan","accueil","services"),("consultant","Consultant","accueil","services"),("coiffure","Coiffure / esthétique","accueil","prestations"),("sante","Santé / bien-être","accueil","osteopathie"),("immobilier","Immobilier","accueil","nos-biens")]
wg="".join(f'<div class="card"><h3>{t}</h3><div class="grid" style="grid-template-columns:1fr 1fr;gap:10px"><img src="assets/img/wp-{v}-{a}.jpg" alt="Modèle {t}, accueil" loading="lazy" data-zoom style="border-radius:8px;border:1px solid var(--line);aspect-ratio:3/4;object-fit:cover;object-position:top;cursor:zoom-in"><img src="assets/img/wp-{v}-{b}.jpg" alt="Modèle {t}, page intérieure" loading="lazy" data-zoom style="border-radius:8px;border:1px solid var(--line);aspect-ratio:3/4;object-fit:cover;object-position:top;cursor:zoom-in"></div></div>' for v,t,a,b in vs)
wp=f'''<section class="hero sub"><div class="wrap">{BANNER.replace("Données fictives : rien n’est envoyé ni payé.","Entreprises et textes fictifs.")}<h1>Modèles de sites WordPress</h1><p class="lead">Six modèles issus de mon kit vitrine WordPress : thème bloc léger, pages légales incluses, formulaire de contact, responsive. Chaque modèle se personnalise à votre activité (textes, photos, couleurs).</p></div></section>
<section><div class="wrap"><div class="grid g2">{wg}</div><p class="muted small" style="margin-top:20px">Cliquez sur une capture pour l’agrandir.</p></div></section>{cta()}'''
page("sites-wordpress.html","Modèles de sites WordPress — kit vitrine | PPIT","Six modèles de sites vitrines WordPress (restaurant, artisan, consultant, coiffure, santé, immobilier) prêts à personnaliser.",wp)

# ---------- MONTAGE VIDEO
vidpage=f'''<section class="hero sub"><div class="wrap">{VIDEO_BANNER}
<span class="tag">Démo — projet d’exemple</span>
<h1>Montage vidéo court — Top 5 TikTok / Shorts</h1>
<p class="lead">{VIDEO_DESC}</p>
</div></section>
<section id="montage-video"><div class="wrap"><div class="video-demo"><div>
<h2>La vidéo</h2>
<p>Format vertical 9:16, pensé pour TikTok et YouTube Shorts. Le filigrane « PREVIEW – PPIT » reste visible sur cette version d’exemple.</p>
<p class="muted">À partir de rushs filmés au téléphone, montés sur une musique libre de droits.</p>
</div>
{video_player()}
</div></div></section>
{cta("Un montage court pour vos réseaux ?","Je monte vos rushs en vidéos TikTok / Shorts, avec un rythme calé sur la musique, des transitions et un habillage à votre image.")}'''
page("montage-video.html","Montage vidéo court — Top 5 TikTok / Shorts | PPIT","Démo — projet d’exemple : montage vidéo court au format vertical 9:16 (TikTok / Shorts), calé sur la musique, avec transitions, ralentis et légendes.",vidpage)

# ---------- legal
leg=f'''<section class="hero sub"><div class="wrap"><h1>Mentions légales</h1></div></section><section><div class="wrap prose card">
<h2>Éditeur</h2><p>PPIT. Contact : <a href="{CODEUR}" target="_blank" rel="noopener">via Codeur.com / message</a>.</p>
<h2>Hébergement</h2><p>GitHub Pages — GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</p>
<h2>Démonstrations</h2><p>Les démos (restaurant, artisan, boutique, blog, application) sont des exemples fictifs. Les noms d’entreprises, produits, prix et articles n’existent pas. Aucune donnée saisie n’est envoyée : tout reste dans le stockage local de votre navigateur (localStorage), que vous pouvez effacer à tout moment. La page « Montage vidéo » présente un projet d’exemple réalisé à partir de rushs fournis pour une démonstration.</p>
<h2>Données personnelles et cookies</h2><p>Ce site n’utilise ni cookie publicitaire ni outil de mesure d’audience. La page « Application web » charge la bibliothèque Chart.js depuis le CDN jsDelivr.</p>
<h2>Crédits</h2><p>Photos d’illustration issues de mon kit WordPress de démonstration. Musique de la vidéo d’exemple : « Funky Chunk » – Kevin MacLeod (incompetech.com), licence <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener">CC BY 4.0</a>.</p></div></section>'''
page("mentions-legales.html","Mentions légales | PPIT","Mentions légales du site de PPIT.",leg)

pages=[h for h,_ in NAV]+["mentions-legales.html"]
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f'<url><loc>{SITE}/{"" if p=="index.html" else p}</loc></url>' for p in pages)+'</urlset>\n')
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
open(".nojekyll","w").write("")
open("404.html","w").write(open("index.html").read())
print("built")
