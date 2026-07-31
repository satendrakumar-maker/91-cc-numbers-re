"""Generate clean 91 CC Numbers dashboard HTML — actual numbers, muted colors, aligned labels, mobile responsive"""
import json
from datetime import datetime

TIMESTAMP = datetime.now().strftime('%d %b %Y, %H:%M')

with open(r'C:\Users\saten\Documents\kimi\workspace\91-cc-numbers-re\dashboard_data.json') as f:
    DB = json.load(f)

CSS = '''
:root {
  --bg: #0f172a; --surface: #1e293b; --surface2: #334155;
  --text: #f1f5f9; --text2: #94a3b8; --accent: #7dd3fc;
  --green: #4ade80; --red: #f87171; --amber: #fbbf24;
  --border: #334155;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', system-ui, sans-serif; background: var(--bg); color: var(--text); min-height: 100vh; }
.header { background: linear-gradient(135deg, #0c4a6e 0%, var(--bg) 100%); padding: 24px 32px; border-bottom: 1px solid var(--border); }
.header h1 { font-size: 28px; font-weight: 700; }
.header p { color: var(--text2); margin-top: 4px; }
.container { max-width: 1600px; margin: 0 auto; padding: 24px 32px; }

.tabs { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 24px; }
.tab { padding: 10px 24px; border-radius: 8px; cursor: pointer; background: var(--surface); border: 1px solid var(--border); color: var(--text2); font-weight: 600; font-size: 14px; transition: all 0.2s; }
.tab:hover { background: var(--surface2); color: var(--text); }
.tab.active { background: var(--accent); color: #0f172a; border-color: var(--accent); }

.kpi-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-bottom: 24px; }
.kpi-card { background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 20px; }
.kpi-card .label { font-size: 11px; color: var(--text2); text-transform: uppercase; letter-spacing: 0.5px; }
.kpi-card .value { font-size: 26px; font-weight: 700; margin-top: 4px; }
.kpi-card .change { font-size: 13px; margin-top: 4px; font-weight: 600; }
.kpi-card .change.up { color: var(--green); }
.kpi-card .change.down { color: var(--red); }

.charts-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(480px, 1fr)); gap: 20px; margin-bottom: 24px; }
.chart-card { background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 20px; }
.chart-card h3 { font-size: 14px; color: var(--text2); margin-bottom: 12px; }
.chart-wrapper { position: relative; height: 320px; }

.data-table { width: 100%; border-collapse: collapse; font-size: 13px; }
.data-table th, .data-table td { padding: 10px 12px; text-align: center; border: 1px solid var(--border); }
.data-table th { background: var(--surface2); color: var(--text2); font-weight: 600; text-transform: uppercase; font-size: 11px; }
.data-table td { background: var(--bg); }
.data-table td:first-child { text-align: left; font-weight: 600; }
.positive { color: var(--green); font-weight: 700; }
.negative { color: var(--red); font-weight: 700; }

.compare-table { width: 100%; border-collapse: collapse; margin-top: 12px; font-size: 13px; }
.compare-table th, .compare-table td { padding: 10px 12px; text-align: left; border-bottom: 1px solid var(--border); }
.compare-table th { color: var(--text2); font-weight: 600; text-transform: uppercase; font-size: 11px; }
.compare-table tr:hover { background: rgba(255,255,255,0.03); }

.panel { background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 20px; margin-bottom: 20px; }
.panel h3 { font-size: 16px; margin-bottom: 14px; }
.panel ul { list-style: none; }
.panel ul li { padding: 10px 12px; border-radius: 8px; margin-bottom: 8px; font-size: 14px; line-height: 1.5; }
.insights-panel ul li { background: rgba(125,211,252,0.08); border-left: 3px solid var(--accent); }
.actions-panel ul li { background: rgba(74,222,128,0.08); border-left: 3px solid var(--green); }

.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
@media (max-width: 1000px) { .two-col { grid-template-columns: 1fr; } }

.section-content { display: none; }
.section-content.active { display: block; animation: fadeIn 0.3s ease; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }

.badge { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600; }
.badge.best { background: rgba(74,222,128,0.15); color: var(--green); }
.badge.worst { background: rgba(248,113,113,0.15); color: var(--red); }

.footer { text-align: center; padding: 24px; color: var(--text2); font-size: 12px; border-top: 1px solid var(--border); margin-top: 24px; }

.month-selectors { display: flex; gap: 16px; margin-bottom: 20px; flex-wrap: wrap; }
.month-selectors label { color: var(--text2); font-size: 13px; }
.month-selectors select { background: var(--bg); color: var(--text); border: 1px solid var(--border); border-radius: 6px; padding: 8px 12px; font-size: 14px; }

/* ==================== MOBILE RESPONSIVE ==================== */
@media (max-width: 768px) {
  .header { padding: 14px 14px; }
  .header h1 { font-size: 18px; }
  .header p { font-size: 11px; }
  .container { padding: 12px; max-width: 100%; }

  .tabs { flex-wrap: nowrap; overflow-x: auto; gap: 5px; padding-bottom: 4px; -webkit-overflow-scrolling: touch; scrollbar-width: none; }
  .tabs::-webkit-scrollbar { display: none; }
  .tab { padding: 7px 12px; font-size: 11px; white-space: nowrap; flex-shrink: 0; border-radius: 6px; }

  .kpi-grid { grid-template-columns: repeat(2, 1fr); gap: 8px; }
  .kpi-card { padding: 10px; border-radius: 8px; }
  .kpi-card .label { font-size: 9px; }
  .kpi-card .value { font-size: 16px; }
  .kpi-card .change { font-size: 10px; }

  .charts-grid { grid-template-columns: 1fr !important; gap: 10px; margin-bottom: 16px; }
  .chart-card { padding: 10px; border-radius: 8px; }
  .chart-card h3 { font-size: 11px; margin-bottom: 8px; }
  .chart-wrapper { height: 200px !important; }

  .panel { padding: 10px; border-radius: 8px; margin-bottom: 12px; }
  .panel h3 { font-size: 12px; margin-bottom: 10px; }
  .panel ul li { font-size: 11px; padding: 6px 8px; margin-bottom: 6px; line-height: 1.4; }

  .two-col { grid-template-columns: 1fr !important; gap: 10px; }

  .data-table { display: block; overflow-x: auto; white-space: nowrap; font-size: 10px; -webkit-overflow-scrolling: touch; }
  .data-table th, .data-table td { padding: 5px 6px; }

  .compare-table { font-size: 11px; display: block; overflow-x: auto; white-space: nowrap; -webkit-overflow-scrolling: touch; }
  .compare-table th, .compare-table td { padding: 6px 8px; }

  .month-selectors { flex-direction: column; gap: 8px; }
  .month-selectors select { padding: 6px 10px; font-size: 12px; }
  .footer { padding: 12px; font-size: 10px; }
  .badge { font-size: 10px; padding: 1px 5px; }
}

@media (max-width: 480px) {
  .kpi-grid { grid-template-columns: 1fr !important; }
  .header h1 { font-size: 16px; }
  .chart-wrapper { height: 170px !important; }
  .tab { padding: 6px 10px; font-size: 10px; }
}
'''

