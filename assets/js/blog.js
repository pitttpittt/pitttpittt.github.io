(function(){
var $=function(s){return document.querySelector(s)},A=[],tag="Tous";
function inline(s){return esc(s).replace(/`([^`]+)`/g,"<code>$1</code>").replace(/\*\*([^*]+)\*\*/g,"<strong>$1</strong>").replace(/\*([^*]+)\*/g,"<em>$1</em>").replace(/\[([^\]]+)\]\((https?:[^)\s]+)\)/g,'<a href="$2" rel="noopener">$1</a>')}
window.md=function(src){var out=[],lines=src.split("\n"),i=0,list=null;function close(){if(list){out.push("</"+list+">");list=null}}
while(i<lines.length){var l=lines[i];
if(/^```/.test(l)){close();var code=[];i++;while(i<lines.length&&!/^```/.test(lines[i])){code.push(lines[i]);i++}out.push("<pre><code>"+esc(code.join("\n"))+"</code></pre>");i++;continue}
var m;if(m=l.match(/^(#{2,3}) (.*)/)){close();out.push("<h"+m[1].length+">"+inline(m[2])+"</h"+m[1].length+">")}
else if(m=l.match(/^- (.*)/)){if(list!=="ul"){close();out.push("<ul>");list="ul"}out.push("<li>"+inline(m[1])+"</li>")}
else if(m=l.match(/^\d+\. (.*)/)){if(list!=="ol"){close();out.push("<ol>");list="ol"}out.push("<li>"+inline(m[1])+"</li>")}
else if(l.trim()===""){close()}else{close();out.push("<p>"+inline(l)+"</p>")}i++}close();return out.join("\n")};
function fdate(d){return new Date(d+"T12:00").toLocaleDateString("fr-FR",{day:"numeric",month:"long",year:"numeric"})}
function renderList(){var q=$("#b-q").value.trim().toLowerCase();var tags=["Tous"].concat(A.reduce(function(s,a){a.tags.forEach(function(t){if(s.indexOf(t)<0)s.push(t)});return s},[]));
$("#b-tags").innerHTML=tags.map(function(t){return'<button type="button" class="tag click'+(t===tag?' on':'')+'" data-t="'+t+'">'+t+'</button>'}).join("");
var L=A.filter(function(a){return(tag==="Tous"||a.tags.indexOf(tag)>-1)&&(!q||(a.title+" "+a.excerpt+" "+a.body).toLowerCase().indexOf(q)>-1)});
$("#b-posts").innerHTML=L.map(function(a){return'<a class="card link" href="?article='+a.slug+'"><span class="small muted">'+fdate(a.date)+'</span><h3 style="margin-top:6px">'+esc(a.title)+'</h3><p class="muted small">'+esc(a.excerpt)+'</p><div style="margin-top:auto">'+a.tags.map(function(t){return'<span class="tag">'+t+'</span>'}).join("")+'</div></a>'}).join("");$("#b-empty").hidden=L.length>0}
function route(){var slug=new URLSearchParams(location.search).get("article"),a=A.filter(function(x){return x.slug===slug})[0];
if(a){$("#b-list").hidden=true;$("#b-article").hidden=false;$("#b-title").textContent=a.title;$("#b-lead").textContent=fdate(a.date)+" · "+a.tags.join(", ");document.title=a.title+" — Démo blog | Peter Philippot";
$("#b-article").innerHTML='<p><a href="blog.html">← Tous les articles</a></p>'+md(a.body)+'<p class="small muted" style="margin-top:30px">Article d’exemple publié sur un blog de démonstration.</p>';window.scrollTo(0,0)}
else{$("#b-list").hidden=false;$("#b-article").hidden=true;renderList()}}
$("#b-tags").addEventListener("click",function(e){var t=e.target.getAttribute("data-t");if(t){tag=t;renderList()}});$("#b-q").addEventListener("input",renderList);
fetch("assets/data/articles.json").then(function(r){if(!r.ok)throw 0;return r.json()}).then(function(d){A=d.sort(function(a,b){return b.date.localeCompare(a.date)});route()}).catch(function(){$("#b-posts").innerHTML='<p class="notice err">Impossible de charger les articles.</p>'});
})();
