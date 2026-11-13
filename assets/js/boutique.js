(function(){
var $=function(s){return document.querySelector(s)};
var P=[{id:1,n:"Coffret apéritif",c:"Coffrets",p:39.9,e:"🧺",pop:9,bg:"#fde68a"},{id:2,n:"Miel de châtaignier 250 g",c:"Épicerie",p:8.5,e:"🍯",pop:7,bg:"#fed7aa"},{id:3,n:"Huile d’olive vierge extra 50 cl",c:"Épicerie",p:14.9,e:"🫒",pop:8,bg:"#d9f99d"},{id:4,n:"Confiture figue-noix",c:"Épicerie",p:6.9,e:"🍓",pop:6,bg:"#fecaca"},{id:5,n:"Tablette chocolat noir 70 %",c:"Sucré",p:5.5,e:"🍫",pop:10,bg:"#e7d3c1"},{id:6,n:"Biscuits sablés au beurre",c:"Sucré",p:4.9,e:"🍪",pop:5,bg:"#fef3c7"},{id:7,n:"Thé noir aux agrumes",c:"Boissons",p:9.9,e:"🫖",pop:4,bg:"#cffafe"},{id:8,n:"Jus de pomme artisanal 1 L",c:"Boissons",p:4.2,e:"🍎",pop:6,bg:"#dcfce7"},{id:9,n:"Coffret découverte du terroir",c:"Coffrets",p:59,e:"🎁",pop:8,bg:"#e0e7ff"}];
var cats=["Tout","Épicerie","Sucré","Boissons","Coffrets"],cur="Tout",KEY="demo-shop-cart",cart=store.get(KEY,{items:{},promo:""});
function find(id){return P.filter(function(p){return p.id==id})[0]}
function totals(){var sub=0,n=0;Object.keys(cart.items).forEach(function(id){var p=find(id);if(p){sub+=p.p*cart.items[id];n+=cart.items[id]}});var disc=cart.promo==="DEMO10"?sub*.1:0,ship=n===0||sub-disc>=60?0:5.9;return{sub:sub,n:n,disc:disc,ship:ship,tot:sub-disc+ship}}
function save(){store.set(KEY,cart);renderCart()}
function renderCats(){$("#s-cats").innerHTML=cats.map(function(c){return'<button type="button" class="tag click'+(c===cur?' on':'')+'" data-c="'+c+'">'+c+'</button>'}).join("")}
function renderProducts(){var q=$("#s-q").value.trim().toLowerCase(),s=$("#s-sort").value;var L=P.filter(function(p){return(cur==="Tout"||p.c===cur)&&(!q||p.n.toLowerCase().indexOf(q)>-1)});
L.sort(function(a,b){return s==="asc"?a.p-b.p:s==="desc"?b.p-a.p:b.pop-a.pop});
$("#products").innerHTML=L.length?L.map(function(p){return'<div class="card" style="display:flex;flex-direction:column"><div style="background:'+p.bg+';border-radius:10px;aspect-ratio:4/3;display:flex;align-items:center;justify-content:center;font-size:3.4rem;margin-bottom:12px" aria-hidden="true">'+p.e+'</div><span class="tag">'+p.c+'</span><h3 style="font-size:1rem;margin-top:6px">'+esc(p.n)+'</h3><div style="margin-top:auto;display:flex;justify-content:space-between;align-items:center"><span class="price">'+eur(p.p)+'</span><button class="btn sm" data-add="'+p.id+'">Ajouter</button></div></div>'}).join(""):'<p class="empty">Aucun produit.</p>'}
function renderCart(){var t=totals(),ids=Object.keys(cart.items);$("#cart-count").textContent=t.n;
if(!ids.length){$("#cart").innerHTML='<p class="empty">Votre panier est vide.</p>';return}
var h=ids.map(function(id){var p=find(id),q=cart.items[id];return'<div style="display:flex;justify-content:space-between;align-items:center;gap:8px;padding:8px 0;border-bottom:1px solid var(--line)"><div style="flex:1"><div style="font-weight:600;font-size:.92rem">'+esc(p.n)+'</div><div class="small muted">'+eur(p.p)+' × '+q+' = '+eur(p.p*q)+'</div></div><div class="qty"><button aria-label="Retirer un" data-dec="'+id+'">−</button><span>'+q+'</span><button aria-label="Ajouter un" data-inc="'+id+'">+</button></div><button class="btn sm ghost" style="color:var(--bad);padding:4px 8px" aria-label="Supprimer" data-rm="'+id+'">✕</button></div>'}).join("");
h+='<table class="tbl" style="margin-top:8px"><tr><td>Sous-total</td><td style="text-align:right">'+eur(t.sub)+'</td></tr>'+(t.disc?'<tr><td>Remise DEMO10</td><td style="text-align:right;color:var(--ok)">−'+eur(t.disc)+'</td></tr>':'')+'<tr><td>Livraison '+(t.ship?'<span class="small muted">(offerte dès 60 €)</span>':'')+'</td><td style="text-align:right">'+(t.ship?eur(t.ship):'Offerte')+'</td></tr><tr><th>Total TTC</th><th style="text-align:right;font-size:1.1rem;color:var(--ink)">'+eur(t.tot)+'</th></tr></table>';
h+='<form id="promo" style="display:flex;gap:6px;margin:10px 0"><input id="promo-in" placeholder="Code promo" value="'+esc(cart.promo)+'" aria-label="Code promo"><button class="btn sm" type="submit">OK</button></form><button class="btn" style="width:100%;justify-content:center" id="go-co">Commander</button>';
$("#cart").innerHTML=h;
$("#promo").addEventListener("submit",function(e){e.preventDefault();var v=$("#promo-in").value.trim().toUpperCase();if(!v){cart.promo="";save();return}if(v==="DEMO10"){cart.promo=v;save();toast("Code DEMO10 appliqué : −10 %")}else toast("Code promo inconnu")});
$("#go-co").addEventListener("click",function(){$("#checkout").hidden=false;$("#co-msg").innerHTML="";$("#co").hidden=false;$("#co-sum").textContent=t.n+" article(s) — total "+eur(t.tot)+" (démo)";$("#checkout").scrollIntoView({behavior:"smooth"})})}
document.addEventListener("click",function(e){var a=e.target.getAttribute&&e.target;if(!a)return;var id;
if(id=a.getAttribute("data-add")){cart.items[id]=(cart.items[id]||0)+1;save();toast("Ajouté au panier")}
else if(id=a.getAttribute("data-inc")){cart.items[id]=Math.min(99,cart.items[id]+1);save()}
else if(id=a.getAttribute("data-dec")){cart.items[id]--;if(cart.items[id]<=0)delete cart.items[id];save()}
else if(id=a.getAttribute("data-rm")){delete cart.items[id];save()}
else if(id=a.getAttribute("data-c")){cur=id;renderCats();renderProducts()}});
$("#s-q").addEventListener("input",renderProducts);$("#s-sort").addEventListener("change",renderProducts);
function setErr(id,msg){var el=$(id);el.classList.toggle("invalid",!!msg);el.parentNode.querySelector(".err").textContent=msg||"";return !msg}
$("#co").addEventListener("submit",function(e){e.preventDefault();var ok=true;
ok=setErr("#co-nom",$("#co-nom").value.trim().length<2?"Indiquez votre nom.":"")&ok;
ok=setErr("#co-mail",/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test($("#co-mail").value.trim())?"":"E-mail invalide.")&ok;
ok=setErr("#co-adr",$("#co-adr").value.trim().length<5?"Adresse incomplète.":"")&ok;
ok=setErr("#co-cp",/^\d{5}$/.test($("#co-cp").value.trim())?"":"5 chiffres.")&ok;
ok=setErr("#co-ville",$("#co-ville").value.trim().length<2?"Indiquez la ville.":"")&ok;
var t=totals();if(!t.n){$("#co-msg").innerHTML='<div class="notice err">Votre panier est vide.</div>';return}
if(!ok)return;var ref="CMD-DEMO-"+Math.floor(1e5+Math.random()*9e5);
$("#co-msg").innerHTML='<div class="notice ok">✅ Commande de démonstration '+ref+' validée : '+t.n+' article(s), '+eur(t.tot)+'. <strong>Aucun paiement n’a eu lieu</strong> et rien n’est expédié. Sur un vrai site, le paiement passerait par Stripe ou PayPal à cette étape.</div>';
$("#co").reset();$("#co").hidden=true;cart={items:{},promo:""};save()});
renderCats();renderProducts();renderCart();
})();