JS = r'''
const dataLabelsPlugin = {
  id: 'dataLabels',
  afterDatasetsDraw(chart) {
    const ctx = chart.ctx;
    ctx.save();
    ctx.font = 'bold 11px Segoe UI, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'bottom';
    chart.data.datasets.forEach((dataset, di) => {
      const meta = chart.getDatasetMeta(di);
      if (meta.hidden) return;
      meta.data.forEach((el, i) => {
        const val = dataset.data[i];
        if (val === 0 || val == null) return;
        let text = typeof val === 'number' ? val.toLocaleString() : String(val);
        if (dataset.label && dataset.label.includes('E2B')) text = val.toFixed(2) + '%';
        const isLine = dataset.type === 'line' || chart.config.type === 'line';
        const x = el.x;
        const y = isLine ? (el.y - 10) : (el.y - 6);
        const pad = 3;
        const w = ctx.measureText(text).width + pad * 2;
        const h = 14;
        ctx.fillStyle = 'rgba(15,23,42,0.75)';
        ctx.beginPath();
        ctx.roundRect(x - w/2, y - h, w, h, 4);
        ctx.fill();
        ctx.fillStyle = '#f1f5f9';
        ctx.fillText(text, x, y);
      });
    });
    ctx.restore();
  }
};

const fmt = n => typeof n === 'number' ? n.toLocaleString() : n;

function makeSectionHTML(sec) {
  const d = DB[sec];
  const s = d.summary;
  const a = d.averages;
  return `
  <div class="kpi-grid">
    <div class="kpi-card"><div class="label">2025 Enquiries</div><div class="value">${fmt(s.e2025)}</div></div>
    <div class="kpi-card"><div class="label">2026 Enquiries</div><div class="value">${fmt(s.e2026)}</div><div class="change ${s.e_chg>=0?'up':'down'}">${s.e_chg>=0?'▲':'▼'} ${Math.abs(s.e_chg)}%</div></div>
    <div class="kpi-card"><div class="label">2025 Bookings</div><div class="value">${fmt(s.b2025)}</div></div>
    <div class="kpi-card"><div class="label">2026 Bookings</div><div class="value">${fmt(s.b2026)}</div><div class="change ${s.b_chg>=0?'up':'down'}">${s.b_chg>=0?'▲':'▼'} ${Math.abs(s.b_chg)}%</div></div>
    <div class="kpi-card"><div class="label">2025 E2B</div><div class="value">${s.e2b2025}%</div></div>
    <div class="kpi-card"><div class="label">2026 E2B</div><div class="value">${s.e2b2026}%</div><div class="change ${s.e2b_chg>=0?'up':'down'}">${s.e2b_chg>=0?'▲':'▼'} ${Math.abs(s.e2b_chg)}pp</div></div>
    <div class="kpi-card"><div class="label">Avg Enq 2025</div><div class="value">${fmt(a.avg_enq_2025)}</div></div>
    <div class="kpi-card"><div class="label">Avg Enq 2026</div><div class="value">${fmt(a.avg_enq_2026)}</div></div>
  </div>
  <div class="charts-grid">
    <div class="chart-card"><h3>Monthly Enquiries Trend</h3><div class="chart-wrapper"><canvas id="chart-${sec}-enq"></canvas></div></div>
    <div class="chart-card"><h3>Monthly Bookings Trend</h3><div class="chart-wrapper"><canvas id="chart-${sec}-bkg"></canvas></div></div>
    <div class="chart-card"><h3>E2B Rate Trend</h3><div class="chart-wrapper"><canvas id="chart-${sec}-e2b"></canvas></div></div>
  </div>
  <div class="two-col">
    <div class="panel insights-panel"><h3>Insights</h3><ul>${d.insights.map(x=>`<li>${x}</li>`).join('')}</ul></div>
    <div class="panel actions-panel"><h3>Actionable Items</h3><ul>${d.actions.map(x=>`<li>${x}</li>`).join('')}</ul></div>
  </div>
  <div class="panel">
    <h3>Month-wise Comparison (2025 vs 2026)</h3>
    <table class="data-table">
      <tr><th>Month</th><th>Enq 2025</th><th>Enq 2026</th><th>Chg</th><th>Book 2025</th><th>Book 2026</th><th>Chg</th><th>E2B 2025</th><th>E2B 2026</th><th>Chg</th></tr>
      ${d.month_compare.map(r=>`<tr>
        <td>${r.month}</td>
        <td>${fmt(r.enq2025)}</td><td>${fmt(r.enq2026)}</td><td class="${r.enq_chg>=0?'positive':'negative'}">${r.enq_chg>0?'+':''}${r.enq_chg}%</td>
        <td>${fmt(r.book2025)}</td><td>${fmt(r.book2026)}</td><td class="${r.book_chg>=0?'positive':'negative'}">${r.book_chg>0?'+':''}${r.book_chg}%</td>
        <td>${r.e2b2025}%</td><td>${r.e2b2026}%</td><td class="${r.e2b_chg>=0?'positive':'negative'}">${r.e2b_chg>0?'+':''}${r.e2b_chg}</td>
      </tr>`).join('')}
    </table>
  </div>`;
}

for (const sec of ['S3','S4','S7','E4','W1','W2','W3']) {
  document.getElementById('sec-' + sec).innerHTML = makeSectionHTML(sec);
}

const secNames = ['S3','S4','S7','E4','W1','W2','W3'];
const C_BLUE   = '#5B8DB8';
const C_GREEN  = '#6B9E75';
const C_AMBER  = '#C4956A';
const C_BLUE_F  = 'rgba(91,141,184,0.15)';
const C_GREEN_F = 'rgba(107,158,117,0.15)';
const C_AMBER_F = 'rgba(196,149,106,0.15)';

let cmpHTML = '<tr><th>Section</th><th>Enq 2025</th><th>Enq 2026</th><th>Enq Δ</th><th>Book 2025</th><th>Book 2026</th><th>Book Δ</th><th>E2B 2025</th><th>E2B 2026</th><th>E2B Δ</th></tr>';
for (const sec of secNames) {
  const s = DB[sec].summary;
  cmpHTML += `<tr><td><b>${sec}</b></td><td>${fmt(s.e2025)}</td><td>${fmt(s.e2026)}</td><td class="${s.e_chg>=0?'positive':'negative'}">${s.e_chg>0?'+':''}${s.e_chg}%</td><td>${fmt(s.b2025)}</td><td>${fmt(s.b2026)}</td><td class="${s.b_chg>=0?'positive':'negative'}">${s.b_chg>0?'+':''}${s.b_chg}%</td><td>${s.e2b2025}%</td><td>${s.e2b2026}%</td><td class="${s.e2b_chg>=0?'positive':'negative'}">${s.e2b_chg>0?'+':''}${s.e2b_chg}</td></tr>`;
}
document.getElementById('all-compare-table').innerHTML = cmpHTML;

let bw = '<table class="compare-table"><tr><th>Metric</th><th>Best</th><th>Worst</th></tr>';
const bestEnq = secNames.reduce((a,b)=>DB[a].summary.e_chg>DB[b].summary.e_chg?a:b);
const worstEnq = secNames.reduce((a,b)=>DB[a].summary.e_chg<DB[b].summary.e_chg?a:b);
const bestBook = secNames.reduce((a,b)=>DB[a].summary.b_chg>DB[b].summary.b_chg?a:b);
const worstBook = secNames.reduce((a,b)=>DB[a].summary.b_chg<DB[b].summary.b_chg?a:b);
const bestE2B = secNames.reduce((a,b)=>DB[a].summary.e2b_chg>DB[b].summary.e2b_chg?a:b);
const worstE2B = secNames.reduce((a,b)=>DB[a].summary.e2b_chg<DB[b].summary.e2b_chg?a:b);
bw += `<tr><td>Enquiries Growth</td><td><span class="badge best">${bestEnq} +${DB[bestEnq].summary.e_chg}%</span></td><td><span class="badge worst">${worstEnq} ${DB[worstEnq].summary.e_chg}%</span></td></tr>`;
bw += `<tr><td>Bookings Growth</td><td><span class="badge best">${bestBook} +${DB[bestBook].summary.b_chg}%</span></td><td><span class="badge worst">${worstBook} ${DB[worstBook].summary.b_chg}%</span></td></tr>`;
bw += `<tr><td>E2B Improvement</td><td><span class="badge best">${bestE2B} +${DB[bestE2B].summary.e2b_chg}pp</span></td><td><span class="badge worst">${worstE2B} ${DB[worstE2B].summary.e2b_chg}pp</span></td></tr>`;
bw += '</table>';
document.getElementById('best-worst').innerHTML = bw;

function makeChart(id, labels, datasets, type='bar', yAxis='') {
  const ctx = document.getElementById(id);
  if (!ctx) return;
  return new Chart(ctx, {
    type: type,
    data: { labels, datasets },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: { legend: { labels: { color: '#94a3b8' } } },
      scales: {
        x: { ticks: { color: '#94a3b8' }, grid: { color: '#334155' } },
        y: { ticks: { color: '#94a3b8', callback: v => yAxis==='pct' ? v+'%' : fmt(v) }, grid: { color: '#334155' } }
      }
    },
    plugins: [dataLabelsPlugin]
  });
}

makeChart('chart-all-enq', secNames, [
  { label: '2025 Enquiries', data: secNames.map(s=>DB[s].summary.e2025), backgroundColor: C_BLUE },
  { label: '2026 Enquiries', data: secNames.map(s=>DB[s].summary.e2026), backgroundColor: C_GREEN }
]);
makeChart('chart-all-bkg', secNames, [
  { label: '2025 Bookings', data: secNames.map(s=>DB[s].summary.b2025), backgroundColor: C_BLUE },
  { label: '2026 Bookings', data: secNames.map(s=>DB[s].summary.b2026), backgroundColor: C_GREEN }
]);
makeChart('chart-all-e2b', secNames, [
  { label: '2025 E2B', data: secNames.map(s=>DB[s].summary.e2b2025), backgroundColor: C_BLUE },
  { label: '2026 E2B', data: secNames.map(s=>DB[s].summary.e2b2026), backgroundColor: C_GREEN }
], 'bar', 'pct');

for (const sec of secNames) {
  const d = DB[sec];
  makeChart(`chart-${sec}-enq`, d.months, [
    { label: 'Enquiries', data: d.enquiries, borderColor: C_BLUE, backgroundColor: C_BLUE_F, fill: true, tension: 0.3, type: 'line', pointRadius: 4, pointBackgroundColor: C_BLUE }
  ], 'line');
  makeChart(`chart-${sec}-bkg`, d.months, [
    { label: 'Bookings', data: d.bookings, borderColor: C_GREEN, backgroundColor: C_GREEN_F, fill: true, tension: 0.3, type: 'line', pointRadius: 4, pointBackgroundColor: C_GREEN }
  ], 'line');
  makeChart(`chart-${sec}-e2b`, d.months, [
    { label: 'E2B %', data: d.e2b, borderColor: C_AMBER, backgroundColor: C_AMBER_F, fill: true, tension: 0.3, type: 'line', pointRadius: 4, pointBackgroundColor: C_AMBER }
  ], 'line', 'pct');
}

const allMonths = new Set();
for (const sec of secNames) {
  for (const m of DB[sec].months) allMonths.add(m);
}
const monthList = Array.from(allMonths).sort((a,b) => {
  const [ma, ya] = a.split(' ');
  const [mb, yb] = b.split(' ');
  if (ya !== yb) return ya.localeCompare(yb);
  const order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  return order.indexOf(ma) - order.indexOf(mb);
});

const sel1 = document.getElementById('cmp-month1');
const sel2 = document.getElementById('cmp-month2');
for (const m of monthList) {
  sel1.add(new Option(m, m));
  sel2.add(new Option(m, m));
}
if (monthList.length >= 2) {
  sel1.value = monthList[monthList.length - 2];
  sel2.value = monthList[monthList.length - 1];
}

function renderCompare() {
  const m1 = sel1.value, m2 = sel2.value;
  let html = '<table class="data-table"><tr><th>Section</th><th>Metric</th><th>'+m1+'</th><th>'+m2+'</th><th>Δ</th></tr>';
  for (const sec of secNames) {
    const d = DB[sec];
    const i1 = d.months.indexOf(m1);
    const i2 = d.months.indexOf(m2);
    const has1 = i1 >= 0, has2 = i2 >= 0;
    const enq1 = has1 ? d.enquiries[i1] : 0;
    const enq2 = has2 ? d.enquiries[i2] : 0;
    const book1 = has1 ? d.bookings[i1] : 0;
    const book2 = has2 ? d.bookings[i2] : 0;
    const e2b1 = has1 ? d.e2b[i1] : 0;
    const e2b2 = has2 ? d.e2b[i2] : 0;
    const enqChg = enq1 > 0 ? ((enq2-enq1)/enq1*100).toFixed(1) : 'N/A';
    const bookChg = book1 > 0 ? ((book2-book1)/book1*100).toFixed(1) : 'N/A';
    const e2bChg = (e2b2-e2b1).toFixed(2);
    html += `<tr><td rowspan="3"><b>${sec}</b></td><td>Enquiries</td><td>${fmt(enq1)}</td><td>${fmt(enq2)}</td><td class="${enqChg>=0?'positive':'negative'}">${enqChg>0?'+':''}${enqChg}%</td></tr>`;
    html += `<tr><td>Bookings</td><td>${fmt(book1)}</td><td>${fmt(book2)}</td><td class="${bookChg>=0?'positive':'negative'}">${bookChg>0?'+':''}${bookChg}%</td></tr>`;
    html += `<tr><td>E2B</td><td>${e2b1.toFixed(2)}%</td><td>${e2b2.toFixed(2)}%</td><td class="${e2bChg>=0?'positive':'negative'}">${e2bChg>0?'+':''}${e2bChg}</td></tr>`;
  }
  html += '</table>';
  document.getElementById('compare-results').innerHTML = html;
}
sel1.onchange = renderCompare;
sel2.onchange = renderCompare;
renderCompare();

document.getElementById('tabs').addEventListener('click', e => {
  if (!e.target.classList.contains('tab')) return;
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.section-content').forEach(s => s.classList.remove('active'));
  e.target.classList.add('active');
  document.getElementById('sec-' + e.target.dataset.section).classList.add('active');
});
'''

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
<title>91 CC Numbers (RE) — Full Dashboard</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<style>{CSS}</style>
</head>
<body>

