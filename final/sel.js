(function(){var K='lla_finalists_v1';function g(){try{return JSON.parse(localStorage.getItem(K))||{}}catch(e){return{}}}function s(d){localStorage.setItem(K,JSON.stringify(d));upd()}
function list(){var d=g();return Object.keys(d).map(function(k){return d[k]})}
function txt(){return list().map(function(x){return x.cat+' | '+x.n+' | '+x.u+(x.c?' | '+x.c:'')}).join('\n')}
function csv(){var q=function(v){return '"'+String(v||'').replace(/"/g,'""')+'"'};return 'category,filename,url,comment\n'+list().map(function(x){return [x.cat,x.n,x.u,x.c].map(q).join(',')}).join('\n')}
window.LLA={g:g,s:s,K:K};
var bar=document.createElement('div');bar.style.cssText='position:fixed;left:0;right:0;bottom:0;background:#06204a;border-top:2px solid #6FA8FF;padding:10px 14px;display:flex;gap:8px;align-items:center;flex-wrap:wrap;z-index:9;font:600 14px system-ui';
bar.innerHTML='<span id="lc"></span><a href="finalists.html" style="color:#fff;background:#2a5bd7;padding:6px 10px;border-radius:6px;text-decoration:none">View finalists</a><button id="lcp">Copy list</button><button id="lcsv">Download CSV</button>';document.body.appendChild(bar);
function upd(){document.getElementById('lc').textContent='⭐ '+list().length+' finalists selected'}
document.getElementById('lcp').onclick=function(){navigator.clipboard.writeText(txt()).then(function(){alert('Copied '+list().length+' items')},function(){prompt('Copy:',txt())})};
document.getElementById('lcsv').onclick=function(){var a=document.createElement('a');a.href=URL.createObjectURL(new Blob([csv()],{type:'text/csv'}));a.download='lla_finalists.csv';a.click()};
document.querySelectorAll('.c[data-p]').forEach(function(c){var p=c.dataset.p,d=g(),w=document.createElement('div');w.style.cssText='margin-top:8px';
w.innerHTML='<label style="font-weight:700;cursor:pointer"><input type="checkbox"> Finalist for upload</label><textarea placeholder="Comment…" style="display:block;width:100%;max-width:320px;margin-top:6px;min-height:44px;border-radius:6px"></textarea>';c.appendChild(w);
var cb=w.querySelector('input'),ta=w.querySelector('textarea');if(d[p]){cb.checked=true;ta.value=d[p].c||''}
function save(){var d=g();if(cb.checked)d[p]={p:p,u:c.dataset.u,cat:c.dataset.cat,n:c.dataset.n,c:ta.value};else delete d[p];s(d);c.style.outline=cb.checked?'2px solid #ffd54a':''}
cb.onchange=save;ta.oninput=function(){if(!cb.checked&&ta.value){cb.checked=true}save()};if(cb.checked)c.style.outline='2px solid #ffd54a'});
window.LLAupd=upd;upd()})();
