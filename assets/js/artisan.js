(function(){
var $=function(s){return document.querySelector(s)};
var T=[{id:"cuisine",n:"Cuisine sur mesure",u:"mètres linéaires",su:"mètre linéaire",p:1450,ic:"🍳",d:"Caissons, plans de travail, intégration de l’électroménager."},
{id:"dressing",n:"Dressing / placard",u:"mètres linéaires",su:"mètre linéaire",p:780,ic:"👔",d:"Rangements optimisés sous pente ou en niche."},
{id:"escalier",n:"Escalier bois",u:"marches",su:"marche",p:320,ic:"🪜",d:"Droit, quart tournant ou suspendu, chêne ou hêtre."},
{id:"terrasse",n:"Terrasse bois",u:"m²",su:"m²",p:135,ic:"🌿",d:"Lames pin traité, ipé ou composite, sur plots."}];
var O=[{id:"pose",n:"Pose par l’atelier",r:.18},{id:"depose",n:"Dépose de l’existant",r:.08},{id:"plan",n:"Plans 3D avant fabrication",f:150},{id:"vernis",n:"Finition vernis / huile",r:.06}];
$("#svc").innerHTML=T.map(function(t){return'<div class="card"><div class="ico">'+t.ic+'</div><h3>'+t.n+'</h3><p class="muted small">'+t.d+'</p><p class="small">À partir de <span class="price">'+eur(t.p)+'</span> / '+t.su+'</p></div>'}).join("");
$("#c-type").innerHTML=T.map(function(t){return'<option value="'+t.id+'">'+t.n+'</option>'}).join("");
$("#c-opts").innerHTML=O.map(function(o){return'<label style="font-weight:400;display:flex;gap:8px;align-items:center"><input type="checkbox" style="width:auto" data-o="'+o.id+'"'+(o.id==="pose"?" checked":"")+'> '+o.n+' <span class="muted small">('+(o.r?"+"+Math.round(o.r*100)+" %":"+"+eur(o.f))+')</span></label>'}).join("");
function calc(){var t=T.filter(function(x){return x.id===$("#c-type").value})[0],q=Math.max(0,parseFloat($("#c-qte").value)||0),fin=+$("#c-fin").value,km=+$("#c-km").value,urg=+$("#c-urg").value;
$("#c-unit").textContent="Quantité ("+t.u+")";$("#c-kmv").textContent=km;
var base=t.p*q*fin,rows=[["Fabrication ("+q+" "+t.u+")",base]];
document.querySelectorAll("[data-o]").forEach(function(c){if(c.checked){var o=O.filter(function(x){return x.id===c.getAttribute("data-o")})[0];rows.push([o.n,o.r?base*o.r:o.f])}});
var dep=km>20?(km-20)*1.2*2:0;if(dep)rows.push(["Déplacement (au-delà de 20 km)",dep]);
var sub=rows.reduce(function(s,r){return s+r[1]},0);if(urg>1)rows.push(["Délai rapide",sub*(urg-1)]);
var tot=rows.reduce(function(s,r){return s+r[1]},0);
$("#c-total").textContent=q?eur(Math.round(tot)):"—";$("#c-range").textContent=q?"Fourchette probable : "+eur(Math.round(tot*.9))+" – "+eur(Math.round(tot*1.1))+" (TVA non incluse)":"Indiquez une quantité.";
$("#c-detail").innerHTML=rows.map(function(r){return'<tr><td>'+r[0]+'</td><td style="text-align:right">'+eur(Math.round(r[1]))+'</td></tr>'}).join("");return tot}
$("#calc").addEventListener("input",calc);$("#calc").addEventListener("change",calc);calc();
function setErr(id,msg){var el=$(id);el.classList.toggle("invalid",!!msg);el.parentNode.querySelector(".err").textContent=msg||"";return !msg}
$("#calc").addEventListener("submit",function(e){e.preventDefault();var a=setErr("#c-nom",$("#c-nom").value.trim().length<2?"Indiquez votre nom.":""),b=setErr("#c-mail",/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test($("#c-mail").value.trim())?"":"E-mail invalide.");
var tot=calc();if(!(parseFloat($("#c-qte").value)>0)){$("#c-msg").innerHTML='<div class="notice err">Indiquez une quantité supérieure à 0.</div>';return}
if(!(a&&b)){$("#c-msg").innerHTML='<div class="notice err">Merci de corriger les champs indiqués.</div>';return}
var ref="D-"+Date.now().toString(36).toUpperCase().slice(-6),L=store.get("demo-artisan-devis",[]);L.push({ref:ref,type:$("#c-type").value,total:Math.round(tot),date:new Date().toISOString()});store.set("demo-artisan-devis",L);
$("#c-msg").innerHTML='<div class="notice ok">✅ Demande '+ref+' enregistrée (démo) pour une estimation de '+eur(Math.round(tot))+'. Dans un vrai site, l’artisan recevrait la demande par e-mail. Ici, rien n’est envoyé.</div>'});
})();
