const express = require("express");
const cors = require("cors");
const app = express();
app.use(cors());
app.use(express.json());

const dealers = [
  { id: 1, name: "TechStore", products: [{ sku: "laptop-1", price: 1200 }] },
  { id: 2, name: "GadgetHub", products: [{ sku: "laptop-1", price: 1150 }] },
];

app.get("/dealers", (req, res) => res.json(dealers));

app.get("/dealers/:id", (req, res) => {
  const d = dealers.find((x) => x.id == req.params.id);
  if (!d) return res.status(404).json({ error: "not found" });
  res.json(d);
});

app.get("/prices/:sku", (req, res) => {
  const sku = req.params.sku;
  const result = dealers
    .filter((d) => d.products.some((p) => p.sku === sku))
    .map((d) => ({
      dealer: d.name,
      price: d.products.find((p) => p.sku === sku).price,
    }));
  res.json(result);
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => console.log(`Dealer API listening ${PORT}`));
