<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>Dealer Evaluation</title>
  <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
  <div id="app">
    <h1>Dealer Evaluation</h1>
    <label>Product:
      <select id="productSelect">
        <option value="laptop-1">Laptop</option>
        <option value="smartphone-1">Smartphone</option>
      </select>
    </label>
    <button id="loadDealers">Show Dealers</button>
    <div id="dealers"></div>
  </div>
<script>
const dealerApi = (window.DEALER_API || "http://localhost:8080");
document.getElementById('loadDealers').addEventListener('click', async ()=>{
  const sku = document.getElementById('productSelect').value;
  const res = await fetch(`${dealerApi}/prices/${sku}`);
  const data = await res.json();
  document.getElementById('dealers').innerText = JSON.stringify(data,null,2);
});
</script>
</body>
</html>