<div class="header">
  <h1>91 CC Numbers (RE)</h1>
  <p>Interactive Dashboard — Actual Numbers on Every Chart | 2025 vs 2026</p>
</div>

<div class="container">
  <div class="tabs" id="tabs">
    <div class="tab active" data-section="all">All Sections</div>
    <div class="tab" data-section="S3">S3</div>
    <div class="tab" data-section="S4">S4</div>
    <div class="tab" data-section="S7">S7</div>
    <div class="tab" data-section="E4">E4</div>
    <div class="tab" data-section="W1">W1</div>
    <div class="tab" data-section="W2">W2</div>
    <div class="tab" data-section="W3">W3</div>
    <div class="tab" data-section="compare">Month Compare</div>
  </div>

  <div class="section-content active" id="sec-all">
    <div class="panel">
      <h3>Section Comparison — 2025 vs 2026 (Sheet Totals)</h3>
      <table class="compare-table" id="all-compare-table"></table>
    </div>
    <div class="charts-grid">
      <div class="chart-card"><h3>Enquiries by Section</h3><div class="chart-wrapper"><canvas id="chart-all-enq"></canvas></div></div>
      <div class="chart-card"><h3>Bookings by Section</h3><div class="chart-wrapper"><canvas id="chart-all-bkg"></canvas></div></div>
      <div class="chart-card"><h3>E2B Rate by Section</h3><div class="chart-wrapper"><canvas id="chart-all-e2b"></canvas></div></div>
    </div>
    <div class="panel"><h3>Best & Worst Performers</h3><div id="best-worst"></div></div>
  </div>

  <div class="section-content" id="sec-S3"></div>
  <div class="section-content" id="sec-S4"></div>
  <div class="section-content" id="sec-S7"></div>
  <div class="section-content" id="sec-E4"></div>
  <div class="section-content" id="sec-W1"></div>
  <div class="section-content" id="sec-W2"></div>
  <div class="section-content" id="sec-W3"></div>

  <div class="section-content" id="sec-compare">
    <div class="panel">
      <h3>Compare Any Two Months Across All Sections</h3>
      <div class="month-selectors">
        <div><label>Month A:</label><select id="cmp-month1"></select></div>
        <div><label>Month B:</label><select id="cmp-month2"></select></div>
      </div>
      <div id="compare-results"></div>
    </div>
  </div>
</div>

<div class="footer">91 CC Numbers (RE) — July 2026 Data Included | Data Labels on All Charts | Last Updated: {TIMESTAMP}</div>

<script>
const DB = {json.dumps(DB)};
{JS}
</script>
</body>
</html>'''

with open(r'C:\Users\saten\Documents\kimi\workspace\91-cc-numbers-re\dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Dashboard regenerated cleanly with mobile responsive CSS!')
