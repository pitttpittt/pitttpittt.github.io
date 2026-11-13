(function(){
var M=[
{n:"Planche de fromages affinés",d:"Cinq fromages de saison, confiture de figue, pain au levain",p:16.5,c:"Entrées",v:1,g:0},
{n:"Velouté de potimarron",d:"Crème crue, graines de courge torréfiées",p:8,c:"Entrées",v:1,g:1},
{n:"Œuf parfait",d:"Crème de champignons, croûtons, ciboulette",p:9.5,c:"Entrées",v:1,g:0},
{n:"Tartare de bœuf au couteau",d:"Câpres, échalote, frites maison",p:19,c:"Plats",v:0,g:1},
{n:"Risotto aux cèpes",d:"Parmesan 24 mois, huile de noisette",p:18,c:"Plats",v:1,g:1},
{n:"Filet de bar rôti",d:"Fenouil braisé, beurre blanc citronné",p:22,c:"Plats",v:0,g:1},
{n:"Burger fermier",d:"Cheddar affiné, oignons confits, frites",p:17.5,c:"Plats",v:0,g:0},
{n:"Moelleux au chocolat",d:"Cœur coulant, glace vanille",p:8.5,c:"Desserts",v:1,g:0},
{n:"Crème brûlée à la vanille",d:"Vanille de Madagascar",p:7.5,c:"Desserts",v:1,g:1},
{n:"Assiette de fromages",d:"Trois fromages, salade de mesclun",p:9,c:"Desserts",v:1,g:1},
{n:"Limonade artisanale",d:"Citron, gingembre",p:4.5,c:"Boissons",v:1,g:1},
{n:"Verre de vin du moment",d:"Sélection du sommelier, 12 cl",p:6,c:"Boissons",v:1,g:1}];
var cats=["Tout","Entrées","Plats","Desserts","Boissons"],cur="Tout";
var $=function(s){return document.querySelector(s)};
function renderCats(){$("#cats").innerHTML=cats.map(function(c){return '<button type="button" class="tag click'+(c===cur?' on':'')+'" data-c="'+c+'">'+c+'</button>'}).join("")}
function render(){var q=$("#q").value.trim().toLowerCase(),veg=$("#veg").checked,gf=$("#gf").checked;
var L=M.filter(function(m){return(cur==="Tout"||m.c===cur)&&(!veg||m.v)&&(!gf||m.g)&&(!q||(m.n+" "+m.d).toLowerCase().indexOf(q)>-1)});
$("#menu").innerHTML=L.map(function(m){return '<div class="card"><div style="display:flex;justify-content:space-between;gap:10px"><h3>'+esc(m.n)+'</h3><span class="price">'+eur(m.p)+'</span></div><p class="muted small">'+esc(m.d)+'</p><span class="tag">'+m.c+'</span>'+(m.v?'<span class="tag" style="background:#ecfdf5;color:#047857">Végétarien</span>':'')+(m.g?'<span class="tag" style="background:#fef3c7;color:#92400e">Sans gluten</span>':'')+'</div>'}).join("");
$("#menu-empty").hidden=L.length>0}
$("#cats").addEventListener("click",function(e){var c=e.target.getAttribute("data-c");if(c){cur=c;renderCats();render()}});
["#q","#veg","#gf"].forEach(function(s){$(s).addEventListener("input",render)});
renderCats();render();
// reservation
var hours=["12:00","12:30","13:00","13:30","19:00","19:30","20:00","20:30","21:00","21:30"];
$("#r-heure").innerHTML='<option value="">Choisir…</option>'+hours.map(function(h){return'<option>'+h+'</option>'}).join("");
var today=new Date();today.setHours(0,0,0,0);var iso=function(d){return d.getFullYear()+"-"+String(d.getMonth()+1).padStart(2,"0")+"-"+String(d.getDate()).padStart(2,"0")};
$("#r-date").min=iso(today);
var KEY="demo-resto-resas";
function setErr(id,msg){var el=$(id);el.classList.toggle("invalid",!!msg);el.parentNode.querySelector(".err").textContent=msg||"";return !msg}
function list(){var R=store.get(KEY,[]);
$("#list").innerHTML=R.length?'<table class="tbl"><tr><th>Date</th><th>Nom</th><th>Pers.</th><th></th></tr>'+R.map(function(r,i){return'<tr><td>'+new Date(r.date+"T12:00").toLocaleDateString("fr-FR",{weekday:"short",day:"numeric",month:"short"})+' · '+r.heure+'</td><td>'+esc(r.nom)+'<br><span class="small muted">'+r.ref+'</span></td><td>'+r.pers+'</td><td><button class="btn sm ghost" style="color:var(--bad)" data-del="'+i+'">Annuler</button></td></tr>'}).join("")+'</table>':'<p class="empty">Aucune réservation pour l’instant.</p>'}
$("#list").addEventListener("click",function(e){var i=e.target.getAttribute("data-del");if(i!==null){var R=store.get(KEY,[]);R.splice(+i,1);store.set(KEY,R);list();toast("Réservation annulée")}});
$("#resa").addEventListener("submit",function(e){e.preventDefault();var ok=true,nom=$("#r-nom").value.trim(),mail=$("#r-mail").value.trim(),date=$("#r-date").value,h=$("#r-heure").value,p=+$("#r-pers").value;
ok=setErr("#r-nom",nom.length<2?"Indiquez votre nom.":"")&ok;
ok=setErr("#r-mail",/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(mail)?"":"E-mail invalide.")&ok;
var dm="";if(!date)dm="Choisissez une date.";else{var d=new Date(date+"T00:00");if(d<today)dm="La date est passée.";else if(d.getDay()===1)dm="Fermé le lundi.";else if((d-today)/864e5>90)dm="Réservations ouvertes à 90 jours max."}
ok=setErr("#r-date",dm)&ok;
var hm=h?"":"Choisissez une heure.";if(!hm&&date===iso(today)){var n=new Date(),hh=h.split(":");if(+hh[0]*60+ +hh[1]<n.getHours()*60+n.getMinutes()+60)hm="Créneau trop proche (1 h minimum)."}
ok=setErr("#r-heure",hm)&ok;
ok=setErr("#r-pers",p>=1&&p<=12&&Math.floor(p)===p?"":"Entre 1 et 12 personnes.")&ok;
var R=store.get(KEY,[]);if(ok){var taken=R.filter(function(r){return r.date===date&&r.heure===h}).reduce(function(s,r){return s+r.pers},0);if(taken+p>20){ok=setErr("#r-heure","Complet sur ce créneau, essayez un autre horaire.")&&false}}
if(!ok){$("#resa-msg").innerHTML='<div class="notice err">Merci de corriger les champs indiqués.</div>';return}
var ref="R-"+Math.random().toString(36).slice(2,7).toUpperCase();
R.push({ref:ref,nom:nom,mail:mail,date:date,heure:h,pers:p,note:$("#r-note").value.trim()});R.sort(function(a,b){return(a.date+a.heure).localeCompare(b.date+b.heure)});store.set(KEY,R);
$("#resa-msg").innerHTML='<div class="notice ok">✅ Réservation confirmée (démo) : '+p+' pers. le '+new Date(date+"T12:00").toLocaleDateString("fr-FR",{weekday:"long",day:"numeric",month:"long"})+' à '+h+'. Référence '+ref+'. Aucun e-mail n’est réellement envoyé.</div>';
$("#resa").reset();$("#r-pers").value=2;list()});
list();
})();
