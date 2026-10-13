function initEnvRain(){
  var sec=document.getElementById('sgifts'),rain=document.getElementById('envRain'),
      btn=document.getElementById('envGift'),body=document.getElementById('envGiftBody'),
      hint=document.getElementById('envGiftHint');
  if(!sec||!rain||!btn) return;
  var raining=true,landed=false,spawnCall=null,alive=0;
  var MAX_ALIVE=18;

  function makeEnvelope(){
    if(alive>=MAX_ALIVE) return;
    alive++;
    var el=document.createElementNS('http://www.w3.org/2000/svg','svg');
    el.setAttribute('viewBox','0 0 34 24');
    el.setAttribute('class','env-rain-item');
    var w=16+Math.random()*16;
    el.style.width=w+'px';el.style.height=(w*24/34)+'px';
    el.style.left=(Math.random()*100)+'%';
    el.innerHTML='<rect x="1" y="1" width="32" height="22" rx="2.5" fill="#FFFFFF" stroke="#7FB8E6" stroke-width="1.2"/>'+
                 '<path d="M1 1 L17 13 L33 1" fill="none" stroke="#7FB8E6" stroke-width="1.2" stroke-linejoin="round"/>';
    rain.appendChild(el);
    var H=sec.offsetHeight+80,dur=5+Math.random()*4;
    function kill(){if(el.parentNode){el.remove();alive--;}}
    gsap.timeline({onComplete:kill})
      .fromTo(el,{y:-46,x:0,rotation:(Math.random()-.5)*50,opacity:0},
                 {y:H,x:(Math.random()-.5)*70,rotation:(Math.random()-.5)*160,
                  duration:dur,ease:'none'},0)
      .fromTo(el,{opacity:0},{opacity:.75,duration:dur*.18,ease:'power1.out'},0)
      .to(el,{opacity:0,duration:dur*.25,ease:'power1.in'},dur*.75);
  }
  /* Spawn por el ticker de GSAP (no setInterval): se pausa con la pestaña. */
  function scheduleSpawn(){
    spawnCall=gsap.delayedCall(.52,function(){
      if(!raining) return;
      makeEnvelope();
      scheduleSpawn();
    });
  }
  function stopRain(){
    raining=false;
    if(spawnCall) spawnCall.kill();
    gsap.to(rain,{opacity:0,duration:1.1,ease:'power2.out',
      onComplete:function(){rain.innerHTML='';alive=0;}});
  }
  function land(){
    if(landed) return; landed=true;
    stopRain();
    gsap.fromTo(btn,
      {opacity:0,y:-150,rotation:-12,scale:.82},
      {opacity:1,y:0,rotation:0,scale:1,duration:1.15,ease:'back.out(1.5)',
       onComplete:function(){
         if(body)body.classList.add('landed');
         if(hint)hint.classList.add('show');
       }});
  }
  for(var i=0;i<7;i++) gsap.delayedCall(i*.26,makeEnvelope);
  scheduleSpawn();
  /* 'center 55%' y no 'center center': el reveal .rv desplaza 28px las
     secciones aún no visibles y el umbral exacto queda fuera de alcance. */
  ScrollTrigger.create({trigger:sec,start:'center 55%',once:true,onEnter:land,onEnterBack:land});

  btn.addEventListener('click',function(e){
    if(e)e.preventDefault();
    if(!landed) return;
    var open=btn.classList.toggle('open');
    btn.setAttribute('aria-expanded',open?'true':'false');
    if(open&&body)body.classList.remove('landed');
    ScrollTrigger.refresh();
  });
}