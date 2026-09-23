const money = n => "₹" + Math.round(n).toLocaleString("en-IN");
const amount = document.getElementById("amount");
const tenure = document.getElementById("tenure");
const rate = document.getElementById("rate");

function syncRate(){
  const option = document.querySelector("#loanType option:checked");
  rate.value = option.dataset.rate;
  calculateEMI();
}
function updateLabels(){
  document.getElementById("amountValue").textContent = money(Number(amount.value));
  document.getElementById("tenureValue").textContent = tenure.value + (tenure.value == 1 ? " Year" : " Years");
}
function calculateEMI(){
  if(!amount) return;
  const P = Number(amount.value), annual = Number(rate.value), years = Number(tenure.value);
  const r = annual / 12 / 100, n = years * 12;
  const emi = r === 0 ? P/n : P*r*Math.pow(1+r,n)/(Math.pow(1+r,n)-1);
  document.getElementById("emi").textContent = money(emi);
  document.getElementById("principal").textContent = money(P);
  document.getElementById("interest").textContent = money(emi*n-P);
  document.getElementById("total").textContent = money(emi*n);
  updateLabels();
}
function selectLoan(name, selectedRate){
  document.getElementById("loanType").value = name;
  document.getElementById("rate").value = selectedRate;
  document.getElementById("loan-calculator").scrollIntoView({behavior:"smooth"});
  calculateEMI();
}
if(amount){
  amount.addEventListener("input", calculateEMI);
  tenure.addEventListener("input", calculateEMI);
  rate.addEventListener("input", calculateEMI);
  calculateEMI();
}

const track = document.getElementById("activityTrack");
const dots = document.getElementById("carouselDots");
if(track && dots){
  const cards = [...track.children];
  let index = 0;
  function getVisible(){ return window.innerWidth <= 600 ? 1 : (window.innerWidth <= 900 ? 2 : 3); }
  function renderDots(){
    dots.innerHTML = "";
    const pages = Math.max(1, cards.length - getVisible() + 1);
    for(let i=0;i<pages;i++){
      const d=document.createElement("span");
      d.className="dot"+(i===index?" on":"");
      dots.appendChild(d);
    }
  }
  function move(){
    const visible = getVisible();
    const maxIndex = Math.max(0,cards.length-visible);
    index = index >= maxIndex ? 0 : index+1;
    const cardWidth = cards[0].getBoundingClientRect().width + 16;
    track.style.transform = `translateX(-${index*cardWidth}px)`;
    renderDots();
  }
  renderDots();
  setInterval(move, 3000);
  window.addEventListener("resize", ()=>{index=0;track.style.transform="translateX(0)";renderDots()});
}
