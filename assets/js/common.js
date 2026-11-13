(function(){
  var b=document.querySelector('.burger'),n=document.querySelector('.nav');
  if(b&&n)b.addEventListener('click',function(){n.classList.toggle('open');b.setAttribute('aria-expanded',n.classList.contains('open'))});
  var lb=document.createElement('div');lb.className='lightbox';lb.innerHTML='<img alt="">';document.body.appendChild(lb);
  lb.addEventListener('click',function(){lb.classList.remove('open')});
  document.addEventListener('click',function(e){var t=e.target;if(t.matches&&t.matches('.gallery img,[data-zoom]')){lb.querySelector('img').src=t.getAttribute('data-full')||t.src;lb.querySelector('img').alt=t.alt||'';lb.classList.add('open')}});
  var y=document.getElementById('year');if(y)y.textContent=new Date().getFullYear();
})();
window.toast=function(msg){var t=document.querySelector('.toast');if(!t){t=document.createElement('div');t.className='toast';t.setAttribute('role','status');document.body.appendChild(t)}t.textContent=msg;t.classList.add('show');clearTimeout(t._h);t._h=setTimeout(function(){t.classList.remove('show')},2400)};
window.eur=function(n){return n.toLocaleString('fr-FR',{style:'currency',currency:'EUR'})};
window.esc=function(s){return String(s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})};
window.store={get:function(k,d){try{var v=JSON.parse(localStorage.getItem(k));return v==null?d:v}catch(e){return d}},set:function(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}};
